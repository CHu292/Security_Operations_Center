# Tuning the Task Scheduler

[Bài Viết Gốc](https://doc.opensuse.org/documentation/leap/archive/42.1/tuning/html/book.sle.tuning/cha.tuning.taskscheduler.html)

---

## 13 Tinh chỉnh Bộ lập lịch Tác vụ

* 13.1 Giới thiệu
* 13.2 Phân loại Tiến trình
* 13.3 Bộ lập lịch Công bằng Hoàn toàn
* 13.4 Thông tin Tham khảo

---

Các hệ điều hành hiện đại, chẳng hạn như openSUSE® Leap, thường chạy nhiều tác vụ khác nhau cùng một lúc. Ví dụ, bạn có thể đang tìm kiếm trong một tệp văn bản trong khi nhận email và sao chép một tệp lớn sang ổ cứng ngoài. Những tác vụ đơn giản này yêu cầu nhiều tiến trình bổ sung được hệ thống chạy. Để cung cấp tài nguyên hệ thống cần thiết cho từng tác vụ, nhân Linux cần một công cụ để phân phối tài nguyên hệ thống sẵn có cho từng tác vụ. Và đó chính là nhiệm vụ của **bộ lập lịch tác vụ**.

Các phần sau đây sẽ giải thích các thuật ngữ quan trọng nhất liên quan đến lập lịch tiến trình. Chúng cũng cung cấp thông tin về chính sách bộ lập lịch, thuật toán lập lịch, mô tả về bộ lập lịch tác vụ được sử dụng bởi openSUSE Leap, và các nguồn tài liệu liên quan khác.

---

### 13.1 Giới thiệu

Nhân Linux kiểm soát cách các tác vụ (hoặc tiến trình) được quản lý trên hệ thống. Bộ lập lịch tác vụ, đôi khi được gọi là **bộ lập lịch tiến trình**, là phần của nhân hệ điều hành quyết định tiến trình nào sẽ chạy tiếp theo. Nó chịu trách nhiệm sử dụng tài nguyên hệ thống một cách tối ưu để đảm bảo rằng nhiều tác vụ được thực hiện đồng thời. Điều này khiến nó trở thành một thành phần cốt lõi của bất kỳ hệ điều hành đa nhiệm nào.


---

#### 13.1.1 Tước quyền (Preemption)

Lý thuyết đằng sau lập lịch tác vụ rất đơn giản. Nếu có các tiến trình có thể chạy trong hệ thống, thì ít nhất phải có một tiến trình đang chạy. Nếu có nhiều tiến trình có thể chạy hơn số bộ xử lý trong hệ thống, thì không phải tất cả tiến trình đều có thể chạy cùng lúc.

Vì vậy, một số tiến trình cần phải được tạm dừng, hoặc **bị treo**, để các tiến trình khác có thể chạy. Bộ lập lịch quyết định tiến trình nào trong hàng đợi sẽ chạy tiếp theo.

Như đã đề cập trước đó, Linux, giống như tất cả các biến thể Unix khác, là một hệ điều hành **đa nhiệm**. Điều này có nghĩa là nhiều tác vụ có thể chạy cùng lúc. Linux cung cấp một hình thức đa nhiệm gọi là **đa nhiệm tước quyền**, trong đó bộ lập lịch quyết định khi nào một tiến trình bị tạm dừng. Việc tạm dừng cưỡng bức này được gọi là **tước quyền (preemption)**. Tất cả các phiên bản Unix đều đã hỗ trợ đa nhiệm có tước quyền từ ban đầu.

---

#### 13.1.2 Lát thời gian (Timeslice)

Khoảng thời gian mà một tiến trình sẽ được chạy trước khi bị tước quyền được xác định trước. Nó được gọi là **lát thời gian (timeslice)** của tiến trình và biểu thị lượng thời gian xử lý mà mỗi tiến trình được cấp. Bằng cách gán lát thời gian, bộ lập lịch đưa ra các quyết định tổng thể cho hệ thống đang chạy và ngăn không cho các tiến trình riêng lẻ chiếm dụng quá mức tài nguyên bộ xử lý.

---

#### 13.1.3 Độ ưu tiên tiến trình (Process Priority)

Bộ lập lịch đánh giá các tiến trình dựa trên mức độ ưu tiên của chúng. Để tính toán mức ưu tiên hiện tại của một tiến trình, bộ lập lịch sử dụng các thuật toán phức tạp. Do đó, mỗi tiến trình được gán một giá trị xác định mức độ mà nó được “cho phép” chạy trên bộ xử lý.

---

### 13.2 Phân loại Tiến trình

Các tiến trình thường được phân loại theo mục đích và hành vi của chúng. Mặc dù ranh giới giữa các loại không phải lúc nào cũng rõ ràng, nhưng nhìn chung có hai tiêu chí chính để phân loại. Hai tiêu chí này độc lập với nhau và không loại trừ lẫn nhau.

Một cách tiếp cận là phân loại tiến trình thành **I/O-bound** hoặc **processor-bound**.

---

**I/O-bound**
I/O là viết tắt của các thiết bị Nhập/Xuất, chẳng hạn như bàn phím, chuột, hoặc đĩa quang và đĩa cứng. **Tiến trình I/O-bound** dành phần lớn thời gian để gửi và chờ các yêu cầu. Chúng được chạy rất thường xuyên, nhưng trong khoảng thời gian ngắn, nhằm không làm chặn các tiến trình khác đang chờ yêu cầu I/O.

---

**Processor-bound**
Ngược lại, **tiến trình processor-bound** sử dụng thời gian của mình để thực thi mã, và thường chạy cho đến khi bị bộ lập lịch tước quyền. Chúng không chặn các tiến trình đang chờ yêu cầu I/O, do đó có thể được chạy ít thường xuyên hơn nhưng trong khoảng thời gian dài hơn.

---

Một cách tiếp cận khác là phân loại tiến trình theo loại: **interactive**, **batch**, và **real-time**.

* **Interactive**: Tiến trình tương tác dành nhiều thời gian để chờ các yêu cầu I/O, chẳng hạn như hoạt động từ bàn phím hoặc chuột. Bộ lập lịch phải đánh thức các tiến trình này một cách nhanh chóng theo yêu cầu của người dùng, nếu không môi trường sẽ trở nên không phản hồi. Độ trễ điển hình là khoảng 100 mili giây. Các ứng dụng văn phòng, trình soạn thảo văn bản hoặc phần mềm chỉnh sửa hình ảnh là ví dụ tiêu biểu.

* **Batch**: Tiến trình theo lô thường chạy ở chế độ nền và không cần phản hồi nhanh. Chúng thường được bộ lập lịch ưu tiên thấp hơn. Các phần mềm chuyển đổi đa phương tiện, công cụ tìm kiếm cơ sở dữ liệu, hoặc trình phân tích tệp nhật ký là ví dụ điển hình.

* **Real-time**: Tiến trình thời gian thực không bao giờ được phép bị chặn bởi các tiến trình ưu tiên thấp hơn, và bộ lập lịch đảm bảo thời gian phản hồi ngắn cho chúng. Các ứng dụng chỉnh sửa nội dung đa phương tiện là ví dụ điển hình.

---

### 13.3 Bộ lập lịch Công bằng Hoàn toàn (Completely Fair Scheduler - CFS)

Kể từ phiên bản nhân Linux 2.6.23, một cách tiếp cận mới đã được áp dụng cho việc lập lịch các tiến trình có thể chạy. Bộ lập lịch Công bằng Hoàn toàn (CFS) trở thành bộ lập lịch mặc định của nhân Linux. Kể từ đó, nhiều thay đổi và cải tiến quan trọng đã được thực hiện.

Thông tin trong chương này áp dụng cho openSUSE Leap với phiên bản nhân từ 2.6.32 trở lên (bao gồm cả nhân 3.x). Môi trường bộ lập lịch được chia thành nhiều phần, và ba tính năng chính đã được giới thiệu:

---

**Nhân bộ lập lịch dạng mô-đun (Modular Scheduler Core)**
Nhân của bộ lập lịch được cải tiến với **các lớp lập lịch (scheduling classes)**. Những lớp này có tính mô-đun và đại diện cho các chính sách lập lịch.

---

**Bộ lập lịch Công bằng Hoàn toàn (Completely Fair Scheduler)**
Được giới thiệu trong nhân 2.6.23 và mở rộng trong 2.6.24, CFS cố gắng đảm bảo rằng mỗi tiến trình nhận được phần "công bằng" về thời gian xử lý.

---

**Lập lịch theo nhóm (Group Scheduling)**
Ví dụ, nếu bạn chia các tiến trình thành nhóm theo người dùng đang chạy chúng, thì CFS sẽ cố gắng cung cấp cùng một lượng thời gian xử lý cho mỗi nhóm.

---

Do đó, CFS mang lại khả năng lập lịch tối ưu cho cả máy chủ lẫn máy tính để bàn.

---

#### 13.3.1 CFS hoạt động như thế nào

CFS cố gắng đảm bảo một cách tiếp cận công bằng cho mỗi tác vụ có thể chạy. Để tìm ra phương pháp cân bằng nhất cho việc lập lịch tác vụ, nó sử dụng khái niệm **cây đỏ-đen (red-black tree)**. Cây đỏ-đen là một dạng cấu trúc dữ liệu tự cân bằng, cho phép chèn và xóa phần tử theo cách hợp lý để đảm bảo cây luôn được cân bằng. (Để biết thêm, bạn có thể tham khảo các trang wiki về cây đỏ-đen.)

Khi một tác vụ đi vào **hàng đợi thực thi (run queue)** — một danh sách có kế hoạch gồm các tiến trình sẽ được thực thi tiếp theo — bộ lập lịch sẽ ghi lại thời điểm hiện tại. Trong khi tiến trình chờ thời gian xử lý, giá trị "chờ" (wait) của nó sẽ tăng lên dựa trên tổng số tiến trình trong hàng đợi và mức ưu tiên của tiến trình. Ngay khi tiến trình được xử lý, giá trị "chờ" sẽ giảm xuống.

Nếu giá trị này giảm xuống dưới một mức nhất định, tiến trình sẽ bị bộ lập lịch tước quyền và các tiến trình khác sẽ được đưa gần hơn đến bộ xử lý. Thông qua thuật toán này, CFS cố gắng đạt đến trạng thái lý tưởng nơi giá trị “chờ” luôn là 0.

---

#### 13.3.2 Nhóm các Tiến trình (Grouping Processes)

Kể từ phiên bản nhân Linux 2.6.24, CFS có thể được điều chỉnh để đảm bảo công bằng cho người dùng hoặc nhóm người dùng thay vì chỉ cho từng tiến trình riêng lẻ. Các tiến trình có thể chạy sẽ được nhóm lại để tạo thành các thực thể, và CFS cố gắng đảm bảo sự công bằng cho các thực thể này thay vì cho từng tiến trình riêng biệt. Bộ lập lịch cũng cố gắng đảm bảo công bằng cho các tiến trình trong từng thực thể đó.

Tiến trình có thể được nhóm theo hai cách loại trừ lẫn nhau:

* Theo ID người dùng (user IDs)
* Theo nhóm điều khiển của nhân (kernel control groups)

Việc bộ lập lịch của nhân cho phép bạn nhóm các tiến trình có thể chạy phụ thuộc vào việc thiết lập các tùy chọn biên dịch nhân sau:

* `CONFIG_FAIR_USER_SCHED`
* `CONFIG_FAIR_CGROUP_SCHED`

Thiết lập mặc định trong openSUSE® Leap 42.1 là sử dụng **control groups**, cho phép bạn tạo nhóm khi cần. Để biết thêm thông tin, xem [**Chương 9, Nhóm điều khiển nhân (Kernel Control Groups)**](https://doc.opensuse.org/documentation/leap/archive/42.1/tuning/html/book.sle.tuning/cha.tuning.cgroups.html).

---

#### 13.3.3 Tùy chọn Cấu hình Nhân (Kernel Configuration Options)

Các khía cạnh cơ bản về hành vi của bộ lập lịch tiến trình có thể được thiết lập thông qua các tùy chọn cấu hình nhân. Việc thiết lập các tùy chọn này là một phần trong quá trình biên dịch nhân. Do quá trình biên dịch nhân khá phức tạp và nằm ngoài phạm vi của tài liệu này, hãy tham khảo các nguồn thông tin liên quan.

---

🔴 **Cảnh báo: Biên dịch nhân**
Nếu bạn chạy openSUSE Leap trên một nhân không được phân phối sẵn theo hệ thống (ví dụ: một nhân được biên dịch thủ công), bạn sẽ **mất toàn bộ quyền hỗ trợ**.

---

#### 13.3.4 Thuật ngữ (Terminology)

Các tài liệu liên quan đến chính sách lập lịch tác vụ thường sử dụng một số thuật ngữ kỹ thuật mà bạn cần hiểu rõ để nắm bắt thông tin chính xác. Dưới đây là một số thuật ngữ:

**Độ trễ (Latency)**
Độ trễ là khoảng thời gian giữa lúc một tiến trình được lên lịch để chạy và thời điểm thực sự được thực thi.

**Độ phân giải (Granularity)**
Mối quan hệ giữa độ phân giải và độ trễ có thể được biểu diễn bằng công thức sau:

```
gran = (lat / rtasks) - (lat / rtasks / rtasks)
```

Trong đó:

* `gran` là độ phân giải,
* `lat` là độ trễ,
* `rtasks` là số lượng tiến trình đang chạy.

---

##### 13.3.4.1 Chính sách lập lịch (Scheduling Policies)

Nhân Linux hỗ trợ các chính sách lập lịch sau:

**SCHED\_FIFO**
Chính sách lập lịch được thiết kế cho các ứng dụng yêu cầu thời gian nghiêm ngặt. Nó sử dụng thuật toán "First In - First Out" (Vào trước - Ra trước).

**SCHED\_BATCH**
Chính sách lập lịch được thiết kế cho các tác vụ sử dụng nhiều CPU.

**SCHED\_IDLE**
Chính sách lập lịch dành cho các tiến trình có mức độ ưu tiên **rất thấp**.

**SCHED\_OTHER**
Chính sách lập lịch chia sẻ thời gian mặc định của Linux, được sử dụng cho phần lớn các tiến trình.

**SCHED\_RR**
Tương tự như **SCHED\_FIFO**, nhưng sử dụng thuật toán lập lịch **vòng tròn (Round Robin)**.

---

#### 13.3.5 Thay đổi Thuộc tính Thời gian Thực của Tiến trình bằng lệnh `chrt`

Lệnh `chrt` dùng để thiết lập hoặc truy vấn các thuộc tính lập lịch thời gian thực của một tiến trình đang chạy, hoặc để chạy một lệnh với các thuộc tính đã được chỉ định. Bạn có thể lấy hoặc đặt cả chính sách lập lịch và mức độ ưu tiên của một tiến trình.

Trong các ví dụ bên dưới, một tiến trình có PID là 16244 được sử dụng.

---

**Để truy vấn** các thuộc tính thời gian thực của một tác vụ hiện có:

```bash
root # chrt -p 16244
pid 16244's current scheduling policy: SCHED_OTHER
pid 16244's current scheduling priority: 0
```

---

Trước khi đặt một chính sách lập lịch mới cho tiến trình, bạn cần kiểm tra phạm vi giá trị **ưu tiên tối thiểu và tối đa** hợp lệ cho từng thuật toán lập lịch:

```bash
root # chrt -m
SCHED_OTHER min/max priority : 0/0
SCHED_FIFO min/max priority : 1/99
SCHED_RR min/max priority : 1/99
SCHED_BATCH min/max priority : 0/0
SCHED_IDLE min/max priority : 0/0
```

---

Trong ví dụ trên:

* Các chính sách **SCHED\_OTHER**, **SCHED\_BATCH**, **SCHED\_IDLE** chỉ cho phép mức ưu tiên là **0**.
* Trong khi đó, **SCHED\_FIFO** và **SCHED\_RR** cho phép phạm vi ưu tiên từ **1 đến 99**.

---

**Để đặt** chính sách lập lịch là **SCHED\_BATCH**:

```bash
root # chrt -b -p 0 16244
pid 16244's current scheduling policy: SCHED_BATCH
pid 16244's current scheduling priority: 0
```

---

 Để biết thêm thông tin về `chrt`, hãy xem trang hướng dẫn của nó bằng lệnh:

```bash
man 1 chrt
```
---

#### 13.3.6 Tinh chỉnh khi chạy với `sysctl`

Giao diện `sysctl` dùng để kiểm tra và thay đổi các tham số của nhân (kernel) trong thời gian thực, cho phép bạn điều chỉnh hành vi mặc định của bộ lập lịch tiến trình. Cú pháp của `sysctl` rất đơn giản, và tất cả các lệnh sau phải được thực hiện từ dòng lệnh với quyền **root**.

---

**Để đọc giá trị của một biến nhân**, nhập:

```bash
sysctl variable
```

---

**Để gán một giá trị**, nhập:

```bash
sysctl variable=value
```

---

**Để lấy danh sách tất cả các biến `sysctl` liên quan đến bộ lập lịch**, nhập:

```bash
sysctl -A | grep "sched" | grep -v "domain"
```

Ví dụ đầu ra:

```bash
root # sysctl -A | grep "sched" | grep -v "domain"
kernel.sched_cfs_bandwidth_slice_us = 5000
kernel.sched_child_runs_first = 0
kernel.sched_compat_yield = 0
kernel.sched_latency_ns = 6000000
kernel.sched_migration_cost_ns = 500000
kernel.sched_min_granularity_ns = 2000000
kernel.sched_nr_migrate = 32
kernel.sched_rr_timeslice_ms = 25
kernel.sched_rt_period_us = 1000000
kernel.sched_rt_runtime_us = 950000
kernel.sched_shares_window_ns = 10000000
kernel.sched_time_avg_ms = 1000
kernel.sched_tunable_scaling = 1
kernel.sched_wakeup_granularity_ns = 2500000
```

---

**Lưu ý**:
Các biến có hậu tố `_ns` và `_us` nhận giá trị tương ứng theo đơn vị **nanosecond** và **microsecond**.

---

Danh sách một số biến tinh chỉnh quan trọng nhất của bộ lập lịch tiến trình thông qua `sysctl` (nằm tại `/proc/sys/kernel/`) cùng mô tả ngắn gọn như sau:

---

**`sched_child_runs_first`**

Một tiến trình con mới tạo sẽ chạy trước khi tiến trình cha tiếp tục thực thi. Thiết lập tham số này thành `1` có lợi cho các ứng dụng mà tiến trình con thực thi trước sẽ hiệu quả hơn.
Ví dụ: lệnh `make -j<NUM_CPU>` hoạt động tốt hơn khi `sched_child_runs_first` được bật.
Giá trị mặc định là `0`.

---

**`sched_compat_yield`**

Kích hoạt hành vi yield tích cực như trong bộ lập lịch Q(1) cũ. Các ứng dụng Java sử dụng đồng bộ hóa nhiều thường hoạt động tốt hơn khi giá trị này là `1`.
Chỉ sử dụng khi bạn thấy có sự suy giảm hiệu suất.
Giá trị mặc định là `0`.
Nên dùng `1` nếu ứng dụng của bạn phụ thuộc vào hành vi của `sched_yield()`.

---

**`sched_migration_cost_ns`**

Là khoảng thời gian sau lần thực thi cuối mà một tác vụ được coi là “nóng trong bộ đệm” (cache hot) để quyết định việc di chuyển (migration).
Một tác vụ “nóng” ít có khả năng bị di chuyển, do đó tăng giá trị này giúp giảm việc di chuyển tiến trình.
Giá trị mặc định: `500000` nanosecond (ns).

Nếu CPU ở trạng thái nhàn rỗi nhiều hơn kỳ vọng khi có nhiều tiến trình đang chờ, hãy giảm giá trị này. Nếu tiến trình bị chuyển giữa các CPU hoặc node quá thường xuyên, hãy tăng giá trị này.

---

**`sched_latency_ns`**

Độ trễ tước quyền (preemption latency) mục tiêu cho các tác vụ nặng về CPU.
Tăng biến này sẽ làm tăng lát thời gian (timeslice) của các tác vụ đó.
Lát thời gian được tính như sau:

```
timeslice = thời kỳ lập lịch * (trọng số của tiến trình / tổng trọng số của các tiến trình trong hàng đợi)
```

* Trọng số tiến trình phụ thuộc vào mức độ ưu tiên và chính sách lập lịch.
  Trọng số tối thiểu của tiến trình với `SCHED_OTHER` là 15 (nice 19), tối đa là 88761 (nice -20).
* Khi tải hệ thống tăng, lát thời gian sẽ nhỏ lại.
* Khi số tiến trình chạy vượt quá `sched_latency_ns / sched_min_granularity_ns`, lát thời gian được tính lại theo:

```
số tiến trình chạy * sched_min_granularity_ns
```

Giá trị này cũng xác định khoảng thời gian tối đa mà một tiến trình ngủ được xem là vẫn đang chạy để tính toán tài nguyên.
Giá trị mặc định: `6000000` ns.

---

**`sched_min_granularity_ns`**

Độ phân giải tước quyền tối thiểu cho các tác vụ nặng về CPU.
Xem thêm `sched_latency_ns` để biết chi tiết.
Giá trị mặc định: `4000000` ns.

---

**`sched_wakeup_granularity_ns`**

Độ phân giải tước quyền khi đánh thức tiến trình.
Tăng biến này sẽ giảm số lần đánh thức tiến trình (wake-up preemption), giảm nhiễu với các tác vụ tính toán.
Giảm biến này sẽ tăng hiệu suất đánh thức các tiến trình nhạy với độ trễ (ví dụ như các tiến trình xử lý thời gian thực).
Giá trị mặc định: `2500000` ns.

---

🔴 **Cảnh báo: Cài đặt giá trị độ phân giải đánh thức (Wake-up Granularity) phù hợp**
Nếu bạn đặt giá trị **lớn hơn một nửa** của `sched_latency_ns`, sẽ không còn xảy ra việc tước quyền khi đánh thức tiến trình.
Các tiến trình có chu kỳ hoạt động ngắn sẽ không thể cạnh tranh hiệu quả với các tiến trình chiếm CPU liên tục.

---

**`sched_rt_period_us`**

Chu kỳ trong đó băng thông dành cho các tiến trình thời gian thực được áp dụng.
Giá trị mặc định là **1.000.000** micro giây (µs).

---

**`sched_rt_runtime_us`**

Khoảng thời gian được cấp phát cho các tiến trình thời gian thực trong mỗi chu kỳ `sched_rt_period_us`.
Thiết lập giá trị là `-1` sẽ vô hiệu hóa kiểm soát băng thông tiến trình thời gian thực.

Mặc định, tiến trình thời gian thực có thể sử dụng đến **95% CPU/giây**, tức là để lại **5% CPU/giây** (hoặc 0,05 giây) cho các tiến trình thuộc loại `SCHED_OTHER`.
Giá trị mặc định là **950000** µs.

---

**`sched_nr_migrate`**

Kiểm soát số lượng tiến trình có thể được di chuyển giữa các bộ xử lý thông qua ngắt phần mềm di chuyển (softirq).
Nếu có nhiều tiến trình thuộc `SCHED_OTHER`, tất cả chúng sẽ chạy trên cùng một bộ xử lý.
Giá trị mặc định là **32**.
Tăng giá trị này giúp cải thiện hiệu năng cho các luồng `SCHED_OTHER` lớn, nhưng sẽ làm tăng độ trễ của các tiến trình thời gian thực.

---

#### 13.3.7 Giao diện Gỡ lỗi và Thống kê Bộ lập lịch

CFS đi kèm với một giao diện gỡ lỗi được cải tiến và cung cấp thông tin thống kê khi chạy. Các tệp liên quan được thêm vào hệ thống tệp **/proc**, có thể được xem đơn giản bằng lệnh `cat` hoặc `less`. Dưới đây là danh sách các tệp liên quan trong `/proc` cùng mô tả ngắn gọn:

---

**`/proc/sched_debug`**

Chứa các giá trị hiện tại của tất cả các biến có thể tinh chỉnh (xem **Mục 13.3.6, “Runtime Tuning with sysctl”**), ảnh hưởng đến hành vi của bộ lập lịch, thống kê của CFS và thông tin về hàng đợi tiến trình chạy trên tất cả các bộ xử lý.

---

Ví dụ đầu ra:

```bash
root # cat /proc/sched_debug
Sched Debug Version: v0.11, 3.12.24-7-default #1
ktime                          : 23533900.395978
sched_clk                      : 23543587.726648
cpu_clk                        : 23533900.396165
jiffies                        : 4300775771
sched_clock_stable             : 0
```

Các tham số từ `sysctl_sched`:

```
.sysctl_sched_latency          : 6.000000
.sysctl_sched_min_granularity : 2.000000
.sysctl_sched_wakeup_granularity : 2.500000
.sysctl_sched_child_runs_first : 0
.sysctl_sched_features         : 154871
.sysctl_sched_tunable_scaling : 1 (Logarithmic)
```

Thông tin về CPU:

```
cpu#0, 2666.762 MHz
.nr_running                    : 1
.load                          : 1024
.nr_switches                   : 1918946
```

Thông tin hàng đợi CFS (`cfs_rq[0]`):

```
.exec_clock                    : 170176.383770
.MIN_vruntime                  : 0.000001
.min_vruntime                  : 347375.854324
.max_vruntime                  : 0.000001
```

Thông tin hàng đợi thời gian thực (`rt_rq[0]`):

```
.rt_nr_running                 : 0
.rt_throttled                  : 0
.rt_time                       : 0.000000
.rt_runtime                    : 950.000000
```

---

**Các tiến trình có thể chạy (runnable tasks):**

```
task   PID     tree-key switches prio exec-runtime sum-exec sum-sleep
R      cat     21772    347375.854324 2    120      347375.854324 0.000000 0 /
```
---

**`/proc/schedstat`**

Hiển thị các thống kê liên quan đến hàng đợi chạy hiện tại. Cũng hiển thị các thống kê theo miền dành cho hệ thống SMP (đa vi xử lý) cho tất cả các bộ xử lý đang kết nối.
Vì định dạng đầu ra không thân thiện với người dùng, hãy đọc nội dung tại:

```
/usr/src/linux/Documentation/scheduler/sched-stats.txt
```

để biết thêm thông tin.

---

**`/proc/PID/sched`**

Hiển thị thông tin lập lịch của tiến trình có ID là **PID**.

Ví dụ:

```bash
root # cat /proc/$(pidof gdm)/sched
gdm (744, #threads: 3)
---------------------------------------------------------
se.exec_start                : 8888.753881
se.vruntime                  : 6062.853815
se.sum_exec_runtime          : 7.836043
se.statistics.wait_start     : 0.000000
se.statistics.sleep_start    : 8888.753881
se.statistics.block_start    : 0.000000
se.statistics.sleep_max      : 1965.987638
[...]
se.avg.decay_count           : 8477
policy                       : 0
prio                         : 120
clock-delta                  : 128
mm->numa_scan_seq            : 0
numa_migrations              : 0
numa_faults_memory, 0, 0, 1, 0, 0, -1
numa_faults_memory, 1, 0, 0, 0, -1
```

**Giải thích một số trường phổ biến:**

* `se.exec_start`: thời gian lần đầu tiến trình bắt đầu chạy
* `se.vruntime`: thời gian ảo mà tiến trình đã sử dụng (dùng để tính toán thứ tự ưu tiên)
* `se.sum_exec_runtime`: tổng thời gian tiến trình đã thực thi
* `policy`: chính sách lập lịch (0 = SCHED\_OTHER)
* `prio`: mức độ ưu tiên của tiến trình (càng nhỏ càng ưu tiên cao)

---

