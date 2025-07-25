# Control Groups

[Bài Viết Gốc](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/cgroups.html)

 **Nhóm Kiểm Soát (Control Groups)**

---

## **1. Nhóm kiểm soát (Control Groups)**

### **1.1 Cgroups là gì?**

Control Groups (hay gọi tắt là **cgroups**) cung cấp một cơ chế để gom nhóm/phân vùng các tập hợp tác vụ, bao gồm cả các tiến trình con trong tương lai, thành các **nhóm phân cấp (hierarchical groups)** với hành vi chuyên biệt.

#### **Định nghĩa:**

* **Một group** là tập hợp các tác vụ (tasks) với một bộ thông số dành cho một hoặc nhiều **subsystem** (hệ thống con).

* **Một subsystem** là một mô-đun sử dụng khả năng nhóm tiến trình do cgroups cung cấp để xử lý các nhóm tác vụ theo những cách cụ thể.
  Subsystem thường là một **"bộ điều khiển tài nguyên" (resource controller)**: nó có thể lên lịch sử dụng tài nguyên hoặc áp dụng giới hạn cho từng nhóm, nhưng cũng có thể là bất kỳ thực thể nào muốn tác động tới một nhóm tiến trình – ví dụ, một subsystem ảo hóa.

* **Một hierarchy (cấu trúc phân cấp)** là một tập hợp các cgroup được sắp xếp theo cây. Mỗi tác vụ trong hệ thống chỉ tồn tại **trong một cgroup duy nhất trong một hierarchy cụ thể**, và mỗi subsystem được gắn trạng thái riêng với từng cgroup trong hierarchy đó.
  Mỗi hierarchy có một bản thể (instance) của **hệ thống tệp ảo cgroup (cgroup virtual filesystem)** tương ứng.

> Tại cùng một thời điểm, hệ thống có thể tồn tại nhiều **hierarchy khác nhau** của các nhóm tác vụ. Mỗi hierarchy là một cách phân vùng tất cả tác vụ trong hệ thống.

---

**Người dùng (user-level code)** có thể:

* Tạo và xóa các cgroup theo tên trong một instance của hệ thống tệp ảo cgroup.
* Gán và truy vấn các tiến trình (PIDs) thuộc cgroup.
* Liệt kê các PID được gán.
  → Những thao tác này chỉ ảnh hưởng đến **hierarchy** tương ứng với instance của hệ thống tệp cgroup đang sử dụng.

---

**Mục đích chính của cgroups là để theo dõi tiến trình công việc đơn giản.** Tuy nhiên, mục tiêu của thiết kế là cho phép các subsystem khác kết nối vào hệ thống cgroup, từ đó:

* Gán thêm thuộc tính cho các cgroup.
* Tính toán/thống kê giới hạn tài nguyên mà các tiến trình trong cgroup có thể truy cập.

**Ví dụ:** `cpusets` (xem thêm [**CPUSETS**]()) cho phép bạn:

* Gán **tập hợp CPU** và **nút bộ nhớ (memory nodes)** cho một cgroup.
* Gắn các tiến trình cụ thể vào cgroup tương ứng.

---

### **1.2 Tại sao cần cgroups?**

Có nhiều nỗ lực nhằm tổng hợp các tiến trình trong nhân Linux, chủ yếu để phục vụ cho mục đích **theo dõi tài nguyên**.
Một số ví dụ gồm: **cpusets**, **CKRM/ResGroups**, **UserBeanCounters**, và **virtual server namespaces**.
Tất cả các nỗ lực này đều yêu cầu một khái niệm cơ bản về **gom nhóm hoặc phân vùng các tiến trình**, trong đó các tiến trình mới được tạo ra sẽ nằm trong cùng một **nhóm (cgroup)** với tiến trình cha của chúng.

---

Bản vá `cgroup` trong nhân Linux cung cấp **những cơ chế tối thiểu cần thiết** để triển khai hiệu quả các nhóm như vậy.
Nó **gây ảnh hưởng rất nhỏ đến các đường xử lý nhanh (fast paths)** của hệ thống, đồng thời cung cấp các **móc giao diện (hooks)** cho các hệ thống con (như cpusets) để thêm hành vi tùy chỉnh khi cần.

---

Việc hỗ trợ **nhiều cấu trúc phân cấp (multiple hierarchies)** là cần thiết cho các tình huống mà việc chia tiến trình vào các nhóm cgroup là **khác nhau tùy theo subsystem**.
Việc tồn tại nhiều cây phân cấp song song (parallel hierarchies) giúp cho hệ thống **phân chia công việc một cách tự nhiên**, **tránh việc ép buộc nhiều subsystem không liên quan phải hoạt động trong cùng một cây cgroup duy nhất** – điều này sẽ rất phức tạp khi quản lý.

---

Ở một thái cực, **mỗi subsystem có thể có một cây phân cấp riêng**. Ở thái cực ngược lại, **mọi subsystem đều gắn vào cùng một cây phân cấp**.

---

**Ví dụ minh họa (ban đầu được đề xuất bởi [vatsa@in.ibm.com](mailto:vatsa@in.ibm.com))**
Một máy chủ tại đại học lớn với nhiều người dùng khác nhau – sinh viên, giáo sư, và các tiến trình hệ thống, v.v.
Việc lên kế hoạch tài nguyên cho máy chủ này có thể thực hiện như sau:

Dưới đây là bản dịch tiếng Việt chính xác cho phần bạn đã gửi:

---

**Sơ đồ phân chia tài nguyên (giả sử tại một trường đại học):**

```bash
CPU :         "Top cpuset"
               /      \
        CPUSet1    CPUSet2
      (Professors)  (Students)

    In addition (system tasks) are attached to topcpuset (so
    that they can run anywhere) with a limit of 20%

Memory : Professors (50%), Students (30%), system (20%)

Disk   : Professors (50%), Students (30%), system (20%)

Network : WWW browsing (20%), Network File System (60%), others (20%)
                      / \
         Professors (15%) students (5%)

```

**Phân bổ tài nguyên:**

* **Bộ nhớ (Memory):** Giáo sư (50%), Sinh viên (30%), Hệ thống (20%)
* **Đĩa (Disk):** Giáo sư (50%), Sinh viên (30%), Hệ thống (20%)
* **Mạng (Network):**

  * Duyệt web (WWW) – 20%
  * Hệ thống tệp mạng (NFS) – 60%
  * Khác – 20%
  * Trong đó: Giáo sư – 15%, Sinh viên – 5%

---

**Diễn giải:**

* Trình duyệt như Firefox hoặc Lynx sẽ được phân loại vào nhóm mạng "WWW".
* Trong khi đó, tiến trình `(k)nfsd` sẽ được đưa vào nhóm mạng "NFS".
* Trình duyệt do giáo sư hoặc sinh viên khởi chạy cũng sẽ chia sẻ tài nguyên CPU và bộ nhớ phù hợp với nhóm tương ứng (giáo sư hoặc sinh viên).

---

**Khả năng phân loại tiến trình theo tài nguyên khác nhau (CPU, Memory, Network) thông qua nhiều hệ thống phân cấp (hierarchies)** cho phép người quản trị viết một script tự động nhận diện người khởi chạy trình duyệt và chuyển tiến trình vào nhóm tương ứng:

```bash
# echo browser_pid > /sys/fs/cgroup/<loại tài nguyên>/<lớp người dùng>/tasks
```

---

**Nếu chỉ có một hệ thống phân cấp (hierarchy):**

* Người quản trị **buộc phải tạo một cgroup riêng cho từng trình duyệt được mở**,
* Gán nó với tài nguyên phù hợp (mạng, CPU...), điều này dẫn đến sự **bùng nổ số lượng cgroup**.

---

**Tình huống nâng cao:**

* Quản trị viên muốn **tạm thời tăng quyền truy cập mạng** cho sinh viên (ví dụ vào ban đêm để học online),
* Hoặc **tăng quyền truy cập CPU** cho các ứng dụng mô phỏng của sinh viên.

Khi có khả năng gán tiến trình (PID) đến các class tài nguyên:

```bash
# echo pid > /sys/fs/cgroup/network/<class_mới>/tasks
# sau một thời gian...
# echo pid > /sys/fs/cgroup/network/<class_cũ>/tasks
```

---

**Nếu không có khả năng này**, người quản trị sẽ phải chia nhóm tiến trình thành nhiều cgroup nhỏ, rồi **gán lại tài nguyên** cho từng nhóm mới – gây tốn công và khó quản lý hơn nhiều.

---

### 1.3 Cgroups được triển khai như thế nào?

Control Groups mở rộng nhân Linux theo các cách sau:

* Mỗi tiến trình (task) trong hệ thống có một con trỏ đếm tham chiếu trỏ đến một đối tượng `css_set`.
* Một `css_set` chứa tập hợp các con trỏ đếm tham chiếu đến các đối tượng `cgroup_subsys_state`, mỗi đối tượng tương ứng với một subsystem (hệ con) của cgroup đã được đăng ký trong hệ thống. Không có liên kết trực tiếp nào từ tiến trình đến cgroup mà nó là thành viên trong mỗi hệ phân cấp, nhưng có thể xác định được điều đó bằng cách đi theo các con trỏ qua các đối tượng `cgroup_subsys_state`. Điều này là do việc truy cập trạng thái của subsystem thường xuyên xảy ra và ảnh hưởng đến hiệu năng, trong khi các thao tác cần truy cập trực tiếp vào cgroup của tiến trình (đặc biệt là di chuyển giữa các cgroup) thì ít xảy ra hơn. Một danh sách liên kết chạy qua trường `cg_list` của mỗi `task_struct` sử dụng `css_set`, và được neo tại `css_set->tasks`.
* Một hệ thống tập tin dạng phân cấp của cgroup có thể được gắn kết để duyệt và thao tác từ không gian người dùng.
* Bạn có thể liệt kê tất cả các tiến trình (theo PID) được gán vào bất kỳ nhóm nào.

Việc triển khai cgroups yêu cầu một vài hook đơn giản vào phần còn lại của nhân hệ điều hành, và không nằm trong các đoạn mã quan trọng về hiệu năng:

* Trong `init/main.c`, để khởi tạo các cgroup gốc và `css_set` ban đầu tại thời điểm khởi động hệ thống.
* Trong `fork` và `exit`, để gán và tách một tiến trình khỏi `css_set` của nó.

Ngoài ra, một hệ thống tập tin kiểu “cgroup” có thể được gắn kết, cho phép duyệt và chỉnh sửa các cgroup hiện có được kernel nhận biết. Khi gắn một hệ phân cấp cgroup, bạn có thể chỉ định một danh sách phân cách bằng dấu phẩy các subsystem để mount dưới dạng các tùy chọn mount của hệ thống tập tin. Mặc định, việc mount hệ thống tập tin cgroup sẽ cố gắng mount một hệ phân cấp chứa tất cả các subsystem đã đăng ký.


Nếu đã tồn tại một hệ phân cấp cgroup đang hoạt động với **chính xác** cùng tập hợp các subsystem, hệ thống sẽ **tái sử dụng** nó cho thao tác mount mới. Nếu **không có** hệ phân cấp nào phù hợp và bất kỳ subsystem nào được yêu cầu **đang được sử dụng** trong một hệ phân cấp khác, thao tác mount sẽ **thất bại** với lỗi `-EBUSY`. Ngược lại, một hệ phân cấp mới sẽ được kích hoạt, liên kết với các subsystem được yêu cầu.

Hiện tại, **không thể** gắn một subsystem mới vào một hệ phân cấp cgroup đã tồn tại hoặc gỡ bỏ subsystem khỏi một hệ phân cấp đang hoạt động. Điều này **có thể** được hỗ trợ trong tương lai, nhưng tiềm ẩn nhiều vấn đề khôi phục lỗi phức tạp.

Khi hệ thống tập tin cgroup bị unmount, nếu có các **cgroup con** được tạo bên dưới cgroup cấp cao nhất, thì hệ phân cấp đó **vẫn hoạt động** mặc dù đã được unmount; nếu **không có cgroup con**, hệ phân cấp đó sẽ bị **vô hiệu hóa**.

**Không có** lời gọi hệ thống (system call) mới nào được thêm vào cho cgroups – tất cả thao tác truy vấn và chỉnh sửa cgroup đều thông qua hệ thống tập tin cgroup này.

Mỗi tiến trình dưới `/proc` có một tệp mới gọi là `cgroup`, hiển thị, đối với **mỗi hệ phân cấp đang hoạt động**, tên của subsystem và tên của cgroup tương ứng (tính từ thư mục gốc của hệ thống tập tin cgroup).

Mỗi cgroup được đại diện bằng một **thư mục** trong hệ thống tập tin cgroup, chứa các tệp mô tả cgroup đó:

* `tasks`: danh sách các tiến trình (theo PID) gắn với cgroup này. Danh sách này **không đảm bảo** được sắp xếp. Ghi một thread ID vào tệp này sẽ **chuyển** thread đó vào cgroup này.
* `cgroup.procs`: danh sách các thread group ID (TGID) trong cgroup này. Danh sách này cũng không đảm bảo được sắp xếp hay loại bỏ trùng lặp, nên không gian người dùng nên tự xử lý. Ghi một thread group ID vào tệp này sẽ **chuyển tất cả các thread** thuộc group đó vào cgroup này.
* `notify_on_release`: cờ báo cho biết có chạy tác vụ release khi thoát hay không.
* `release_agent`: đường dẫn tới chương trình xử lý thông báo khi release (chỉ tồn tại trong cgroup cấp cao nhất).

Các subsystem khác như **cpusets** có thể thêm các tệp bổ sung vào mỗi thư mục cgroup.

Các **cgroup mới** được tạo ra bằng cách sử dụng lệnh hệ thống `mkdir` hoặc lệnh shell. Các thuộc tính của một cgroup, chẳng hạn như các cờ (flags), được thay đổi bằng cách ghi vào các tệp tương ứng trong thư mục của cgroup, như đã liệt kê phía trên.

Cấu trúc **phân cấp có tên** của các cgroup lồng nhau cho phép chia nhỏ một hệ thống lớn thành các phần nhỏ hơn, có thể thay đổi linh hoạt – gọi là **"phân vùng mềm"** (soft-partitions).

Việc gắn mỗi tác vụ (task) vào một cgroup – thao tác này được **kế thừa tự động khi fork** bởi các tiến trình con – giúp tổ chức khối lượng công việc trên hệ thống thành các nhóm tác vụ liên quan. Một tác vụ có thể được gắn lại vào một cgroup khác, nếu được **phân quyền hợp lệ** trên các thư mục hệ thống tệp của cgroup.

Khi một tác vụ được chuyển từ cgroup này sang cgroup khác, nó nhận một con trỏ mới đến `css_set`. Nếu có sẵn một `css_set` chứa tập hợp cgroup mong muốn, nó sẽ được **tái sử dụng**; nếu không thì một `css_set` mới sẽ được **cấp phát**. Hệ thống sẽ tìm `css_set` phù hợp bằng cách tra cứu trong một **bảng băm (hash table)**.

Để cho phép truy cập từ một cgroup đến các `css_set` (và do đó là các task), một tập hợp các đối tượng `cg_cgroup_link` sẽ tạo thành một **mạng lưới liên kết**. Mỗi `cg_cgroup_link` được liên kết vào danh sách `cg_cgroup_links` cho một cgroup thông qua trường `cgrp_link_list`, và đồng thời cũng được liên kết vào danh sách `cg_cgroup_links` cho một `css_set` thông qua trường `cg_link_list`.

Do đó, tập hợp các task trong một cgroup có thể được liệt kê bằng cách **duyệt qua từng `css_set`** liên quan đến cgroup đó, và tiếp tục **lặp qua từng tập task** trong các `css_set` đó.

Việc sử dụng hệ thống tệp ảo của Linux (**virtual file system - vfs**) để biểu diễn cấu trúc phân cấp của cgroup cho phép giữ lại mô hình phân quyền và đặt tên quen thuộc cho các group, đồng thời **giảm thiểu code bổ sung trong nhân (kernel)**.

---

### **1.4 `notify_on_release` dùng để làm gì?**

Nếu cờ `notify_on_release` được bật (giá trị 1) trong một cgroup, thì bất cứ khi nào tác vụ cuối cùng trong cgroup đó rời đi (thoát hoặc gắn vào cgroup khác) **và** nhóm con cuối cùng của cgroup đó bị xóa, kernel sẽ chạy lệnh được chỉ định trong tệp `release_agent` nằm ở thư mục gốc của phân cấp cgroup tương ứng. Đường dẫn được truyền cho lệnh chính là đường dẫn của cgroup bị bỏ lại (tính tương đối so với điểm mount của hệ thống tệp cgroup).

Cơ chế này cho phép **tự động dọn dẹp các cgroup không còn sử dụng**.

* Giá trị mặc định của `notify_on_release` trong **root cgroup khi khởi động hệ thống** là **tắt (0)**.
* Giá trị mặc định của các cgroup khác khi tạo ra sẽ **kế thừa từ giá trị hiện tại của `notify_on_release` của cgroup cha**.
* Giá trị mặc định của đường dẫn `release_agent` trong một hệ phân cấp cgroup là **trống**.

---

### **1.5 `clone_children` dùng để làm gì?**

Cờ này **chỉ ảnh hưởng đến bộ điều khiển `cpuset`**. Nếu cờ `clone_children` được bật (giá trị 1) trong một cgroup, thì **một cgroup con `cpuset` mới sẽ sao chép cấu hình từ cgroup cha** trong quá trình khởi tạo.

---

### **1.6 Làm cách nào để sử dụng cgroups?**

Để bắt đầu một tác vụ mới và chứa nó trong một cgroup, sử dụng hệ thống con `cpuset` của cgroup, các bước sẽ như sau:

```bash
1) mount -t tmpfs cgroup_root /sys/fs/cgroup
2) mkdir /sys/fs/cgroup/cpuset
3) mount -t cgroup -ocpuset cpuset /sys/fs/cgroup/cpuset
4) Tạo cgroup mới bằng cách sử dụng lệnh mkdir hoặc ghi (echo) vào
   hệ thống tập tin ảo /sys/fs/cgroup/cpuset.
5) Khởi động một tiến trình sẽ là “tiến trình cha sáng lập” của job mới.
6) Gán tiến trình đó vào cgroup mới bằng cách ghi PID của nó vào
   file `tasks` trong thư mục cgroup tương ứng.
7) Thực hiện fork, exec hoặc clone các tiến trình công việc từ tiến trình cha sáng lập này.
```

---

**Ví dụ**, chuỗi lệnh sau sẽ tạo một cgroup tên là “Charlie”, chứa chỉ CPU 2 và 3, và Node bộ nhớ 1. Sau đó sẽ khởi động một shell phụ (`sh`) trong cgroup đó:

```bash
mount -t tmpfs cgroup_root /sys/fs/cgroup
mkdir /sys/fs/cgroup/cpuset
mount -t cgroup cpuset -ocpuset /sys/fs/cgroup/cpuset
cd /sys/fs/cgroup/cpuset
mkdir Charlie
cd Charlie
/bin/echo 2-3 > cpuset.cpus       # Gán CPU 2 và 3
/bin/echo 1 > cpuset.mems         # Gán Node bộ nhớ 1
/bin/echo $$ > tasks              # Gán tiến trình hiện tại vào nhóm
sh                                # Mở shell trong cgroup mới

# Shell 'sh' hiện đang chạy trong cgroup Charlie
# Dòng tiếp theo sẽ hiển thị '/Charlie'
cat /proc/self/cgroup
```

---

## 2. Ví dụ Sử dụng và Cú pháp

### 2.1 Sử dụng cơ bản

Việc tạo, sửa đổi và sử dụng cgroups có thể được thực hiện thông qua hệ thống tập tin ảo của cgroup.

Để mount (gắn kết) một hệ phân cấp cgroup với tất cả các subsystem sẵn có, hãy gõ:

```bash
# mount -t cgroup xxx /sys/fs/cgroup
```

> “xxx” không được cgroup code diễn giải, nhưng sẽ xuất hiện trong `/proc/mounts`, vì vậy nó có thể là bất kỳ chuỗi định danh nào bạn muốn.

**Lưu ý**: Một số subsystem sẽ không hoạt động nếu không có dữ liệu người dùng cung cấp trước. Ví dụ, nếu `cpusets` được bật, người dùng sẽ phải điền vào các file `cpus` và `mems` cho mỗi cgroup mới được tạo trước khi có thể sử dụng nhóm đó.

Như đã giải thích trong mục **1.2 Tại sao cần cgroups?**, bạn nên tạo các hệ phân cấp khác nhau của cgroups cho từng nguồn tài nguyên riêng lẻ hoặc nhóm tài nguyên mà bạn muốn kiểm soát. Vì vậy, bạn nên mount một hệ thống `tmpfs` tại `/sys/fs/cgroup` và tạo các thư mục cho mỗi tài nguyên hoặc nhóm tài nguyên cgroup như sau:

```bash
# mount -t tmpfs cgroup_root /sys/fs/cgroup
# mkdir /sys/fs/cgroup/rg1
```

Để mount một hệ phân cấp cgroup chỉ với subsystem `cpuset` và `memory`, gõ:

```bash
# mount -t cgroup -o cpuset,memory hier1 /sys/fs/cgroup/rg1
```

> Dù việc remount (mount lại) cgroups hiện được hỗ trợ, **nhưng không được khuyến khích sử dụng**. Remount cho phép thay đổi các subsystem đã liên kết và `release_agent`. Việc gắn lại như vậy thường không hữu ích vì chỉ hoạt động khi hệ phân cấp đang trống và `release_agent` cần được thay thế bằng cơ chế `fnotify` thông thường. Việc hỗ trợ remount sẽ bị loại bỏ trong tương lai.

Để mount một hệ phân cấp cgroup chỉ với các subsystem `cpuset` và `memory`, hãy dùng lệnh:

```bash
# mount -t cgroup -o cpuset,memory hier1 /sys/fs/cgroup/rg1
```

Mặc dù việc remount (gắn lại) cgroups hiện tại được hỗ trợ, **nhưng không được khuyến khích sử dụng**. Việc remount cho phép thay đổi các subsystem đã liên kết và `release_agent`. Tuy nhiên, việc thay đổi như vậy hầu như không hữu ích vì chỉ hoạt động khi hệ phân cấp đang rỗng, và bản thân `release_agent` nên được thay bằng phương pháp theo dõi thông thường như `fsnotify`. Việc hỗ trợ remount sẽ bị loại bỏ trong tương lai.

---

Để chỉ định `release_agent` cho một hệ phân cấp, sử dụng lệnh:

```bash
# mount -t cgroup -o cpuset,release_agent="/sbin/cpuset_release_agent" \
  xxx /sys/fs/cgroup/rg1
```

> **Lưu ý:** Nếu chỉ định `release_agent` nhiều hơn một lần, hệ thống sẽ báo lỗi.

---

Cũng cần lưu ý rằng việc thay đổi tập hợp subsystem hiện **chỉ được hỗ trợ khi hệ phân cấp bao gồm một cgroup duy nhất (gốc)**. Khả năng liên kết hoặc hủy liên kết subsystem tùy ý trong một hệ phân cấp cgroup hiện tại sẽ được triển khai trong tương lai.

Sau đó, dưới `/sys/fs/cgroup/rg1`, bạn có thể tìm thấy cây (tree) tương ứng với cấu trúc cgroup của hệ thống. Ví dụ, `/sys/fs/cgroup/rg1` là cgroup chứa toàn bộ hệ thống.

---

Nếu bạn muốn thay đổi giá trị của `release_agent`, hãy sử dụng lệnh:

```bash
# echo "/sbin/new_release_agent" > /sys/fs/cgroup/rg1/release_agent
```

Nó cũng có thể được thay đổi thông qua lệnh remount.

---

Nếu bạn muốn tạo một cgroup mới dưới `/sys/fs/cgroup/rg1`, hãy thực hiện:

```bash
# cd /sys/fs/cgroup/rg1
# mkdir my_cgroup
```

---

Bây giờ bạn muốn thực hiện thao tác gì đó với cgroup này:

```bash
# cd my_cgroup
```

Trong thư mục này, bạn có thể tìm thấy một số file:

```bash
# ls
cgroup.procs  notify_on_release  tasks
```

(cùng với các file khác được thêm vào bởi các subsystem đi kèm)

---

Gắn shell hiện tại của bạn vào cgroup này:

```bash
# /bin/echo $$ > tasks
```

---

Bạn cũng có thể tạo các cgroup con bên trong cgroup hiện tại bằng cách dùng `mkdir` trong thư mục đó:

```bash
# mkdir my_sub_cs
```

---

Để xóa một cgroup, chỉ cần dùng `rmdir`:

```bash
# rmdir my_sub_cs
```

**Lưu ý:** Việc này sẽ thất bại nếu cgroup đó đang được sử dụng (ví dụ: chứa cgroup con, có tiến trình đang hoạt động, hoặc bị giữ bởi các tham chiếu đặc biệt từ subsystem khác).

---

### 2.2 Gắn tiến trình (Attaching processes)

```bash
# /bin/echo PID > tasks
```

Lưu ý rằng là **PID**, không phải **PIDs**. Bạn chỉ có thể gắn **một tiến trình tại một thời điểm**. Nếu bạn có nhiều tiến trình muốn gắn, bạn phải thực hiện lần lượt từng cái một:

```bash
# /bin/echo PID1 > tasks
# /bin/echo PID2 > tasks
...
# /bin/echo PIDn > tasks
```

Bạn cũng có thể gắn **tiến trình shell hiện tại** bằng cách echo giá trị 0:

```bash
# echo 0 > tasks
```

---

Bạn có thể sử dụng **file `cgroup.procs`** thay vì file `tasks` để **di chuyển toàn bộ các luồng trong một threadgroup** cùng lúc. Khi ghi **PID của một tiến trình bất kỳ** trong một threadgroup vào `cgroup.procs`, tất cả các luồng thuộc threadgroup đó sẽ được gắn vào cgroup. Ghi giá trị `0` vào `cgroup.procs` sẽ di chuyển toàn bộ các luồng trong threadgroup của tiến trình đang ghi.

---

**Lưu ý:** Vì mỗi tiến trình luôn là thành viên của **duy nhất một cgroup** trong mỗi hệ phân cấp đã được mount, nên để di chuyển một tiến trình sang cgroup khác, bạn phải ghi nó vào file `tasks` của cgroup mới (có thể là root cgroup).

**Lưu ý:** Do một số giới hạn được áp đặt bởi một số subsystem cgroup, **việc di chuyển tiến trình sang cgroup khác có thể thất bại**.

---

### 2.3 Gắn hệ phân cấp theo tên

Truyền tùy chọn `name=<x>` khi mount một hệ phân cấp cgroups sẽ **gắn tên được chỉ định với hệ phân cấp đó**. Tùy chọn này có thể được sử dụng khi mount một hệ phân cấp đã tồn tại, để tham chiếu đến nó **theo tên** thay vì theo tập hợp các subsystem đang hoạt động. Mỗi hệ phân cấp hoặc là **không có tên**, hoặc có **một tên duy nhất**.

Tên được gán phải khớp với biểu thức chính quy: `[w.-]+`

---

Khi truyền tùy chọn `name=<x>` cho một hệ phân cấp mới, **bạn phải chỉ rõ các subsystem một cách thủ công**; hành vi cũ (legacy behavior) là tự động mount tất cả subsystem khi không chỉ định gì **không còn được hỗ trợ** khi bạn đặt tên cho subsystem.

Tên của subsystem sẽ hiển thị như một phần mô tả của hệ phân cấp trong:

* `/proc/mounts`
* `/proc/<pid>/cgroups`

---

## 3. Kernel API

### 3.1 Tổng quan

Mỗi **subsystem của nhân (kernel subsystem)** muốn kết nối vào hệ thống cgroup tổng quát thì cần tạo một đối tượng `cgroup_subsys`. Đối tượng này chứa nhiều phương thức khác nhau, được dùng làm **callback từ hệ thống cgroup**, cùng với một **ID của subsystem** sẽ được hệ thống cgroup gán.

---

Các trường khác trong đối tượng `cgroup_subsys` bao gồm:

* **subsys\_id**: chỉ số mảng duy nhất cho subsystem này, cho biết subsystem nên quản lý mục nào trong `cgroup->subsys[]`.

* **name**: cần được khởi tạo thành tên duy nhất của subsystem. Tên này không được dài hơn hằng `MAX_CGROUP_TYPE_NAMELEN`.

* **early\_init**: chỉ định xem subsystem có cần khởi tạo sớm trong quá trình khởi động hệ thống hay không.

---

Mỗi đối tượng cgroup được tạo ra bởi hệ thống sẽ có một **mảng con trỏ**, được đánh chỉ mục bởi subsystem ID. Con trỏ này **hoàn toàn được quản lý bởi subsystem**, còn mã code chung của cgroup sẽ **không bao giờ đụng tới con trỏ này**.

---

### 3.2 Đồng bộ hóa

Có một **mutex toàn cục** tên là `cgroup_mutex`, được hệ thống cgroup sử dụng. Bất kỳ thành phần nào muốn **thay đổi một cgroup** thì đều phải giữ mutex này. Mutex này cũng có thể được sử dụng để **ngăn cgroup bị thay đổi**, tuy nhiên trong một số tình huống cụ thể, **việc sử dụng các loại khóa đặc thù hơn** có thể phù hợp hơn.

Xem thêm trong tệp `kernel/cgroup.c` để biết chi tiết.

---

Các subsystem có thể **giữ/thả `cgroup_mutex`** thông qua các hàm `cgroup_lock()` và `cgroup_unlock()`.

---

Việc truy cập con trỏ đến cgroup của một tiến trình (task) có thể được thực hiện theo các cách sau:

* Khi đang giữ `cgroup_mutex`
* Khi đang giữ `alloc_lock` của tiến trình (thông qua `task_lock()`)
* Bên trong đoạn mã có `rcu_read_lock()` thông qua hàm `rcu_dereference()`

---

### 3.3 Giao diện Lập trình Subsystem (Subsystem API)

Mỗi subsystem cần:

* thêm một mục vào tệp `linux/cgroup_subsys.h`
* định nghĩa một đối tượng `cgroup_subsys` với tên `<tên>_cgrp_subsys`

Mỗi subsystem có thể cung cấp các phương thức dưới đây. Phương thức **bắt buộc** là `css_alloc` và `css_free`. Tất cả các phương thức khác nếu không có thì được xem là không làm gì (no-op).

---

```c
struct cgroup_subsys_state *css_alloc(struct cgroup *cgrp);
```

(*người gọi phải giữ `cgroup_mutex`*)

Được gọi để cấp phát một đối tượng trạng thái subsystem cho một cgroup. Subsystem cần tự cấp phát bộ nhớ cho đối tượng trạng thái này, và trả về con trỏ đến đối tượng nếu thành công hoặc giá trị lỗi `ERR_PTR()` nếu thất bại.
Nếu thành công, con trỏ này sẽ trỏ đến một cấu trúc thuộc kiểu `cgroup_subsys_state` (thường được nhúng trong một đối tượng lớn hơn thuộc subsystem), và sẽ được hệ thống cgroup khởi tạo.
Chú ý: lời gọi này cũng có thể được thực hiện để khởi tạo trạng thái subsystem gốc (root). Khi đó, `cgroup` sẽ có parent là `NULL`.

---

```c
int css_online(struct cgroup *cgrp);
```

(*người gọi phải giữ `cgroup_mutex`*)

Được gọi sau khi `@cgrp` đã hoàn tất việc cấp phát và trở nên có thể thấy được trong các vòng lặp `cgroup_for_each_child/descendant_*()`.
Subsystem có thể từ chối hoạt động bằng cách trả về lỗi `-errno`.
Hàm này có thể được sử dụng để triển khai việc **chia sẻ và lan truyền trạng thái** trong toàn bộ cây phân cấp.

---

```c
void css_offline(struct cgroup *cgrp);
```

(*người gọi phải giữ `cgroup_mutex`*)

Đây là hàm đối ứng với `css_online()`, và chỉ được gọi khi `css_online()` đã thành công trên `@cgrp`.
Hàm này đánh dấu sự bắt đầu quá trình loại bỏ `@cgrp` và subsystem nên **giải phóng mọi tham chiếu** đang giữ đối với `@cgrp`.
Khi mọi tham chiếu đã được loại bỏ, hệ thống sẽ tiến hành đến bước tiếp theo là gọi `css_free()`.

---

```c
void css_free(struct cgroup *cgrp);
```

(*người gọi phải giữ `cgroup_mutex`*)

Được gọi ngay trước khi hệ thống loại bỏ hoàn toàn `@cgrp`; subsystem nên **giải phóng đối tượng trạng thái subsystem** tại đây.
Khi hàm này được gọi, `@cgrp` chắc chắn là **đã không còn được sử dụng** nữa.

---

```c
int can_attach(struct cgroup *cgrp, struct cgroup_taskset *tset);
```

(*người gọi phải giữ `cgroup_mutex`*)

Được gọi **trước khi** gắn một hay nhiều tác vụ vào cgroup. Nếu subsystem trả về lỗi, thao tác gắn sẽ bị từ chối.
Biến `@tset` chứa tập các tác vụ được gắn vào, và được đảm bảo là sẽ có ít nhất một tiến trình.

---

Nếu có nhiều tác vụ trong tập `taskset`, thì:

* Đảm bảo rằng tất cả đều thuộc cùng một nhóm luồng (thread group)
* `@tset` chứa tất cả các tác vụ từ nhóm luồng đó dù có thay đổi `cgroup` hay không
* Tác vụ đầu tiên là tác vụ "leader"

Mỗi mục trong `@tset` cũng chứa `cgroup` cũ của tác vụ, và những tác vụ không chuyển đổi `cgroup` có thể được bỏ qua dễ dàng bằng cách sử dụng trình lặp `cgroup_taskset_for_each()`.
Lưu ý: đoạn mã này không được gọi trong trường hợp fork().
Nếu phương thức `can_attach()` trả về `0` (thành công), thì nó cần vẫn còn hợp lệ trong khi người gọi đang giữ `cgroup_mutex`, và **phải đảm bảo rằng hoặc `attach()` hoặc `cancel_attach()` sẽ được gọi tiếp theo trong tương lai.**

---

```c
void css_reset(struct cgroup_subsys_state *css);
```

(*người gọi phải giữ `cgroup_mutex`*)

Đây là một thao tác tùy chọn dùng để **khôi phục cấu hình của `@css` về trạng thái ban đầu**.
Thường chỉ được sử dụng trong hệ thống cây phân cấp thống nhất (unified hierarchy), khi một subsystem bị vô hiệu hóa qua `cgroup.subtree_control`, nhưng vẫn cần tồn tại vì các subsystem khác còn phụ thuộc.
Core của `cgroup` có thể ẩn subsystem bằng cách gỡ các tệp giao diện liên quan, sau đó gọi `css_reset()` để subsystem trở lại trạng thái trung lập ban đầu, **tránh ảnh hưởng đến các tài nguyên hệ thống khi bị vô tình điều khiển bởi subsystem đã bị ẩn.**

---

```c
void cancel_attach(struct cgroup *cgrp, struct cgroup_taskset *tset);
```

(*người gọi phải giữ `cgroup_mutex`*)

Được gọi khi thao tác `attach` một tác vụ thất bại **sau khi `can_attach()` đã thành công**.
Nếu subsystem có tác dụng phụ khi thực hiện `can_attach()` thì nên định nghĩa hàm này để thực hiện rollback (hoàn tác). Nếu không cần, có thể bỏ qua.
Chỉ áp dụng với những subsystem mà `can_attach()` đã trả về thành công trước đó.

---

```c
void attach(struct cgroup *cgrp, struct cgroup_taskset *tset);
```

(*người gọi phải giữ `cgroup_mutex`*)

Hàm này thực hiện thao tác gắn thực sự các tác vụ vào `cgroup`.
Tham số `@tset` chứa các tác vụ sẽ được gắn, và chắc chắn là có ít nhất một tác vụ trong đó.

---

Sau khi một tác vụ đã được gắn vào `cgroup`, nếu cần thực hiện một số thao tác sau khi gắn (post-attachment), chẳng hạn như **cấp phát bộ nhớ hoặc thao tác chặn (blocking)**, thì có thể gọi các hàm sau (các tham số giống như trong `can_attach()`):

---

```c
void fork(struct task_struct *task)
```

**Được gọi khi một tác vụ được fork vào trong một `cgroup`.**

---

```c
void exit(struct task_struct *task)
```

**Được gọi khi tác vụ thoát (exit).**

---

```c
void free(struct task_struct *task)
```

**Được gọi khi cấu trúc `task_struct` được giải phóng.**

---

```c
void bind(struct cgroup *root) 
```

(*người gọi phải giữ `cgroup_mutex`*)

**Được gọi khi một subsystem của `cgroup` được chuyển (rebound) sang một hệ thống phân cấp khác và `cgroup` gốc.**

Hiện tại thao tác này **chỉ liên quan đến việc di chuyển giữa hệ phân cấp mặc định** (vốn không có sub-cgroups) **và một hệ phân cấp khác đang được tạo hoặc hủy** (và do đó không có sub-cgroups).

---

### 4. Sử dụng thuộc tính mở rộng (Extended attribute usage)

Hệ thống tệp `cgroup` hỗ trợ một số loại **thuộc tính mở rộng** (extended attributes) trên thư mục và tập tin. Các loại hiện được hỗ trợ là:

* **Trusted** (`XATTR_TRUSTED`)
* **Security** (`XATTR_SECURITY`)

Cả hai loại đều yêu cầu quyền **`CAP_SYS_ADMIN`** để thiết lập.

Tương tự như `tmpfs`, các thuộc tính mở rộng trong hệ thống tệp `cgroup` được lưu trong bộ nhớ kernel, và **nên hạn chế sử dụng** để tránh tiêu tốn tài nguyên. Vì lý do này, **các thuộc tính mở rộng do người dùng định nghĩa không được hỗ trợ**, bởi vì người dùng có thể ghi tùy ý và không có giới hạn về kích thước giá trị.

Các ứng dụng đã biết hiện tại sử dụng tính năng này bao gồm:

* **SELinux**: để giới hạn việc sử dụng cgroup trong container.
* **Systemd**: để lưu trữ một số siêu dữ liệu như **PID chính trong một cgroup** (vì systemd tạo một cgroup cho mỗi service).

---

### 5. Câu hỏi thường gặp (Questions)

> **Q: Chuyện gì xảy ra với `/bin/echo` vậy?**

> **A:** Lệnh `echo` được tích hợp sẵn trong bash **không kiểm tra lỗi khi gọi `write()`**.
> Nếu bạn dùng nó trong hệ thống tệp `cgroup`, **bạn sẽ không biết được câu lệnh đã thực hiện thành công hay thất bại**.
> Vì vậy cần dùng `/bin/echo` từ hệ thống file, không phải `echo` tích hợp của bash.

---

> **Q: Khi tôi gán tiến trình, chỉ tiến trình đầu tiên trong dòng được gán thật sự!**

> **A:** Vì hệ thống chỉ có thể trả về **một mã lỗi duy nhất cho mỗi lần gọi `write()`**, nên **chỉ nên ghi một PID duy nhất** mỗi lần.

---
