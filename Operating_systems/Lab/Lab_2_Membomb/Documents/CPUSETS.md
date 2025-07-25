# CPUSETS

[Bài Viết Gốc](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/cpusets.html)

---

## 1. Cpuset

### 1.1 Cpuset là gì?

Cpuset cung cấp một cơ chế để **gán một tập hợp các CPU và các nút bộ nhớ (Memory Nodes)** cho một tập hợp các tác vụ. Trong tài liệu này, "Memory Node" đề cập đến một nút đang hoạt động và có chứa bộ nhớ.

Cpuset giới hạn việc sử dụng CPU và bộ nhớ của các tác vụ **chỉ trong phạm vi cpuset hiện tại của tác vụ đó**. Chúng tạo thành một hệ phân cấp lồng nhau, có thể nhìn thấy qua hệ thống tệp ảo. Đây là các móc (hooks) cần thiết để quản lý việc phân bổ tác vụ linh hoạt trên các hệ thống lớn.

Cpuset sử dụng **hệ thống con cgroup** tổng quát được mô tả trong phần [Control Groups](./Control_Groups.md).

---

Yêu cầu từ một tác vụ, sử dụng lệnh gọi hệ thống `sched_setaffinity(2)` để đưa CPU vào mặt nạ affinity của CPU, và sử dụng `mbind(2)` hoặc `set_mempolicy(2)` để đưa các nút bộ nhớ vào chính sách bộ nhớ, đều được lọc thông qua cpuset của tác vụ. Cụ thể:

* Những CPU hoặc nút bộ nhớ không thuộc cpuset của tác vụ sẽ bị lọc bỏ.
* **Bộ lập lịch (scheduler)** sẽ không lập lịch một tác vụ trên CPU không nằm trong `cpus_allowed`.
* **Bộ cấp phát trang của kernel (kernel page allocator)** sẽ không cấp phát trang bộ nhớ trên nút không nằm trong `mems_allowed`.

---

Ở mức người dùng (user level), có thể tạo và xóa cpuset theo tên trong hệ thống tệp ảo cgroup. Có thể quản lý các thuộc tính và quyền của cpuset, xác định CPU và nút bộ nhớ nào được gán cho mỗi cpuset, tra cứu và gán tác vụ (PID) vào cpuset tương ứng.

---

### 1.2 Tại sao cần cpuset?

Việc quản lý các hệ thống máy tính lớn, với nhiều bộ xử lý (CPU), cấu trúc bộ nhớ đệm phức tạp và nhiều **nút bộ nhớ (Memory Nodes)** có thời gian truy cập không đồng đều (NUMA), tạo ra nhiều thách thức cho việc lập lịch (scheduling) hiệu quả và phân bổ bộ nhớ cho các tiến trình.

---

Trong nhiều trường hợp, các hệ thống có quy mô vừa phải vẫn có thể hoạt động hiệu quả bằng cách **để hệ điều hành tự động chia sẻ tài nguyên CPU và bộ nhớ hiện có giữa các tác vụ** yêu cầu.

Tuy nhiên, với **các hệ thống lớn hơn**, việc phân bổ tài nguyên CPU và bộ nhớ cẩn thận sẽ giúp **giảm độ trễ truy cập bộ nhớ và tránh tranh chấp tài nguyên**, từ đó tận dụng hiệu quả khoản đầu tư lớn cho hệ thống. Khi đó, việc gán các tác vụ vào các tập con hệ thống có kích thước phù hợp sẽ đem lại hiệu quả tối ưu hơn.

---

Điều này đặc biệt hữu ích đối với:

* **Máy chủ web (Web Servers)** chạy nhiều phiên bản của cùng một ứng dụng web,
* **Máy chủ chạy nhiều ứng dụng khác nhau** (ví dụ như vừa là web server, vừa là cơ sở dữ liệu),
* **Hệ thống NUMA** chạy các ứng dụng HPC (tính toán hiệu năng cao) với yêu cầu hiệu suất khắt khe.

---

Những tập con này, hay còn gọi là các "phân vùng mềm (soft partitions)", cần có khả năng **điều chỉnh linh hoạt** theo sự thay đổi của khối lượng công việc, **mà không ảnh hưởng tới các tiến trình đang chạy song song** khác. Vị trí của các trang bộ nhớ của tác vụ đang chạy cũng có thể được thay đổi nếu vị trí bộ nhớ thay đổi.

---

Bản vá cpuset trong nhân (kernel) Linux cung cấp các cơ chế tối thiểu cần thiết để triển khai hiệu quả các tập con như vậy. Nó **tận dụng các cơ chế sẵn có** về gán CPU và bộ nhớ trong nhân Linux, **tránh tác động đến các phần quan trọng** như bộ lập lịch hoặc bộ cấp phát bộ nhớ.

---

### 1.3 Cpuset được triển khai như thế nào?

Cpuset cung cấp một cơ chế trong nhân Linux để giới hạn CPU và các nút bộ nhớ (Memory Nodes) được sử dụng bởi một tiến trình hoặc một nhóm tiến trình.

Nhân Linux đã có sẵn hai cơ chế để chỉ định các CPU mà một tiến trình có thể được lập lịch (qua `sched_setaffinity`) và các nút bộ nhớ mà tiến trình có thể sử dụng (qua `mbind`, `set_mempolicy`).

Cpuset mở rộng hai cơ chế này như sau:

* Cpuset là tập hợp các CPU và nút bộ nhớ được phép, được nhân kernel nhận biết.
* Mỗi tiến trình trong hệ thống đều được gắn vào một cpuset, thông qua một con trỏ trong cấu trúc task trỏ tới một cấu trúc cgroup có bộ đếm tham chiếu.
* Các lời gọi đến `sched_setaffinity` sẽ được lọc chỉ còn những CPU cho phép trong cpuset của tiến trình đó.
* Các lời gọi đến `mbind` và `set_mempolicy` cũng bị giới hạn chỉ sử dụng các nút bộ nhớ được phép trong cpuset của tiến trình.
* Cpuset gốc (root cpuset) chứa tất cả các CPU và nút bộ nhớ của hệ thống.
* Mỗi cpuset con có thể định nghĩa các cpuset con khác chứa tập con tài nguyên CPU và Memory Node của cpuset cha.
* Cây phân cấp của cpuset có thể được mount tại `/dev/cpuset`, cho phép duyệt và thao tác từ không gian người dùng.
* Một cpuset có thể được đánh dấu là "exclusive" – điều này đảm bảo không có cpuset nào khác (ngoại trừ tổ tiên trực tiếp hoặc con trực tiếp) có thể dùng chung CPU hoặc nút bộ nhớ với nó.
* Bạn có thể liệt kê tất cả các tiến trình (theo PID) đang được gán vào bất kỳ cpuset nào.

---

Việc triển khai cpuset chỉ yêu cầu một vài điểm móc (hook) đơn giản trong nhân Linux, không ảnh hưởng đến các đường dẫn quan trọng về hiệu năng:

* Trong `init/main.c`, để khởi tạo cpuset gốc khi hệ thống khởi động.
* Trong `fork` và `exit`, để gắn và tách tiến trình khỏi cpuset của nó.
* Trong `sched_setaffinity`, để lọc các CPU theo cpuset tương ứng.
* Trong `sched.c::migrate_live_tasks()`, để giữ cho các tác vụ di chuyển vẫn nằm trong các CPU được cpuset cho phép (nếu có thể).
* Trong `mbind` và `set_mempolicy`, để lọc các nút bộ nhớ theo cpuset tương ứng.
* Trong `page_alloc.c`, để giới hạn việc cấp phát bộ nhớ vào các node được cho phép.
* Trong `vmscan.c`, để giới hạn việc thu hồi bộ nhớ về đúng cpuset hiện tại.

---


Bạn nên **mount** hệ thống tập tin `"cgroup"` để cho phép duyệt và chỉnh sửa các cpuset hiện có trong kernel. Không có lời gọi hệ thống (system call) mới nào được thêm vào để hỗ trợ cpuset – tất cả việc truy vấn và sửa đổi cpuset đều được thực hiện thông qua hệ thống tập tin cpuset này.

Tập tin `/proc/<pid>/status` cho mỗi tiến trình sẽ có thêm bốn dòng, hiển thị:

* `cpus_allowed`: danh sách CPU mà tiến trình có thể được lập lịch trên đó.
* `mems_allowed`: danh sách các Memory Node mà tiến trình có thể sử dụng bộ nhớ từ đó.

Ví dụ:

```
Cpus_allowed:        ffffffff,ffffffff,ffffffff,ffffffff
Cpus_allowed_list:   0-127
Mems_allowed:        ffffffff,ffffffff
Mems_allowed_list:   0-63
```

---

Mỗi cpuset được đại diện bởi một thư mục trong hệ thống tập tin cgroup, chứa (ngoài các tập tin cgroup tiêu chuẩn) các tập tin sau mô tả cpuset đó:

* `cpuset.cpus`: danh sách các CPU trong cpuset đó.
* `cpuset.mems`: danh sách các Memory Node trong cpuset đó.
* `cpuset.memory_migrate`: cờ (flag) – nếu được đặt, sẽ di chuyển các trang bộ nhớ đến các node thuộc cpuset.
* `cpuset.cpu_exclusive`: cờ – cpuset có độc quyền sử dụng CPU không?
* `cpuset.mem_exclusive`: cờ – cpuset có độc quyền sử dụng bộ nhớ không?
* `cpuset.mem_hardwall`: cờ – có bắt buộc sử dụng memory node chỉ trong cpuset không?
* `cpuset.memory_pressure`: đo lường mức độ áp lực bộ nhớ trong cpuset.
* `cpuset.memory_spread_page`: cờ – nếu đặt, cache trang bộ nhớ sẽ được phân tán đều trên các node được phép.
* `cpuset.memory_spread_slab`: **ĐÃ BỎ** – không còn chức năng.
* `cpuset.sched_load_balance`: cờ – nếu đặt, cho phép cân bằng tải giữa các CPU trong cpuset.
* `cpuset.sched_relax_domain_level`: mức độ tìm kiếm khi di chuyển các tiến trình.

---

Ngoài ra, chỉ có cpuset gốc (root cpuset) có thêm tập tin sau:

* `cpuset.memory_pressure_enabled`: cờ – bật/tắt việc tính toán memory\_pressure?

---

Các cpuset mới được tạo bằng cách sử dụng lời gọi hệ thống `mkdir` hoặc lệnh shell thông thường. Các thuộc tính của một cpuset, chẳng hạn như cờ (flag), các CPU và Node bộ nhớ được cho phép, và các tác vụ (task) được gán, có thể được chỉnh sửa bằng cách ghi vào các tập tin thích hợp trong thư mục của cpuset đó, như đã liệt kê ở phần trước.

Cấu trúc phân cấp có tên của các cpuset lồng nhau cho phép phân chia một hệ thống lớn thành các phần lồng nhau, có thể thay đổi động, được gọi là “phân vùng mềm” (*soft-partitions*).

Việc gán mỗi tác vụ (task), được kế thừa tự động khi `fork` bởi bất kỳ tiến trình con nào, vào một cpuset, cho phép tổ chức tải công việc trên hệ thống thành các nhóm tác vụ có liên quan, sao cho mỗi nhóm bị ràng buộc phải sử dụng các CPU và Node bộ nhớ của một cpuset cụ thể. Một tác vụ có thể được gán lại vào bất kỳ cpuset nào khác nếu quyền truy cập vào các thư mục hệ thống cpuset cho phép điều đó.

Việc quản lý hệ thống ở quy mô lớn như vậy sẽ tích hợp một cách mượt mà với quá trình phân bổ chi tiết cho từng tiến trình và vùng bộ nhớ, bằng cách sử dụng các lời gọi hệ thống `sched_setaffinity`, `mbind` và `set_mempolicy`.

---

**Các quy tắc sau được áp dụng cho mỗi cpuset:**

* CPU và Node bộ nhớ của nó phải là một tập con của cpuset cha.
* Không thể được đánh dấu là "exclusive" trừ khi cpuset cha cũng là "exclusive".
* Nếu CPU hoặc bộ nhớ là "exclusive", thì chúng không được trùng lặp với bất kỳ cpuset anh chị em nào khác.

---

Những quy tắc này, cùng với cấu trúc phân cấp tự nhiên của cpuset, cho phép thực thi hiệu quả cam kết “exclusive” (độc quyền), mà không cần phải quét toàn bộ cpuset mỗi khi có thay đổi để đảm bảo rằng không có cpuset nào chồng lấn nhau. Ngoài ra, việc sử dụng hệ thống tập tin ảo (VFS) của Linux để biểu diễn hệ phân cấp cpuset cung cấp một không gian tên và quyền truy cập quen thuộc, với yêu cầu tối thiểu về mã kernel bổ sung.

Các tập tin `cpus` và `mems` trong cpuset gốc (top\_cpuset) là chỉ đọc (read-only). Tập tin `cpus` sẽ tự động theo dõi giá trị của `cpu_online_mask` bằng cách sử dụng thông báo hotplug của CPU, còn tập tin `mems` sẽ theo dõi tự động giá trị của `node_states[N_MEMORY]` — tức là các node có bộ nhớ — bằng hook `cpuset_track_online_nodes()`.

Các tập tin `cpuset.effective_cpus` và `cpuset.effective_mems` thông thường là bản sao chỉ đọc của `cpuset.cpus` và `cpuset.mems`. Nếu hệ thống tệp cpuset được mount với tùy chọn đặc biệt `"cpuset_v2_mode"`, hành vi của các tập tin này sẽ giống với các tập tin tương ứng trong cpuset phiên bản 2. Nói cách khác, các sự kiện hotplug sẽ không thay đổi `cpuset.cpus` và `cpuset.mems`. Những sự kiện này chỉ ảnh hưởng đến `cpuset.effective_cpus` và `cpuset.effective_mems`, hai tập tin này thể hiện các CPU và node bộ nhớ thực tế hiện đang được cpuset sử dụng.

**Xem [Control Group v2](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)** để biết thêm thông tin về hành vi của cpuset phiên bản 2.

---

### 1.4 Cpuset độc quyền (exclusive) là gì?

Nếu một cpuset được đánh dấu là **cpu exclusive** hoặc **mem exclusive**, thì **không có cpuset nào khác**, ngoại trừ **tổ tiên trực tiếp hoặc hậu duệ trực tiếp**, được phép chia sẻ bất kỳ CPU hoặc Memory Node nào với nó.

Một cpuset được thiết lập với `cpuset.mem_exclusive` **hoặc** `cpuset.mem_hardwall` được gọi là **"hardwalled"**, tức là nó giới hạn việc cấp phát bộ nhớ của kernel cho các trang (page), buffer và dữ liệu khác mà kernel thường chia sẻ giữa nhiều người dùng. Tất cả các cpuset — dù có "hardwalled" hay không — đều giới hạn việc cấp phát bộ nhớ cho không gian người dùng. Điều này cho phép cấu hình hệ thống sao cho nhiều tác vụ độc lập có thể chia sẻ dữ liệu kernel chung, như các trang hệ thống tập tin, trong khi vẫn cách ly việc cấp phát bộ nhớ cho từng tác vụ người dùng riêng biệt trong cpuset riêng của nó.

Để làm điều này, cần tạo một cpuset lớn có thuộc tính `mem_exclusive` để chứa tất cả các tác vụ, sau đó tạo các cpuset con — không có `mem_exclusive` — dành riêng cho từng tác vụ.

Chỉ một lượng rất nhỏ bộ nhớ kernel thông thường — chẳng hạn như các yêu cầu từ **trình xử lý ngắt (interrupt handlers)** — được phép lấy ngoài cpuset có `mem_exclusive`.

---

### 1.5 Áp lực bộ nhớ (memory\_pressure) là gì?

`memory_pressure` của một cpuset cung cấp một **chỉ số đơn lẻ trên mỗi cpuset** về **tốc độ** mà các tác vụ trong cpuset đó đang cố gắng **giải phóng bộ nhớ** trên các node bộ nhớ được gán cho cpuset, nhằm đáp ứng các yêu cầu bộ nhớ bổ sung.

Chỉ số này giúp các bộ quản lý tác vụ hàng loạt (batch manager) giám sát các tác vụ đang chạy trong các cpuset chuyên dụng một cách hiệu quả, để phát hiện **mức độ áp lực bộ nhớ** mà mỗi tác vụ đang gây ra.

Điều này đặc biệt hữu ích trên các hệ thống quản lý chặt chẽ, nơi có nhiều loại tác vụ gửi vào cùng lúc, mà hệ thống có thể cần phải **chấm dứt** hoặc **ưu tiên lại** các tác vụ đang sử dụng nhiều bộ nhớ hơn mức được chỉ định. Nó cũng rất quan trọng với các tác vụ tính toán khoa học quy mô lớn, chạy lâu dài, vốn dễ thất bại nghiêm trọng nếu vượt quá ngưỡng sử dụng bộ nhớ được cấp phát.

Cơ chế này cung cấp một cách **kinh tế và hiệu quả** để người quản lý batch giám sát cpuset để phát hiện dấu hiệu của áp lực bộ nhớ. Việc hành động như thế nào là tùy thuộc vào batch manager hoặc mã chương trình của người dùng.

---

**Lưu ý:** Tính năng này **chỉ được bật** khi ghi `"1"` vào file `/dev/cpuset/memory_pressure_enabled`. Nếu không bật cờ này, mã cân bằng bộ nhớ trong hàm `__alloc_pages()` sẽ **không tính toán chỉ số `memory_pressure`** và chỉ nhận biết rằng cờ đang tắt.

---

**Tại sao cần dùng chỉ số chạy trung bình theo từng cpuset?**

* Vì chỉ số này tính trên từng cpuset, **không phải trên từng tác vụ hoặc từng vùng bộ nhớ**, nên hệ thống tránh được việc phải quét toàn bộ danh sách tác vụ → giảm tải đáng kể trên hệ thống lớn.

* Vì đây là **giá trị trung bình động**, thay vì bộ đếm cộng dồn, nên bộ lập lịch batch có thể phát hiện áp lực bộ nhớ chỉ trong một lần đọc duy nhất, thay vì phải theo dõi nhiều lần để tích lũy kết quả.

* Vì nó tính theo từng cpuset, nên có thể lấy thông tin áp lực bộ nhớ nhanh chóng chỉ qua một lần đọc, thay vì phải truy vấn toàn bộ các tác vụ (có thể thay đổi liên tục) trong cpuset.

---

**Cơ chế hoạt động**

Một **bộ lọc số đơn giản** được duy trì cho mỗi cpuset (gồm một spinlock và ba từ dữ liệu), được cập nhật bởi bất kỳ tác vụ nào trong cpuset nếu nó kích hoạt mã reclaim bộ nhớ theo kiểu đồng bộ (trực tiếp).

File `memory_pressure` của cpuset cung cấp một số nguyên, biểu thị tốc độ gần đây (nửa vòng đời 10 giây) của các đợt reclaim trang trực tiếp do các tác vụ trong cpuset gây ra, tính bằng số reclaim/giây và nhân với 1000.

---

### 1.6 Memory spread là gì?

Có hai **cờ dạng boolean** cho mỗi cpuset để điều khiển nơi kernel phân bổ các trang bộ nhớ cho buffer hệ thống tệp và các cấu trúc dữ liệu liên quan trong kernel. Chúng là:

* `cpuset.memory_spread_page`
* `cpuset.memory_spread_slab`

---

* Nếu cờ `cpuset.memory_spread_page` được bật, kernel sẽ phân bổ **các buffer hệ thống tệp (page cache)** đều trên **tất cả các node bộ nhớ** mà tác vụ được phép sử dụng, thay vì ưu tiên ghi lên node nơi tác vụ đang chạy.

* Nếu cờ `cpuset.memory_spread_slab` được bật, kernel sẽ phân bổ **các cache slab hệ thống tệp** (ví dụ inode, dentry) đều trên tất cả các node mà tác vụ được phép sử dụng, thay vì ưu tiên ghi lên node đang chạy tác vụ đó.

Các cờ này **không ảnh hưởng** đến vùng dữ liệu ẩn danh hay ngăn xếp (stack) của một tiến trình.

---

**Mặc định:**

* Các cờ này **tắt** (giá trị "0") → các trang bộ nhớ được phân bổ trên **node local**, tức là node nơi tác vụ đang chạy.
* Nếu bật (`"1"`), kernel sẽ áp dụng chính sách phân bổ bộ nhớ rải đều (spread).

---

**Kế thừa:**

* Khi tạo cpuset mới, nó **kế thừa** cấu hình memory spread từ cpuset cha.

---

**Ảnh hưởng đến NUMA:**

* Nếu bật memory spread, việc phân bổ sẽ **bỏ qua** cấu hình `mempolicy` NUMA.
* Gọi `mbind()` hoặc `set_mempolicy()` cũng không có tác dụng nếu memory spread đang bật.
* Nếu tắt memory spread → `mempolicy` NUMA hiện tại sẽ lại có hiệu lực.

---

**Cách triển khai (implementation):**

1. **`cpuset.memory_spread_page`**:

   * Bật cờ này → gán cờ `PFA_SPREAD_PAGE` cho từng tiến trình.
   * Khi cần phân trang, kernel gọi hàm `cpuset_mem_spread_node()` để chọn node tiếp theo để phân bổ theo thứ tự vòng tròn (round-robin).

2. **`cpuset.memory_spread_slab`**:

   * Bật cờ này → gán `PFA_SPREAD_SLAB` cho cache slab.
   * Các slab sẽ được phân đều lên các node do `cpuset_mem_spread_node()` trả về.

---

**Thuật toán lựa chọn node:**

* Dựa trên biến `cpuset_mem_spread_rotor` riêng của từng tiến trình.
* Biến này chọn **node tiếp theo** từ danh sách `mems_allowed` của cpuset → phân bổ theo vòng tròn (round-robin hoặc interleave).

---

**Lợi ích:**

Chính sách memory spread có thể giúp:

* Các job truy cập dữ liệu **phân tán** hiệu quả hơn (ví dụ thread đọc ghi song song).
* Giảm **thiên lệch phân bổ bộ nhớ** trong job (nếu chỉ có một thread truy cập một vùng dữ liệu → các node có thể bị phân bố lệch nếu không có memory spread).

---

### 1.7 sched\_load\_balance là gì?

Bộ lập lịch của kernel (`kernel/sched/core.c`) tự động **cân bằng tải các tác vụ giữa các CPU**. Nếu một CPU bị sử dụng ít, đoạn mã của kernel đang chạy trên CPU đó sẽ tìm kiếm các tác vụ từ các CPU khác đang bị quá tải và di chuyển chúng sang CPU hiện tại — trong giới hạn của các cơ chế như `cpusets` và `sched_setaffinity`.

---

**Tại sao cần chia sched domain?**

Chi phí thuật toán của việc cân bằng tải tăng lên **hơn tuyến tính** theo số lượng CPU được cân bằng. Điều này ảnh hưởng đến các cấu trúc dữ liệu kernel chia sẻ như **task list**.

→ Kernel hỗ trợ chia hệ thống CPU thành **sched domain** nhỏ hơn để chỉ cân bằng trong từng sched domain.

* Mỗi `sched domain` bao phủ một tập con các CPU.
* **Không có sched domain nào chồng lắp nhau**.
* Một số CPU có thể không nằm trong sched domain nào → **không được cân bằng tải**.

---

**Tóm tắt:**

* **Cân bằng tải giữa hai domain nhỏ tốn ít chi phí hơn** so với một domain lớn.
* Nhưng nhược điểm: một domain có thể bị quá tải, và **không được hỗ trợ từ domain còn lại**.

---

**Mặc định:**

* Có một sched domain bao phủ **toàn bộ CPU** (kể cả CPU bị "isolate" qua `isolcpus=` ở kernel boot).
* Tuy nhiên, **CPU bị isolate sẽ không tham gia cân bằng tải**, trừ khi được gán cụ thể.

---

**Các tình huống mà mặc định này **không phù hợp**:**

1. **Hệ thống lớn**: cân bằng toàn bộ CPU rất tốn kém → không cần thiết nếu các tác vụ độc lập chạy riêng trên từng cpuset.
2. **Hệ thống real-time**: cần giảm chi phí hệ thống tối đa → nên **tránh cân bằng tải tự động** nếu không cần.

---

**Cờ `cpuset.sched_load_balance`**

* **Mặc định: `enabled`**

  * → Tất cả CPU trong cpuset được gộp chung vào **một sched domain**.
  * → Kernel được phép di chuyển tác vụ giữa các CPU trong cpuset (nếu không bị `sched_setaffinity` chặn).

* **Khi `disabled`:**

  * Kernel **tránh cân bằng tải** giữa các CPU trong cpuset.
  * Ngoại lệ: nếu một cpuset con có `sched_load_balance` bật → kernel có thể cho phép cân bằng giữa các CPU đó.

---

**Ví dụ:**

Nếu **cpuset cha (top)** có `cpuset.sched_load_balance` bật:

* Kernel xem toàn bộ CPU như một sched domain.
* → Việc bật/tắt `sched_load_balance` ở các cpuset con **không có tác dụng**.

→ Nếu muốn kiểm soát tốt hơn:

* Hãy **tắt `sched_load_balance` ở cpuset cha**.
* Và **chỉ bật ở một số cpuset con** cần cân bằng.

---

Khi thực hiện việc này, bạn thường **không muốn để bất kỳ tác vụ nào chưa được ghim (unpinned)** trong cpuset gốc (`top cpuset`) mà có thể sử dụng một lượng CPU đáng kể, vì những tác vụ này có thể bị giới hạn một cách giả tạo chỉ sử dụng một phần tập CPU nhất định, phụ thuộc vào cách cờ `sched_load_balance` được thiết lập trong các cpuset con. Ngay cả khi tác vụ đó có thể sử dụng chu kỳ CPU rảnh ở các CPU khác, bộ lập lịch của kernel **có thể không cân nhắc** đến khả năng cân bằng tải của tác vụ đó sang CPU đang bị sử dụng thấp.

Tất nhiên, những tác vụ đã được ghim cố định vào một CPU cụ thể có thể **nằm trong cpuset đã tắt `cpuset.sched_load_balance`**, vì chúng vốn dĩ cũng sẽ không chuyển đi đâu.

---

Có một sự **mismatch (không tương thích)** ở đây giữa `cpusets` và `sched domains`.

* **Cpusets là phân cấp và có dạng lồng nhau.**
* **Sched domains thì phẳng** (flat); không chồng lắp, và **mỗi CPU chỉ thuộc tối đa một sched domain**.

Sched domains **phải phẳng**, vì việc cân bằng tải trên các tập CPU chồng lắp một phần sẽ dẫn đến **động học không ổn định** — điều này nằm ngoài khả năng điều khiển của chúng ta.
→ Nếu hai cpusets chồng chéo mà đều bật `cpuset.sched_load_balance`, kernel sẽ tạo ra một sched domain bao trùm cả hai. Tác vụ sẽ không được chuyển ra ngoài cpuset của nó, **nhưng kernel vẫn phải kiểm tra**, gây lãng phí chu kỳ tính toán không cần thiết.

---

Chính sự khác biệt này làm cho **không thể có một mối quan hệ đơn giản 1–1** giữa cpuset bật `cpuset.sched_load_balance` và cách các sched domain được cấu hình:

* Nếu **cpuset bật cờ này**, nó sẽ được cân bằng tải với toàn bộ các CPU trong nó.
* Nhưng **nếu tắt cờ này**, nó **chỉ được đảm bảo không bị cân bằng tải** khi không có cpuset nào chồng lắp bật cờ.

---

Nếu hai cpuset có vùng `cpuset.cpus` **chồng lắp một phần**, và chỉ một trong hai có bật cờ:
→ Tác vụ của cpuset kia sẽ chỉ được **cân bằng một phần**, trên phần CPU chồng lắp.

Ví dụ như cpuset gốc (`top_cpuset`):

* Đừng để các tác vụ tiêu tốn nhiều tài nguyên **trôi nổi trong các cpuset có vùng CPU chỉ chồng lắp một phần**, vì kernel có thể **không cân bằng tải đủ**.

---

**CPUs nằm trong `cpuset.isolcpus`** sẽ **không bao giờ được cân bằng tải**, vì đã bị loại trừ từ đầu thông qua tùy chọn kernel boot `isolcpus=...`.
→ Không bị ảnh hưởng bởi giá trị của `cpuset.sched_load_balance` trong bất kỳ cpuset nào.

---


#### 1.7.1 Chi tiết triển khai `sched_load_balance`

Cờ `cpuset.sched_load_balance` theo từng cpuset **mặc định là bật** (khác với hầu hết các cờ cpuset khác).
Khi được bật cho một cpuset, kernel sẽ đảm bảo rằng **nó có thể thực hiện cân bằng tải trên tất cả các CPU trong cpuset đó**
(điều này có nghĩa là tất cả các CPU trong `cpus_allowed` của cpuset đó đều phải thuộc cùng một sched domain).

Nếu **hai cpuset có vùng CPU chồng lắp nhau** và **cả hai đều bật `cpuset.sched_load_balance`**, thì **chúng sẽ thuộc cùng một sched domain** (hoặc bắt buộc phải vậy).

Nếu cpuset gốc (`top cpuset`) **bật `cpuset.sched_load_balance`** (đây là mặc định), thì như đã đề cập trước đó, **toàn bộ hệ thống sẽ chỉ có một sched domain duy nhất**, bao trùm tất cả CPU, bất kể các thiết lập khác của những cpuset con là gì.

---

Kernel cam kết với userspace rằng **nó sẽ tránh cân bằng tải nếu có thể**.
Tuy nhiên, nó vẫn sẽ chia nhỏ thành các sched domain có độ chi tiết cao nhất có thể để phục vụ việc cân bằng tải **trên các tập CPU được cho phép** của cpuset **bật `cpuset.sched_load_balance`**.

---

**Giao diện giữa cpuset nội bộ và scheduler** truyền từ mã cpuset sang mã scheduler **một phân vùng các CPU cần cân bằng tải trong hệ thống**.
Phân vùng này là **tập hợp các tập con** (biểu diễn bằng mảng các struct `cpumask`) gồm các CPU **không chồng lắp nhau**, và bao phủ toàn bộ CPU cần cân bằng tải.

---

Mã cpuset sẽ xây dựng phân vùng mới này và truyền nó cho mã scheduler (trong phần setup sched domain), để **rebuild sched domain mỗi khi có thay đổi**, bao gồm:

* Khi cờ `cpuset.sched_load_balance` của một cpuset (với các CPU không rỗng) thay đổi.
* Khi một CPU được thêm vào hoặc rời khỏi cpuset có cờ này bật.
* Khi `cpuset.sched_relax_domain_level` của một cpuset có CPU thay đổi trong lúc cờ `sched_load_balance` đang bật.
* Khi một cpuset có CPU bị **gỡ bỏ cờ `sched_load_balance`**.
* Khi một CPU bị **tắt/mở (offlined/onlined)**.

---

Phân vùng này **xác định chính xác** sched domain mà kernel sẽ thiết lập — mỗi phần tử trong `cpumask` là một sched domain riêng biệt.

---

**Scheduler sẽ nhớ các sched domain đang hoạt động hiện tại.**
Khi **hàm `partition_sched_domains()`** được gọi từ mã cpuset để cập nhật sched domains, kernel sẽ **so sánh phân vùng mới với phân vùng hiện tại** và thực hiện cập nhật nếu khác biệt — **xóa domain cũ và thêm domain mới tương ứng** với từng thay đổi.

---

### 1.8 `sched_relax_domain_level` là gì?

Trong sched domain (miền lập lịch), trình lập lịch (scheduler) di chuyển các tác vụ theo 2 cách:

* Cân bằng tải định kỳ theo chu kỳ tick.
* Và tại các thời điểm xảy ra một số sự kiện lập lịch đặc biệt.

---

Khi một tác vụ được đánh thức, scheduler sẽ cố gắng di chuyển nó sang một CPU đang nhàn rỗi.

Ví dụ: nếu một tác vụ A đang chạy trên CPU X và đánh thức tác vụ B cũng thuộc cùng CPU X,
**và nếu CPU Y là “sibling” (cùng lõi hoặc cùng nhóm) với CPU X và đang nhàn rỗi**,
thì scheduler có thể **di chuyển tác vụ B sang CPU Y** để B có thể bắt đầu thực hiện **mà không phải chờ tác vụ A kết thúc trên CPU X**.

---

Tương tự, nếu một CPU hết tác vụ trong hàng đợi (runqueue), nó sẽ cố gắng kéo thêm tác vụ từ các CPU đang bận khác để xử lý sớm hơn trước khi rảnh hoàn toàn.

---

Tuy nhiên, quá trình tìm kiếm các tác vụ có thể di chuyển hoặc các CPU rảnh cũng mất thời gian.
Vì vậy, scheduler **không phải lúc nào cũng tìm kiếm toàn bộ CPU trong domain**.
Trên một số kiến trúc, **phạm vi tìm kiếm bị giới hạn trong cùng socket hoặc node** (nơi CPU đó nằm), còn cân bằng tải theo tick thì tìm khắp nơi.

---

Ví dụ:

Giả sử CPU Z nằm khá xa so với CPU X.
Ngay cả khi CPU Z đang rảnh mà CPU X và các “sibling” của nó đang bận,
scheduler **không thể di chuyển tác vụ B từ CPU X sang CPU Z** vì Z nằm ngoài **phạm vi tìm kiếm**.
Kết quả là tác vụ B trên CPU X phải **chờ tác vụ A hoàn tất hoặc chờ tick tiếp theo để được cân bằng tải**.

Trong một số ứng dụng yêu cầu phản hồi thời gian ngắn, việc **chờ 1 tick có thể là quá lâu**.

---

Tệp `cpuset.sched_relax_domain_level` cho phép bạn **tùy chỉnh phạm vi tìm kiếm** theo mong muốn.

Tệp này nhận một **giá trị số nguyên** biểu thị cấp độ phạm vi tìm kiếm theo bảng sau (giá trị mặc định là `-1`, nghĩa là không yêu cầu đặc biệt và sử dụng cấu hình hệ thống):

| Giá trị | Ý nghĩa                                                                    |
| ------- | -------------------------------------------------------------------------- |
| -1      | Không yêu cầu. Dùng mặc định hệ thống hoặc theo yêu cầu từ nơi khác.       |
| 0       | Không tìm kiếm gì cả.                                                      |
| 1       | Tìm trong các “sibling” (ví dụ: hyperthreads cùng một core).               |
| 2       | Tìm trong các core cùng một package (bộ xử lý vật lý).                     |
| 3       | Tìm trong tất cả các CPU của một node (= toàn hệ thống nếu không có NUMA). |
| 4       | Tìm trong các node trong một nhóm (chunk) \[trên hệ thống NUMA].           |
| 5       | Tìm trên toàn bộ hệ thống \[trên hệ thống NUMA].                           |

---

Không phải tất cả các cấp độ tìm kiếm đều có thể tồn tại, và các giá trị có thể thay đổi tùy thuộc vào kiến trúc hệ thống và cấu hình kernel.
Hãy kiểm tra tại đường dẫn:

```
/sys/kernel/debug/sched/domains/cpu*/domain*/
```

để biết thông tin cụ thể của hệ thống.

---

Giá trị mặc định của hệ thống phụ thuộc vào kiến trúc phần cứng.
Giá trị mặc định này có thể được thay đổi thông qua tham số khởi động kernel: `relax_domain_level=`.

---

Tệp này là theo từng **cpuset riêng biệt** và ảnh hưởng đến sched domain mà cpuset đó thuộc về.
Vì vậy, nếu **cpuset** có **flag `cpuset.sched_load_balance` bị tắt**, thì **`cpuset.sched_relax_domain_level` sẽ không có tác dụng** vì cpuset đó **không thuộc sched domain nào** cả.

---

Nếu nhiều cpuset **bị chồng lặp lên nhau** và vì thế hình thành một sched domain chung, thì **giá trị lớn nhất** trong số các `sched_relax_domain_level` sẽ được sử dụng.
**Hãy cẩn thận:** nếu một cpuset yêu cầu mức 0 và các cpuset khác là `-1` (không yêu cầu), thì **giá trị 0 sẽ được dùng**.

---

Lưu ý rằng: việc sửa đổi tệp này **có thể có cả tác động tốt lẫn xấu**, và việc nó có phù hợp hay không phụ thuộc vào từng tình huống cụ thể.
**Không nên chỉnh sửa nếu bạn không chắc chắn.**

---

**Nếu bạn đang trong các tình huống sau:**

* **Chi phí di chuyển giữa các CPU là rất nhỏ** (đối với bạn), do ứng dụng của bạn có hành vi đặc biệt hoặc có phần cứng hỗ trợ tốt cho việc truy cập cache CPU.
* **Chi phí tìm kiếm không đáng kể** với bạn, hoặc bạn có thể giảm chi phí tìm kiếm đủ nhỏ bằng cách tổ chức lại cpuset sao cho gọn gàng.
* **Độ trễ là cần thiết**, ngay cả khi phải hy sinh tỷ lệ trúng cache (cache hit rate), thì **việc tăng `sched_relax_domain_level` là có lợi**.

---


### 1.9 Tôi sử dụng cpusets như thế nào?

Để giảm thiểu tác động của cpusets lên các mã kernel quan trọng như bộ lập lịch (scheduler), và vì kernel không hỗ trợ việc một tiến trình thay đổi trực tiếp vị trí bộ nhớ của tiến trình khác, nên tác động đến một tiến trình khi thay đổi CPU hoặc vùng nhớ (Memory Nodes) của cpuset mà nó đang gắn vào, hoặc khi chuyển tiến trình đó sang cpuset khác, sẽ chỉ xảy ra một cách tinh tế, không trực tiếp.

---

Nếu một cpuset bị thay đổi các **Memory Nodes**, thì với mỗi tiến trình được gắn vào cpuset đó, lần tiếp theo kernel cố gắng cấp phát một trang bộ nhớ cho tiến trình đó, kernel sẽ phát hiện thay đổi trong cpuset và cập nhật vị trí bộ nhớ riêng của tiến trình (per-task memory placement) sao cho phù hợp với cpuset mới.

* Nếu tiến trình đang sử dụng `mempolicy MPOL_BIND`, và các node được gán trong `MPOL_BIND` vẫn còn nằm trong cpuset mới, thì tiến trình sẽ tiếp tục sử dụng các node đó.
* Nếu các node `MPOL_BIND` không còn hợp lệ trong cpuset mới, tiến trình sẽ được xử lý như thể đang được gán lại MPOL\_BIND vào cpuset mới, mặc dù cấu hình NUMA không thay đổi (theo `get_mempolicy()`).
* Nói cách khác, nếu một tiến trình được chuyển sang cpuset khác, kernel sẽ điều chỉnh lại vị trí cấp phát bộ nhớ của tiến trình đó trong lần tiếp theo khi cần cấp phát trang bộ nhớ.

---

Nếu cpuset bị thay đổi `cpuset.cpus`, thì tất cả các tiến trình trong cpuset đó sẽ được cập nhật ngay lập tức vùng CPU được phép chạy.

* Tương tự, nếu `pid` của một tiến trình được ghi vào tệp `tasks` của một cpuset khác, vùng CPU được phép chạy của tiến trình sẽ được cập nhật ngay lập tức.
* Nếu trước đó tiến trình đã bị ép buộc chạy trên một tập con CPU cụ thể bởi `sched_setaffinity()`, thì sau khi chuyển sang cpuset mới, nó sẽ được phép chạy trên bất kỳ CPU nào trong cpuset mới, làm vô hiệu hóa hiệu lực của `sched_setaffinity()` trước đó.

---

Tóm lại:

* Vị trí bộ nhớ (memory placement) của một tiến trình sẽ được kernel cập nhật **khi trang bộ nhớ tiếp theo được cấp phát**.
* Vị trí xử lý (processor placement) thì được cập nhật **ngay lập tức**.

---

Thông thường, sau khi một trang được cấp phát (tức là được ánh xạ tới một vùng vật lý của bộ nhớ chính), thì trang đó sẽ giữ nguyên node mà nó đã được đặt, miễn là nó còn tồn tại trong bộ nhớ, **ngay cả khi cấu hình `cpuset.mems` có thay đổi** sau đó.

* Nếu `cpuset.memory_migrate` được thiết lập thành **true**, thì khi tiến trình được gán vào cpuset đó:

  * Bất kỳ trang bộ nhớ nào mà tiến trình đó đã sử dụng trước đó ở cpuset cũ sẽ được di chuyển sang cpuset mới.
  * Kernel sẽ cố gắng giữ nguyên mối quan hệ tương đối giữa các node nếu có thể. Ví dụ: nếu trang ở node thứ hai trong cpuset cũ, nó sẽ được đặt ở node thứ hai trong cpuset mới (nếu hợp lệ).

---

Ngoài ra:

* Nếu `cpuset.memory_migrate` là **true**, và `cpuset.mems` bị thay đổi:

  * Tất cả các trang bộ nhớ đã được gán cho các tiến trình trong cpuset đó, nằm trên các node không còn thuộc `cpuset.mems` mới, sẽ được **di chuyển sang các node mới** theo thiết lập mới.
  * Những trang không nằm trong cpuset cũ hoặc nằm ngoài vùng được `cpuset.mems` chỉ định, **sẽ không bị di chuyển**.

---

**Có một ngoại lệ thứ hai đối với phần trên**

`GFP_ATOMIC` là các yêu cầu cấp phát bộ nhớ bên trong kernel mà **phải được thỏa mãn ngay lập tức**. Kernel có thể bỏ qua một số yêu cầu, và trong vài trường hợp hiếm hoi thậm chí **có thể panic** nếu một phép cấp phát `GFP_ATOMIC` thất bại.

Nếu yêu cầu đó **không thể được thỏa mãn trong cpuset hiện tại** của tiến trình, thì kernel sẽ **nới lỏng giới hạn cpuset**, và tìm bộ nhớ ở bất kỳ nơi nào có thể. Điều này tốt hơn việc giữ ràng buộc cpuset quá chặt và khiến kernel gặp lỗi.

---

**Các bước để khởi chạy một tiến trình mới trong một cpuset**

1. Tạo thư mục mới: `mkdir /sys/fs/cgroup/cpuset`
2. Mount hệ thống tệp cpuset:
   `mount -t cgroup -ocpuset cpuset /sys/fs/cgroup/cpuset`
3. Tạo cpuset mới bằng cách `mkdir` và ghi vào các file tương ứng trong `/sys/fs/cgroup/cpuset`.
4. Khởi chạy tiến trình đầu tiên của job (gọi là "founding father").
5. Gắn tiến trình đó vào cpuset mới bằng cách ghi PID vào tệp `tasks` của cpuset đó.
6. Tạo tiến trình con (fork), exec hoặc clone từ tiến trình cha đã được gắn.

---

**Ví dụ: tạo cpuset tên “Charlie” chỉ chứa CPU 2 và 3, và Memory Node 1**

```bash
mount -t cgroup -ocpuset cpuset /sys/fs/cgroup/cpuset
cd /sys/fs/cgroup/cpuset
mkdir Charlie
cd Charlie
/bin/echo 2-3 > cpuset.cpus
/bin/echo 1 > cpuset.mems
/bin/echo $$ > tasks
sh
# Subshell 'sh' hiện tại đang chạy trong cpuset Charlie
# Dòng tiếp theo sẽ hiển thị đường dẫn là '/Charlie'
cat /proc/self/cpuset
```

---

**Các cách để truy vấn hoặc thay đổi cpuset:**

* Truy cập trực tiếp hệ thống file cpuset bằng các lệnh như `cd`, `mkdir`, `echo`, `cat`, `rmdir` từ shell (hoặc tương đương trong ngôn ngữ C).
* Qua thư viện C `libcgroup`: [https://github.com/libcgroup/libcgroup/](https://github.com/libcgroup/libcgroup/libcgroup/)
* Qua thư viện Python `cset`: [http://code.google.com/p/cpuset/](http://code.google.com/p/cpuset/)
* Qua các chương trình tiện ích: `runon`, `taskset` (của SGI hoặc Robert Love)
* Qua `numactl` để thiết lập chính sách bộ nhớ (`mbind`, `set_mempolicy`)

---

## 2. Ví dụ sử dụng và cú pháp

### 2.1 Sử dụng cơ bản

Việc tạo, chỉnh sửa và sử dụng cpuset có thể thực hiện thông qua hệ thống tập tin ảo cpuset (cpuset virtual filesystem).

Để mount nó, hãy gõ lệnh:

```bash
# mount -t cgroup -o cpuset cpuset /sys/fs/cgroup/cpuset
```

Sau đó, trong thư mục `/sys/fs/cgroup/cpuset`, bạn sẽ thấy một cây thư mục tương ứng với cấu trúc cây của các cpuset trong hệ thống. Ví dụ, `/sys/fs/cgroup/cpuset` là cpuset gốc chứa toàn bộ hệ thống.

Nếu bạn muốn tạo một cpuset mới bên trong `/sys/fs/cgroup/cpuset`:

```bash
# cd /sys/fs/cgroup/cpuset
# mkdir my_cpuset
```

Giờ bạn muốn làm gì đó với cpuset này:

```bash
# cd my_cpuset
```

Trong thư mục này, bạn có thể thấy nhiều tệp như sau:

```bash
# ls
cgroup.clone_children        cpuset.memory_pressure
cgroup.event_control         cpuset.memory_spread_page
cgroup.procs                 cpuset.memory_spread_slab
cpuset.cpu_exclusive         cpuset.mems
cpuset.cpus                  cpuset.sched_load_balance
cpuset.mem_exclusive         cpuset.sched_relax_domain_level
cpuset.mem_hardwall          notify_on_release
cpuset.memory_migrate        tasks
```

Việc đọc các tệp này sẽ cung cấp cho bạn thông tin về trạng thái của cpuset đó: những CPU và nút bộ nhớ (Memory Nodes) mà nó có thể sử dụng, các tiến trình đang sử dụng nó, và các thuộc tính liên quan.
**Bằng cách ghi vào các tệp này, bạn có thể điều khiển và cấu hình cpuset.**

---

**Đặt một số cờ:**

```bash
# /bin/echo 1 > cpuset.cpu_exclusive
```

**Thêm một số CPU:**

```bash
# /bin/echo 0-7 > cpuset.cpus
```

**Thêm một số nút bộ nhớ (mems):**

```bash
# /bin/echo 0-7 > cpuset.mems
```

**Gắn shell hiện tại của bạn vào cpuset này:**

```bash
# /bin/echo $$ > tasks
```

**Bạn cũng có thể tạo các cpuset bên trong cpuset của bạn bằng cách sử dụng `mkdir` trong thư mục này:**

```bash
# mkdir my_sub_cs
```

**Để xóa một cpuset, chỉ cần dùng lệnh `rmdir`:**

```bash
# rmdir my_sub_cs
```

> *Lưu ý:* Lệnh này sẽ thất bại nếu cpuset đang được sử dụng (có cpuset con bên trong hoặc có tiến trình đang gắn vào).

---

**Lưu ý:** vì lý do tương thích với các phiên bản cũ, hệ thống tập tin "cpuset" tồn tại như một lớp bao quanh hệ thống tập tin `cgroup`.

Lệnh sau:

```bash
mount -t cpuset X /sys/fs/cgroup/cpuset
```

Tương đương với:

```bash
mount -t cgroup -ocpuset,noprefix X /sys/fs/cgroup/cpuset
echo "/sbin/cpuset_release_agent" > /sys/fs/cgroup/cpuset/release_agent
```

---

Dưới đây là bản dịch chuẩn sang tiếng Việt của phần **2.2 Thêm/Xoá CPU**:

---

### **2.2 Thêm / xoá CPU**

Đây là cú pháp khi ghi vào các tệp `cpus` hoặc `mems` trong các thư mục cpuset:

```bash
# /bin/echo 1-4 > cpuset.cpus   -> đặt danh sách CPU thành 1,2,3,4
# /bin/echo 1,2,3,4 > cpuset.cpus   -> đặt danh sách CPU thành 1,2,3,4
```

---

Để thêm một CPU vào cpuset, hãy ghi danh sách mới các CPU bao gồm cả CPU muốn thêm. Ví dụ, để thêm CPU 6 vào cpuset ở trên:

```bash
# /bin/echo 1-4,6 > cpuset.cpus   -> đặt danh sách CPU thành 1,2,3,4,6
```

---

Tương tự, để xoá một CPU khỏi cpuset, bạn chỉ cần ghi lại danh sách mới các CPU, không bao gồm CPU muốn xoá.

---

**Để xoá toàn bộ CPU khỏi cpuset:**

```bash
# /bin/echo "" > cpuset.cpus   -> xoá danh sách CPU (clear cpus list)
```

---

Dưới đây là bản dịch chuẩn sang tiếng Việt cho phần **2.3**, **2.4** và **3. Questions**:

---

### **2.3 Đặt cờ (flag)**

Cú pháp rất đơn giản:

```bash
# /bin/echo 1 > cpuset.cpu_exclusive   -> bật cờ 'cpuset.cpu_exclusive'
# /bin/echo 0 > cpuset.cpu_exclusive   -> tắt cờ 'cpuset.cpu_exclusive'
```

---

### **2.4 Gắn tiến trình vào cpuset**

```bash
# /bin/echo PID > tasks
```

Lưu ý rằng đây là **PID (mã số tiến trình)**, không phải PIDs. Bạn chỉ có thể gắn **một tiến trình tại một thời điểm**. Nếu có nhiều tiến trình cần gắn, bạn phải thực hiện từng cái một theo thứ tự:

```bash
# /bin/echo PID1 > tasks
# /bin/echo PID2 > tasks
...
# /bin/echo PIDn > tasks
```

---

## **3. Câu hỏi thường gặp**

**Q:**
Chuyện gì xảy ra với việc dùng `'/bin/echo'`?

**A:**
Lệnh `echo` được tích hợp sẵn trong bash **không kiểm tra lỗi khi gọi write()**. Nếu bạn dùng `echo` (mặc định trong shell) để ghi vào hệ thống tệp cpuset, bạn sẽ **không thể biết** được lệnh có thực hiện thành công hay không.
\=> Vì vậy, nên dùng `/bin/echo` để đảm bảo ghi chính xác.

---

**Q:**
Khi tôi gắn tiến trình vào, chỉ có tiến trình đầu tiên trong dòng được gắn vào thật sự!

**A:**
Vì chỉ có thể trả về **một mã lỗi duy nhất cho mỗi lần gọi `write()`**, nên bạn chỉ nên ghi **một PID mỗi lần**.

---

