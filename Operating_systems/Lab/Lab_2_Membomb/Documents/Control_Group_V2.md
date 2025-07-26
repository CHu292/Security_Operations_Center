# Control Group Version 2

>**Nhóm điều khiển (Control Group) v2**

[Bài Viết Gốc](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html)

Đây là tài liệu chính thức về thiết kế, giao diện và quy ước của cgroup phiên bản 2. Nó mô tả tất cả các khía cạnh mà người dùng có thể thấy được của cgroup, bao gồm phần lõi và hành vi của các bộ điều khiển cụ thể. Mọi thay đổi trong tương lai đều phải được phản ánh trong tài liệu này.
Tài liệu cho phiên bản v1 có sẵn tại: [Control Group Version 1](../README.md)

---

## 1. **Giới thiệu**

### **Thuật ngữ**

“cgroup” là viết tắt của “control group” (nhóm điều khiển) và **không bao giờ viết hoa**.
Dạng số ít được dùng để chỉ toàn bộ tính năng này cũng như để bổ nghĩa như trong “group controllers” (bộ điều khiển nhóm).
Khi nói rõ về nhiều nhóm điều khiển riêng biệt, dạng số nhiều “cgroups” sẽ được sử dụng.

---

### **Cgroup là gì?**

Cgroup là một cơ chế dùng để tổ chức các tiến trình theo dạng phân cấp và phân phối tài nguyên hệ thống dọc theo hệ phân cấp đó một cách có kiểm soát và có thể cấu hình được.

Cgroup chủ yếu gồm hai phần – phần lõi (core) và các bộ điều khiển (controllers). Phần lõi của cgroup chịu trách nhiệm chính trong việc tổ chức các tiến trình theo cấu trúc phân cấp. Bộ điều khiển cgroup thường đảm nhiệm việc phân phối một loại tài nguyên hệ thống cụ thể theo phân cấp, mặc dù cũng có những bộ điều khiển tiện ích phục vụ các mục đích khác ngoài việc phân phối tài nguyên.

Các cgroup tạo thành một cấu trúc cây và mỗi tiến trình trong hệ thống chỉ thuộc về một và chỉ một cgroup duy nhất. Tất cả các luồng (threads) của một tiến trình đều thuộc về cùng một cgroup. Khi được tạo ra, mọi tiến trình đều được đưa vào cgroup mà tiến trình cha của nó đang thuộc về tại thời điểm đó. Một tiến trình có thể được di chuyển sang một cgroup khác. Việc di chuyển một tiến trình không ảnh hưởng đến các tiến trình con đã tồn tại trước đó.

Dựa trên một số ràng buộc cấu trúc nhất định, các bộ điều khiển có thể được bật hoặc tắt chọn lọc trên một cgroup. Tất cả hành vi của bộ điều khiển đều mang tính phân cấp – nếu một bộ điều khiển được bật trên một cgroup, nó sẽ ảnh hưởng đến tất cả tiến trình thuộc các nhóm nằm trong cây phân cấp con của cgroup đó. Khi một bộ điều khiển được bật ở một cgroup con (nested), nó sẽ luôn giới hạn việc phân phối tài nguyên nhiều hơn nữa. Các ràng buộc được thiết lập gần gốc hơn trong cây phân cấp sẽ không thể bị ghi đè bởi các cgroup nằm xa hơn.

---

## 2. **Các thao tác cơ bản**

### **Mount**

Không giống như v1, cgroup v2 chỉ có một cây phân cấp duy nhất. Cây phân cấp của cgroup v2 có thể được mount bằng lệnh sau:

```bash
# mount -t cgroup2 none $MOUNT_POINT
```

Hệ thống tập tin của cgroup2 có số magic là `0x63677270` (tức là “cgrp”). Tất cả các bộ điều khiển (controllers) hỗ trợ v2 và chưa được gắn vào cây phân cấp v1 sẽ tự động được gắn vào cây phân cấp v2 và hiển thị tại gốc. Những bộ điều khiển không được sử dụng tích cực trong v2 vẫn có thể được gắn vào các cây phân cấp khác. Điều này cho phép kết hợp cây phân cấp v2 với hệ thống phân cấp v1 cũ một cách tương thích ngược hoàn toàn.

Một bộ điều khiển chỉ có thể được chuyển đổi giữa các cây phân cấp khi nó không còn được tham chiếu trong cây hiện tại. Do trạng thái của mỗi bộ điều khiển per-cgroup bị hủy bất đồng bộ và có thể có tham chiếu còn sót lại, một bộ điều khiển có thể không xuất hiện ngay trong v2 sau khi đã được gỡ khỏi cây phân cấp trước đó. Tương tự, một bộ điều khiển cần được vô hiệu hóa hoàn toàn trước khi có thể được chuyển ra khỏi cây phân cấp hợp nhất, và có thể mất một khoảng thời gian để bộ điều khiển đã bị vô hiệu hóa này trở nên khả dụng ở các cây khác. Ngoài ra, do có các phụ thuộc giữa các bộ điều khiển, một số bộ điều khiển khác cũng có thể cần bị vô hiệu hóa theo.

Dù hữu ích cho phát triển và cấu hình thủ công, việc di chuyển bộ điều khiển giữa v2 và các cây phân cấp khác một cách động là điều không được khuyến khích trong môi trường sản xuất. Nên quyết định rõ ràng cây phân cấp và sự liên kết giữa các bộ điều khiển trước khi bắt đầu sử dụng hệ thống cgroup.

Trong quá trình chuyển sang v2, phần mềm quản lý hệ thống có thể vẫn sẽ tự động mount hệ thống tập tin cgroup v1 và chiếm quyền điều khiển tất cả các bộ điều khiển trong quá trình khởi động, trước khi việc can thiệp thủ công có thể thực hiện được. Để việc kiểm thử và thử nghiệm dễ dàng hơn, kernel cho phép sử dụng tham số `cgroup_no_v1=` để vô hiệu hóa các bộ điều khiển trong v1 và làm cho chúng chỉ khả dụng trong v2.

**cgroup v2 hiện hỗ trợ các tùy chọn mount sau:**

**nsdelegate**

Xem namespace của cgroup như là ranh giới ủy quyền. Tùy chọn này có phạm vi toàn hệ thống và chỉ có thể được thiết lập khi mount hoặc remount từ namespace khởi tạo (`init namespace`). Tùy chọn mount này sẽ bị bỏ qua khi thực hiện mount từ các namespace không phải là init. Tham khảo phần “Delegation” để biết thêm chi tiết.

---

**favordynmods**

Giảm độ trễ trong các thao tác sửa đổi cgroup động, chẳng hạn như di chuyển tác vụ và bật/tắt controller — tuy nhiên sẽ làm tăng chi phí cho các thao tác nóng như `fork` và `exit`. Mô hình sử dụng tĩnh kiểu tạo cgroup, kích hoạt controller, sau đó gán tác vụ với `CLONE_INTO_CGROUP` sẽ không bị ảnh hưởng bởi tùy chọn này.

---

**memory\_localevents**

Chỉ ghi các sự kiện `memory.events` với dữ liệu của cgroup hiện tại, không bao gồm các cây con. Đây là hành vi cũ (legacy), còn hành vi mặc định nếu không có tùy chọn này là bao gồm cả số liệu của cây con. Tùy chọn này áp dụng toàn hệ thống và chỉ có thể được thiết lập khi mount hoặc remount từ namespace khởi tạo. Nó sẽ bị bỏ qua nếu mount từ namespace không phải init.

---

**memory\_recursiveprot**

Áp dụng đệ quy các ràng buộc bảo vệ `memory.min` và `memory.low` cho toàn bộ cây con, mà không cần khai báo rõ ràng việc truyền xuống các cgroup con. Điều này giúp bảo vệ toàn bộ cây con khỏi nhau, trong khi vẫn giữ được sự cạnh tranh tự do giữa các cây đó. Tùy chọn này nên là mặc định, nhưng được đưa vào như một tùy chọn mount để tránh gây lỗi cho các thiết lập cũ vốn phụ thuộc vào ngữ nghĩa ban đầu (ví dụ: đặt giá trị “bypass” quá cao ở các cấp cây cao hơn).

---

**memory\_hugetlb\_accounting**

Tính toán mức sử dụng bộ nhớ HugeTLB vào tổng lượng bộ nhớ của cgroup, để phục vụ cho controller bộ nhớ (cho mục đích báo cáo thống kê và bảo vệ bộ nhớ). Đây là hành vi mới có thể làm thay đổi các thiết lập hiện có, vì vậy cần phải kích hoạt thủ công thông qua tùy chọn mount này.

---

**Một vài lưu ý quan trọng cần nhớ:**

* **Không có cơ chế quản lý pool HugeTLB trong memory controller.** Pool được cấp phát trước không thuộc về bất kỳ ai. Cụ thể, khi một folio HugeTLB mới được cấp phát cho pool, nó sẽ **không** được tính vào bộ nhớ từ góc nhìn của memory controller. Nó chỉ được tính vào một cgroup khi thực sự được sử dụng (ví dụ: khi được dùng đầy một trang). Quản lý overcommit bộ nhớ phía host phải xem xét điều này khi cấu hình các giới hạn cứng. Nói chung, việc quản lý pool HugeTLB nên được xử lý qua các cơ chế khác (như HugeTLB controller).

* **Việc không tính folio HugeTLB vào memory controller sẽ dẫn đến lỗi SIGBUS.** Điều này có thể xảy ra **ngay cả khi** pool HugeTLB vẫn còn trang khả dụng (nhưng giới hạn của nhóm bị chạm và nỗ lực reclaim thất bại).

* **Tính toán bộ nhớ HugeTLB trong memory controller sẽ ảnh hưởng đến bảo vệ bộ nhớ và động lực reclaim.** Bất kỳ tinh chỉnh nào từ phía userspace (như thiết lập giới hạn tối thiểu hoặc tối đa bộ nhớ) cần tính đến điều này.

* **Các trang HugeTLB được sử dụng khi tùy chọn này không được bật sẽ không được memory controller theo dõi,** ngay cả khi sau đó cgroup v2 được remount lại.

---

**pids\_localevents**

Tùy chọn này khôi phục hành vi giống v1 của `pids.events:max`, tức là **chỉ tính toán cục bộ** (bên trong cgroup hiện tại) các lỗi fork. Nếu không bật tùy chọn này, `pids.events.max` sẽ đại diện cho toàn bộ giới hạn `pids.max` trên toàn bộ cây con của cgroup.

---

## 3. Organizing Processes and Threads

>Tổ chức tiến trình và luồng

### **Processes - Tiến trình**

Ban đầu, chỉ tồn tại `cgroup` gốc mà tất cả các tiến trình thuộc về. Một `cgroup` con có thể được tạo ra bằng cách tạo một thư mục con:

```
# mkdir $CGROUP_NAME
```

Một `cgroup` cụ thể có thể có nhiều `cgroup` con, tạo thành một cấu trúc dạng cây. Mỗi `cgroup` có một file giao tiếp `group.procs` cho phép đọc và ghi. Khi đọc file này, nó liệt kê các **PID** (Process ID) của tất cả các tiến trình thuộc về `cgroup`, mỗi PID một dòng. Các PID này không được sắp xếp và cùng một PID có thể xuất hiện nhiều lần nếu tiến trình đã bị di chuyển sang `cgroup` khác rồi quay lại, hoặc PID đó bị tái sử dụng trong quá trình đọc.

Một tiến trình có thể được di chuyển sang `cgroup` khác bằng cách ghi **PID** của nó vào file `cgroup.procs` của `cgroup` đích. Chỉ một tiến trình có thể được di chuyển trong một lệnh `write(2)` duy nhất. Nếu một tiến trình có nhiều luồng (threads), thì việc ghi PID của bất kỳ luồng nào cũng sẽ di chuyển tất cả các luồng sang `cgroup` đích.

Khi một tiến trình tạo ra một tiến trình con, tiến trình mới sẽ được sinh ra trong cùng `cgroup` với tiến trình cha tại thời điểm thực hiện thao tác. Sau khi tiến trình kết thúc, nó vẫn duy trì trong `cgroup` mà nó thuộc về cho đến khi được thu hồi (`reaped`). Tuy nhiên, **tiến trình zombie** sẽ không xuất hiện trong file `cgroup.procs`, và do đó **không thể được di chuyển** sang `cgroup` khác.

Một `cgroup` không có tiến trình con hoặc tiến trình đang sống có thể bị xóa bằng cách xóa thư mục. Lưu ý rằng `cgroup` chỉ chứa **tiến trình zombie** (và không có tiến trình con nào) cũng được coi là rỗng và có thể bị xóa:

```
# rmdir $CGROUP_NAME
```

---

File `/proc/$PID/cgroup` liệt kê danh sách các `cgroup` mà một tiến trình thuộc về. Nếu hệ thống đang sử dụng `cgroup` v1, file này có thể chứa nhiều dòng, mỗi dòng đại diện cho một hierarchy. Với `cgroup` v2, dòng thông tin luôn có định dạng `0::ĐƯỜNG_DẪN`:

```
# cat /proc/842/cgroup
...
0::/test-cgroup/test-cgroup-nested
```

Nếu tiến trình trở thành zombie và `cgroup` mà nó thuộc về bị xóa sau đó, thì `" (deleted)"` sẽ được thêm vào cuối đường dẫn:

```
# cat /proc/842/cgroup
...
0::/test-cgroup/test-cgroup-nested (deleted)
```

---

### **Luồng (Threads)**

`cgroup v2` hỗ trợ mức độ chi tiết theo luồng cho một số controller, nhằm phục vụ các tình huống cần phân phối tài nguyên theo hệ thứ bậc giữa các luồng trong một nhóm tiến trình. Theo mặc định, tất cả các luồng của một tiến trình thuộc về cùng một `cgroup`, và `cgroup` đó cũng chính là **miền tài nguyên** chứa các tài nguyên tiêu thụ không gán riêng cho tiến trình hoặc luồng cụ thể nào. **Chế độ luồng (thread mode)** cho phép các luồng được phân tán trong một cây con, nhưng vẫn chia sẻ cùng một miền tài nguyên.

Các controller hỗ trợ chế độ luồng được gọi là **threaded controllers**. Ngược lại, các controller không hỗ trợ chế độ này được gọi là **domain controllers**.

Việc đánh dấu một `cgroup` là **threaded** sẽ khiến nó gia nhập **miền tài nguyên** của `cgroup` cha như một `cgroup` dạng threaded. `Cgroup` cha đó có thể là một `cgroup` dạng threaded khác, với miền tài nguyên nằm xa hơn trong hệ phân cấp. Gốc của cây con threaded – tức là tổ tiên gần nhất không phải dạng threaded – được gọi là **threaded domain** hoặc **thread root**. Nó đóng vai trò là **miền tài nguyên chung** cho toàn bộ cây con threaded.

---

Trong một cây con dạng threaded, **các luồng của một tiến trình có thể được đặt vào các `cgroup` khác nhau** và không bị ràng buộc bởi ràng buộc nội bộ theo tiến trình. Các `threaded controller` có thể được bật trên bất kỳ `cgroup` con (non-leaf cgroups) nào, dù có chứa luồng hay không.

Do `cgroup` đóng vai trò **threaded domain** lưu giữ tất cả hoạt động tiêu thụ tài nguyên trong cây con của nó, nó được coi là có **ràng buộc nội bộ**, tức là chịu trách nhiệm tài nguyên ngay cả khi không có tiến trình nào hoạt động bên trong. Đồng thời, nó không thể có các `cgroup` con mà **không ở chế độ threaded**.

Do `cgroup` gốc không bị ràng buộc bởi hạn chế nội bộ này, nó có thể vừa làm `threaded domain`, vừa làm cha của các `domain cgroups`.

---

Chế độ hoạt động hiện tại (loại) của một `cgroup` được hiển thị trong file `cgroup.type`. File này cho biết `cgroup` đó là:

* một domain bình thường,
* một domain đang đóng vai trò **miền tài nguyên** cho cây con dạng threaded,
* hoặc một `cgroup` dạng threaded.

Khi được tạo, một `cgroup` luôn là **domain group** mặc định, và có thể được chuyển sang dạng `threaded` bằng cách ghi `"threaded"` vào file `cgroup.type`.

Thao tác này chỉ có một chiều:

```
# echo threaded > cgroup.type
```

Khi một `cgroup` đã chuyển sang chế độ **threaded**, nó **không thể trở lại làm domain** được nữa. Để chuyển sang chế độ threaded, các điều kiện sau **phải được thỏa mãn**:

* Vì `cgroup` sẽ gia nhập **miền tài nguyên của cha nó**, nên cha của nó phải là một `cgroup` dạng **domain hợp lệ (threaded hoặc domain)**.
* Nếu cha là một **domain không phải threaded**, thì **không được có bất kỳ controller dạng domain nào đang bật**, hoặc các `cgroup` con nào đang ở chế độ domain. Gốc (`root`) không được miễn trừ khỏi điều kiện này.

---

**Về mặt cấu trúc (topology)**, một `cgroup` có thể rơi vào **trạng thái không hợp lệ**. Xét ví dụ:

```
A (threaded domain) - B (threaded) - C (domain, vừa được tạo)
```

Trong đó:

* `C` được tạo ra là một domain nhưng **chưa được kết nối** tới một `cgroup` cha có thể chứa các domain con.
* Do đó, `C` **không thể sử dụng được** cho đến khi nó được chuyển thành `cgroup` dạng **threaded**.
* File `cgroup.type` sẽ báo `domain (invalid)` trong trường hợp này.
* Các thao tác thất bại do cấu trúc không hợp lệ sẽ trả về lỗi `EOPNOTSUPP`.

---

Một `domain cgroup` sẽ được chuyển thành **threaded domain** khi một trong các `cgroup` con của nó chuyển thành threaded **hoặc** khi **các controller dạng threaded được bật** trong file `cgroup.subtree_control` **và có tiến trình** đang tồn tại trong `cgroup` đó. `Threaded domain` sẽ trở lại thành `domain thông thường` khi các điều kiện trên không còn đúng.

---

Khi đọc file `cgroup.threads`, ta nhận được danh sách các **thread ID (TID)** của toàn bộ luồng trong `cgroup`. Khác biệt so với `cgroup.procs` là:

* Các thao tác ở đây được thực hiện theo **luồng (thread)** thay vì theo **tiến trình (process)**.
* Về hình thức, `cgroup.threads` có cấu trúc và cách hoạt động tương tự như `cgroup.procs`.

Tuy nhiên:

* File `cgroup.threads` **chỉ có thể ghi vào từ bên trong cùng một `threaded domain`**, nghĩa là **luồng chỉ có thể di chuyển trong cùng một miền threaded**.

---

`Threaded domain cgroup` đóng vai trò làm **miền tài nguyên** cho toàn bộ cây con:

* Dù các luồng có thể bị phân tán khắp nơi trong cây con, nhưng **mọi hoạt động tiêu thụ tài nguyên** đều được quy về `threaded domain` này.
* Trong `cgroup.procs` của `threaded domain`, có thể thấy danh sách các **PID của toàn bộ tiến trình trong cây con**.
* Tuy nhiên, `cgroup.procs` **không thể đọc được từ các nhánh con**, nhưng **có thể ghi từ bất kỳ đâu trong cây con** để di chuyển toàn bộ luồng của tiến trình tương ứng vào `cgroup` đó.

---

Chỉ các **threaded controller** mới được bật trong `threaded cgroup`. Khi một controller dạng threaded được bật trong cây con dạng threaded:

* Nó **chỉ ghi nhận và điều khiển tài nguyên gắn liền với các luồng trong `cgroup` và cây con của nó**.
* Các tiêu thụ tài nguyên không thuộc về tiến trình cụ thể nào sẽ được quy về `threaded domain`.

---

Do cây con dạng threaded không bị ràng buộc bởi các hạn chế nội bộ theo tiến trình, nên **mỗi `threaded controller` phải tự xử lý sự cạnh tranh tài nguyên giữa các luồng** nằm trong `cgroup` mẹ và `cgroup` con. Mỗi controller sẽ định nghĩa cách riêng để xử lý cạnh tranh này.

---

Hiện tại, các controller sau đây **hỗ trợ chế độ threaded** và **có thể được bật trong một `cgroup` dạng threaded**:

```
- cpu
- cpuset
- perf_event
- pids
```

---

## 4.  Thông báo \[Không]/Đã có tiến trình (`[Un]populated Notification`)

Mỗi `cgroup` không phải là gốc đều có một tệp `cgroup.events`, trong đó chứa trường **`populated`** cho biết liệu cây con (sub-hierarchy) của `cgroup` đó có chứa tiến trình đang chạy hay không. Giá trị của trường này là:

* `0` nếu không có tiến trình nào đang hoạt động trong `cgroup` và các nhóm con của nó,
* `1` nếu có ít nhất một tiến trình đang hoạt động.

Các sự kiện `poll` và `id`/`notify` sẽ được kích hoạt khi giá trị này thay đổi. Điều này có thể được sử dụng để khởi động một thao tác dọn dẹp (clean-up) sau khi **tất cả các tiến trình trong một cây con nhất định đã thoát**.

Trạng thái `populated` và các thông báo liên quan được cập nhật **đệ quy**. Xét ví dụ sau, trong đó các số trong ngoặc biểu thị số lượng tiến trình trong mỗi `cgroup`:

```
A(4) - B(0) - C(1)
      \
       D(0)
```

Trong tình huống này:

* Trường `populated` của A, B và C có giá trị là `1`,
* Trường `populated` của D là `0`.

Khi tiến trình duy nhất trong `C` thoát ra:

* Trường `populated` của B và C sẽ chuyển thành `0`,
* Sự kiện "file modified" sẽ được kích hoạt trên tệp `cgroup.events` của cả hai `cgroup` B và C.

---

## 5. Kiểm soát các bộ điều khiển (Controlling Controllers)

### Bật và Tắt (Enabling and Disabling)

Mỗi `cgroup` có một tệp **`cgroup.controllers`**, liệt kê tất cả các **bộ điều khiển (controller)** có sẵn để có thể kích hoạt cho `cgroup` đó:

```bash
# cat cgroup.controllers
cpu io memory
```

Không có bộ điều khiển nào được kích hoạt theo mặc định. Việc **bật hoặc tắt** các controller được thực hiện bằng cách ghi vào tệp **`cgroup.subtree_control`**, ví dụ:

```bash
# echo "+cpu +memory -io" > cgroup.subtree_control
```

Chỉ những controller có trong `cgroup.controllers` mới có thể được bật. Nếu có nhiều thao tác cùng lúc như ví dụ trên, tất cả các thao tác phải thành công, nếu không sẽ bị hủy toàn bộ. Nếu có nhiều thao tác liên quan đến cùng một controller, thao tác cuối cùng sẽ có hiệu lực.

Việc bật controller trong một `cgroup` có nghĩa là **việc phân phối tài nguyên mục tiêu đến các nhóm con trực tiếp của nó sẽ được kiểm soát**. Hãy xem cây phân cấp sau, trong đó các controller đã bật được ghi trong ngoặc:

```
A(cpu,memory) - B(memory) - C()
                 \
                  D()
```

Trong ví dụ trên:

* A bật `cpu` và `memory`, do đó **A kiểm soát phân phối tài nguyên CPU và bộ nhớ cho các nhóm con trực tiếp**, cụ thể là B.
* B chỉ bật `memory`, **không bật `cpu`**, nên C và D **cạnh tranh CPU một cách tự do**, nhưng **bộ nhớ mà B được cấp phát sẽ được chia cho C và D theo `memory` controller**.

---

Khi một controller được bật để phân phối tài nguyên cho các nhóm con, nó sẽ tạo ra các **tệp giao diện controller** trong các nhóm con. Ví dụ:

* Bật `cpu` ở B sẽ tạo ra các tệp giao diện bắt đầu bằng `cpu.` trong C và D.
* Nếu tắt `memory` từ B, các tệp giao diện bắt đầu bằng `memory.` trong C và D sẽ bị xóa.

Nói cách khác: **Các tệp giao diện controller (không bắt đầu bằng `cgroup.`) thuộc về `parent` đã bật controller, không phải nhóm con.**

---

### **Ràng buộc từ trên xuống (Top-down Constraint)**

Tài nguyên được phân phối theo hướng từ trên xuống, và một `cgroup` chỉ có thể tiếp tục phân phối lại tài nguyên nếu nó đã được phân phối từ `parent` của nó.

Điều này có nghĩa là tất cả các tệp **`cgroup.subtree_control`** (ngoại trừ ở `root`) chỉ được phép chứa các bộ điều khiển (**controllers**) đã được bật trong tệp **`cgroup.subtree_control`** của `parent`.

* Một controller chỉ có thể được bật nếu **controller đó đã được bật ở cấp cha (parent)**.
* Ngược lại, một controller **không thể bị tắt nếu bất kỳ nhóm con nào còn đang bật nó**.

---

Hiểu đơn giản: quyền kiểm soát tài nguyên phải được cấp phép từ trên xuống dưới. Nếu cha không cho phép, con cũng không được dùng. Và nếu con đang dùng, cha chưa thể rút quyền đó lại.

### **Ràng buộc Không Có Tiến Trình Nội Bộ (No Internal Process Constraint)**

Các `cgroup` không phải gốc (non-root cgroups) chỉ có thể phân phối tài nguyên miền (domain resources) cho các nhóm con **khi chúng không có bất kỳ tiến trình (process) nào của riêng mình**.
Nói cách khác, **chỉ những domain group không chứa tiến trình** mới được phép bật các **bộ điều khiển miền (domain controllers)** trong tệp `cgroup.subtree_control`.

---

**Điều này đảm bảo rằng**: khi một bộ điều khiển miền hoạt động trên một phần của cây phân cấp, thì các tiến trình chỉ được phép tồn tại ở **các lá (leaf nodes)**, **không phải ở giữa cây**. Nhờ đó, tránh tình trạng các `child cgroup` cạnh tranh tài nguyên với các tiến trình nội bộ của `parent`.

---

**Tuy nhiên, nhóm gốc (root cgroup) không bị ràng buộc bởi điều này**:

* Nhóm gốc có thể chứa các tiến trình và tiêu tốn tài nguyên mà không thể gán cho `cgroup` nào khác.
* Do đó, mỗi bộ điều khiển phải xử lý nhóm gốc theo cách riêng.

---

**Lưu ý thêm**:
Ràng buộc này **chỉ áp dụng khi có ít nhất một controller đã được bật** trong `cgroup.subtree_control`.

* Nếu không có controller nào được bật, thì `cgroup` vẫn có thể chứa tiến trình và tạo nhóm con bình thường.
* Tuy nhiên, **để bật controller**, `cgroup` đó **phải chuyển hết tiến trình của mình sang các nhóm con**, rồi mới được phép bật controller trong `cgroup.subtree_control`.

---

## 6. **Ủy quyền (Delegation)**

### **Mô hình Ủy quyền (Model of Delegation)**

Một `cgroup` có thể được ủy quyền theo hai cách:

1. **Cách thứ nhất**: cấp quyền ghi thư mục và các tệp như `cgroup.procs`, `cgroup.threads` và `cgroup.subtree_control` cho một người dùng có quyền thấp hơn.
2. **Cách thứ hai**: nếu tùy chọn mount `nsdelegate` được bật, hệ thống sẽ tự động tạo một **không gian tên cgroup (cgroup namespace)** khi tạo namespace.

---

Vì các tệp điều khiển tài nguyên trong thư mục cgroup kiểm soát việc phân phối tài nguyên của cha, **người được ủy quyền (delegatee)** không nên được phép ghi vào chúng.

* Với cách **thứ nhất**, điều này được đảm bảo bằng cách **không cấp quyền truy cập ghi** vào các tệp này.
* Với cách **thứ hai**, các tệp nằm ngoài namespace sẽ bị ẩn khỏi người được ủy quyền **nhờ việc tách không gian tên** (ít nhất là namespace cho mount), và kernel sẽ từ chối các lệnh ghi đến các tệp tại gốc của namespace từ bên trong namespace, **trừ các tệp trong danh sách trắng** tại `/sys/kernel/cgroup/delegate/` (như `cgroup.procs`, `cgroup.threads`, `cgroup.subtree_control`,...).

---

**Kết quả sau khi ủy quyền**

Dù theo cách nào, kết quả đều giống nhau:
Người được ủy quyền có thể:

* **Tạo cây phân cấp con (sub-hierarchy)** bên dưới thư mục được cấp;
* Tổ chức các tiến trình trong đó tùy ý;
* Và **phân phối lại tài nguyên đã được nhận từ nhóm cha**.

Các giới hạn và thiết lập khác từ các controller **vẫn có hiệu lực theo phân cấp (hierarchical)**. Do đó, **không có gì trong nhóm được ủy quyền có thể vượt qua giới hạn tài nguyên của cha**.

---

Hiện tại, `cgroup` **không giới hạn số lượng nhóm con hoặc độ sâu lồng nhau** trong hệ phân cấp được ủy quyền. Tuy nhiên, điều này **có thể bị giới hạn rõ ràng trong tương lai**.

### **Giới hạn Ủy quyền (Delegation Containment)**

Một hệ phân cấp con được ủy quyền (delegated sub-hierarchy) **bị ràng buộc** ở chỗ:
**các tiến trình không thể được chuyển vào hoặc ra khỏi hệ phân cấp con này bởi người được ủy quyền (delegatee)**.

---

**Đối với ủy quyền cho người dùng có quyền thấp hơn:**

Việc này được đảm bảo bằng cách yêu cầu **hai điều kiện sau** để một tiến trình (PID) không phải root có thể được di chuyển vào `cgroup` bằng cách ghi vào tệp `cgroup.procs`:

* Người ghi **phải có quyền ghi vào tệp `cgroup.procs` của cgroup đích**.
* Người ghi **phải có quyền ghi vào tệp `cgroup.procs` của tổ tiên chung** giữa cgroup nguồn và cgroup đích.

⟶ Hai điều kiện trên đảm bảo rằng **người được ủy quyền chỉ có thể di chuyển tiến trình trong phạm vi hệ phân cấp được ủy quyền**, **không thể kéo tiến trình từ ngoài vào hoặc đẩy ra ngoài** hệ phân cấp đó.

---

**Ví dụ minh họa:**

Giả sử:

* Các `cgroup` **C0** và **C1** được ủy quyền cho người dùng **U0**.
* U0 tạo thêm `C00`, `C01` bên dưới C0, và `C10` bên dưới C1 như sau:

```
~~~~~~~~~~~~~ - C0 - C00
~  cgroup   ~      \ C01
~ hierarchy ~
~~~~~~~~~~~~~ - C1 - C10
```

* Tất cả các tiến trình trong các `cgroup` trên đều thuộc về người dùng U0.

---

**Trường hợp vi phạm:**

Giả sử U0 muốn ghi PID của một tiến trình hiện đang nằm trong **C10** vào `C00/cgroup.procs`.

* U0 **có quyền ghi** vào `C00/cgroup.procs`, **nhưng**:
* **Tổ tiên chung** của `C10` (nguồn) và `C00` (đích) là `C0`, nằm **trên phạm vi được ủy quyền**.
* U0 **không có quyền ghi vào `C0/cgroup.procs`**, nên thao tác ghi **sẽ bị từ chối** với lỗi `-EACCES`.

---

**Đối với ủy quyền dựa trên namespace:**

Giới hạn cũng được đảm bảo bằng cách yêu cầu rằng **cả `cgroup` nguồn và đích đều phải được truy cập được từ cùng một namespace** với tiến trình đang cố gắng di chuyển.

⟶ Nếu **một trong hai không thể truy cập**, việc di chuyển **sẽ bị từ chối với lỗi `-ENOENT`**.

---

## 7. **Guidelines - Hướng dẫn**


### **Tổ chức một lần và kiểm soát**

Việc di chuyển một tiến trình giữa các `cgroup` là một thao tác tốn kém và các tài nguyên có trạng thái như bộ nhớ **sẽ không được di chuyển theo tiến trình**. Đây là một quyết định thiết kế có chủ đích, vì việc di chuyển thường kèm theo đánh đổi với chi phí đồng bộ và các luồng xử lý nóng.

Do đó, **việc thường xuyên di chuyển tiến trình giữa các `cgroup` để áp dụng các giới hạn tài nguyên khác nhau là không được khuyến khích**. Thay vào đó, **tải công việc nên được gán cho một `cgroup` phù hợp ngay từ đầu theo cấu trúc hợp lý và cấu hình tài nguyên của hệ thống**. Những điều chỉnh động về phân bổ tài nguyên có thể được thực hiện bằng cách thay đổi cấu hình bộ điều khiển thông qua các file giao diện.

---

### **Tránh trùng tên**

Các tệp giao diện (`interface files`) của một `cgroup` và các `cgroup` con nằm cùng trong một thư mục. Do đó **có thể vô tình tạo `cgroup` con trùng tên với tệp giao diện**, gây xung đột.

* **Tất cả các file giao diện lõi (`core interface files`) của `cgroup` được đặt tên bắt đầu bằng “`cgroup.`”**
* **File giao diện của mỗi controller thì được đặt tên bắt đầu bằng tên controller và dấu chấm, ví dụ “`cpu.stat`”**.

Tên của controller được tạo từ chữ cái thường và dấu gạch dưới (`_`) nhưng **không bao giờ bắt đầu bằng dấu gạch dưới**. Vì vậy, **có thể dùng `_` làm ký tự bắt đầu để tránh trùng tên**.

Ngoài ra:

* **Tên file giao diện sẽ không bắt đầu hay kết thúc bằng các từ như `job`, `service`, `slice`, `unit`, hoặc `workload`**, những từ thường dùng để phân loại tác vụ.

> `cgroup` **không tự động ngăn việc trùng tên**. Do đó, **người dùng phải có trách nhiệm tránh điều này**.

## 8. **Mô hình Phân phối Tài nguyên (Resource Distribution Models)**

Các bộ điều khiển `cgroup` triển khai nhiều cơ chế phân phối tài nguyên khác nhau tùy theo loại tài nguyên và trường hợp sử dụng mong đợi. Phần này mô tả các cơ chế chính đang được sử dụng cùng với hành vi dự kiến của chúng.

---

### **Trọng số (Weights)**

Tài nguyên của `cgroup` cha được phân phối bằng cách **cộng tất cả trọng số của các `cgroup` con đang hoạt động**, sau đó cấp cho mỗi `cgroup` con **một phần tương ứng với tỷ lệ trọng số của nó trên tổng**. Chỉ những `cgroup` con có thể sử dụng tài nguyên tại thời điểm phân phối mới được tính, vì vậy mô hình này đảm bảo không lãng phí. Do tính chất động, mô hình này **thường dùng cho tài nguyên không lưu trạng thái**.

* Tất cả các trọng số nằm trong khoảng **\[1, 10000]**, mặc định là **100**.
* Cho phép điều chỉnh thiên lệch đối xứng theo cả hai hướng với độ chi tiết cao mà vẫn trực quan.
* **Miễn là trọng số hợp lệ**, mọi kết hợp cấu hình đều được chấp nhận, không có lý do gì để từ chối thay đổi cấu hình hoặc di chuyển tiến trình.

Ví dụ: `cpu.weight` phân phối chu kỳ CPU theo tỷ lệ trọng số giữa các `cgroup` con đang hoạt động.

---

### **Giới hạn (Limits)**

Một `cgroup` con **chỉ có thể tiêu thụ tối đa lượng tài nguyên được cấu hình**. Các giới hạn **có thể bị quá mức (over-committed)** — nghĩa là tổng giới hạn của các `cgroup` con có thể vượt quá tổng tài nguyên của `cgroup` cha.

* Giới hạn nằm trong khoảng **\[0, max]**, mặc định là **"max"** (không giới hạn).
* **Dù bị quá mức**, mọi cấu hình đều hợp lệ, và không bị từ chối khi thay đổi cấu hình hoặc di chuyển tiến trình.

Ví dụ: `io.max` giới hạn tốc độ đọc/ghi (BPS hoặc IOPS) tối đa mà một `cgroup` có thể sử dụng trên thiết bị I/O.

---

### **Bảo vệ (Protections)**

Một `cgroup` được bảo vệ theo lượng tài nguyên đã cấu hình, **miễn là toàn bộ tổ tiên của nó** vẫn nằm trong các mức bảo vệ đã cấu hình. Bảo vệ có thể là **cam kết cứng (hard guarantees)** hoặc **giới hạn mềm với nỗ lực tối đa (best-effort soft boundaries)**. Việc bảo vệ cũng có thể bị **over-committed** — khi đó, chỉ lượng tài nguyên sẵn có ở `cgroup` cha mới được chia lại cho các `cgroup` con để bảo vệ.

* Giá trị bảo vệ nằm trong khoảng **\[0, max]**, mặc định là **0** (nghĩa là không có bảo vệ).
* Do bảo vệ có thể bị over-committed, nên **mọi cấu hình đều hợp lệ**, không có lý do để từ chối thay đổi cấu hình hoặc di chuyển tiến trình.

Ví dụ: `memory.low` là một loại bảo vệ bộ nhớ theo cơ chế best-effort.

---

### **Phân bổ (Allocations)**

Một `cgroup` được **phân bổ độc quyền** một lượng tài nguyên hữu hạn đã xác định. **Không thể over-commit** phân bổ — tổng phân bổ cho các `cgroup` con **không được vượt quá** lượng tài nguyên sẵn có của `cgroup` cha.

* Phạm vi phân bổ nằm trong khoảng **\[0, max]**, mặc định là **0** (không phân bổ tài nguyên).
* Do **không thể over-commit**, một số cấu hình sẽ **không hợp lệ và bị từ chối**.
* Nếu tài nguyên là bắt buộc để thực thi tiến trình, việc di chuyển tiến trình có thể **bị từ chối**.

Ví dụ: `cpu.rt.max` là một dạng phân bổ cứng tài nguyên thời gian thực (realtime slices).

Dưới đây là bản dịch tiếng Việt của phần "Interface Files – Format" trong ảnh:

---

## 9. **Tập tin giao diện (Interface Files)**

### **Định dạng (Format)**

Tất cả các tập tin giao diện nên sử dụng một trong các định dạng sau khi có thể:

```
Giá trị phân cách bằng dòng mới (New-line separated values)
(khi chỉ một giá trị có thể được ghi tại một thời điểm)

    VAL0\n
    VAL1\n
    ...

Giá trị phân cách bằng khoảng trắng (Space separated values)
(khi chỉ cho đọc hoặc có thể ghi nhiều giá trị cùng lúc)

    VAL0 VAL1 ...\n

Định dạng khóa phẳng (Flat keyed)

    KEY0 VAL0\n
    KEY1 VAL1\n
    ...

Định dạng khóa lồng nhau (Nested keyed)

    KEY0 SUB_KEY0=VAL00 SUB_KEY1=VAL01...
    KEY1 SUB_KEY0=VAL10 SUB_KEY1=VAL11...
    ...
```

Đối với tập tin có thể ghi, định dạng ghi **nên tương thích với định dạng đọc**; tuy nhiên, các controller có thể cho phép **bỏ qua các trường phía sau** hoặc **cho phép viết rút gọn** đối với các trường hợp sử dụng phổ biến.

Đối với các tập tin định dạng khóa phẳng hoặc khóa lồng nhau:

* **Chỉ các giá trị tương ứng với một khóa có thể được ghi cùng lúc**.
* Với định dạng khóa lồng nhau, **các cặp khóa con có thể được chỉ định theo bất kỳ thứ tự nào**, và **không bắt buộc phải chỉ định đầy đủ tất cả các cặp**.

---

### Quy ước

* Cài đặt cho một tính năng duy nhất nên được chứa trong một tập tin duy nhất.

* **Cgroup gốc** (root cgroup) nên được miễn khỏi việc kiểm soát tài nguyên và do đó **không nên có các tập tin giao diện điều khiển tài nguyên**.

* Đơn vị thời gian mặc định là **micro giây**. Nếu sử dụng đơn vị khác, **phải có hậu tố đơn vị rõ ràng** được ghi kèm.

* Các giá trị theo phần trăm nên sử dụng **số thập phân dạng phần trăm với ít nhất hai chữ số phần thập phân**, ví dụ: `13.40`.

* Nếu một controller thực hiện phân phối tài nguyên dựa trên trọng số, thì **tập tin giao diện nên được đặt tên là “weight”** và có giá trị nằm trong **khoảng \[1, 10000]**, với giá trị mặc định là **100**. Các giá trị này được chọn để cung cấp đủ độ lệch theo cả hai hướng trong khi vẫn dễ hiểu (mặc định là 100%).

* Nếu một controller thực hiện **cam kết tuyệt đối về tài nguyên hoặc giới hạn tài nguyên**, thì tập tin giao diện nên được đặt tên là **“min”** và **“max”** tương ứng.
  Nếu controller chỉ cam kết theo kiểu "nỗ lực tối đa" (best effort), thì tập tin nên được đặt tên là **“low”** và **“high”**.

  Trong bốn tập tin kiểm soát trên, **ký hiệu đặc biệt “max”** nên được sử dụng để biểu thị **vô cực tăng dần**, cho cả ghi và đọc.

* Nếu một thiết lập có giá trị mặc định cấu hình được và có các override (ghi đè) theo khóa, thì dòng mặc định phải có **khóa là “default”** và phải là mục **đầu tiên** trong tập tin.

  Giá trị mặc định có thể được cập nhật bằng cách ghi `default $VAL` hoặc `$SVAL`.

  Khi ghi đè một giá trị cụ thể, có thể dùng **“default”** để biểu thị việc **xóa bỏ ghi đè**.
  Các override ghi đè bằng giá trị “default” sẽ không xuất hiện khi đọc lại.

Dưới đây là bản dịch tiếng Việt của nội dung trong ảnh:

---

Ví dụ, một thiết lập được đánh chỉ mục (keyed) theo số hiệu thiết bị dạng **major\:minor** với giá trị kiểu số nguyên có thể trông như sau:

```
# cat cgroup-example-interface-file
default 150
8:0 300
```

**Giá trị mặc định có thể được cập nhật bằng cách:**

```
# echo 125 > cgroup-example-interface-file
```

hoặc:

```
# echo "default 125" > cgroup-example-interface-file
```

**Ghi đè (override) có thể được thiết lập bằng:**

```
# echo "8:16 170" > cgroup-example-interface-file
```

**Và được xóa bằng:**

```
# echo "8:0 default" > cgroup-example-interface-file
# cat cgroup-example-interface-file
default 125
8:16 170
```

---

* Đối với các sự kiện không có tần suất quá cao, một tập tin giao diện có tên **“events”** nên được tạo ra, trong đó liệt kê các cặp khóa-giá trị của sự kiện. Mỗi khi xảy ra một sự kiện cần được thông báo, một sự kiện sửa đổi tập tin (file modified event) nên được sinh ra trên tập tin này.

---

### **Tập tin giao diện lõi (Core Interface Files)**

Tất cả các tập tin lõi của cgroup đều được đặt tiền tố là `"cgroup."`

---

**cgroup.type**

Một tập tin có thể đọc-ghi với một giá trị duy nhất, tồn tại trên các cgroup không phải là root.

Khi đọc, nó biểu thị loại hiện tại của cgroup, có thể là một trong các giá trị sau:

* `"domain"`: Một cgroup domain hợp lệ thông thường.
* `"domain threaded"`: Một cgroup domain dạng threaded đang làm gốc cho một cây con threaded.
* `"domain invalid"`: Một nhóm ở trạng thái không hợp lệ. Không thể chứa tiến trình hay bật các bộ điều khiển. Có thể được phép chuyển sang dạng `threaded`.
* `"threaded"`: Một cgroup dạng threaded là thành viên của một cây con threaded.

Một cgroup có thể được chuyển sang dạng threaded bằng cách ghi `"threaded"` vào tập tin này.

---

**cgroup.procs**

Một tập tin có thể đọc-ghi, chứa các giá trị được phân tách theo dòng mới, tồn tại trên tất cả các cgroup.

Khi đọc, nó liệt kê các PID của tất cả các tiến trình thuộc về cgroup, mỗi PID trên một dòng. Các PID không được sắp xếp và cùng một PID có thể xuất hiện nhiều lần nếu tiến trình được chuyển sang một cgroup khác rồi quay lại hoặc PID đó bị tái sử dụng trong lúc đọc.

Một PID có thể được ghi vào tập tin này để di chuyển tiến trình tương ứng sang cgroup. Người ghi phải thỏa mãn tất cả các điều kiện sau:

* Phải có quyền ghi vào tập tin `"cgroup.procs"`.
* Phải có quyền ghi vào `"cgroup.procs"` của tổ tiên chung giữa cgroup nguồn và cgroup đích.

Khi ủy quyền một cây con (sub-hierarchy), quyền ghi vào tập tin này cũng phải được cấp cùng với thư mục chứa nó.

Trong một cgroup dạng threaded, khi đọc tập tin này sẽ trả về lỗi **EOPNOTSUPP** vì tất cả các tiến trình đều thuộc về gốc của thread. Tuy nhiên, việc ghi là được hỗ trợ và sẽ di chuyển toàn bộ thread của tiến trình sang cgroup.

---

**cgroup.threads**

Một tập tin đọc-ghi chứa các giá trị phân tách theo dòng mới, tồn tại trên tất cả các cgroup.

Khi đọc, nó liệt kê các TID của tất cả các luồng thuộc về cgroup, mỗi TID nằm trên một dòng. Các TID không được sắp xếp theo thứ tự và cùng một TID có thể xuất hiện nhiều lần nếu luồng được di chuyển sang một cgroup khác rồi quay lại, hoặc TID bị tái sử dụng trong lúc đọc.

Một TID có thể được ghi vào để di chuyển luồng liên quan sang cgroup. Người ghi phải đáp ứng tất cả các điều kiện sau:

* Phải có quyền ghi vào tập tin `"cgroup.threads"`.
* Cgroup hiện tại của luồng phải nằm trong cùng một miền tài nguyên với cgroup đích.
* Phải có quyền ghi vào tập tin `"cgroup.procs"` của tổ tiên chung giữa cgroup nguồn và cgroup đích.

Khi ủy quyền một cây con (sub-hierarchy), quyền ghi vào tập tin này cũng phải được cấp cùng với thư mục chứa nó.

---

**cgroup.controllers**

Một tập tin chỉ-đọc chứa các giá trị phân tách bằng khoảng trắng, tồn tại trên tất cả các cgroup.

Nó hiển thị danh sách các bộ điều khiển (controller) có sẵn cho cgroup. Danh sách này không được sắp xếp.

---

**cgroup.subtree\_control**

Một tập tin đọc-ghi chứa các giá trị phân tách bằng khoảng trắng, tồn tại trên tất cả các cgroup. Ban đầu tập tin này rỗng.

Khi đọc, nó hiển thị danh sách các bộ điều khiển được bật để phân phối tài nguyên từ cgroup cha cho các con của nó.

Danh sách bộ điều khiển có thể được ghi với tiền tố `'+'` hoặc `'-'` để bật hoặc tắt controller tương ứng. Một bộ điều khiển với tiền tố `'+'` sẽ được bật, và với `'-'` sẽ bị tắt. Nếu một controller xuất hiện nhiều hơn một lần trong danh sách, chỉ mục cuối cùng sẽ có hiệu lực. Nếu nhiều thao tác bật/tắt được ghi cùng lúc, thì tất cả phải thành công hoặc tất cả sẽ thất bại.

---

**cgroup.events**

Một tập tin chỉ đọc có định dạng khóa-phẳng (flat-keyed) tồn tại trên các cgroup không phải gốc. Các mục sau được định nghĩa. Trừ khi có chỉ định khác, việc thay đổi giá trị trong tập tin này sẽ sinh ra sự kiện "file modified".

* **populated**
  Giá trị là `1` nếu cgroup hoặc bất kỳ con nào của nó chứa tiến trình đang hoạt động; ngược lại là `0`.

* **frozen**
  Giá trị là `1` nếu cgroup đang bị đóng băng; ngược lại là `0`.

---

**cgroup.max.descendants**

Một tập tin đơn giá trị đọc-ghi. Mặc định là `"max"`.

Chỉ định số lượng tối đa các cgroup con được phép. Nếu số lượng cgroup con hiện tại bằng hoặc vượt quá giới hạn này, thì mọi cố gắng tạo cgroup mới trong hệ phân cấp sẽ thất bại.

---

**cgroup.max.depth**

Một tập tin đơn giá trị đọc-ghi. Mặc định là `"max"`.

Chỉ định độ sâu tối đa được phép của cây cgroup bên dưới cgroup hiện tại. Nếu độ sâu hiện tại bằng hoặc lớn hơn giới hạn này, mọi cố gắng tạo cgroup con mới sẽ thất bại.

---

**cgroup.stat**

Một tập tin chỉ đọc định dạng khóa-phẳng với các mục sau:

* **nr\_descendants**
  Tổng số lượng cgroup con có thể thấy được.

* **nr\_dying\_descendants**
  Tổng số lượng cgroup con đang ở trạng thái "dying" (chết dần). Một cgroup rơi vào trạng thái này sau khi bị xóa bởi người dùng, và sẽ duy trì trạng thái này một thời gian không xác định (phụ thuộc vào tải hệ thống) trước khi bị tiêu hủy hoàn toàn.

  * Một tiến trình không thể vào cgroup đang chết trong mọi trường hợp.
  * Cgroup đang chết không thể hồi sinh.
  * Một cgroup đang chết vẫn có thể tiêu tốn tài nguyên hệ thống không vượt quá giới hạn đã tồn tại tại thời điểm nó bị xóa.

* **nr\_subsys\_\<cgroup\_subsys>**
  Tổng số lượng cgroup con đang hoạt động của một subsystem cụ thể (ví dụ memory cgroup), tại hoặc bên dưới cgroup hiện tại.

* **nr\_dying\_subsys\_\<cgroup\_subsys>**
  Tổng số lượng cgroup con đang chết của một subsystem cụ thể (ví dụ memory cgroup), tại hoặc bên dưới cgroup hiện tại.

---

**cgroup.freeze**

Một tập tin đơn giá trị có thể đọc-ghi tồn tại trên các cgroup không phải gốc. Giá trị cho phép là “0” và “1”. Mặc định là “0”.

* Ghi “1” vào tập tin này sẽ đóng băng cgroup và tất cả các cgroup con. Điều này có nghĩa là tất cả các tiến trình thuộc về các cgroup đó sẽ bị dừng và không được chạy lại cho đến khi cgroup được mở đóng băng một cách rõ ràng. Việc đóng băng có thể mất thời gian. Khi hoàn tất, giá trị `"frozen"` trong tập tin điều khiển `cgroup.events` sẽ được cập nhật thành “1” và một thông báo tương ứng sẽ được phát ra.

* Một cgroup có thể bị đóng băng bởi cài đặt của chính nó hoặc của bất kỳ cgroup tổ tiên nào. Nếu một cgroup tổ tiên bị đóng băng, cgroup con cũng sẽ vẫn bị đóng băng.

* Các tiến trình trong cgroup bị đóng băng vẫn có thể bị giết bởi tín hiệu gây chết. Chúng cũng có thể ra/vào cgroup bị đóng băng: hoặc do người dùng di chuyển rõ ràng, hoặc nếu fork() xảy ra trong lúc đang đóng băng. Nếu một tiến trình bị di chuyển vào cgroup đã đóng băng, nó sẽ dừng lại. Nếu bị di chuyển ra ngoài, nó sẽ trở lại trạng thái đang chạy.

* Trạng thái đóng băng không ảnh hưởng đến các thao tác cây cgroup: vẫn có thể xóa cgroup bị đóng băng (nếu rỗng) và tạo mới các cgroup con.

---

**cgroup.kill**

Một tập tin chỉ ghi, đơn giá trị, tồn tại trên các cgroup không phải gốc. Giá trị duy nhất được cho phép là “1”.

* Ghi “1” vào tập tin này sẽ khiến cgroup và tất cả cgroup con bị tiêu diệt. Tất cả tiến trình trong cây cgroup đó sẽ bị giết bằng tín hiệu SIGKILL.

* Việc giết cây cgroup sẽ xử lý đúng các tình huống fork đồng thời và được bảo vệ khỏi việc di chuyển tiến trình.

* Trong cgroup dạng “threaded”, ghi vào tập tin này sẽ thất bại với lỗi EOPNOTSUPP vì thao tác này là theo hướng tiến trình (process-directed), ảnh hưởng đến toàn bộ nhóm luồng.

---

**cgroup.pressure**

Một tập tin đơn giá trị đọc-ghi cho phép giá trị “0” và “1”. Mặc định là “1”.

* Ghi “0” sẽ tắt tính năng tính toán PSI của cgroup. Ghi “1” sẽ bật lại tính năng này.

* Thuộc tính điều khiển này không mang tính phân cấp, tức là bật/tắt PSI trong một cgroup sẽ không ảnh hưởng đến việc tính PSI của các cgroup con, và không cần truyền trạng thái từ gốc.

* Lý do tồn tại thuộc tính này là vì PSI tính toán độ trễ (stall) riêng biệt cho từng cgroup và tổng hợp lại ở mỗi mức trong cây phân cấp. Việc này có thể gây quá tải đáng kể cho một số loại tải khi ở sâu trong cây cgroup, vì thế ta có thể dùng thuộc tính này để tắt PSI ở những cgroup không phải lá.

---

**irq.pressure**

Một tập tin dạng lồng (nested-keyed) có thể đọc-ghi.

Hiển thị thông tin về tình trạng nghẽn (pressure stall) của IRQ/SOFTIRQ. Xem [Documentation/accounting/psi.rst](https://www.kernel.org/doc/html/latest/accounting/psi.html#psi) để biết chi tiết.

---

## 10. **Controllers**

### CPU

Bộ điều khiển “cpu” điều chỉnh việc phân phối chu kỳ CPU. Bộ điều khiển này triển khai các mô hình giới hạn băng thông tuyệt đối và phân phối theo trọng số cho chính sách lập lịch thông thường, cũng như mô hình phân bổ băng thông tuyệt đối cho chính sách lập lịch thời gian thực (realtime).

Trong tất cả các mô hình trên, việc phân phối chu kỳ chỉ được xác định dựa trên thời gian (temporal base), và không tính đến tần số mà tại đó các tác vụ được thực thi. Hỗ trợ hạn chế mức sử dụng (utilization clamping) cho phép gợi ý cho governor `schedutil cpufreq` về tần số tối thiểu nên được cung cấp bởi CPU, cũng như tần số tối đa mà CPU không nên vượt quá.

**CẢNH BÁO**: Bộ điều khiển CPU của cgroup2 hiện **chưa hỗ trợ kiểm soát (băng thông) các tiến trình realtime**. Đối với hạt nhân được biên dịch với tùy chọn `CONFIG_RT_GROUP_SCHED` cho phép lập lịch nhóm các tiến trình realtime, bộ điều khiển CPU chỉ có thể được kích hoạt khi tất cả các tiến trình realtime nằm trong nhóm gốc (root cgroup). Hãy lưu ý rằng phần mềm quản lý hệ thống có thể đã di chuyển các tiến trình realtime ra khỏi nhóm gốc trong quá trình khởi động hệ thống, và những tiến trình này có thể cần được chuyển trở lại nhóm gốc trước khi bộ điều khiển CPU có thể được kích hoạt với hạt nhân có bật `CONFIG_RT_GROUP_SCHED`.

Khi `CONFIG_RT_GROUP_SCHED` bị vô hiệu hóa, giới hạn này không áp dụng và một số tệp giao diện sẽ không ảnh hưởng hoặc không tính đến các tiến trình realtime. Chỉ bộ điều khiển CPU bị ảnh hưởng bởi `CONFIG_RT_GROUP_SCHED`. Các bộ điều khiển khác có thể được sử dụng để kiểm soát tài nguyên của các tiến trình realtime bất kể `CONFIG_RT_GROUP_SCHED`.

---

### **Tệp giao diện CPU (CPU Interface Files)**

Sự tương tác của một tiến trình với bộ điều khiển CPU phụ thuộc vào chính sách lập lịch và trình lập lịch (scheduler) cơ bản. Từ góc độ của bộ điều khiển CPU, các tiến trình có thể được phân loại như sau:

* Tiến trình sử dụng trình lập lịch loại fair-class.
* Tiến trình sử dụng trình lập lịch BPF có callback `cgroup_set_weight`.
* Tất cả các trường hợp còn lại: `SCHED_{FIFO, RR, DEADLINE}` và các tiến trình dùng trình lập lịch BPF mà **không** có callback `cgroup_set_weight`.

---

Để biết chi tiết về thời điểm một tiến trình nằm trong trình lập lịch loại fair-class hoặc BPF scheduler, hãy xem tại:
[**Documentation/scheduler/sched-ext.rst**](https://www.kernel.org/doc/html/latest/scheduler/sched-ext.html#sched-ext)

Đối với từng tệp giao diện dưới đây, các phân loại đã nêu sẽ được áp dụng. **Tất cả thời lượng thời gian được tính bằng micro giây (microseconds).**

---

**`cpu.stat`**

Một tệp chỉ đọc, có định dạng khóa phẳng (flat-keyed). Tệp này tồn tại bất kể bộ điều khiển có được kích hoạt hay không.
Nó luôn báo cáo ba thống kê sau, áp dụng cho tất cả tiến trình trong cgroup:

* `usage_usec`
* `user_usec`
* `system_usec`

Và năm thống kê sau **chỉ khi bộ điều khiển được bật**, áp dụng **chỉ cho các tiến trình sử dụng fair-class scheduler**:

* `nr_periods`
* `nr_throttled`
* `throttled_usec`
* `nr_bursts`
* `burst_usec`

---

**`cpu.weight`**

Một tệp giá trị đơn có thể đọc-ghi, tồn tại trên các cgroup không phải root. Giá trị mặc định là **"100"**.

Đối với các nhóm không ở trạng thái nhàn rỗi (`cpu.idle = 0`), giá trị `weight` nằm trong phạm vi **\[1, 10000]**.

Nếu cgroup được cấu hình là **`SCHED_IDLE`** (`cpu.idle = 1`), thì trọng số (`weight`) sẽ hiển thị là **0**.

Tệp này **chỉ ảnh hưởng tới các tiến trình sử dụng fair-class scheduler và BPF scheduler** có callback **`cgroup_set_weight`**, tùy thuộc vào việc callback thực hiện điều gì.

---

**`cpu.weight.nice`**

Một tệp có thể đọc-ghi, chứa giá trị đơn, tồn tại trên các cgroup không phải root. Giá trị mặc định là **"0"**.

Giá trị nice nằm trong phạm vi **\[-20, 19]**.

Tệp giao diện này là một giao diện thay thế cho `cpu.weight`, cho phép đọc và thiết lập trọng số bằng các giá trị giống như được dùng trong hàm `nice(2)`. Vì phạm vi nhỏ hơn và độ phân giải thô hơn so với `cpu.weight`, nên giá trị đọc được sẽ gần đúng nhất với trọng số hiện tại.

Tệp này **chỉ ảnh hưởng tới các tiến trình sử dụng trình lập lịch fair-class và BPF** có sử dụng callback `cgroup_set_weight`, tùy thuộc vào chức năng cụ thể của callback.

---

**`cpu.max`**

Một tệp có thể đọc-ghi gồm **hai giá trị**, tồn tại trên các cgroup không phải root. Mặc định là **"max 100000"**.

Giới hạn băng thông tối đa. Có định dạng:

```
$MAX $PERIOD
```

Ý nghĩa là nhóm cgroup có thể sử dụng tối đa `$MAX` đơn vị trong mỗi khoảng thời gian `$PERIOD`. Nếu `$MAX` là `"max"` thì nghĩa là **không giới hạn**. Nếu chỉ ghi một giá trị, `$MAX` sẽ được cập nhật.

Tệp này **chỉ ảnh hưởng tới các tiến trình sử dụng fair-class scheduler**.

---

**`cpu.max.burst`**

Một tệp đọc-ghi giá trị đơn, tồn tại trên các cgroup không phải root. Mặc định là **"0"**.

Giá trị burst (bùng nổ) nằm trong phạm vi **\[0, \$MAX]**.

Tệp này **chỉ ảnh hưởng tới các tiến trình sử dụng fair-class scheduler**.

---

**`cpu.pressure`**

Một tệp đọc-ghi có định dạng khóa lồng nhau (nested-keyed file).

Hiển thị thông tin tắc nghẽn (stall) của CPU. Xem chi tiết tại: [**Documentation/accounting/psi.rst**](https://www.kernel.org/doc/html/latest/accounting/psi.html#psi).

Tệp này **áp dụng cho tất cả các tiến trình trong cgroup**.


**`cpu.uclamp.min`**

Một tệp có thể đọc-ghi, chứa giá trị đơn, tồn tại trên các cgroup không phải root. Mặc định là **"0"**, tức là không tăng cường mức sử dụng (utilization boosting).

Giá trị yêu cầu sử dụng tối thiểu (bảo vệ) được tính theo phần trăm dưới dạng số thập phân hợp lý, ví dụ: `12.34` tương đương với **12.34%**.

Giao diện này cho phép đọc và thiết lập giới hạn mức sử dụng tối thiểu tương tự như hàm `sched_setattr(2)`. Giá trị này được dùng để áp đặt giới hạn sử dụng tối thiểu cho các tiến trình, kể cả tiến trình real-time.

Giá trị yêu cầu tối thiểu **luôn bị giới hạn bởi giá trị tối đa hiện tại**, tức là bị chặn bởi `cpu.uclamp.max`.

Tệp này ảnh hưởng tới **tất cả các tiến trình trong cgroup**.

---

**`cpu.uclamp.max`**

Một tệp có thể đọc-ghi, chứa giá trị đơn, tồn tại trên các cgroup không phải root. Mặc định là **"max"**, tức là không giới hạn mức sử dụng tối đa (no capping).

Giá trị yêu cầu mức sử dụng tối đa được tính theo phần trăm, ví dụ: `98.76` tương đương **98.76%**.

Giao diện này cho phép đọc và thiết lập giới hạn mức sử dụng tối đa tương tự như `sched_setattr(2)`. Giá trị này dùng để giới hạn mức sử dụng tối đa của các tiến trình, kể cả tiến trình real-time.

Tệp này ảnh hưởng tới **tất cả các tiến trình trong cgroup**.

---

**`cpu.idle`**

Một tệp có thể đọc-ghi, chứa giá trị đơn, tồn tại trên các cgroup không phải root. Mặc định là **0**.

Đây là tương đương với chính sách lập lịch `SCHED_IDLE` cho từng tiến trình. Thiết lập giá trị này thành **1** sẽ làm cho chính sách lập lịch của cgroup trở thành `SCHED_IDLE`.

Các luồng bên trong cgroup vẫn giữ được mức độ ưu tiên tương đối, nhưng toàn bộ cgroup sẽ được coi là có **mức độ ưu tiên rất thấp** so với các cgroup khác.

Tệp này **chỉ ảnh hưởng tới các tiến trình sử dụng fair-class scheduler**.

Dưới đây là bản dịch tiếng Việt của nội dung trong ảnh:

---

## **Bộ điều khiển bộ nhớ (Memory)**

Bộ điều khiển `"memory"` quản lý việc phân phối bộ nhớ. Bộ điều khiển này có trạng thái và triển khai cả mô hình giới hạn và bảo vệ. Do sự đan xen giữa việc sử dụng bộ nhớ, áp lực thu hồi (reclaim pressure) và tính trạng thái của bộ nhớ, mô hình phân phối bộ nhớ trở nên tương đối phức tạp.

Mặc dù không hoàn toàn chính xác tuyệt đối, nhưng tất cả các loại sử dụng bộ nhớ chính của một cgroup đều được theo dõi để tổng lượng bộ nhớ tiêu thụ có thể được ghi nhận và kiểm soát ở mức hợp lý. Hiện tại, các loại sử dụng bộ nhớ sau được theo dõi:

* Bộ nhớ người dùng: bộ nhớ ẩn danh và bộ nhớ đệm trang (page cache).
* Cấu trúc dữ liệu hạt nhân như dentry và inode.
* Bộ đệm ổ cắm TCP.

---

## 11. **Các tệp giao diện bộ nhớ (Memory Interface Files)**

Tất cả giá trị bộ nhớ đều được tính bằng byte. Nếu một giá trị không căn chỉnh với `PAGE_SIZE` được ghi, giá trị có thể được làm tròn lên đến bội số `PAGE_SIZE` gần nhất khi đọc lại.

---

**`memory.current`**

Tệp chỉ đọc, chứa giá trị đơn, tồn tại trên các cgroup không phải root.

> Tổng dung lượng bộ nhớ hiện tại đang được sử dụng bởi cgroup và tất cả các nhóm con của nó.

---

**`memory.min`**

Tệp có thể đọc-ghi, chứa giá trị đơn, tồn tại trên các cgroup không phải root. Mặc định là **"0"**.

> **Bảo vệ bộ nhớ cứng.** Nếu lượng bộ nhớ sử dụng của cgroup nằm trong ngưỡng `min` hiệu lực, bộ nhớ của cgroup sẽ không bị thu hồi trong bất kỳ điều kiện nào.
> Nếu không còn bộ nhớ có thể thu hồi mà không bị bảo vệ, OOM killer sẽ được kích hoạt. Nếu vượt ngưỡng `min`, các trang sẽ bị thu hồi tỷ lệ với phần vượt mức, giúp giảm áp lực reclaim đối với các vùng vượt nhỏ hơn.

Giá trị giới hạn hiệu lực của `memory.min` bị giới hạn bởi giá trị `memory.min` của tất cả các tổ tiên.
Nếu có vượt quá giới hạn `memory.min` (ví dụ: nhóm con yêu cầu nhiều bộ nhớ bảo vệ hơn so với nhóm cha có thể cung cấp), mỗi nhóm con sẽ nhận được phần bảo vệ tương ứng theo tỷ lệ sử dụng bộ nhớ thực tế của nó nằm dưới `memory.min`.

> Việc sử dụng quá nhiều bộ nhớ dưới dạng được bảo vệ này không được khuyến khích vì có thể dẫn đến tình trạng thiếu bộ nhớ (OOM) liên tục.

Nếu một cgroup không chứa tiến trình nào, thì giá trị `memory.min` của nó sẽ bị bỏ qua.

---

**`memory.low`**

Tệp giá trị đơn có thể đọc-ghi, tồn tại trên các cgroup không phải root. Giá trị mặc định là `"0"`.

> **Bảo vệ bộ nhớ ở mức nỗ lực tốt nhất**. Nếu mức sử dụng bộ nhớ của một cgroup nằm trong giới hạn `low` hiệu lực, bộ nhớ của cgroup sẽ không bị thu hồi trừ khi không còn bộ nhớ nào có thể thu hồi trong các cgroup không được bảo vệ. Khi vượt qua giới hạn `low`, các trang sẽ bị thu hồi theo tỷ lệ phần vượt, giúp giảm áp lực reclaim cho những vùng vượt nhỏ.

Ranh giới `low` hiệu lực bị giới hạn bởi các giá trị `memory.low` của tất cả các tổ tiên. Nếu có vượt quá giới hạn `memory.low` (ví dụ: nhóm con yêu cầu nhiều bộ nhớ được bảo vệ hơn mức cha có thể cung cấp), thì mỗi nhóm con sẽ nhận được phần bảo vệ tương ứng theo tỷ lệ bộ nhớ thực tế sử dụng dưới `memory.low`.

> Không khuyến khích đưa vào bộ nhớ nhiều hơn lượng có sẵn dưới cơ chế bảo vệ này.

---

**`memory.high`**

Tệp giá trị đơn có thể đọc-ghi, tồn tại trên các cgroup không phải root. Giá trị mặc định là `"max"`.

> **Giới hạn điều tiết việc sử dụng bộ nhớ**. Nếu một cgroup sử dụng bộ nhớ vượt quá giới hạn `high`, các tiến trình trong cgroup sẽ bị điều tiết (throttle) và đưa vào trạng thái áp lực reclaim mạnh.

Vượt qua giới hạn `high` **không bao giờ kích hoạt OOM killer**, nhưng trong điều kiện khắc nghiệt, giới hạn có thể bị vi phạm. Giới hạn này nên được dùng trong các trường hợp mà một tiến trình bên ngoài giám sát cgroup bị giới hạn để giảm áp lực reclaim.

Nếu `memory.high` được mở với cờ `O_NONBLOCK`, thì quá trình reclaim đồng bộ sẽ bị bỏ qua. Điều này hữu ích cho các tiến trình quản trị cần điều chỉnh giới hạn bộ nhớ động cho công việc mà không tiêu tốn tài nguyên CPU của chính chúng vào reclaim. Công việc sẽ kích hoạt reclaim và/hoặc bị điều tiết trong lần yêu cầu cấp phát tiếp theo.

> **Lưu ý**: khi dùng `O_NONBLOCK`, có khả năng cgroup mục tiêu sẽ mất một khoảng thời gian không xác định để giảm mức sử dụng bộ nhớ xuống dưới giới hạn do yêu cầu cấp phát bị trì hoãn hoặc do việc truy cập bộ nhớ liên tục làm chậm quá trình reclaim.

---

**`memory.max`**

Tệp giá trị đơn có thể đọc-ghi, tồn tại trên các cgroup không phải root. Giá trị mặc định là `"max"`.

> **Giới hạn cứng sử dụng bộ nhớ.** Đây là cơ chế chính để giới hạn lượng bộ nhớ mà một cgroup có thể sử dụng. Nếu mức sử dụng bộ nhớ của một cgroup đạt đến giới hạn này và không thể giảm xuống, OOM killer sẽ được kích hoạt trong cgroup đó. Trong một số trường hợp, mức sử dụng có thể tạm thời vượt quá giới hạn.

Trong cấu hình mặc định, các phép cấp phát thứ tự 0 thông thường luôn thành công trừ khi OOM killer chọn tác vụ hiện tại làm nạn nhân.

Một số loại cấp phát không kích hoạt OOM killer. Trình gọi có thể thử lại chúng theo cách khác, trả về không gian người dùng dưới dạng `-ENOMEM`, hoặc âm thầm bỏ qua như trong trường hợp đọc trước đĩa (read-ahead).

Nếu `memory.max` được mở với cờ `O_NONBLOCK`, thì quá trình reclaim đồng bộ và OOM-kill sẽ bị bỏ qua. Điều này hữu ích cho các tiến trình quản trị cần điều chỉnh giới hạn bộ nhớ của công việc mà không tiêu tốn tài nguyên CPU vào việc reclaim bộ nhớ. Công việc sẽ kích hoạt reclaim và/hoặc OOM-kill trong lần yêu cầu cấp phát tiếp theo.

> **Lưu ý** rằng khi dùng `O_NONBLOCK`, có khả năng cgroup mục tiêu sẽ mất một khoảng thời gian không xác định để giảm mức sử dụng xuống dưới giới hạn, do yêu cầu cấp phát bị trì hoãn hoặc do truy cập bộ nhớ liên tục khiến reclaim chậm lại.

---

**`memory.reclaim`**

Tệp dạng lồng có thể ghi duy nhất, tồn tại trên tất cả các cgroup.

> Đây là một giao diện đơn giản để kích hoạt reclaim bộ nhớ trong cgroup mục tiêu.

**Ví dụ:**

```
echo "1G" > memory.reclaim
```

> **Lưu ý:** Kernel có thể reclaim nhiều hoặc ít hơn lượng chỉ định từ cgroup mục tiêu. Nếu reclaim ít hơn, sẽ trả về lỗi `-EAGAIN`.

> Ngoài ra, quá trình reclaim chủ động (được kích hoạt bởi giao diện này) **không có nghĩa là** báo hiệu áp lực bộ nhớ lên cgroup. Do đó, cơ chế cân bằng bộ nhớ socket thường được kích hoạt bởi reclaim bộ nhớ sẽ **không được thực hiện** trong trường hợp này. Điều này có nghĩa là tầng mạng sẽ **không thích ứng** với reclaim do `memory.reclaim` gây ra.

---

### Các khóa lồng nhau sau đây được định nghĩa:

\| **swappiness** | **Giá trị swappiness để reclaim với** |

Việc chỉ định một giá trị `swappiness` sẽ hướng dẫn kernel thực hiện reclaim bộ nhớ với giá trị swappiness đó. Lưu ý rằng điều này có cùng ý nghĩa với `vm.swappiness` được áp dụng cho reclaim trong `memcg`, bao gồm các giới hạn hiện tại và khả năng mở rộng trong tương lai.

Phạm vi hợp lệ cho `swappiness` là `[0–200, max]`, thiết lập `swappiness=max` sẽ chỉ reclaim bộ nhớ ẩn danh.

---

**`memory.peak`**

Tệp giá trị đơn có thể đọc-ghi, tồn tại trên các cgroup không phải root.

Ghi lại mức sử dụng bộ nhớ tối đa của cgroup và các hậu duệ của nó kể từ khi cgroup được tạo ra hoặc từ lần reset gần nhất cho FD đó.

Việc ghi bất kỳ chuỗi không rỗng nào vào tệp này sẽ đặt lại giá trị hiện tại về mức sử dụng bộ nhớ để đọc lại về sau bằng cùng một bộ mô tả tệp (file descriptor).

---

**`memory.oom.group`**

Tệp giá trị đơn có thể đọc-ghi, tồn tại trên các cgroup không phải root. Giá trị mặc định là `"0"`.

Xác định xem cgroup có nên được xem là một khối lượng công việc không thể chia nhỏ đối với OOM killer hay không. Nếu được bật, tất cả các tiến trình thuộc cgroup hoặc các hậu duệ của nó (nếu cgroup không phải là một nhóm lá) sẽ bị tiêu diệt cùng lúc hoặc không bị tiêu diệt chút nào. Điều này nhằm tránh tình trạng giết một phần tiến trình và đảm bảo tính toàn vẹn của khối lượng công việc.

Các tiến trình có bật bảo vệ OOM (`oom_score_adj` được đặt là -1000) được coi là ngoại lệ và **không bao giờ bị giết**.

Nếu OOM killer được kích hoạt trong một cgroup, nó **sẽ không giết** bất kỳ tiến trình nào bên ngoài cgroup đó, **bất kể** các giá trị `memory.oom.group` của tổ tiên (ancestor cgroups).

---

**`memory.events`**

Một tệp chỉ đọc, định dạng flat-keyed, tồn tại trên các cgroup không phải root. Các mục sau đây được định nghĩa. Trừ khi có chỉ định khác, việc thay đổi giá trị trong tệp này sẽ sinh ra một sự kiện sửa đổi tệp.

Lưu ý rằng tất cả các trường trong tệp này đều mang tính phân cấp (hierarchical) và sự kiện sửa đổi tệp có thể được tạo ra bởi sự kiện xảy ra ở cấp dưới trong hệ phân cấp. Đối với các sự kiện cục bộ ở cấp độ cgroup, xem `memory.events.local`.

* **`low`**
  Số lần cgroup bị reclaim do áp lực bộ nhớ cao, mặc dù việc sử dụng bộ nhớ vẫn dưới giới hạn thấp. Thông thường điều này cho thấy giới hạn thấp bị vượt quá do phân bổ quá nhiều.

* **`high`**
  Số lần các tiến trình trong cgroup bị giới hạn (throttled) và được chuyển hướng để thực hiện reclaim trực tiếp do vượt quá giới hạn bộ nhớ cao. Đối với một nhóm có giới hạn cao thay vì áp lực bộ nhớ toàn hệ thống, sự kiện này là điều bình thường.

* **`max`**
  Số lần mức sử dụng bộ nhớ của cgroup tiến gần đến giới hạn tối đa. Nếu reclaim trực tiếp không thành công để giảm mức sử dụng, cgroup sẽ chuyển sang trạng thái OOM (Out-Of-Memory).

* **`oom`**
  Số lần cgroup đạt đến giới hạn bộ nhớ và việc cấp phát (allocation) sắp thất bại.
  Sự kiện này **không được kích hoạt** nếu OOM killer không được xem là một lựa chọn (ví dụ: do cấp phát bậc cao thất bại) hoặc nếu trình gọi yêu cầu không thử lại.

* **`oom_kill`**
  Số lượng tiến trình thuộc cgroup này đã bị giết bởi **bất kỳ loại OOM killer** nào.

* **`oom_group_kill`**
  Số lần xảy ra một **OOM tập thể** (group OOM).

---

**`memory.events.local`**

Tương tự như `memory.events`, nhưng các trường trong tệp này chỉ phản ánh các sự kiện **cục bộ** ở cấp độ cgroup, **không phân cấp**. Sự kiện sửa đổi tệp này chỉ phản ánh các sự kiện địa phương.

---

**`memory.stat`**

Là một tệp chỉ đọc dạng phẳng (flat-keyed), tồn tại trên các cgroup không phải root.

Tệp này phân tích mức tiêu thụ bộ nhớ của cgroup thành các loại bộ nhớ khác nhau, chi tiết theo loại và thông tin về trạng thái và các sự kiện trước đây của hệ thống quản lý bộ nhớ.

Tất cả các đơn vị bộ nhớ đều được tính theo **byte**.

Các mục được sắp xếp để dễ đọc cho con người, và có thể có các mục mới xuất hiện ở giữa. **Không nên dựa vào vị trí cố định của các mục**, hãy sử dụng khóa (key) để tra cứu giá trị cụ thể!

Nếu một mục không có bộ đếm theo từng nút (per-node) hoặc không hiển thị trong `memory.numa_stat`, thì nó sẽ có nhãn `npn` (non-per-node), nghĩa là nó **sẽ không xuất hiện** trong `memory.numa_stat`.

---

**Các trường thông dụng:**

* **anon**: Bộ nhớ dùng cho ánh xạ ẩn danh như `brk()`, `sbrk()`, `mmap(MAP_ANONYMOUS)`.
* **file**: Bộ nhớ cache cho dữ liệu hệ thống tệp, bao gồm `tmpfs` và bộ nhớ dùng chung.
* **kernel (npn)**: Tổng bộ nhớ nhân, bao gồm `kernel_stack`, `pagetables`, `percpu`, `vmalloc`, `slab`.
* **kernel\_stack**: Bộ nhớ cấp phát cho ngăn xếp của nhân.
* **pagetables**: Bộ nhớ dùng cho bảng trang.
* **sec\_pagetables**: Bộ nhớ bảng trang phụ (như trong KVM, IOMMU).
* **percpu (npn)**: Bộ nhớ cho các cấu trúc dữ liệu nhân riêng theo từng CPU.
* **sock (npn)**: Bộ nhớ dùng trong các bộ đệm truyền thông mạng.
* **vmalloc (npn)**: Bộ nhớ dùng cho ánh xạ ảo `vmap`.
* **shmem**: Bộ nhớ cache có thể hoán đổi, như `tmpfs`, `shm`, `mmap()` chia sẻ ẩn danh.
* **zswap**: Bộ nhớ dùng bởi cơ chế nén `zswap`.
* **zswapped**: Bộ nhớ ứng dụng đã được swap ra bằng `zswap`.

---

**Liên quan đến `THP` (Transparent Huge Pages):**

* **anon\_thp**: Bộ nhớ ánh xạ ẩn danh sử dụng THP.
* **file\_thp**: Dữ liệu cache hệ thống tệp sử dụng THP.
* **shmem\_thp**: `shmem`, `tmpfs`, `mmap()` dùng THP.

---

**`file_*`**

* **file\_mapped**: Dữ liệu hệ thống tệp được ánh xạ với `mmap()`.
* **file\_dirty**: Dữ liệu cache đã bị chỉnh sửa nhưng chưa ghi đĩa.
* **file\_writeback**: Dữ liệu cache đang được ghi đĩa.
* **swapcached**: Lượng swap đang được giữ lại trong bộ nhớ RAM.

---

**Hoạt động bộ nhớ:**

* **inactive\_anon**, **active\_anon**, **inactive\_file**, **active\_file**, **unevictable**: Bộ nhớ trên danh sách quản lý nội bộ.
* **slab\_reclaimable**: Một phần của `slab` có thể reclaim, như `dentries`, `inodes`.
* **slab\_unreclaimable**: Một phần của `slab` không thể reclaim.
* **slab (npn)**: Tổng bộ nhớ dùng cho cấu trúc dữ liệu trong nhân.

---

**Workingset:**

* **workingset\_refault\_**\*: Số lần trang bị đưa trở lại bộ nhớ sau khi bị đuổi ra.
* **workingset\_activate\_**\*: Số lần trang vừa bị fault lập tức được đưa vào active set.
* **workingset\_restore\_**\*: Trang được khôi phục trước khi bị reclaim.
* **workingset\_nodereclaim**: Số lần reclaim node "shadow".

---

**Swap:**

* **pswpin (npn)**, **pswpout (npn)**: Số lượng trang được swap vào/ra.
* **swpin\_zero**, **swpout\_zero**: Trang swap được tối ưu I/O vì chứa toàn số 0.
* **zswpin**, **zswpout**, **zswpwb**: Di chuyển qua lại giữa RAM và `zswap`.

---

**Page scan & reclaim:**

* **pgscan\_**\*: Số lượng trang được quét.
* **pgsteal\_**\*: Số lượng trang đã reclaim.
* **pgfault (npn)**, **pgmajfault (npn)**: Số lượng page fault.
* **pgrefill**, **pgactivate**, **pgdeactivate**: Trang được chuyển sang active/inactive.
* **pglazyfree**, **pglazyfreed**: Trang được giải phóng theo cơ chế "lazy".

---

**Transparent Huge Pages:**

* **thp\_fault\_alloc (npn)**: THP được cấp phát do page fault.
* **thp\_collapse\_alloc (npn)**: THP được cấp để gom nhiều trang nhỏ.
* **thp\_swpout (npn)**: THP bị swap out nguyên khối.
* **thp\_swpout\_fallback (npn)**: THP bị tách nhỏ vì thiếu không gian swap liên tục.

---

**NUMA:**

* **numa\_pages\_migrated**, **numa\_pte\_updates**, **numa\_hint\_faults**: Số liệu liên quan đến việc cân bằng bộ nhớ NUMA.

---

**Page demotion:**

* **pgdemote\_**\*: Trang bị giảm cấp từ bộ nhớ nhanh xuống bộ nhớ chậm.

---

**`hugetlb`:**

* **hugetlb**: Bộ nhớ được sử dụng bởi các trang `hugetlb`. Chỉ hiện khi `memory_hugetlb_accounting` được bật trong `memory.current`.

---

**`memory.numa_stat`**

Là tệp chỉ đọc, dạng khóa lồng nhau (nested-keyed), tồn tại trên các cgroup không phải root.

Tệp này phân tích mức sử dụng bộ nhớ của cgroup theo từng loại bộ nhớ, chi tiết theo loại, và thông tin trên từng **node vật lý (NUMA node)** trong hệ thống quản lý bộ nhớ.

Điều này hữu ích để theo dõi thông tin phân bổ bộ nhớ theo NUMA trong cgroup, vì các trang bộ nhớ có thể được cấp phát từ bất kỳ node vật lý nào. Một trường hợp sử dụng thực tế là đánh giá hiệu năng ứng dụng bằng cách kết hợp thông tin này với phân bổ CPU của ứng dụng.

* Tất cả đơn vị đo đều là **byte**.
* Định dạng đầu ra:

```txt
type N0=<byte ở node 0> N1=<byte ở node 1> ...
```

* Các mục được sắp xếp để dễ đọc, có thể thay đổi theo thời gian nên **không nên dựa vào vị trí cố định**, hãy sử dụng **tên khóa** để tra cứu giá trị.

Các khóa ở đây có thể tham chiếu từ `memory.stat`.

---

**`memory.swap.current`**

* Tệp chỉ đọc, giá trị đơn.
* Tổng lượng **swap hiện đang được sử dụng** bởi cgroup và các cgroup con.

---

**`memory.swap.high`**

* Tệp đọc-ghi, giá trị đơn. Mặc định là `"max"`.
* **Giới hạn swap mềm**: Nếu mức sử dụng swap vượt ngưỡng này, mọi cấp phát thêm sẽ bị hạn chế (throttle) để cho phép không gian người dùng xử lý tình huống out-of-memory (OOM).
* Đây **không phải là công cụ để quản lý hoạt động swap thông thường**, mà là **rào chắn cảnh báo**.
* Không nên chạm tới ngưỡng này trong các workload ổn định.

---

**`memory.swap.peak`**

* Tệp đọc-ghi, giá trị đơn.
* Ghi lại mức sử dụng swap cao nhất kể từ khi cgroup được tạo ra hoặc kể từ lần reset gần nhất.
* Ghi bất kỳ chuỗi không rỗng nào vào tệp này sẽ **reset** giá trị hiện tại cho lần đọc tiếp theo.

---

**`memory.swap.max`**

* Tệp đọc-ghi, giá trị đơn. Mặc định là `"max"`.
* **Giới hạn swap cứng**: Nếu vượt qua ngưỡng này, **bộ nhớ ẩn danh sẽ không được swap ra**.

---

**`memory.swap.events`**

* Tệp chỉ đọc, dạng khóa phẳng (flat-keyed).
* Ghi nhận các sự kiện liên quan đến việc sử dụng swap. Khi có thay đổi giá trị, sẽ tạo ra sự kiện sửa đổi tệp.

Các khóa:

* **high**: Số lần vượt ngưỡng `memory.swap.high`.
* **max**: Số lần cố gắng swap vượt quá giới hạn `memory.swap.max` và thất bại.
* **fail**: Số lần cấp phát swap thất bại do hệ thống hết swap hoặc vượt `memory.swap.max`.

> Khi giảm ngưỡng swap dưới mức sử dụng hiện tại, các mục swap sẽ được reclaim từ từ, nên mức sử dụng swap có thể cao hơn giới hạn một thời gian, để giảm tác động đến hiệu suất và quản lý bộ nhớ.

---

**`memory.zswap.current`**

* Tệp chỉ đọc, giá trị đơn.
* Lượng bộ nhớ hiện đang được **zswap backend nén giữ lại**.

---

**`memory.zswap.max`**

* Tệp đọc-ghi, giá trị đơn. Mặc định là `"max"`.
* **Giới hạn cứng cho zswap**: Nếu zswap pool vượt giới hạn này, **không thể nén thêm** trước khi các mục cũ được fault-in hoặc ghi ra đĩa.

---

**`memory.zswap.writeback`**

* Tệp đọc-ghi, giá trị đơn. Mặc định là `"1"`.
* Đây là một cài đặt **có tính kế thừa theo thứ bậc** — nếu bị tắt ở cgroup cha, thì con cũng bị tắt.

Giá trị:

* **0**: Tắt hoàn toàn việc ghi swap ra thiết bị swap, bao gồm:

  * Ghi từ `zswap` ra ổ đĩa.
  * Swap do zswap store thất bại.
* Việc tắt này có thể gây **hiệu quả reclaim thấp**, nếu các trang không thể nén được liên tục bị từ chối.
* Lưu ý: khác với `memory.swap.max = 0`, vì vẫn cho phép ghi bộ nhớ vào zswap.

> Nếu `zswap` bị tắt, thì thiết lập này **không có hiệu lực**.

---

**`memory.pressure`**

* Tệp chỉ đọc, khóa lồng nhau.
* Hiển thị **thông tin áp lực bộ nhớ (memory pressure stall information - PSI)**.
* Xem thêm tài liệu `[Documentation/accounting/psi.rst](https://www.kernel.org/doc/html/latest/accounting/psi.html#psi)` để biết chi tiết.

---

### **Hướng dẫn sử dụng (Usage Guidelines)**

`memory.high` là cơ chế chính để kiểm soát việc sử dụng bộ nhớ. Việc **phân bổ vượt giới hạn cao** (tổng các giới hạn cao > tổng bộ nhớ có sẵn) và để hệ thống áp lực bộ nhớ toàn cục tự phân bổ bộ nhớ theo mức sử dụng là một chiến lược khả thi.

Vì việc vượt quá giới hạn `memory.high` **không kích hoạt OOM killer** mà chỉ làm nghẽn (throttle) cgroup vi phạm, nên trình quản lý có **nhiều cơ hội** để theo dõi và đưa ra hành động phù hợp như: **cấp thêm bộ nhớ hoặc chấm dứt workload**.

Xác định xem một cgroup có đủ bộ nhớ hay không là việc **không đơn giản**, vì mức sử dụng bộ nhớ không thể hiện rõ workload có đang cần thêm bộ nhớ hay không. Ví dụ, một workload ghi dữ liệu nhận từ mạng vào tệp có thể sử dụng toàn bộ bộ nhớ khả dụng, **nhưng vẫn có thể hoạt động hiệu quả với lượng bộ nhớ nhỏ**. Do đó, cần có một cơ chế đo lường **áp lực bộ nhớ** – tức workload bị ảnh hưởng bao nhiêu do thiếu bộ nhớ – để xác định workload có thực sự cần thêm bộ nhớ không. **Đáng tiếc, hiện tại cơ chế theo dõi áp lực bộ nhớ vẫn chưa được triển khai.**

---

### **Quyền sở hữu bộ nhớ (Memory Ownership)**

Một vùng bộ nhớ được **tính vào cgroup đã tạo ra nó** và sẽ tiếp tục bị tính vào cgroup đó **cho đến khi vùng bộ nhớ được giải phóng**. Việc **di chuyển một tiến trình** sang cgroup khác **không làm di chuyển lượng bộ nhớ** mà nó đã tạo ra khi còn ở cgroup cũ sang cgroup mới.

Một vùng bộ nhớ có thể được **sử dụng bởi các tiến trình từ nhiều cgroup khác nhau**. Việc **vùng đó bị tính vào cgroup nào là không xác định**; tuy nhiên theo thời gian, vùng bộ nhớ đó thường sẽ được tính vào cgroup có đủ hạn mức bộ nhớ để **tránh bị reclaim (thu hồi) gắt gao**.

Nếu một cgroup **quét qua một lượng lớn bộ nhớ** mà có khả năng sẽ được truy cập nhiều bởi các cgroup khác, thì nên sử dụng `POSIX_FADV_DONTNEED` để **từ bỏ quyền sở hữu vùng bộ nhớ** đó — điều này giúp đảm bảo quyền sở hữu bộ nhớ đúng đắn.

---

## 12. **I/O**

Bộ điều khiển `"io"` điều phối việc phân phối tài nguyên I/O. Bộ điều khiển này hỗ trợ cả phân phối theo trọng số (weight) và giới hạn tuyệt đối dựa trên **băng thông** hoặc **IOPS**. Tuy nhiên:

* Phân phối theo trọng số chỉ khả dụng nếu `cfq-iosched` đang được sử dụng.
* Không có phương pháp nào áp dụng được cho các thiết bị sử dụng `blk-mq`.

---

### **Tệp giao diện I/O (IO Interface Files)**

**`io.stat`**

* Là một tệp chỉ đọc, sử dụng định dạng nested-keyed.
* Các dòng được đánh chỉ số theo số hiệu thiết bị `$MAJ:$MIN` và **không có thứ tự cố định**.
* Các khóa con (nested keys) được định nghĩa như sau:

| **Khóa** | **Ý nghĩa**                       |
| -------- | --------------------------------- |
| `rbytes` | Số byte đã đọc                    |
| `wbytes` | Số byte đã ghi                    |
| `rios`   | Số thao tác đọc (read IOs)        |
| `wios`   | Số thao tác ghi (write IOs)       |
| `dbytes` | Số byte bị loại bỏ                |
| `dios`   | Số thao tác loại bỏ (discard IOs) |

---

**Ví dụ đầu ra của lệnh đọc `io.stat`:**

```
8:16 rbytes=1459200 wbytes=314773504 rios=192 wios=353 dbytes=0 dios=0
8:0  rbytes=90430464 wbytes=299008000 rios=8950 wios=1252 dbytes=50331648 dios=3021
```

Ở đây:

* `8:16` và `8:0` là mã thiết bị.
* Các giá trị hiển thị số byte đọc/ghi, số thao tác IO và số byte bị loại bỏ tương ứng với từng thiết bị.

---

**`io.cost.qos`**

Đây là tệp **có thể đọc và ghi**, sử dụng **định dạng nested-keyed**, **chỉ tồn tại trên `root cgroup`**.

Tệp này cấu hình **Chất lượng dịch vụ (Quality of Service)** của **mô hình chi phí IO (IO cost model)** thông qua bộ điều khiển `CONFIG_BLK_CGROUP_IOCOST`, hiện đang triển khai phương pháp kiểm soát tỉ lệ **`io.weight`**.

* Các dòng được đánh chỉ số theo định dạng `$MAJ:$MIN` (số hiệu thiết bị) và **không có thứ tự**.
* Dòng tương ứng với một thiết bị sẽ được ghi vào lần đầu tiên thiết bị đó ghi vào `io.cost.qos` hoặc `io.cost.model`.

**Các khóa con (nested keys) được định nghĩa như sau:**

| **Khóa** | **Ý nghĩa**                                                |
| -------- | ---------------------------------------------------------- |
| `enable` | Kích hoạt kiểm soát dựa trên trọng số                      |
| `ctrl`   | “auto” hoặc “user” (tự động hoặc do người dùng điều khiển) |
| `rpct`   | Phần trăm độ trễ đọc (read latency percentile) \[0, 100]   |
| `rlat`   | Ngưỡng độ trễ đọc                                          |
| `wpct`   | Phần trăm độ trễ ghi (write latency percentile) \[0, 100]  |
| `wlat`   | Ngưỡng độ trễ ghi                                          |
| `min`    | Phần trăm tỉ lệ tối thiểu \[1, 10000]                      |
| `max`    | Phần trăm tỉ lệ tối đa \[1, 10000]                         |

---

**Ghi chú:**

* **Bộ điều khiển này mặc định bị vô hiệu hóa**, có thể được bật bằng cách đặt `enable = 1`.
* Các tham số `rpct` và `wpct` mặc định là 0.
* Bộ điều khiển sử dụng trạng thái bão hòa thiết bị nội bộ để điều chỉnh tốc độ IO tổng thể trong khoảng giữa `min` và `max`.

---

**Khi cần chất lượng IO tốt hơn:**

Bạn có thể cấu hình các tham số QoS liên quan đến độ trễ, ví dụ như `rpct`, `rlat`, `wpct`, `wlat`, để đảm bảo kiểm soát tốt hơn đối với hành vi truy cập IO.

```
8:16 enable=1 ctrl=auto rpct=95.00 rlat=75000 wpct=95.00 wlat=150000 min=50.00 max=150.0
```
---

Ví dụ cho thấy rằng, trên thiết bị **sdb**, khi bộ điều khiển được bật, thiết bị sẽ được coi là **bị bão hòa** nếu **percentile thứ 95** của độ trễ hoàn thành thao tác **đọc vượt quá 75ms** hoặc **ghi vượt quá 150ms**, và sẽ điều chỉnh **tổng tốc độ thực hiện IO** nằm trong khoảng từ **50% đến 150%** tương ứng.

---

Càng giảm **ngưỡng bão hòa** thì chất lượng dịch vụ IO theo độ trễ (**latency QoS**) càng tốt, nhưng đánh đổi lại là **băng thông tổng thể bị giảm**. Khoảng điều chỉnh giữa giá trị `min` và `max` càng hẹp thì hành vi IO càng phù hợp với mô hình chi phí. Tuy nhiên, cần lưu ý rằng:

* Tốc độ cơ bản của IO có thể khác xa 100%.
* Thiết lập `min` và `max` một cách mù quáng có thể dẫn đến **giảm hiệu suất thiết bị** hoặc **mất khả năng kiểm soát**.

Các giá trị `min` và `max` hữu ích trong việc điều chỉnh các thiết bị có hành vi biến đổi theo thời gian — ví dụ, một ổ SSD có thể ghi rất nhanh trong một thời gian, nhưng sau đó **đột ngột dừng lại** trong vài giây.

---

Khi `ctrl` được đặt là `"auto"`:

* Các tham số được điều khiển bởi kernel và có thể **tự động thay đổi**.
* Nếu đặt `ctrl` thành `"user"` hoặc cấu hình bất kỳ giá trị nào trong các tham số percentile hoặc độ trễ, chế độ `"user"` sẽ được kích hoạt và **tắt các thay đổi tự động**.

Bạn có thể khôi phục lại chế độ tự động bằng cách đặt lại `ctrl` thành `"auto"`.

---

**`io.cost.model`**

Một tệp có khóa lồng nhau, chỉ đọc/ghi, chỉ tồn tại trên `root cgroup`.

---

Tệp này cấu hình mô hình chi phí của bộ điều khiển dựa trên mô hình chi phí IO (được bật qua tùy chọn `CONFIG_BLK_CGROUP_IOCOST`), hiện đang triển khai kiểm soát theo tỷ lệ `io.weight`. Các dòng được đánh chỉ mục theo số thiết bị `$MAJ:$MIN` và không được sắp xếp. Dòng cho một thiết bị cụ thể sẽ được ghi lần đầu tiên tại tệp `io.cost.qos` hoặc `io.cost.model`. Các khóa con sau được định nghĩa:

| Khóa    | Mô tả                                     |
| ------- | ----------------------------------------- |
| `ctrl`  | `"auto"` hoặc `"user"`                    |
| `model` | Mô hình chi phí đang sử dụng – `"linear"` |

---

* Khi `ctrl` là `"auto"`, kernel có thể tự động thay đổi tất cả các tham số.
* Khi `ctrl` được đặt thành `"user"` hoặc bất kỳ tham số nào khác được ghi vào, `ctrl` sẽ trở thành `"user"` và các thay đổi tự động sẽ bị vô hiệu hóa.

---

Khi `model` là `"linear"`, các tham số mô hình sau được định nghĩa:

| Tham số | Mô tả        |                                     |
| ------- | ------------ | ----------------------------------- |
| \`\[r   | w]bps\`      | Tốc độ IO tuần tự tối đa            |
| \`\[r   | w]seqiops\`  | Số IO tuần tự 4k tối đa mỗi giây    |
| \`\[r   | w]randiops\` | Số IO ngẫu nhiên 4k tối đa mỗi giây |

---

Dựa trên các thông số trên, mô hình tuyến tính tích hợp trong kernel sẽ xác định chi phí cơ bản của IO tuần tự và ngẫu nhiên, cũng như hệ số chi phí cho dịch vụ IO. Mặc dù đơn giản, mô hình này có thể bao phủ các lớp thiết bị phổ biến một cách chấp nhận được.

Nếu cần, mô hình chi phí IO có thể được tinh chỉnh chính xác hơn bằng cách sử dụng các công cụ để tạo hệ số thiết bị cụ thể, chẳng hạn như:

```
tools/cgroup/iocost_coef_gen.py
```
---

**`io.weight`**

Một tệp có khóa phẳng chỉ đọc/ghi, tồn tại trên các `non-root cgroups`. Mặc định là `"default 100"`.

---

* Dòng đầu tiên là trọng số mặc định áp dụng cho các thiết bị không có ghi đè cụ thể.
* Các dòng còn lại là các ghi đè, được đánh khóa theo số thiết bị `$MAJ:$MIN` và không được sắp xếp.
* Trọng số nằm trong phạm vi \[1, 10000] và chỉ định lượng thời gian IO tương đối mà cgroup có thể sử dụng so với các cgroup anh em.

---

Trọng số mặc định có thể được cập nhật bằng cách ghi `"default $WEIGHT"` hoặc đơn giản là `"$WEIGHT"`.
Ghi đè có thể được thiết lập bằng cách ghi `"$MAJ:$MIN $WEIGHT"` và được xóa bằng cách ghi `"$MAJ:$MIN default"`.

---

**Ví dụ kết quả đọc từ tệp:**

```
default 100
8:16 200
8:0 50
```

---

Ý nghĩa:

* Trọng số mặc định là `100` cho tất cả các thiết bị nếu không có ghi đè cụ thể.
* Thiết bị `8:16` (ví dụ /dev/sdb) có trọng số `200`.
* Thiết bị `8:0` (ví dụ /dev/sda) có trọng số `50`.

---

**`io.max`**

Một tệp chỉ đọc/ghi có định dạng khóa lồng nhau, tồn tại trên các cgroup không phải gốc.

Giới hạn IO dựa trên BPS (byte mỗi giây) và IOPS (lượt thao tác IO mỗi giây). Các dòng được đánh khóa theo số thiết bị `$MAJ:$MIN` và không được sắp xếp. Các khóa con được định nghĩa như sau:

| Khóa    | Ý nghĩa                        |
| ------- | ------------------------------ |
| `rbps`  | Số byte đọc tối đa mỗi giây    |
| `wbps`  | Số byte ghi tối đa mỗi giây    |
| `riops` | Số lượt IO đọc tối đa mỗi giây |
| `wiops` | Số lượt IO ghi tối đa mỗi giây |

---

Khi ghi, có thể chỉ định bất kỳ số cặp khóa-giá trị nào theo bất kỳ thứ tự nào. Giá trị `"max"` có thể dùng để **xóa bỏ giới hạn** cụ thể.

Nếu cùng một khóa được chỉ định nhiều lần, kết quả là **không xác định**.

Các giới hạn BPS và IOPS được tính riêng cho từng chiều IO. Nếu vượt quá giới hạn, IO sẽ bị **trì hoãn** (nhưng các burst tạm thời vẫn được cho phép).

---

Ví dụ: đặt giới hạn đọc ở mức 2MB/s và ghi ở 120 IOPS cho thiết bị `8:16`:

```bash
echo "8:16 rbps=2097152 wiops=120" > io.max
```

Đọc lại sẽ cho kết quả:

```bash
8:16 rbps=2097152 wbps=max riops=max wiops=120
```

Muốn **xóa giới hạn ghi IOPS**, dùng:

```bash
echo "8:16 wiops=max" > io.max
```

Đọc lại sẽ thấy:

```bash
8:16 rbps=2097152 wbps=max riops=max wiops=max
```

---

**`io.pressure`**

Là tệp chỉ đọc có khóa lồng nhau.

Hiển thị thông tin thống kê về độ "tắc nghẽn" (pressure stall) liên quan đến IO.
Xem thêm tại tài liệu: [`Documentation/accounting/psi.rst`](https://www.kernel.org/doc/html/latest/accounting/psi.html#psi)

---

### Ghi lại bộ đệm (Writeback)

Bộ đệm trang (page cache) bị "làm bẩn" (dirty) thông qua các thao tác ghi có bộ đệm và chia sẻ mmap, sau đó được ghi bất đồng bộ vào hệ thống tập tin bằng cơ chế writeback. Writeback nằm giữa bộ nhớ và miền IO, điều phối tỷ lệ bộ nhớ bị làm bẩn và ghi IO.

Bộ điều khiển IO (io controller), kết hợp với bộ điều khiển bộ nhớ (memory controller), kiểm soát IO ghi bộ đệm trang. Bộ điều khiển bộ nhớ xác định miền bộ nhớ nơi tỷ lệ dirty memory được tính toán và duy trì, còn io controller xác định miền IO nơi thực hiện ghi các trang bẩn. Cả trạng thái dirty memory toàn hệ thống và theo từng cgroup đều được xét đến, trong đó mức ràng buộc chặt hơn sẽ được áp dụng.

---

**Cgroup writeback** yêu cầu hệ thống tập tin hỗ trợ rõ ràng. Hiện tại, writeback theo cgroup chỉ được hỗ trợ trên các hệ thống tập tin như: `ext2`, `ext4`, `btrfs`, `f2fs`, và `xfs`. Với các hệ thống tập tin khác, tất cả IO writeback đều quy về cgroup gốc (`root cgroup`).

Có sự khác biệt nội tại giữa quản lý bộ nhớ và writeback, ảnh hưởng đến cách theo dõi quyền sở hữu cgroup:

* **Bộ nhớ** được theo dõi **theo từng trang** (per page).
* **Writeback** được theo dõi **theo từng inode**.

Đối với mục đích ghi lại (writeback), một inode được gán cho một cgroup, và tất cả các IO ghi các trang từ inode đó sẽ được tính cho cgroup tương ứng.

---

Do quyền sở hữu bộ nhớ được theo dõi theo từng trang, có thể xảy ra trường hợp các trang thuộc về cgroup khác với cgroup của inode. Các trang này gọi là **trang ngoại lai** (foreign pages). Writeback sẽ theo dõi những trang này và, nếu cgroup ngoại lai trở thành nhóm chiếm đa số sau một khoảng thời gian, quyền sở hữu inode sẽ được chuyển sang cgroup đó.

---

Mặc dù mô hình này đủ cho hầu hết các trường hợp, nhưng nếu nhiều cgroup cùng ghi vào một inode đồng thời thì việc ghi có thể bị ghi nhận sai lệch. Bộ điều khiển bộ nhớ thường chỉ định quyền sở hữu trang ngay lần sử dụng đầu tiên và không cập nhật lại cho đến khi trang bị giải phóng. Do đó, nếu writeback tuân theo quyền sở hữu trang một cách nghiêm ngặt thì việc nhiều cgroup ghi đè lên nhau sẽ không như mong đợi. **Khuyến cáo không sử dụng những mô hình như vậy**.

---

### Các tham số sysctl ảnh hưởng đến hành vi writeback của cgroup bao gồm:

* `vm.dirty_background_ratio`, `vm.dirty_ratio`
  → Các tỷ lệ này áp dụng cho writeback theo cgroup giống như bình thường, với lượng bộ nhớ khả dụng bị giới hạn bởi bộ điều khiển bộ nhớ và hệ thống làm sạch bộ nhớ.

* `vm.dirty_background_bytes`, `vm.dirty_bytes`
  → Với cgroup, các thông số này được tính theo tỷ lệ so với tổng bộ nhớ của hệ thống và áp dụng giống như `vm.dirty[_background]_ratio`.

---

### Độ trễ IO (IO Latency)

Đây là một bộ điều khiển trong **cgroup v2** nhằm bảo vệ tải công việc IO. Bạn có thể cung cấp cho một nhóm một ngưỡng độ trễ, và nếu độ trễ trung bình vượt quá ngưỡng đó, bộ điều khiển sẽ **giới hạn (throttle)** các nhóm ngang cấp khác có ngưỡng độ trễ thấp hơn so với workload được bảo vệ.

Các giới hạn này **chỉ được áp dụng ở cấp độ ngang hàng** trong cây phân cấp cgroup. Điều này có nghĩa là, trong sơ đồ bên dưới, chỉ các nhóm **A, B và C** sẽ ảnh hưởng lẫn nhau, và nhóm **D và F** cũng ảnh hưởng lẫn nhau. Nhóm **G** sẽ **không bị ảnh hưởng bởi bất kỳ ai** và cũng **không ảnh hưởng đến ai cả**:

```
         [root]
        /   |   \
       A    B    C
      / \   |    
     D   F  G 
```

---

### Cách cấu hình lý tưởng:

Bạn nên thiết lập `io.latency` cho các nhóm **A, B và C**. Thông thường, **không nên đặt giá trị thấp hơn độ trễ mà thiết bị của bạn có thể hỗ trợ**.

Hãy thử nghiệm để tìm ra giá trị phù hợp nhất với workload của bạn:

* Bắt đầu với giá trị **cao hơn** độ trễ kỳ vọng.
* Theo dõi giá trị `avg_lat` trong tệp `io.stat` của nhóm workload để có ý tưởng về độ trễ thực tế trong điều kiện vận hành bình thường.
* Sau đó, sử dụng giá trị `avg_lat` làm cơ sở và **đặt ngưỡng thực tế cao hơn từ 10–15%** so với giá trị đó.

---

### Cách cơ chế giới hạn độ trễ IO hoạt động

`io.latency` là một bộ điều khiển có tính bảo toàn hiệu suất — tức là **chừng nào tất cả các nhóm đều đáp ứng được ngưỡng độ trễ của mình thì bộ điều khiển sẽ không làm gì cả**.

Một khi một nhóm **bắt đầu không đáp ứng ngưỡng độ trễ**, nó sẽ bắt đầu **giới hạn (throttle) các nhóm ngang cấp khác** mà có ngưỡng cao hơn chính nó. Việc giới hạn này diễn ra dưới hai hình thức:

* **Giới hạn theo độ sâu hàng đợi (Queue Depth Throttling)**: Đây là số lượng IO chưa hoàn thành mà một nhóm được phép giữ lại. Hệ thống sẽ **giảm dần giới hạn này một cách nhanh chóng**, từ không giới hạn xuống còn 1 IO tại một thời điểm.

* **Tạo độ trễ nhân tạo (Artificial Delay Induction)**: Một số loại IO không thể bị giới hạn mà không ảnh hưởng xấu đến các nhóm ưu tiên cao hơn, ví dụ: IO liên quan đến swap hoặc metadata. Những IO này vẫn được phép diễn ra bình thường, **nhưng độ trễ sẽ bị "tính vào" nhóm nguồn phát sinh IO**. Nếu nhóm đó đang bị giới hạn, bạn sẽ thấy các trường `use_delay` và `delay` trong `io.stat` tăng lên. Trường `delay` thể hiện số micro giây được thêm vào cho mỗi tiến trình trong nhóm này. Nếu có nhiều hoạt động swap/metadata, giá trị này có thể tăng cao, vì vậy hệ thống giới hạn mỗi sự kiện trì hoãn ở mức tối đa là **1 giây mỗi lần**.

Khi một nhóm bị giới hạn **đáp ứng lại ngưỡng độ trễ**, bộ điều khiển sẽ **dỡ bỏ giới hạn cho các nhóm ngang cấp khác** đã bị giới hạn trước đó. Nếu nhóm đó **ngừng thực hiện IO hoàn toàn**, bộ đếm toàn cục sẽ điều chỉnh để dỡ bỏ giới hạn một cách thích hợp.

---

### Các tệp giao diện độ trễ IO (IO Latency Interface Files)

* **`io.latency`**
  Có định dạng tương tự như các bộ điều khiển khác:

  ```
  MAJOR:MINOR target=<giá trị độ trễ mục tiêu tính bằng micro giây>
  ```

* **`io.stat`**
  Nếu bộ điều khiển được bật, bạn sẽ thấy các chỉ số bổ sung trong `io.stat` ngoài các chỉ số bình thường.

  * `depth`: Số IO hiện đang trong hàng đợi của nhóm.

  * `avg_lat`: Trung bình trượt mũ (Exponential Moving Average) với tốc độ suy giảm 1/exp được giới hạn bởi khoảng lấy mẫu (sampling interval). Khoảng thời gian lấy mẫu có thể tính bằng:

    ```
    win * số mẫu trong cửa sổ lấy mẫu
    ```

  * `win`: Kích thước cửa sổ lấy mẫu, đơn vị mili giây. Đây là khoảng thời gian tối thiểu giữa các lần đánh giá độ trễ. Windows chỉ trôi khi có hoạt động IO. Các khoảng rảnh (idle) kết thúc cửa sổ gần nhất.

---

### Ưu Tiên I/O

Một thuộc tính duy nhất điều khiển hành vi của chính sách nhóm ưu tiên I/O, cụ thể là thuộc tính `io.prio.class`. Các giá trị sau đây được chấp nhận cho thuộc tính này:

* **no-change**
  Không thay đổi lớp ưu tiên I/O.

* **promote-to-rt**
  Với các yêu cầu không thuộc lớp ưu tiên RT, chuyển chúng thành RT. Đồng thời chuyển mức độ ưu tiên của các yêu cầu này thành 4. Không thay đổi các yêu cầu đã thuộc lớp RT.

* **restrict-to-be**
  Với các yêu cầu không có lớp ưu tiên I/O hoặc thuộc lớp RT, chuyển chúng thành BE (best-effort). Đồng thời thiết lập mức độ ưu tiên thành 0. Không thay đổi các yêu cầu thuộc lớp IDLE.

* **idle**
  Chuyển tất cả các yêu cầu thành lớp ưu tiên IDLE — lớp có ưu tiên thấp nhất.

* **none-to-rt**
  (Đã ngừng sử dụng) — chỉ là bí danh (alias) cho `promote-to-rt`.

---

**Các giá trị số tương ứng với chính sách ưu tiên I/O:**

| Chính sách     | Giá trị số |
| -------------- | ---------- |
| no-change      | 0          |
| promote-to-rt  | 1          |
| restrict-to-be | 2          |
| idle           | 3          |

---

**Giá trị số tương ứng với từng lớp ưu tiên I/O là:**

| Lớp ưu tiên I/O                 | Giá trị số |
| ------------------------------- | ---------- |
| IOPRIO\_CLASS\_NONE             | 0          |
| IOPRIO\_CLASS\_RT (real-time)   | 1          |
| IOPRIO\_CLASS\_BE (best effort) | 2          |
| IOPRIO\_CLASS\_IDLE             | 3          |

---

**Thuật toán đặt lớp ưu tiên I/O cho một yêu cầu:**

* Nếu chính sách là `promote-to-rt`, thì:

  * Đổi lớp ưu tiên của yêu cầu thành `IOPRIO_CLASS_RT`
  * Đặt mức độ ưu tiên thành 4

* Nếu chính sách KHÔNG phải là `promote-to-rt`, thì:

  * Chuyển chính sách thành một số
  * Đặt lớp ưu tiên của yêu cầu là **giá trị lớn nhất** giữa:

    * số vừa chuyển đổi từ chính sách
    * lớp ưu tiên gốc của yêu cầu

---

## 13. **PID**

Bộ điều khiển số lượng tiến trình (PID controller) được dùng để cho phép một **cgroup** dừng việc tạo thêm tiến trình mới thông qua `fork()` hoặc `clone()` sau khi đạt đến một giới hạn cụ thể.

Số lượng tiến trình trong một cgroup có thể bị cạn kiệt theo những cách mà các controller khác không ngăn được, do đó nó cần một controller riêng. Ví dụ, một "fork bomb" (tấn công bằng cách sinh tiến trình hàng loạt) có thể làm cạn kiệt số lượng task trước khi bị giới hạn bởi bộ nhớ.

> Lưu ý: PID trong controller này thực ra là **TID** – Thread IDs – như được sử dụng bởi kernel.

---

### **Tệp Giao Diện PID (PID Interface Files)**

* **pids.max**
  Tệp đơn có thể đọc/ghi, chỉ tồn tại trên các cgroup không phải root. Mặc định là `"max"`.
  → Đây là giới hạn cứng cho số lượng tiến trình.

* **pids.current**
  Tệp chỉ đọc, cho biết số tiến trình hiện có trong cgroup và tất cả các cgroup con.

* **pids.peak**
  Tệp chỉ đọc, cho biết số tiến trình **cao nhất từng được ghi nhận** trong cgroup và các cgroup con.

* **pids.events**
  Tệp chỉ đọc dạng key-value. Khi có thay đổi về giá trị, sẽ tạo sự kiện `file modified`.
  Bao gồm khóa sau:

  * **max** – số lần tổng số tiến trình chạm ngưỡng `pids.max`.

* **pids.events.local**
  Tương tự như `pids.events`, nhưng **chỉ phản ánh các sự kiện cục bộ** của cgroup (không phân cấp). Không ảnh hưởng bởi các tiến trình trong cgroup con.

---

**Lưu ý**

Các thao tác quản lý tổ chức không bị chặn bởi chính sách cgroup. Do đó, vẫn có thể xảy ra `pids.current > pids.max` bằng cách:

* Gán `pids.current` nhỏ hơn `pids.max`, hoặc
* Gắn thêm tiến trình vào cgroup sao cho `pids.current` vượt quá `pids.max`.

Tuy nhiên, **không thể tạo mới tiến trình nếu hành động đó sẽ vi phạm chính sách PID của cgroup**. Các thao tác như `fork()` hoặc `clone()` sẽ bị chặn và trả về lỗi **`-EAGAIN`** nếu vượt giới hạn `pids.max`.


---

### **Cpuset**

Bộ điều khiển “cpuset” cung cấp cơ chế giới hạn CPU và vị trí của node bộ nhớ dành cho các tác vụ, chỉ trong phạm vi tài nguyên được chỉ định trong các tệp giao diện cpuset của cgroup hiện tại của tác vụ.

Cơ chế này đặc biệt hữu ích trên các hệ thống NUMA lớn, nơi việc phân công tác vụ cho các bộ xử lý phù hợp và node bộ nhớ hợp lý giúp **giảm việc truy cập bộ nhớ chéo node và cạnh tranh tài nguyên**, từ đó **cải thiện hiệu năng toàn hệ thống**.

> Bộ điều khiển “cpuset” có tính chất phân cấp (hierarchical), nghĩa là một cgroup con **không được phép sử dụng CPU hoặc node bộ nhớ mà cgroup cha không cho phép**.

---

### **Các Tệp Giao Diện Cpuset (Cpuset Interface Files)**

**cpuset.cpus**

* Là tệp cho phép đọc/ghi nhiều giá trị, chỉ tồn tại trong các cgroup có cpuset được bật.
* Nó liệt kê danh sách các CPU **được yêu cầu** sử dụng bởi các tác vụ trong cgroup này.
* Tuy nhiên, danh sách CPU thực tế có thể **khác với yêu cầu**, do bị giới hạn bởi cgroup cha.

> Các CPU được liệt kê là các số cách nhau bằng dấu phẩy, hoặc theo dải, ví dụ:

```bash
# cat cpuset.cpus
0-4,6,8-10
```

* Nếu giá trị trống, cgroup sẽ sử dụng cấu hình cpuset của cgroup cha gần nhất (nơi `cpuset.cpus` không trống). Nếu không tìm thấy, mặc định là tất cả các CPU khả dụng.
* Giá trị `cpuset.cpus` giữ nguyên cho đến khi được cập nhật lại và **không bị ảnh hưởng bởi sự kiện thay đổi trạng thái CPU (CPU hotplug)**.

---

**cpuset.cpus.effective**

* Là tệp chỉ đọc, chứa danh sách **các CPU thực sự được cấp quyền** bởi cgroup cha.
* Đây là các CPU được phép sử dụng bởi các tác vụ trong cgroup hiện tại.

> Nếu `cpuset.cpus` rỗng, thì `cpuset.cpus.effective` sẽ hiển thị tất cả các CPU mà cgroup cha cấp phép.
> Nếu không rỗng, thì `cpuset.cpus.effective` phải là tập con của `cpuset.cpus` (nếu không thì hệ thống sẽ coi như `cpuset.cpus` đang rỗng).

* Giá trị này **bị ảnh hưởng bởi sự kiện thay đổi trạng thái CPU (CPU hotplug)**.

**cpuset.mems**

Là một tệp có thể đọc-ghi chứa nhiều giá trị, tồn tại trên các cgroup (nhóm điều khiển) không phải root nhưng được bật `cpuset`.

* Tệp này liệt kê **các node bộ nhớ được yêu cầu** sử dụng bởi các tác vụ trong cgroup này.
* Tuy nhiên, **danh sách thực tế các node được cấp phép** sẽ bị giới hạn bởi cgroup cha, và có thể **khác với yêu cầu**.

> Các node bộ nhớ được liệt kê bằng **số** hoặc **dải số**, cách nhau bởi dấu phẩy. Ví dụ:

```bash
# cat cpuset.mems
0-1,3
```

* Nếu để trống: cgroup sẽ **kế thừa cấu hình từ cgroup cha gần nhất** mà có `cpuset.mems` không rỗng. Nếu không tìm thấy thì sẽ sử dụng **tất cả các node bộ nhớ khả dụng**.
* Giá trị `cpuset.mems` sẽ giữ nguyên cho đến khi cập nhật lại và **không bị ảnh hưởng bởi hotplug của node bộ nhớ**.
* **Nếu gán giá trị mới cho `cpuset.mems` trong khi cgroup đang sử dụng node khác**, hệ thống **sẽ chuyển (migrate) bộ nhớ** sang node mới.

  * **Việc chuyển này có thể không hoàn tất**, và có thể mất dữ liệu bộ nhớ.
  * Do đó, chỉ nên cấu hình `cpuset.mems` **trước khi khởi chạy tác vụ**, và **không nên thay đổi thường xuyên**.

---

**cpuset.mems.effective**

Là tệp chỉ đọc, chứa danh sách **các node bộ nhớ thực sự được cấp quyền** từ cgroup cha.

* Nếu `cpuset.mems` rỗng, `cpuset.mems.effective` sẽ chứa **toàn bộ các node từ cgroup cha**.
* Nếu không rỗng, thì `cpuset.mems.effective` phải là **tập con của `cpuset.mems`**, trừ khi node đó không khả dụng.

> Nó **sẽ bị ảnh hưởng bởi các sự kiện hotplug của node bộ nhớ**.

---

**cpuset.cpus.exclusive**

Là tệp có thể đọc-ghi chứa danh sách **các CPU chỉ dành riêng** cho cgroup này (exclusive CPUs).

* Danh sách này không có hiệu lực cho đến khi cgroup trở thành **partition root**.
* Khi thành partition root, các CPU thật sự được cấp quyền sẽ nằm trong `cpuset.cpus.exclusive.effective`.

  * Nếu trước đó có đặt `cpuset.cpus.exclusive`, thì `cpuset.cpus.exclusive.effective` luôn là **tập con** của nó.

> Người dùng có thể tự gán giá trị cho `cpuset.cpus.exclusive`, khác với `cpuset.cpus`.
> Tuy nhiên:

* Các CPU trong danh sách **phải là độc quyền** so với các sibling (cgroup anh em).
* Nếu `cpuset.cpus.exclusive` của sibling không được đặt, thì `cpuset.cpus.exclusive` của cgroup hiện tại **không được là tập con** (để ít nhất một CPU còn lại).
* Nếu vi phạm quy tắc này, việc ghi sẽ bị **từ chối (write error)**.

> Với cgroup cha, \*\*mỗi CPU exclusive chỉ được cấp cho **một cgroup con**.
> Nếu một CPU xuất hiện trong nhiều cgroup con dưới cùng một cha -> **vi phạm luật độc quyền (exclusivity rule)**.

> Cgroup gốc (root) luôn là **partition root**, và toàn bộ CPU khả dụng sẽ nằm trong **exclusive CPU set** của nó.


---

**`cpuset.cpus.exclusive.effective`**

* **Tệp chỉ đọc**, tồn tại trên tất cả các cgroup `cpuset` không phải root.
* Hiển thị **danh sách CPU độc quyền thực sự** có thể dùng để tạo một "partition root".
* Nội dung tệp này luôn là **tập con** của `cpuset.cpus.exclusive.effective` của cgroup cha, nếu cha không phải là `root`.
* Nếu `cpuset.cpus.exclusive` không được thiết lập, nó sẽ được **ngầm hiểu là giá trị `cpuset.cpus`** để tạo local partition.

---

**`cpuset.cpus.isolated`**

* Là **tệp chỉ đọc**, chỉ có trong `root` cgroup.
* Hiển thị **tập hợp các CPU bị cô lập** đang được sử dụng bởi các partition dạng "isolated".
* Nếu không có isolated partition nào tồn tại, tệp này sẽ **rỗng**.

---

**`cpuset.cpus.partition`**

* Là **tệp chỉ đọc-ghi**, nằm trong các cgroup không phải root có hỗ trợ `cpuset`.
* Quyền kiểm soát tệp này thuộc về **cgroup cha**.
* Chỉ chấp nhận các giá trị sau:

| Giá trị    | Mô tả                                                 |
| ---------- | ----------------------------------------------------- |
| `member`   | Không thuộc root partition                            |
| `root`     | Là một root partition                                 |
| `isolated` | Là root partition nhưng **không dùng load balancing** |

---

**Giải thích về Partition**

* Một **partition** là một tập hợp các cgroup hỗ trợ `cpuset`, có một **partition root** ở đỉnh.
* Partition sở hữu một **tập CPU độc quyền**, các cgroup ngoài partition này **không thể sử dụng** bất kỳ CPU nào trong đó.

**Phân loại partition:**

1. **Local Partition:**

   * Cgroup cha cũng là một partition root.
   * Không bắt buộc phải có `cpuset.cpus.exclusive`.

2. **Remote Partition:**

   * Cgroup cha **không phải** là partition root → cần cấu hình chính xác các giá trị `cpuset.cpus.exclusive`.
   * Không được tạo dưới một local partition.

> Nhóm `root` **luôn luôn** là partition root, không thể thay đổi trạng thái của nó. Các cgroup khác ban đầu có trạng thái là `member`.

---

**Ý nghĩa của giá trị partition:**

* `root`: Cgroup này là **gốc của một partition** (có thể lập lịch). CPU độc quyền được xác định bởi `cpuset.cpus.exclusive.effective`.

* `isolated`: Các CPU trong partition này **bị cô lập**, không dùng load balancing.

  * Tác vụ cần được **phân phối chính xác đến từng CPU riêng lẻ**.

> Lưu ý: Partition có thể rơi vào trạng thái **hợp lệ hoặc không hợp lệ**. Nếu không hợp lệ, nó sẽ bị coi như "member" và không thể đảm bảo cách ly tài nguyên như mong muốn.

---

Tất cả các trạng thái có thể chuyển đổi giữa `member`, `root` và `isolated`.

---

**Các giá trị mà tệp `cpuset.cpus.partition` có thể hiển thị:**

| Giá trị                      | Mô tả                                                 |
| ---------------------------- | ----------------------------------------------------- |
| `member`                     | Thành viên không phải root của một partition          |
| `root`                       | Partition root                                        |
| `isolated`                   | Partition root ở chế độ cách ly, không load balancing |
| `root invalid (<lý do>)`     | Partition root không hợp lệ                           |
| `isolated invalid (<lý do>)` | Partition root cách ly không hợp lệ                   |

Nếu một partition root bị đánh dấu là không hợp lệ, chuỗi mô tả lý do sẽ được đưa vào trong ngoặc.

---

**Điều kiện để local partition root hợp lệ:**

1. Cgroup cha phải là một partition root hợp lệ.
2. Tệp `cpuset.cpus.exclusive.effective` không được rỗng (có thể bao gồm cả CPU offline).
3. Tệp `cpuset.cpus.effective` không được rỗng trừ khi partition không có task nào.

---

**Điều kiện để remote partition root hợp lệ:**

* Phải thỏa mãn tất cả các điều kiện như trên **ngoại trừ điều kiện đầu tiên** (cgroup cha không cần là partition root).

---

**Các tình huống và lưu ý:**

* Các sự kiện như hotplug CPU, thay đổi `cpuset.cpus`, hoặc `cpuset.cpus.exclusive` có thể khiến partition trở nên **không hợp lệ** và ngược lại.
* Một task **không thể** được chuyển vào một cgroup có `cpuset.cpus.effective` rỗng.
* Một non-root partition hợp lệ có thể phân phối tất cả CPU của nó cho các local partition con nếu không có task nào đang sử dụng CPU.

---

**Cẩn trọng khi chuyển trạng thái:**

* Nếu một partition root chuyển sang `member`, **tất cả các local partition con của nó** cũng sẽ bị chuyển trạng thái → có thể gây **gián đoạn đến task** đang chạy trong các partition đó.
* Những partition bị vô hiệu hóa có thể được khôi phục nếu cgroup cha được chuyển lại thành partition root hợp lệ và có thiết lập đúng trong `cpuset.cpus` hoặc `cpuset.cpus.exclusive`.

---

**Các sự kiện `poll` và `notify`:**

* Được kích hoạt khi trạng thái của `cpuset.cpus.partition` thay đổi.
* Điều này giúp người dùng có thể **giám sát các thay đổi bất ngờ** mà không cần liên tục truy vấn thủ công.

---

**Ghi chú thêm:**

* Người dùng có thể định cấu hình một số CPU ở chế độ cô lập từ lúc khởi động bằng tùy chọn dòng lệnh `isolcpus`.
* Nếu muốn đưa các CPU đó vào một partition thì **bắt buộc phải là partition dạng isolated**.

---

### Trình điều khiển thiết bị (Device controller)

Trình điều khiển thiết bị quản lý quyền truy cập đến các tập tin thiết bị. Nó bao gồm cả việc tạo mới tập tin thiết bị (dùng lệnh `mknod`) và quyền truy cập đến các tập tin thiết bị hiện có.

Trình điều khiển thiết bị trong cgroup v2 không có tệp giao diện riêng và được triển khai dựa trên **cgroup BPF**.
Để kiểm soát quyền truy cập đến các tập tin thiết bị, người dùng có thể tạo các chương trình BPF với kiểu `BPF_PROG_TYPE_CGROUP_DEVICE` và gắn chúng vào cgroup với cờ `BPF_CGROUP_DEVICE`.

Khi có một yêu cầu truy cập đến tập tin thiết bị, chương trình BPF tương ứng sẽ được thực thi. Tùy thuộc vào giá trị trả về, thao tác sẽ được cho phép hoặc bị từ chối với lỗi `EPERM`.

---

Một chương trình `BPF_PROG_TYPE_CGROUP_DEVICE` nhận một con trỏ đến cấu trúc `bpf_cgroup_dev_ctx`, mô tả thông tin về yêu cầu truy cập thiết bị, bao gồm:

* **Loại thao tác truy cập**: `mknod` / `read` / `write`
* **Thiết bị**: (loại, số major, số minor)

Nếu chương trình trả về 0 → thao tác bị từ chối với lỗi `-EPERM`.
Nếu không, thao tác được chấp nhận.

---

Ví dụ về chương trình `BPF_PROG_TYPE_CGROUP_DEVICE` có thể được tìm thấy trong file:

```
tools/testing/selftests/bpf/progs/dev_cgroup.c
```

trong cây mã nguồn của nhân Linux.

---

## 14. RDMA

Bộ điều khiển “rdma” điều phối việc phân phối và kiểm soát tài nguyên RDMA.

---

### Các tập tin giao diện RDMA

**`rdma.max`**

Một tập tin có thể đọc-ghi theo định dạng key lồng nhau, tồn tại với tất cả các cgroup (trừ root), mô tả giới hạn tài nguyên RDMA/IB hiện đang được cấu hình cho một thiết bị.

* Các dòng trong file được phân theo tên thiết bị và không theo thứ tự.
* Mỗi dòng chứa các tên tài nguyên cách nhau bằng dấu cách và giới hạn cấu hình tương ứng có thể được phân phối.

**Các khóa lồng nhau được định nghĩa như sau:**

| Khóa         | Mô tả                           |
| ------------ | ------------------------------- |
| `hca_handle` | Số lượng tối đa của HCA Handles |
| `hca_object` | Số lượng tối đa của HCA Objects |

**Ví dụ cho thiết bị `mlx4` và `ocrdma` như sau:**

```
mlx4 0 hca_handle=2 hca_object=2000
ocrdma1 hca_handle=3 hca_object=max
```

---

**`rdma.current`**

Một tập tin chỉ đọc mô tả việc sử dụng tài nguyên hiện tại. Nó tồn tại với tất cả các cgroup trừ root.

**Ví dụ cho thiết bị `mlx4` và `ocrdma`:**

```
mlx4 0 hca_handle=1 hca_object=20
ocrdma1 hca_handle=1 hca_object=23
```

---

## 15. DMEM

Bộ điều khiển “dmem” quản lý việc phân phối và ghi nhận bộ nhớ thiết bị (device memory) theo vùng. Vì mỗi vùng bộ nhớ có thể có kích thước trang riêng (page size), không nhất thiết phải trùng với kích thước trang hệ thống, nên đơn vị đo luôn là **byte**.

---

### Các tập tin giao diện DMEM

**`dmem.max`, `dmem.min`, `dmem.low`**

Là một tập tin có thể ghi theo định dạng key lồng nhau, tồn tại trong tất cả các cgroup (trừ root), dùng để mô tả giới hạn tài nguyên hiện được cấu hình cho một vùng bộ nhớ.

**Ví dụ cho thiết bị `xe`:**

```
drm/0000:03:00.0/vram0 1073741824
drm/0000:03:00.0/stolen max
```

> Ý nghĩa tương tự như với bộ điều khiển bộ nhớ (`memory cgroup controller`), và được tính toán theo cùng cách.

---

**`dmem.capacity`**

Một tập tin chỉ đọc mô tả dung lượng tối đa của vùng bộ nhớ. Nó **chỉ tồn tại ở cgroup gốc (root)**. Không phải toàn bộ bộ nhớ đều có thể được phân bổ cho các cgroup vì kernel giữ lại một phần để sử dụng nội bộ.

**Ví dụ cho thiết bị `xe`:**

```
drm/0000:03:00.0/vram0 8514437120
drm/0000:03:00.0/stolen 67108864
```

---

**`dmem.current`**

Một tập tin chỉ đọc mô tả mức sử dụng tài nguyên hiện tại. Nó tồn tại với tất cả các cgroup (trừ root).

**Ví dụ cho thiết bị `xe`:**

```
drm/0000:03:00.0/vram0 12550144
drm/0000:03:00.0/stolen 8650752
```
---

## 16. HugeTLB

Bộ điều khiển HugeTLB cho phép giới hạn mức sử dụng HugeTLB theo từng nhóm điều khiển (control group - cgroup) và áp dụng giới hạn của bộ điều khiển trong quá trình xử lý lỗi trang bộ nhớ (page fault).

---

### Các tệp giao diện HugeTLB

**`hugetlb.<kích_thước_trang>.current`**

Hiển thị mức sử dụng hiện tại của HugeTLB với kích thước trang `<hugepagesize>`. Tồn tại cho tất cả cgroup, ngoại trừ cgroup gốc.

---

**`hugetlb.<kích_thước_trang>.max`**

Thiết lập/hiển thị giới hạn trên cho việc sử dụng HugeTLB với kích thước trang `<hugepagesize>`. Giá trị mặc định là `max`. Tồn tại cho tất cả cgroup trừ cgroup gốc.

---

**`hugetlb.<kích_thước_trang>.events`**

Tệp chỉ đọc, kiểu dữ liệu phẳng, tồn tại trên các cgroup không phải root.

* **max** – Số lần thất bại khi cấp phát do vượt giới hạn HugeTLB.

---

**`hugetlb.<kích_thước_trang>.events.local`**

Tương tự như `hugetlb.<kích_thước_trang>.events`, nhưng các trường trong tệp này chỉ áp dụng cục bộ cho cgroup (không phân cấp). Sự kiện được ghi trong tệp này chỉ phản ánh những sự kiện nội bộ của chính cgroup đó.

---

**`hugetlb.<kích_thước_trang>.numa_stat`**

Tương tự như `memory.numa_stat`, tệp này hiển thị thông tin NUMA liên quan đến các trang HugeTLB có kích thước `<hugepagesize>` trong cgroup hiện tại. Chỉ các trang HugeTLB đang hoạt động mới được ghi nhận. Các giá trị theo từng node được tính bằng byte.

---

## 17. Misc (Hỗn hợp)

Nhóm điều khiển Miscellaneous (cgroup hỗn hợp) cung cấp cơ chế giới hạn và theo dõi tài nguyên cho các tài nguyên vô hướng (scalar resources) mà không thể trừu tượng hóa như các tài nguyên cgroup khác. Bộ điều khiển này được kích hoạt thông qua tùy chọn cấu hình `CONFIG_CGROUP_MISC`.

Một tài nguyên có thể được thêm vào bộ điều khiển thông qua `enum misc_res_type{}` trong file `include/linux/misc_cgroup.h`, và tên tương ứng qua `misc_res_name[]` trong file `kernel/cgroup/misc.c`. Bên cung cấp tài nguyên phải thiết lập dung lượng (capacity) trước khi sử dụng tài nguyên bằng cách gọi hàm `misc_cg_set_capacity()`.

Khi dung lượng đã được thiết lập, việc sử dụng tài nguyên có thể được cập nhật bằng các API `charge` và `uncharge`. Tất cả các API tương tác với bộ điều khiển misc được định nghĩa trong `include/linux/misc_cgroup.h`.

---

### Các tệp giao diện của bộ điều khiển Misc

Bộ điều khiển Miscellaneous cung cấp 3 tệp giao diện. Nếu hai tài nguyên `misc` (ví dụ: `res_a` và `res_b`) được đăng ký thì:

---

**`misc.capacity`**

* Tệp chỉ đọc, định dạng phẳng (flat-keyed), chỉ tồn tại trong `root cgroup`.
* Hiển thị các tài nguyên vô hướng loại misc hiện có trên hệ thống cùng với số lượng của chúng.

Ví dụ:

```
$ cat misc.capacity
res_a 50
res_b 10
```

---

**`misc.current`**

* Tệp chỉ đọc, định dạng phẳng.
* Tồn tại trong tất cả các cgroup.
* Hiển thị mức sử dụng hiện tại của tài nguyên trong cgroup và các cgroup con của nó.

Ví dụ:

```
$ cat misc.current
res_a 3
res_b 0
```

---

**`misc.peak`**

* Tệp chỉ đọc, định dạng phẳng.
* Tồn tại trong tất cả các cgroup.
* Hiển thị mức sử dụng tài nguyên cao nhất trong lịch sử của cgroup và các cgroup con.

Ví dụ:

```
$ cat misc.peak
res_a 10
res_b 8
```

---

**`misc.max`**

* Tệp đọc-ghi, định dạng phẳng.
* Tồn tại trong các `non-root cgroup`.
* Xác định mức sử dụng tối đa cho phép của tài nguyên trong cgroup và các cgroup con.

Ví dụ:

```
$ cat misc.max
res_a max
res_b 4
```

**Cài đặt giới hạn:**

```bash
# echo res_a 1 > misc.max
```

**Cài đặt giới hạn ở mức tối đa (`max`):**

```bash
# echo res_a max > misc.max
```

> *Lưu ý:* Giới hạn có thể được đặt cao hơn giá trị `capacity` trong tệp `misc.capacity`.

---

**`misc.events`**

* Tệp chỉ đọc, định dạng phẳng.
* Tồn tại trong các `non-root cgroup`.
* Hiển thị các sự kiện liên quan đến việc sử dụng tài nguyên vượt ngưỡng giới hạn `max`.

Trường hợp được định nghĩa:

* `max`: số lần việc sử dụng tài nguyên trong cgroup suýt vượt quá giới hạn `max`.

---

**`misc.events.local`**

* Tương tự `misc.events` nhưng chỉ phản ánh các sự kiện cục bộ của cgroup hiện tại (không theo cấu trúc phân cấp).

---

**Di chuyển và Quyền sở hữu**

Một tài nguyên vô hướng loại Misc (miscellaneous scalar resource) sẽ được tính cho cgroup đầu tiên sử dụng nó, và vẫn được tính cho cgroup đó cho đến khi tài nguyên được giải phóng. Việc di chuyển một tiến trình sang cgroup khác **không** chuyển kèm theo phần tài nguyên đã bị tính; tài nguyên vẫn tính vào cgroup ban đầu nơi tiến trình đã sử dụng nó.

---

### **Khác**

**`perf_event`**

Bộ điều khiển `perf_event`, nếu không được gắn trên hệ thống phân cấp cũ (legacy hierarchy), thì sẽ tự động được bật trên hệ thống phân cấp `cgroup v2`, do đó các sự kiện `perf` luôn có thể được lọc bằng đường dẫn `cgroup v2`. Bộ điều khiển này vẫn có thể được chuyển sang hệ thống phân cấp cũ sau khi `v2 hierarchy` đã được thiết lập đầy đủ.

---

**Thông tin không mang tính chuẩn hóa**

Mục này chứa thông tin **không được xem là một phần của API kernel ổn định**, do đó có thể thay đổi.

---

**Hành vi của bộ điều khiển CPU trong root cgroup**

Khi phân phối chu kỳ CPU trong `root cgroup`, mỗi luồng trong `cgroup` này sẽ được xử lý như thể nó đang chạy trong một `cgroup con riêng biệt` của `root cgroup`. Trọng số (weight) của `cgroup con này` phụ thuộc vào mức độ `nice` của luồng đó.

> Chi tiết về cách ánh xạ `nice` → `trọng số` có thể được tìm thấy trong mảng `sched_prio_to_weight` trong tệp `kernel/sched/core.c`. Các giá trị từ mảng này sẽ được điều chỉnh tỷ lệ, với giá trị trung lập (nice = 0) tương ứng với trọng số 100 (trong hệ 1024).

---

**Hành vi của tiến trình trong IO root cgroup**

Tiến trình trong `root cgroup` sẽ được đặt vào một `nút con ảo` (implicit leaf child node). Khi phân phối tài nguyên IO, `nút con ảo` này sẽ được tính như một `cgroup con bình thường` của `root cgroup`, với trọng số IO là **200**.

---

## 18. **Namespace**

### **Cơ bản**

**Namespace của cgroup** cung cấp một cơ chế để ảo hóa cái nhìn của file `/proc/SPID/cgroup` và việc mount cgroup. Cờ `CLONE_NEWCGROUP` có thể được sử dụng với các lệnh `clone(2)` và `unshare(2)` để tạo ra một namespace cgroup mới. Các tiến trình chạy bên trong namespace cgroup sẽ có đầu ra `/proc/SPID/cgroup` bị giới hạn chỉ hiển thị tới gốc của cgroups tại thời điểm tạo namespace.

---

**Không có namespace cgroup**, file `/proc/SPID/cgroup` sẽ hiển thị đầy đủ đường dẫn cgroup của tiến trình. Trong các thiết lập container, khi muốn cô lập tiến trình khỏi thông tin hệ thống cấp cao, việc hiển thị toàn bộ đường dẫn này có thể làm rò rỉ thông tin. Ví dụ:

```sh
# cat /proc/self/cgroup
0::/batchjobs/container_id1
```

Đường dẫn `/batchjobs/container_id1` có thể được xem là dữ liệu hệ thống và không mong muốn hiển thị cho tiến trình bị cô lập. Do đó, có thể sử dụng namespace cgroup để **ẩn** đường dẫn này.

Ví dụ, trước khi tạo namespace cgroup, người dùng sẽ thấy:

```sh
# ls -l /proc/self/ns/cgroup
lrwxrwxrwx 1 root root 0 2014-07-15 10:37 /proc/self/ns/cgroup -> cgroup:[4026531835]

# cat /proc/self/cgroup
0::/batchjobs/container_id1
```

Sau khi tách (unshare) một namespace mới, cái nhìn sẽ thay đổi:

```sh
# ls -l /proc/self/ns/cgroup
lrwxrwxrwx 1 root root 0 2014-07-15 10:35 /proc/self/ns/cgroup -> cgroup:[4026532183]

# cat /proc/self/cgroup
0::/
```

---

Khi một luồng trong tiến trình nhiều luồng tách namespace cgroup, thì namespace mới sẽ được áp dụng cho toàn bộ tiến trình (bao gồm tất cả luồng). Điều này là mặc định với cgroup v2; với các phiên bản cũ hơn thì hành vi có thể khác.

Một namespace cgroup tồn tại **chừng nào còn có tiến trình bên trong** hoặc còn **mount giữ** nó. Khi không còn tiến trình hay mount nào sử dụng, namespace sẽ tự động bị hủy. Gốc của cgroup và các vùng bộ nhớ thực tế cũng bị xóa theo.

---

### **Gốc và Cách Nhìn (The Root and Views)**

**‘Gốc của cgroups’** đối với một namespace cgroup là cgroup tại thời điểm tiến trình gọi `unshare(2)` đang chạy. Ví dụ, nếu một tiến trình trong cgroup `/batchjobs/container_id1` gọi `unshare`, thì `/batchjobs/container_id1` sẽ trở thành gốc của cgroups. Đối với `init_cgroup_ns`, đây là gốc thực sự (`/`) của hệ thống.

**Gốc của cgroups sẽ không thay đổi**, ngay cả khi tiến trình tạo namespace sau đó di chuyển sang cgroup khác:

```sh
# ~ /unshare -c # unshare cgroups trong một cgroup nào đó
# cat /proc/self/cgroup
0::/

# mkdir sub_cgrp_1
# echo 0 > sub_cgrp_1/cgroup.procs
# cat /proc/self/cgroup
0::/sub_cgrp_1
```

---

**Mỗi tiến trình sẽ có cái nhìn riêng biệt** trong namespace của nó thông qua file `/proc/SPID/cgroup`.

Các tiến trình chạy bên trong namespace cgroup sẽ **chỉ thấy các đường dẫn cgroup bên trong gốc cgroup của chúng**, thông qua `/proc/self/cgroup`.

Từ một namespace cgroup đã unshare:

```sh
# sleep 100000 &
[1] 7353

# echo 7353 > sub_cgrp_1/cgroup.procs
# cat /proc/7353/cgroup
0::/sub_cgrp_1
```

---

**Từ namespace gốc ban đầu**, đường dẫn cgroup thực sự của tiến trình sẽ hiển thị như sau:

```sh
# cat /proc/7353/cgroup
0::/batchjobs/container_id1/sub_cgrp_1
```

Từ một namespace khác (tức là một namespace được root tại cgroup khác), đường dẫn cgroup sẽ được hiển thị tương đối so với root namespace của nó. Ví dụ, nếu namespace của PID 7353 có gốc tại `/batchjobs/container_id2`, thì nó sẽ thấy:

```sh
# cat /proc/7353/cgroup
0::/../container_id2/sub_cgrp_1
```

**Lưu ý**: Đường dẫn tương đối luôn bắt đầu với `/` để biểu thị rằng nó là **tương đối so với root namespace của cgroup của người gọi**.

---

### **Di chuyển và setns(2)**

Các tiến trình bên trong một namespace cgroup có thể di chuyển vào hoặc ra khỏi gốc namespace nếu chúng có quyền truy cập hợp lệ vào cgroups bên ngoài. Ví dụ: từ bên trong một namespace có gốc cgroups tại `/batchjobs/container_id1`, và giả sử rằng toàn bộ hệ phân cấp toàn cục vẫn có thể truy cập được từ bên trong cgroups:

```sh
# cat /proc/7353/cgroup
0::/sub_cgrp_1

# echo 7353 > batchjobs/container_id2/cgroup.procs

# cat /proc/7353/cgroup
0::/../container_id2
```

**Lưu ý**: Cách cấu hình như trên **không được khuyến khích**. Một tác vụ bên trong namespace cgroup chỉ nên được phơi bày với hệ phân cấp cgroups riêng của nó.

Việc gọi `setns(2)` tới một namespace cgroup khác chỉ được phép khi:

a. Tiến trình có quyền **CAP\_SYS\_ADMIN** đối với namespace người dùng hiện tại của nó
b. Tiến trình có quyền **CAP\_SYS\_ADMIN** đối với namespace người dùng của namespace cgroup đích

Không có thay đổi cgroup ngầm định nào xảy ra khi gắn với namespace cgroup khác. Cần phải chắc chắn rằng tiến trình được gắn phải được di chuyển rõ ràng đến gốc namespace cgroup đích.

---

### **Tương tác với Các Namespace Khác**

Một hệ phân cấp cgroup cụ thể của namespace có thể được mount bởi một tiến trình đang chạy bên trong một namespace cgroup không phải init:

```sh
# mount -t cgroup2 none $MOUNT_POINT
```

Lệnh này sẽ mount toàn bộ hệ phân cấp cgroup thống nhất với gốc cgroups là gốc của hệ thống tập tin. Tiến trình cần có quyền **CAP\_SYS\_ADMIN** đối với cả namespace người dùng và namespace mount.

Việc kết hợp giữa việc ảo hóa `/proc/self/cgroup` và giới hạn việc xem hệ phân cấp cgroup bằng namespace riêng tư cung cấp cái nhìn cách ly đúng đắn về cgroup cho tiến trình bên trong container.

---

## 19. **Thông tin về Lập trình nhân Linux (Kernel Programming)**

Phần này chứa thông tin lập trình nhân trong các lĩnh vực có liên quan đến cgroup. Không bao gồm lõi cgroup và các bộ điều khiển.

---

### **Hỗ trợ hệ thống tập tin cho Writeback**

Một hệ thống tập tin có thể hỗ trợ writeback (ghi dữ liệu lại từ bộ nhớ đệm xuống ổ đĩa) thông qua cập nhật `address_space_operations->writepages()` để chú thích các `bio` bằng cách sử dụng hai hàm sau:

#### `wbc_init_bio(@wbc, @bio)`

* Nên được gọi cho mỗi `bio` mang dữ liệu writeback và liên kết `bio` với `cgroup` của inode sở hữu và hàng đợi yêu cầu tương ứng.
* Phải được gọi sau khi một hàng đợi (thiết bị) đã được liên kết với `bio` và trước khi gửi đi.

#### `wbc_account_cgroup_owner(@wbc, @folio, @bytes)`

* Nên được gọi cho mỗi phân đoạn dữ liệu đang được ghi.
* Mặc dù hàm này không quan tâm được gọi chính xác vào lúc nào trong quá trình writeback, nhưng cách dễ nhất và tự nhiên nhất là gọi nó khi phân đoạn dữ liệu được thêm vào `bio`.

Với các `bio` đã được chú thích, hỗ trợ cgroup có thể được bật trên từng `super_block` bằng cách thiết lập `SB_I_CGROUPWB` trong `s_iflags`.

* Điều này cho phép bật/tắt hỗ trợ writeback của cgroup một cách linh hoạt, đặc biệt hữu ích khi một số tính năng hệ thống tập tin (ví dụ như chế độ dữ liệu dạng nhật ký) không tương thích.

`wbc_init_bio()` gắn `bio` được chỉ định với `cgroup` tương ứng.

* Tùy thuộc vào cấu hình, `bio` có thể được thực thi ở mức ưu tiên thấp hơn, và nếu phiên writeback giữ tài nguyên chia sẻ (ví dụ: mục nhập nhật ký), có thể dẫn đến **nghịch đảo ưu tiên** (priority inversion).
* Không có giải pháp dễ dàng nào cho vấn đề này. Các hệ thống tập tin có thể cố gắng xử lý từng trường hợp cụ thể bằng cách **bỏ qua** `wbc_init_bio()` và sử dụng trực tiếp `bio_associate_blkg()`.

---

### **Tính năng lỗi thời của cgroup v1**

* Không hỗ trợ **nhiều hệ phân cấp**, bao gồm cả các hệ phân cấp có tên.
* Không hỗ trợ tất cả các tuỳ chọn **mount** trong v1.
* **Tập tin “tasks” bị xóa**, và “cgroup.procs” không còn được sắp xếp.
* `cgroup.clone_children` đã bị loại bỏ.
* `/proc/cgroups` không còn ý nghĩa trong v2. Sử dụng “cgroup.controllers” hoặc các tệp “cgroup.stat” ở gốc thay thế.

---

## 20. **Vấn đề với cgroup v1 và lý do ra đời cgroup v2**

### **1. Nhiều hệ phân cấp (Multiple Hierarchies)**

Cgroup v1 cho phép tạo số lượng hệ phân cấp tùy ý và mỗi hệ có thể chứa nhiều controller. Mặc dù điều này có vẻ linh hoạt, nhưng thực tế lại không hiệu quả.

Ví dụ, vì mỗi controller chỉ có một bản thể, các controller kiểu tiện ích như `freezer` chỉ có thể dùng trong một hệ, dù có thể hữu ích ở tất cả. Ngoài ra, một khi các hệ phân cấp đã được khởi tạo, controller không thể chuyển sang hệ khác. Thêm vào đó, tất cả các controller trong cùng một hệ bị ép buộc phải có cùng một cấu trúc phân cấp — không thể điều chỉnh độ chi tiết riêng cho từng controller.

Trong thực tế, điều này giới hạn khả năng đặt nhiều controller trên cùng một hệ. Phần lớn cấu hình đều phải đặt mỗi controller vào một hệ riêng. Chỉ những controller có quan hệ chặt như `cpu` và `cpuacct` mới có thể chia sẻ hệ phân cấp. Điều này khiến userland phải quản lý nhiều hệ tương tự, lặp đi lặp lại thao tác mỗi khi cần quản lý hệ phân cấp.

Ngoài ra, việc hỗ trợ nhiều hệ làm cho cgroup core rất phức tạp, và quan trọng hơn là giới hạn khả năng sử dụng cgroup và các chức năng controller có thể thực hiện.

Không có giới hạn số lượng hệ, dẫn đến việc tư cách thành viên cgroup của một luồng không thể mô tả trong độ dài cố định — khóa xác định có thể rất dài. Điều này gây khó khăn khi thao tác, dẫn đến việc thêm controller chỉ để xác định tư cách thành viên, lại càng làm bùng phát số hệ phân cấp.

Hơn nữa, vì một controller không thể giả định gì về cấu trúc hệ phân cấp mà các controller khác dùng, nên mỗi controller phải xử lý như thể các controller khác hoàn toàn tách biệt — khiến việc phối hợp giữa chúng gần như không khả thi.

Thông thường, không cần phải đặt các controller vào các hệ hoàn toàn riêng biệt. Thực tế, cần khả năng áp dụng các mức độ chi tiết khác nhau tùy vào controller. Ví dụ, có thể không cần kiểm soát bộ nhớ chi tiết ở sâu, nhưng lại muốn kiểm soát phân phối CPU.

---

### **2. Độ chi tiết theo luồng (Thread Granularity)**

Cgroup v1 cho phép các luồng (threads) trong cùng một tiến trình thuộc về các cgroup khác nhau. Điều này không phù hợp với một số controller, dẫn đến việc mỗi controller phải tự xử lý tình huống này theo cách riêng.

Về mặt nguyên tắc, chỉ tiến trình mới biết được trạng thái của các luồng bên trong nó. Do đó, việc phân loại luồng yêu cầu sự tham gia chủ động từ chính ứng dụng sở hữu tiến trình.

Cgroup v1 có mô hình ủy quyền mơ hồ, dễ bị lạm dụng khi kết hợp với cơ chế theo luồng. Cgroup có thể được ủy quyền cho ứng dụng để chúng tự tạo và quản lý hệ con — biến cgroup thành một API kiểu như syscall lộ diện tới chương trình thường.

Tuy nhiên, cgroup không có giao diện phù hợp để sử dụng như vậy. Để thao tác với các `knob` (điều khiển), tiến trình phải lấy đường dẫn từ `/proc/self/cgroup`, ghép nối với tên knob, rồi mở và đọc/ghi — điều này không chỉ rườm rà, mà còn dễ bị điều kiện tranh chấp (race condition).

Nhiều `knob` được triển khai không có quy ước hoặc trừu tượng rõ ràng, tiết lộ chi tiết nội bộ kernel — và bị lạm dụng như cách tạo API công cộng không kiểm duyệt.

Việc này gây rắc rối cho cả userland và kernel — userland có giao diện kém ổn định, còn kernel thì vô tình bị ràng buộc bởi các chi tiết không đáng có.

---

### **3. Cạnh tranh giữa các node cha và luồng (Competition Between Inner Nodes and Threads)**

Cgroup v1 cho phép threads tồn tại ở bất kỳ cấp nào, dẫn đến việc threads ở cgroup cha và con cạnh tranh tài nguyên — đây là mâu thuẫn loại hình và không có cách rõ ràng để xử lý. Các controller khác nhau lại chọn cách xử lý khác nhau.

Ví dụ:

* `cpu` controller coi thread và cgroup như nhau, ánh xạ `nice level` thành trọng số (weight). Cách này thất bại khi các cgroup con yêu cầu tỷ lệ tài nguyên cụ thể, nhưng số thread thay đổi liên tục — khiến phân bổ không ổn định.
* `io` controller tạo một leaf node ẩn để chứa threads, với các `knob` riêng có tiền tố `leaf_`. Cách này gây phức tạp hóa cấu trúc và làm rối giao diện.
* `memory` controller không có cơ chế kiểm soát tương tác giữa tasks nội bộ và cgroup con, dẫn đến hành vi không xác định. Những nỗ lực sửa bằng các `knob` tạm thời khiến hệ thống ngày càng khó duy trì.

Tóm lại, việc xử lý tasks nội bộ là vấn đề phổ biến và cần giải quyết một cách thống nhất trong cgroup core.

---

### **4. Các vấn đề giao diện khác (Other Interface Issues)**

Cgroup v1 phát triển thiếu kiểm soát, dẫn đến nhiều bất nhất và sự khác biệt kỳ quặc.

Ví dụ:

* Khi cgroup trống, một chương trình helper được fork để xử lý sự kiện — không có đệ quy, không thể ủy quyền.
* Một số controller bỏ qua hệ thống phân cấp, coi tất cả cgroup là con trực tiếp của root.
* Không có sự nhất quán khi tạo cgroup mới: một số controller cho phép sử dụng tài nguyên ngay, số khác thì không.
* Cách đặt tên, định dạng của `knob` rất khác nhau, thậm chí ngay trong cùng một controller.

Cgroup v2 đặt ra các quy ước chung và cập nhật các controller để cung cấp giao diện đơn giản và nhất quán.

---

### **5. Các vấn đề của controller và hướng khắc phục (Controller Issues and Remedies)**

#### **Memory Controller**

**Vấn đề với giới hạn mềm (soft limit):**

* `soft limit` mặc định là chưa đặt → reclaim ưu tiên nhóm opt-in → kiểm tra rất tốn kém.
* Không có tính phân cấp — tất cả nhóm vào chung một cây RB, không thể phân quyền.
* Thuật toán reclaim quá tích cực → tăng độ trễ cấp phát → giảm hiệu năng.

**Cgroup v2: `memory.low`**

* Là một mức bảo lưu từ trên xuống.
* Khi usage dưới mức này → được bảo vệ khỏi reclaim.
* Khi vượt mức này → chịu reclaim tương ứng với phần vượt.

**Vấn đề với giới hạn cứng (hard limit - memory.limit\_in\_bytes)**

* Là ràng buộc tuyệt đối → dễ gây OOM nếu đoán sai working set.
* Không thể giảm giới hạn khi usage đang cao do điều kiện tranh chấp.

**Cgroup v2: `memory.high` và `memory.max`**

* `memory.high`: khi vượt → buộc reclaim nhưng không OOM → có thể hiệu chỉnh hiệu suất dần.
* `memory.max`: để giới hạn tràn, ngăn chặn ứng dụng lỗi hoặc độc hại.

**Swap**

* Cgroup v2 phân tách rõ ràng memory và swap thay vì dùng chung một bộ đếm như v1.

---
