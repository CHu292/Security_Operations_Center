# CFS Scheduler

---

## **1. TỔNG QUAN**

CFS là viết tắt của “Completely Fair Scheduler” (Bộ lập lịch hoàn toàn công bằng), là bộ lập lịch tiến trình "dành cho máy tính để bàn" do Ingo Molnar phát triển và được tích hợp vào Linux từ phiên bản 2.6.23. Khi được tích hợp lần đầu, nó đã thay thế cho bộ lập lịch trước đó là `SCHED_OTHER` – bộ lập lịch tương tác tiêu chuẩn. Ngày nay, CFS đang dần được thay thế bởi EEVDF, tài liệu về EEVDF có thể được tìm thấy tại [EEVDF Scheduler](https://www.kernel.org/doc/html/latest/scheduler/sched-eevdf.html).

80% thiết kế của CFS có thể được tóm gọn trong một câu:
**CFS về cơ bản mô phỏng một “CPU đa nhiệm lý tưởng, chính xác” trên phần cứng thực tế.**

“CPU lý tưởng cho đa nhiệm” là một khái niệm giả định: một CPU có 100% công suất vật lý và có thể chạy từng tác vụ ở tốc độ chia đều, song song, với tốc độ là 1 / số lượng tác vụ đang chạy. Ví dụ: nếu có 2 tác vụ đang chạy, mỗi tác vụ sẽ chạy với 50% công suất thực — nghĩa là, thực sự chạy song song.

Trên phần cứng thực tế, CPU chỉ có thể chạy một tác vụ tại một thời điểm, vì vậy cần giới thiệu khái niệm “thời gian chạy ảo” (virtual runtime). Thời gian chạy ảo của một tác vụ chỉ định thời điểm mà lần chia thời gian (timeslice) tiếp theo của nó sẽ bắt đầu chạy trên CPU đa nhiệm lý tưởng nói trên. Trên thực tế, thời gian chạy ảo của một tác vụ chính là thời gian chạy thực tế của nó được chuẩn hóa theo tổng số tác vụ đang chạy.

---

## **2. MỘT SỐ CHI TIẾT TRIỂN KHAI**

Trong CFS, **thời gian chạy ảo (virtual runtime)** được biểu diễn và theo dõi thông qua giá trị `p->se.vruntime` (đơn vị nano giây) của từng tiến trình. Nhờ đó, ta có thể đánh dấu thời điểm chính xác và đo lường “thời gian CPU kỳ vọng” mà một tiến trình lẽ ra phải nhận được.

> **Chi tiết nhỏ:** Trên phần cứng “lý tưởng”, tại mọi thời điểm, tất cả các tiến trình sẽ có cùng giá trị `p->se.vruntime`, tức là các tiến trình sẽ được thực thi đồng thời và không có tiến trình nào bị “mất cân bằng” so với phần chia CPU “lý tưởng”.

**Logic lựa chọn tiến trình** của CFS dựa trên giá trị `p->se.vruntime`, và nó rất đơn giản: luôn cố gắng chạy tiến trình có giá trị `p->se.vruntime` nhỏ nhất (tức là tiến trình đã được thực thi ít nhất cho đến thời điểm đó).
CFS luôn cố gắng phân chia thời gian CPU giữa các tiến trình có thể chạy sao cho gần với “phần cứng đa nhiệm lý tưởng” nhất có thể.

Phần lớn các phần còn lại trong thiết kế của CFS được xây dựng dựa trên khái niệm đơn giản này, chỉ bổ sung thêm một vài tính năng như cấp độ ưu tiên (`nice`), xử lý đa lõi (`multiprocessing`), và các biến thể thuật toán để nhận biết tiến trình đang ngủ (`sleepers`).


---

## **3. CÂY ĐỎ-ĐEN (RBTREE)**

Thiết kế của CFS khá triệt để: nó không sử dụng các cấu trúc dữ liệu cũ cho hàng đợi tiến trình, mà dùng **cây đỏ-đen có thứ tự thời gian** để xây dựng một “dòng thời gian” cho việc thực thi các tác vụ trong tương lai, do đó không xuất hiện hiện tượng “chuyển mảng” (array switch) như ở các bộ lập lịch cũ như vanilla scheduler hay RSDL/SD.

CFS cũng duy trì giá trị `rq->cfs.min_vruntime`, là giá trị tăng đơn điệu đại diện cho **thời gian chạy nhỏ nhất** trong số các tiến trình trong hàng đợi. Tổng khối lượng công việc được theo dõi bằng `min_vruntime`; giá trị này được dùng để đưa các tiến trình mới tạo vào phía bên trái của cây càng nhiều càng tốt.

**Tổng số tiến trình đang chạy** trong hàng đợi được tính thông qua `rq->cfs.load`, là tổng của trọng số của các tiến trình đang xếp trong hàng đợi.

CFS duy trì một cây đỏ-đen được sắp xếp theo thứ tự thời gian, nơi tất cả các tiến trình sẵn sàng chạy được sắp theo khóa `p->se.vruntime`. CFS chọn tiến trình **“bên trái nhất”** từ cây này và chạy nó. Khi hệ thống tiến hành thực thi, các tiến trình đã chạy được đưa dần về phía bên phải --- một cách chậm rãi nhưng chắc chắn, điều đó cho mọi tiến trình cơ hội trở thành “tiến trình trái nhất” và được CPU chọn trong một khoảng thời gian xác định.

**Tóm lại, CFS hoạt động như sau:** nó chạy một tiến trình trong một thời gian ngắn, rồi khi có tick lập lịch (hoặc scheduler tick), **thời gian sử dụng CPU thực tế** của tiến trình sẽ được cộng vào `p->se.vruntime`. Khi giá trị này đủ cao để tiến trình không còn là “tiến trình trái nhất” nữa (so với các tiến trình khác trong cây), thì tiến trình mới “trái nhất” sẽ được chọn và tiến trình hiện tại bị dừng (preempted). Điều này giúp tránh việc lập lịch quá mức và phá vỡ bộ nhớ đệm (cache).

---

## **4. MỘT SỐ ĐẶC ĐIỂM CỦA CFS**

* CFS sử dụng tính toán thời gian ở độ phân giải nano giây và không phụ thuộc vào jiffies hoặc thông số HZ khác. Vì vậy, **CFS không sử dụng khái niệm “khoảng thời gian” (timeslice)** như bộ lập lịch trước đây và **không sử dụng bất kỳ heuristic (quy luật thực nghiệm) nào**. Nó chỉ có duy nhất một tham số có thể điều chỉnh:

  ```
  /sys/kernel/debug/sched/base_slice_ns
  ```

* Tham số này có thể được dùng để điều chỉnh lập lịch từ chế độ “máy để bàn” (độ trễ thấp) đến chế độ “máy chủ” (tối ưu cho xử lý theo lô). Mặc định, giá trị này phù hợp với các tác vụ máy để bàn. Các tiến trình `SCHED_BATCH` cũng được xử lý bởi module lập lịch CFS.

* Nếu tham số `CONFIG_HZ` làm cho `base_slice_ns < TICK_NSEC`, thì giá trị của `base_slice_ns` sẽ hầu như không ảnh hưởng đến khối lượng công việc.

* Với thiết kế của mình, bộ lập lịch CFS **không dễ bị các “tấn công heuristic”** mà các bộ lập lịch truyền thống (stock scheduler) gặp phải. Ví dụ, các tệp như: `fiftyp.c`, `thud.c`, `chew.c`, `ring-test.c`, `massive_intr.c` đều hoạt động tốt và **không ảnh hưởng đến tính tương tác**, đồng thời vẫn đảm bảo hành vi mong đợi.

* Bộ lập lịch CFS có **khả năng xử lý mức độ “nice” và tiến trình `SCHED_BATCH` tốt hơn nhiều** so với bộ lập lịch vanilla trước đó: cả hai loại tiến trình được cách ly và xử lý mạnh mẽ hơn.

* **Cân bằng tải SMP (đa xử lý song song)** đã được viết lại và làm sạch: các giả định trước đây về cách duyệt hàng đợi đã bị loại bỏ khỏi mã cân bằng tải, và các trình lặp của module lập lịch được đơn giản hóa hơn. Mã cân bằng tải vì thế trở nên đơn giản hơn.

---

## **5. Chính sách lập lịch**

CFS triển khai ba chính sách lập lịch:

* **`SCHED_NORMAL`** *(truyền thống gọi là `SCHED_OTHER`)*:
  Chính sách lập lịch được sử dụng cho các tiến trình thông thường.

* **`SCHED_BATCH`**:
  Không thực hiện ngắt tiến trình thường xuyên như các tác vụ thông thường, nhờ đó cho phép tiến trình chạy lâu hơn và sử dụng bộ nhớ đệm (cache) hiệu quả hơn, nhưng **đổi lại là giảm khả năng tương tác với người dùng**. Phù hợp với các công việc theo lô (batch jobs).

* **`SCHED_IDLE`**:
  Còn yếu hơn cả mức ưu tiên `nice 19`, nhưng **không phải là một bộ lập lịch chờ thực sự**. Nó được thiết kế như vậy để tránh các vấn đề về đảo ngược ưu tiên (priority inversion) có thể dẫn đến tình trạng **treo hệ thống**.

---

Các chính sách **`SCHED_FIFO` và `SCHED_RR`** được triển khai trong `sched/rt.c` và tuân theo chuẩn **POSIX**.

Lệnh `chrt` từ gói `util-linux-ng` phiên bản 2.13.1.1 có thể thiết lập tất cả các chính sách **ngoại trừ `SCHED_IDLE`**.

---

## 6. **LỚP LẬP LỊCH**

Bộ lập lịch CFS mới được thiết kế sao cho có thể giới thiệu các **“Lớp lập lịch”** (*Scheduling Classes*) — một hệ thống phân cấp có thể mở rộng của các module lập lịch. Các module này đóng gói chi tiết chính sách lập lịch và được xử lý bởi lõi bộ lập lịch mà không cần lõi phải biết quá nhiều thông tin cụ thể.

* **`sched/fair.c`** triển khai bộ lập lịch CFS đã mô tả ở trên.
* **`sched/rt.c`** triển khai ngữ nghĩa của **`SCHED_FIFO` và `SCHED_RR`** đơn giản hơn so với bộ lập lịch vanilla trước đó. Nó sử dụng 100 hàng đợi chạy (*runqueues*) tương ứng với 100 mức ưu tiên RT, thay vì 140 như trước đây, và **không cần mảng hết hạn (expired array)**.

---

Các lớp lập lịch được triển khai thông qua cấu trúc **`sched_class`**, chứa các **hook** tới các hàm cần được gọi khi có sự kiện đáng chú ý xảy ra.

Dưới đây là **danh sách một phần** các hook:

---

* **`enqueue_task(...)`**
  Được gọi khi một tiến trình chuyển sang trạng thái sẵn sàng chạy. Hàm này đưa thực thể lập lịch (task) vào **cây đỏ-đen (red-black tree)** và tăng biến `nr_running`.

* **`dequeue_task(...)`**
  Được gọi khi một tiến trình không còn ở trạng thái sẵn sàng chạy. Hàm này xóa thực thể lập lịch ra khỏi cây đỏ-đen và giảm `nr_running`.

* **`yield_task(...)`**
  Thực chất là một lần gọi `dequeue` rồi `enqueue` ngay sau đó. Nếu `compat_yield sysctl` được bật, task sẽ được đưa vào vị trí cuối cùng bên phải của cây đỏ-đen.

* **`wakeup_preempt(...)`**
  Hàm này kiểm tra xem một tiến trình mới vào trạng thái sẵn sàng chạy có nên **giành quyền điều khiển CPU** từ tiến trình đang chạy hay không.

* **`pick_next_task(...)`**
  Chọn tiến trình thích hợp nhất để chạy tiếp theo.

* **`set_next_task(...)`**
  Được gọi khi tiến trình **thay đổi lớp lập lịch**, nhóm tiến trình hoặc chuẩn bị được lập lịch lại.

* **`task_tick(...)`**
  Thường được gọi từ hàm tick định kỳ của hệ thống. Có thể gây ra chuyển đổi tiến trình (**process switch**), đóng vai trò trong việc kích hoạt **preemption** (giành CPU).

---

## 7. **MỞ RỘNG BỘ LẬP LỊCH NHÓM TRONG CFS**

Thông thường, bộ lập lịch hoạt động trên các tiến trình riêng lẻ và cố gắng phân chia thời gian CPU công bằng cho từng tiến trình. Tuy nhiên, đôi khi sẽ **hữu ích nếu nhóm các tiến trình lại và phân chia thời gian CPU cho từng nhóm**, ví dụ như phân thời gian CPU cho từng người dùng, rồi sau đó đến từng tiến trình thuộc về người dùng đó.

`CONFIG_CGROUP_SCHED` được thiết kế để hỗ trợ điều này. Nó cho phép nhóm các tiến trình lại và **phân phối thời gian CPU công bằng giữa các nhóm**.

* `CONFIG_RT_GROUP_SCHED`: Cho phép nhóm các tiến trình **real-time** (ví dụ: `SCHED_FIFO`, `SCHED_RR`).
* `CONFIG_FAIR_GROUP_SCHED`: Cho phép nhóm các tiến trình CFS (ví dụ: `SCHED_NORMAL`, `SCHED_BATCH`).

> Các tùy chọn này yêu cầu bật `CONFIG_CGROUPS` và quản trị viên phải tạo các **nhóm tiến trình tuỳ ý** bằng cách sử dụng hệ thống tệp giả “cgroup”.
> (Xem thêm: **[Control Groups](https://www.kernel.org/doc/Documentation/cgroup-v1/cgroups.txt)** để biết thêm thông tin.)

---

Khi `CONFIG_FAIR_GROUP_SCHED` được bật, một file `cpu.shares` sẽ được tạo cho mỗi nhóm. File này được sử dụng để điều chỉnh tỉ lệ CPU mà nhóm đó được cấp phát.

#### Ví dụ về tạo nhóm và điều chỉnh phân phối CPU:

```bash
# Mount hệ thống tệp cgroup
mount -t tmpfs cgroup_root /sys/fs/cgroup
mkdir /sys/fs/cgroup/cpu
mount -t cgroup -ocpu none /sys/fs/cgroup/cpu
cd /sys/fs/cgroup/cpu

# Tạo nhóm tiến trình
mkdir multimedia     # nhóm "multimedia"
mkdir browser        # nhóm "browser"

# Cấu hình multimedia nhận gấp đôi băng thông CPU so với browser
echo 2048 > multimedia/cpu.shares
echo 1024 > browser/cpu.shares

# Khởi chạy firefox và đưa vào nhóm browser
firefox &
echo <firefox_pid> > browser/tasks

# Khởi chạy gmpplayer (hoặc media player khác) và đưa vào nhóm multimedia
echo <movie_player_pid> > multimedia/tasks
```

---
