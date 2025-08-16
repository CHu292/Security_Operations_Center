## Table of Contents

1. [Introduction](#1-introduction)

1.1. [Linux Structure](#11-linux-structure)

1.2. [Linux Distributions](#12-linux-distributions)

1.3. [Introduction to Shell](#13-introduction-to-shell)

---

2. [The Shell](#2-the-shell)

2.1. [Prompt Description](#21-prompt-description)

2.2. [Getting Help](#22-getting-help)

2.3. [System Information](#23-system-information)

---

3. [Workflow](#3-workflow)

3.1 [Navigation](#31-navigation)


# 1. Introduction
## 1.1. Linux Structure
**Cấu trúc Linux**


Linux, như bạn có thể đã biết, là một hệ điều hành được sử dụng cho máy tính cá nhân, máy chủ, và thậm chí cả thiết bị di động. Tuy nhiên, Linux đóng vai trò như một trụ cột nền tảng trong an ninh mạng, nổi tiếng với độ ổn định, tính linh hoạt và mã nguồn mở. Trong phần này, chúng ta sẽ tìm hiểu về cấu trúc Linux, lịch sử, triết lý, kiến trúc, và hệ thống phân cấp tệp — những kiến thức thiết yếu đối với bất kỳ chuyên gia an ninh mạng nào. Bạn có thể coi đây như buổi học lái xe đầu tiên với một chiếc xe mới, để hiểu cơ bản về phương tiện, nó gồm những gì, và tại sao nó lại có hình thức như hiện tại.

Trước tiên, hãy định nghĩa Linux là gì. Linux là một hệ điều hành, giống như Windows, macOS, iOS hoặc Android. Hệ điều hành (OS) là phần mềm quản lý tất cả tài nguyên phần cứng của máy tính, giúp giao tiếp giữa các ứng dụng phần mềm và các thành phần phần cứng. Không giống như một số hệ điều hành khác, Linux có nhiều bản phân phối khác nhau — thường được gọi là “distros” — là các phiên bản Linux được tùy chỉnh để phù hợp với nhiều nhu cầu và sở thích khác nhau.

### Lịch sử

Nhiều sự kiện đã dẫn đến việc tạo ra nhân Linux đầu tiên và cuối cùng là hệ điều hành (OS) Linux, bắt đầu từ việc phát hành hệ điều hành Unix bởi Ken Thompson và Dennis Ritchie (cả hai đều làm việc cho AT\&T vào thời điểm đó) vào năm 1970. Berkeley Software Distribution (BSD) được phát hành năm 1977, nhưng do chứa mã nguồn Unix thuộc sở hữu của AT\&T nên một vụ kiện đã hạn chế sự phát triển của BSD. Richard Stallman bắt đầu dự án GNU vào năm 1983 với mục tiêu tạo ra một hệ điều hành miễn phí giống Unix, và một phần công việc của ông dẫn đến việc tạo ra Giấy phép Công cộng GNU (GPL). Các dự án khác trong những năm sau đó đã thất bại trong việc tạo ra một nhân hệ điều hành miễn phí, hoạt động, được chấp nhận rộng rãi cho đến khi nhân Linux ra đời.

Ban đầu, Linux là một dự án cá nhân được bắt đầu vào năm 1991 bởi một sinh viên người Phần Lan tên là Linus Torvalds. Mục tiêu của ông là tạo ra một nhân hệ điều hành mới, miễn phí. Qua nhiều năm, nhân Linux đã phát triển từ một số ít tệp viết bằng C dưới giấy phép cấm phân phối thương mại thành phiên bản mới nhất với hơn 23 triệu dòng mã nguồn (không tính chú thích), được cấp phép theo GNU General Public License v2.

Linux có hơn 600 bản phân phối (hoặc hệ điều hành dựa trên nhân Linux và phần mềm, thư viện hỗ trợ). Một số bản phổ biến và nổi tiếng nhất bao gồm Ubuntu, Debian, Fedora, OpenSUSE, elementary, Manjaro, Gentoo Linux, RedHat và Linux Mint.

Linux thường được coi là an toàn hơn so với các hệ điều hành khác, và mặc dù trước đây đã từng có nhiều lỗ hổng nhân, nhưng điều này ngày càng hiếm gặp. Linux ít bị tấn công bởi phần mềm độc hại hơn so với Windows và thường xuyên được cập nhật. Linux cũng rất ổn định và thường mang lại hiệu suất rất cao cho người dùng cuối. Tuy nhiên, nó có thể khó sử dụng hơn cho người mới bắt đầu và không có nhiều trình điều khiển phần cứng như Windows.

Vì Linux miễn phí và mã nguồn mở, mã nguồn có thể được chỉnh sửa và phân phối thương mại hoặc phi thương mại bởi bất kỳ ai. Các hệ điều hành dựa trên Linux chạy trên máy chủ, máy tính lớn, máy tính để bàn, hệ thống nhúng như bộ định tuyến, TV, máy chơi game và hơn thế nữa. Hệ điều hành Android tổng thể chạy trên điện thoại thông minh và máy tính bảng được xây dựng trên nhân Linux, và vì lý do này, Linux là hệ điều hành được cài đặt rộng rãi nhất.

Linux là một hệ điều hành giống như Windows, iOS, Android hoặc macOS. Hệ điều hành là phần mềm quản lý tất cả tài nguyên phần cứng liên quan đến máy tính của chúng ta, đồng thời quản lý toàn bộ giao tiếp giữa phần mềm và phần cứng. Ngoài ra, còn có nhiều bản phân phối (distro) khác nhau, tương tự như các phiên bản của Windows.

Với các bài thực hành tương tác, chúng ta sẽ truy cập vào Pwnbox, một phiên bản tùy chỉnh của Parrot OS. Đây sẽ là hệ điều hành chính mà chúng ta sẽ làm việc xuyên suốt các mô-đun. Parrot OS là một bản phân phối Linux dựa trên Debian, tập trung vào bảo mật, quyền riêng tư và phát triển.

Hãy tưởng tượng Linux như một công ty thịnh vượng, nơi các bộ phận của nó là những nhân viên tận tụy, mỗi người đảm nhận các vai trò và trách nhiệm cụ thể để duy trì hoạt động trơn tru. Kiến trúc đóng vai trò như cơ cấu tổ chức, phác thảo cách các nhân viên này được sắp xếp thành các phòng ban và cách họ giao tiếp để đạt hiệu quả và năng suất. Triết lý đại diện cho văn hóa và giá trị cốt lõi của công ty, hướng dẫn cách nhân viên làm việc cá nhân và hợp tác, thúc đẩy các nguyên tắc như đơn giản, minh bạch và hợp tác để đạt được mục tiêu chung.

---

### Triết lý

Triết lý của Linux tập trung vào sự đơn giản, tính mô-đun và tính mở. Nó khuyến khích việc xây dựng các chương trình nhỏ, chuyên biệt để thực hiện một nhiệm vụ duy nhất một cách tốt nhất. Các chương trình này có thể được kết hợp theo nhiều cách để thực hiện các thao tác phức tạp, thúc đẩy hiệu quả và tính linh hoạt. Linux tuân theo năm nguyên tắc cốt lõi sau:

| Nguyên tắc                                                                                                                          | Mô tả                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Everything is a file** (Mọi thứ đều là tệp)                                                                                       | Tất cả các tệp cấu hình cho các dịch vụ khác nhau đang chạy trên hệ điều hành Linux đều được lưu trữ trong một hoặc nhiều tệp văn bản.                              |
| **Small, single-purpose programs** (Chương trình nhỏ, chuyên biệt)                                                                  | Linux cung cấp nhiều công cụ khác nhau mà chúng ta sẽ làm việc cùng, có thể kết hợp để hoạt động chung.                                                             |
| **Ability to chain programs together to perform complex tasks** (Khả năng liên kết các chương trình để thực hiện nhiệm vụ phức tạp) | Việc tích hợp và kết hợp các công cụ khác nhau cho phép chúng ta thực hiện nhiều nhiệm vụ lớn và phức tạp, chẳng hạn như xử lý hoặc lọc các kết quả dữ liệu cụ thể. |
| **Avoid captive user interfaces** (Tránh giao diện người dùng bị giới hạn)                                                          | Linux được thiết kế để chủ yếu làm việc với shell (hoặc terminal), giúp người dùng kiểm soát hệ điều hành tốt hơn.                                                  |
| **Configuration data stored in a text file** (Dữ liệu cấu hình được lưu trong tệp văn bản)                                          | Ví dụ về một tệp như vậy là tệp `/etc/passwd`, lưu trữ tất cả người dùng đã được đăng ký trên hệ thống.                                                             |

---

### Thành phần

| Thành phần          | Mô tả                                                                                                                                                                                                                                                                                              |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bootloader**      | Một đoạn mã hướng dẫn quá trình khởi động để bắt đầu hệ điều hành. Parrot Linux sử dụng GRUB Bootloader.                                                                                                                                                                                           |
| **OS Kernel**       | Kernel là thành phần chính của hệ điều hành. Nó quản lý tài nguyên cho các thiết bị I/O của hệ thống ở cấp phần cứng.                                                                                                                                                                              |
| **Daemons**         | Các dịch vụ nền được gọi là “daemon” trong Linux. Mục đích của chúng là đảm bảo các chức năng chính như lập lịch, in ấn và đa phương tiện hoạt động đúng cách. Các chương trình nhỏ này được tải sau khi khởi động hoặc đăng nhập vào máy tính.                                                    |
| **OS Shell**        | Trình shell của hệ điều hành hoặc bộ thông dịch ngôn ngữ lệnh (còn gọi là dòng lệnh) là giao diện giữa hệ điều hành và người dùng. Giao diện này cho phép người dùng yêu cầu hệ điều hành thực hiện các tác vụ. Các shell thường dùng gồm Bash, Tcsh/Csh, Ksh, Zsh và Fish.                        |
| **Graphics server** | Cung cấp hệ thống con đồ họa (gọi là “X” hoặc “X-server”) cho phép các chương trình đồ họa chạy cục bộ hoặc từ xa trên hệ thống X-window.                                                                                                                                                          |
| **Window Manager**  | Còn được gọi là giao diện người dùng đồ họa (GUI). Có nhiều tùy chọn như GNOME, KDE, MATE, Unity và Cinnamon. Môi trường desktop thường bao gồm nhiều ứng dụng, như trình duyệt tệp và trình duyệt web, cho phép người dùng truy cập và quản lý các tính năng, dịch vụ cần thiết của hệ điều hành. |
| **Utilities**       | Ứng dụng hoặc tiện ích là các chương trình thực hiện các chức năng cụ thể cho người dùng hoặc cho chương trình khác.                                                                                                                                                                               |

---

### Kiến trúc Linux

Hệ điều hành Linux có thể được chia thành các lớp:

| Lớp                | Mô tả                                                                                                                                                                                                                                                   |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hardware**       | Các thiết bị ngoại vi như RAM hệ thống, ổ cứng, CPU và các thành phần khác.                                                                                                                                                                             |
| **Kernel**         | Lõi của hệ điều hành Linux, có chức năng ảo hóa và kiểm soát tài nguyên phần cứng như CPU, bộ nhớ được phân bổ, dữ liệu được truy cập… Kernel cung cấp tài nguyên ảo cho mỗi tiến trình và ngăn ngừa/giảm thiểu xung đột giữa các tiến trình khác nhau. |
| **Shell**          | Giao diện dòng lệnh (CLI), còn gọi là shell, cho phép người dùng nhập lệnh để thực thi các chức năng của kernel.                                                                                                                                        |
| **System Utility** | Cung cấp cho người dùng quyền truy cập vào tất cả các chức năng của hệ điều hành.                                                                                                                                                                       |

---

### Cấu trúc hệ thống tệp

Hệ điều hành Linux được tổ chức theo dạng cây phân cấp và được ghi lại trong tiêu chuẩn **Filesystem Hierarchy Standard (FHS)**.
Linux được cấu trúc với các thư mục cấp cao tiêu chuẩn sau:

![](./img/2_Linux_Fundamentals/1.1.1.webp)

| **Đường dẫn** | **Mô tả**                                                                                                                                                                                                                                                                                                          |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `/`           | Thư mục gốc của hệ thống tệp, chứa tất cả các tệp cần thiết để khởi động hệ điều hành trước khi các hệ thống tệp khác được gắn, cũng như các tệp cần thiết để khởi động các hệ thống tệp khác. Sau khi khởi động, tất cả các hệ thống tệp khác được gắn tại các điểm mount tiêu chuẩn như là thư mục con của root. |
| `/bin`        | Chứa các tệp nhị phân lệnh thiết yếu.                                                                                                                                                                                                                                                                              |
| `/boot`       | Gồm bộ nạp khởi động tĩnh, tệp thực thi nhân (kernel) và các tệp cần thiết để khởi động hệ điều hành Linux.                                                                                                                                                                                                        |
| `/dev`        | Chứa các tệp thiết bị để hỗ trợ truy cập mọi thiết bị phần cứng gắn với hệ thống.                                                                                                                                                                                                                                  |
| `/etc`        | Các tệp cấu hình hệ thống cục bộ. Tệp cấu hình cho ứng dụng đã cài đặt cũng có thể được lưu tại đây.                                                                                                                                                                                                               |
| `/home`       | Mỗi người dùng trên hệ thống có một thư mục con tại đây để lưu trữ dữ liệu.                                                                                                                                                                                                                                        |
| `/lib`        | Các thư viện dùng chung cần thiết cho quá trình khởi động hệ thống.                                                                                                                                                                                                                                                |
| `/media`      | Các thiết bị lưu trữ di động bên ngoài như USB được gắn tại đây.                                                                                                                                                                                                                                                   |
| `/mnt`        | Điểm mount tạm thời cho các hệ thống tệp thông thường.                                                                                                                                                                                                                                                             |
| `/opt`        | Chứa các tệp tùy chọn như các công cụ của bên thứ ba.                                                                                                                                                                                                                                                              |
| `/root`       | Thư mục cá nhân của người dùng root.                                                                                                                                                                                                                                                                               |
| `/sbin`       | Chứa các tệp thực thi dùng cho quản trị hệ thống (các tệp nhị phân hệ thống).                                                                                                                                                                                                                                      |
| `/tmp`        | Hệ điều hành và nhiều chương trình dùng thư mục này để lưu trữ tệp tạm thời. Thư mục này thường bị xóa khi khởi động lại hệ thống và có thể bị xóa bất cứ lúc nào mà không cần cảnh báo.                                                                                                                           |
| `/usr`        | Chứa các tệp thực thi, thư viện, tệp hướng dẫn (man) và các tệp khác.                                                                                                                                                                                                                                              |
| `/var`        | Chứa các tệp dữ liệu thay đổi như tệp nhật ký (log), hộp thư đến, tệp liên quan đến ứng dụng web, tệp cron, và nhiều hơn nữa.                                                                                                                                                                                      |

---

## 1.2. Linux Distributions

**Các bản phân phối Linux**

Các bản phân phối Linux – hay còn gọi là distros – là các hệ điều hành dựa trên nhân Linux. Chúng được sử dụng cho nhiều mục đích khác nhau, từ máy chủ và các thiết bị nhúng cho đến máy tính để bàn và điện thoại di động. Các bản phân phối Linux giống như các nhánh khác nhau của cùng một công ty, mỗi nhánh được điều chỉnh để phục vụ các thị trường hoặc nhóm khách hàng cụ thể. Mặc dù tất cả chúng đều chia sẻ cùng một nhóm thành phần (thành phần nhân), cấu trúc tổ chức và văn hóa công ty, nhưng mỗi bản phân phối lại cung cấp các sản phẩm và dịch vụ riêng biệt (cấu hình và phần mềm), tùy chỉnh trải nghiệm để đáp ứng những nhu cầu đa dạng – tất cả vẫn hoạt động dưới thương hiệu và các nguyên tắc chung của Linux. Mỗi bản phân phối Linux đều khác nhau, có bộ tính năng, gói phần mềm và công cụ riêng. Một số bản phân phối phổ biến bao gồm:

* Ubuntu
* Fedora
* CentOS
* Debian
* Red Hat Enterprise Linux

Nhiều người chọn Linux cho máy tính để bàn vì nó miễn phí, mã nguồn mở và có khả năng tùy biến cao. Ubuntu và Fedora là hai lựa chọn phổ biến dành cho máy tính để bàn và người mới bắt đầu. Nó cũng được sử dụng rộng rãi làm hệ điều hành máy chủ vì tính bảo mật, độ ổn định và khả năng cập nhật thường xuyên và đều đặn. Cuối cùng, với tư cách là các chuyên gia an ninh mạng, họ thường chọn Linux vì nó là mã nguồn mở, đồng nghĩa với việc mã nguồn có thể được kiểm tra và tùy chỉnh. Nhờ sự tùy biến này, chúng ta có thể tối ưu và cấu hình bản phân phối Linux của mình theo cách mong muốn và điều chỉnh cho phù hợp với các trường hợp sử dụng cụ thể nếu cần.

Chúng ta có thể dùng các bản phân phối này ở mọi nơi, bao gồm (máy chủ) web, thiết bị di động, hệ thống nhúng, điện toán đám mây và máy tính để bàn. Đối với các chuyên gia an ninh mạng, một số bản phân phối Linux phổ biến nhất bao gồm nhưng không giới hạn ở:

|                 |        |         |
| --------------- | ------ | ------- |
| ParrotOS        | Ubuntu | Debian  |
| Raspberry Pi OS | CentOS | BackBox |
| BlackArch       | Pentoo |         |

Sự khác biệt chính giữa các bản phân phối Linux nằm ở các gói phần mềm được bao gồm, giao diện người dùng và công cụ sẵn có. Kali Linux là bản phân phối phổ biến nhất dành cho các chuyên gia an ninh mạng, bao gồm nhiều công cụ và gói phần mềm tập trung vào bảo mật. Ubuntu phổ biến với người dùng máy tính để bàn, trong khi Debian phổ biến cho máy chủ và hệ thống nhúng. Cuối cùng, Red Hat Enterprise Linux và CentOS được ưa chuộng cho môi trường điện toán cấp doanh nghiệp.

---

**Debian**

Debian là một bản phân phối Linux được biết đến rộng rãi và được đánh giá cao nhờ tính ổn định và độ tin cậy. Nó được sử dụng cho nhiều mục đích, bao gồm máy tính để bàn, máy chủ và hệ thống nhúng. Debian sử dụng công cụ quản lý gói nâng cao (APT – Advanced Package Tool) để xử lý các bản cập nhật phần mềm và bản vá bảo mật. Hệ thống quản lý gói này giúp hệ thống luôn được cập nhật và bảo mật bằng cách tự động tải xuống và cài đặt các bản cập nhật bảo mật ngay khi có sẵn. Việc này có thể thực hiện thủ công hoặc thiết lập tự động.

Debian có thể khó học hơn so với một số bản phân phối khác, nhưng nó được đánh giá là một trong những bản phân phối Linux linh hoạt và tùy biến nhất. Quá trình cấu hình và cài đặt có thể phức tạp, nhưng nó cũng cung cấp quyền kiểm soát tuyệt đối đối với hệ thống, điều này có thể tốt cho người dùng nâng cao. Càng kiểm soát được nhiều hệ thống Linux, người dùng càng thấy phức tạp hơn. Tuy nhiên, điều đó chỉ có nghĩa là so với các tùy chọn và khả năng mà nó mang lại, việc thực hiện những tác vụ “dễ” có thể mất thời gian hơn so với khi chúng ta học được cách sử dụng một vài lệnh và công cụ cơ bản.

Tính ổn định và độ tin cậy là những điểm mạnh chính của Debian. Bản phân phối này nổi tiếng với các bản hỗ trợ dài hạn, có thể cung cấp các bản cập nhật và bản vá bảo mật trong vòng 5 năm. Điều này đặc biệt quan trọng đối với máy chủ và các hệ thống cần hoạt động liên tục 24/7. Debian có lịch sử lâu dài về bảo mật và độ tin cậy, cùng với cam kết mạnh mẽ đối với quyền riêng tư và an ninh. Debian là một bản phân phối Linux mạnh mẽ và đáng tin cậy, được sử dụng rộng rãi cho nhiều mục đích khác nhau. Nhờ sự ổn định, độ tin cậy và cam kết bảo mật, Debian trở thành lựa chọn hấp dẫn cho nhiều trường hợp sử dụng, bao gồm cả an ninh mạng.

---

## 1.3. Introduction to Shell
**Giới thiệu về Shell**

Việc học cách sử dụng shell của Linux là rất quan trọng, vì có rất nhiều máy chủ được xây dựng dựa trên Linux. Chúng thường được sử dụng vì Linux ít xảy ra lỗi hơn so với máy chủ Windows.

Ví dụ, các máy chủ web thường chạy trên nền tảng Linux. Biết cách sử dụng hệ điều hành để kiểm soát nó một cách hiệu quả đòi hỏi phải hiểu và nắm vững một phần thiết yếu của Linux, đó là **Shell**.

Khi chúng ta lần đầu chuyển từ Windows sang Linux, giao diện sẽ trông giống như thế này:

![](./img/2_Linux_Fundamentals/1.3.1.webp)

Một terminal trong Linux, còn được gọi là **shell** hoặc **command line**, cung cấp giao diện nhập/xuất (I/O) dựa trên văn bản giữa người dùng và kernel của hệ điều hành. Thuật ngữ *console* cũng thường được sử dụng nhưng không chỉ một cửa sổ, mà là một màn hình ở chế độ văn bản. Trong cửa sổ terminal, các lệnh có thể được thực thi để điều khiển hệ thống.

Chúng ta có thể coi shell như một giao diện GUI dạng văn bản, nơi ta nhập các lệnh để thực hiện các thao tác như di chuyển đến thư mục khác, làm việc với tệp, và lấy thông tin từ hệ thống nhưng với nhiều khả năng hơn.

---

### Trình giả lập Terminal

Trình giả lập terminal là phần mềm mô phỏng chức năng của một terminal. Nó cho phép sử dụng các chương trình dựa trên văn bản trong môi trường đồ họa (**GUI**). Ngoài ra còn có các giao diện dòng lệnh (**CLI**) chạy như các terminal bổ sung bên trong một terminal. Nói ngắn gọn, terminal đóng vai trò là giao diện tới trình thông dịch shell.

Hãy tưởng tượng bạn đang ở một tòa nhà văn phòng lớn, nơi shell là phòng máy chủ chính xử lý toàn bộ dữ liệu và lệnh của công ty. Terminal giống như bàn tiếp tân, nơi tiếp nhận và chuyển yêu cầu tới phòng máy chủ (shell). Bạn đến bàn tiếp tân (terminal) để gửi hướng dẫn hoặc yêu cầu cho phòng máy chủ.

Bây giờ, giả sử bạn đang làm việc từ xa. Phần mềm giả lập terminal hoạt động như một bàn tiếp tân ảo trên màn hình máy tính của bạn (**GUI**), cho phép bạn tương tác với phòng máy chủ mà không cần có mặt trực tiếp tại văn phòng. Nó mô phỏng chức năng của bàn tiếp tân thật, cho phép bạn sử dụng các chương trình và lệnh dựa trên văn bản trong môi trường đồ họa.

Ngoài ra, các **giao diện dòng lệnh (CLI)** chạy như các terminal bổ sung bên trong một terminal giống như việc bạn có nhiều bàn tiếp tân ảo mở trên màn hình cùng lúc. Mỗi bàn cho phép bạn gửi các hướng dẫn khác nhau tới phòng máy chủ một cách độc lập, nhưng đều thông qua cùng một giao diện chính. Về bản chất, terminal đóng vai trò là cổng giao tiếp để điều khiển các hoạt động cốt lõi do shell quản lý.

Các trình giả lập và công cụ phân luồng terminal là những phần mở rộng hữu ích. Chúng cung cấp nhiều phương pháp và chức năng khác nhau để làm việc với terminal, chẳng hạn như chia terminal thành nhiều cửa sổ, làm việc trong nhiều thư mục, tạo không gian làm việc khác nhau, và nhiều hơn nữa. Một ví dụ về công cụ như vậy là **Tmux**, có thể được sử dụng như sau:

![](./img/2_Linux_Fundamentals/1.3.2.webp)

### Shell

Shell được sử dụng phổ biến nhất trong Linux là **Bourne-Again Shell (BASH)**, và là một phần của dự án GNU. Mọi việc chúng ta làm thông qua giao diện đồ họa (GUI) đều có thể thực hiện bằng shell. Shell mang đến cho chúng ta nhiều khả năng hơn để tương tác với các chương trình và tiến trình nhằm lấy thông tin nhanh hơn.

Ngoài ra, nhiều tiến trình có thể được tự động hóa một cách dễ dàng thông qua các script nhỏ hoặc lớn, giúp công việc thủ công trở nên đơn giản hơn nhiều.

Bên cạnh Bash, còn có nhiều loại shell khác như **Tcsh/Csh**, **Ksh**, **Zsh**, **Fish** và các shell khác.

---

# 2. The Shell
## 2.1. Prompt Description
**Mô tả về Prompt**

Prompt trong bash rất dễ hiểu. Theo mặc định, nó hiển thị thông tin như tên người dùng (username – bạn là ai), tên máy tính (hostname), và thư mục/directory mà bạn đang làm việc. Đây là một dòng văn bản xuất hiện trên màn hình để cho bạn biết rằng hệ thống đã sẵn sàng. Prompt xuất hiện trên một dòng mới, và con trỏ (dấu nhấp nháy hoặc ô vuông) sẽ nằm ngay sau đó, chờ bạn nhập lệnh.

Prompt có thể được tùy chỉnh để hiển thị thông tin hữu ích cho người dùng. Cấu trúc có thể trông như sau:

```
<username>@<hostname>:<current working directory>$
```

Thư mục chính (home directory) của một người dùng được đánh dấu bằng dấu ngã `~` và là thư mục mặc định khi đăng nhập.
Ví dụ:

```
<username>@<hostname>:~$
```

Ký hiệu `$` ở đây thể hiện cho người dùng thông thường.

Khi đăng nhập với quyền **root**, ký tự này sẽ đổi thành dấu `#` và có dạng:

```
root@htb:[/htb]#
```

Ví dụ, khi chúng ta tải và chạy shell trên máy mục tiêu, có thể sẽ không thấy tên người dùng, hostname và thư mục hiện tại. Điều này có thể do biến môi trường `PS1` không được đặt đúng. Trong trường hợp này, prompt có thể hiển thị như sau:

* **Prompt của User (không đặc quyền)**

```
$
```

* **Prompt của Root (có đặc quyền)**

```
#
```

Tùy chỉnh prompt có thể là một cách hữu ích để khiến trải nghiệm terminal của bạn trở nên cá nhân hóa và hiệu quả hơn. Nó cũng có thể là một công cụ hỗ trợ tốt cho việc khắc phục sự cố và giải quyết vấn đề, vì nó có thể cung cấp thông tin quan trọng về trạng thái của hệ thống tại bất kỳ thời điểm nào.

Ngoài việc tùy chỉnh prompt, chúng ta còn có thể tùy chỉnh môi trường terminal với các bảng màu khác nhau, phông chữ, và các thiết lập khác để khiến môi trường làm việc trở nên trực quan và dễ sử dụng hơn.

Tuy nhiên, chúng ta cũng thấy sự tương đồng với khi làm việc trên giao diện đồ họa Windows (GUI). Chúng ta đăng nhập với tư cách một người dùng trên một máy tính có tên cụ thể, và biết mình đang ở thư mục nào khi điều hướng trong hệ thống. Bash prompt cũng có thể được tùy chỉnh và thay đổi theo nhu cầu của chúng ta. Việc điều chỉnh bash prompt không nằm trong phạm vi của mô-đun này. Tuy nhiên, chúng ta có thể tham khảo **bash-prompt-generator** và **powerline**, giúp chúng ta có thể điều chỉnh prompt phù hợp với nhu cầu.

---

## 2.2. Getting Help

Khi đã có nền tảng vững chắc về cấu trúc Linux, các bản phân phối khác nhau và mục đích của shell, giờ đây chúng ta có thể bắt đầu áp dụng kiến thức này vào thực tế. Đã đến lúc làm việc trực tiếp với terminal, cũng như học cách tìm kiếm sự trợ giúp khi gặp phải những công cụ không quen thuộc.

Chúng ta sẽ luôn bắt gặp những công cụ hoặc tham số tùy chọn mà mình không nhớ rõ hoặc chưa từng thấy bao giờ. Vì vậy, điều quan trọng là phải biết cách tự tìm hiểu để làm quen với những công cụ đó. Hai cách đầu tiên là **man pages** và **help functions**. Luôn là một ý tưởng tốt khi làm quen với công cụ trước khi sử dụng. Chúng ta cũng sẽ học một số mẹo hay với những công cụ tưởng như không thể làm được. Trong **man pages**, chúng ta sẽ tìm thấy các tài liệu hướng dẫn chi tiết kèm giải thích cụ thể.

---

**Lệnh đầu tiên:**

```bash
Chloe9902@htb[/htb]$ ls
```

Kết quả:

```
cacert.der  Documents  Music  Public  Videos
Desktop     Downloads  Pictures  Templates
```

Lệnh **`ls`** trong Linux và Unix được dùng để liệt kê các tệp và thư mục trong thư mục hiện tại hoặc thư mục được chỉ định, giúp bạn xem bên trong và quản lý tệp hiệu quả hơn. Giống như hầu hết các lệnh Linux khác, **`ls`** có thêm nhiều tùy chọn và tính năng hỗ trợ lọc hoặc định dạng đầu ra theo ý muốn.

Để biết công cụ hoặc lệnh nào có những tùy chọn gì, có nhiều cách để nhận trợ giúp. Một trong số đó là dùng lệnh **`man`**, hiển thị các trang hướng dẫn sử dụng chi tiết cho lệnh đó.

---

**Cú pháp:**

```bash
Chloe9902@htb[/htb]$ man <tool>
```

---

**Ví dụ:**

```bash
Chloe9902@htb[/htb]$ man ls
```

```bash
LS(1)                            User Commands                           LS(1)

NAME
       ls - list directory contents

SYNOPSIS
       ls [OPTION]... [FILE]...

DESCRIPTION
       List  information  about  the FILEs (the current directory by default).
       Sort entries alphabetically if none of -cftuvSUX nor --sort  is  speci‐
       fied.

       Mandatory  arguments  to  long  options are mandatory for short options
       too.

       -a, --all
              do not ignore entries starting with .

       -A, --almost-all
              do not list implied . and ..

       --author
 Manual page ls(1) line 1 (press h for help or q to quit)

```

Sau khi xem qua một số ví dụ, chúng ta cũng có thể nhanh chóng xem các tham số tùy chọn mà không cần đọc toàn bộ tài liệu hướng dẫn. Có nhiều cách để làm điều đó.

---

**Cú pháp:**

```bash
Chloe9902@htb[/htb]$ <tool> --help
```

---
**Ví dụ:**

```bash
Chloe9902@htb[/htb]$ ls --help
```

**Kết quả:**

```
Usage: ls [OPTION]... [FILE]...
List information about the FILEs (the current directory by default).
Sort entries alphabetically if none of -cftuvSUX nor --sort is specified.

Mandatory arguments to long options are mandatory for short options too.
  -a, --all                  do not ignore entries starting with .
  -A, --almost-all           do not list implied . and ..
      --author               with -l, print the author of each file
  -b, --escape               print C-style escapes for nongraphic characters
      --block-size=SIZE      with -l, scale sizes by SIZE when printing them;
                             e.g., '--block-size=M'; see SIZE format below
  -B, --ignore-backups       do not list implied entries ending with ~
  -c                         with -lt: sort by, and show, ctime (time of last
                             modification of file status information);
                             with -l: show ctime and sort by name;
                             otherwise: sort by ctime, newest first
  -C                         list entries by columns
<...>
```

---

Một số công cụ hoặc lệnh như `curl` có thể hiển thị phiên bản rút gọn của phần trợ giúp bằng cách dùng tùy chọn `-h` thay vì `--help`:

---

**Cú pháp:**

```bash
Chloe9902@htb[/htb]$ <tool> -h
```

**Ví dụ:**

```bash
Chloe9902@htb[/htb]$ curl -h

Usage: curl [options...] <url>
     --abstract-unix-socket <path> Connect via abstract Unix domain socket
     --anyauth       Pick any authentication method
 -a, --append        Append to target file when uploading
     --basic         Use HTTP Basic Authentication
     --cacert <file> CA certificate to verify peer against
     --capath <dir>  CA directory to verify peer against
 -E, --cert <certificate[:password]> Client certificate file and password
<SNIP>
```

Như chúng ta có thể thấy, kết quả của mỗi lệnh trong ví dụ này không khác nhau nhiều.
Một công cụ khác có thể hữu ích cho người mới bắt đầu là **`apropos`**.
Mỗi trang hướng dẫn (manual page) có một mô tả ngắn bên trong. Công cụ này tìm kiếm các mô tả đó để tìm những mục có chứa từ khóa đã cho.

---

**Cú pháp:**

```bash
Chloe9902@htb[/htb]$ apropos <từ_khóa>
```

---

**Ví dụ:**

```bash
Chloe9902@htb[/htb]$ apropos sudo
```

Kết quả:

```
sudo (8)         - execute a command as another user
sudo.conf (5)    - configuration for sudo front end
sudo_plugin (8)  - Sudo Plugin API
sudo_root (8)    - How to run administrative commands
sudoedit (8)     - execute a command as another user
sudoers (5)      - default sudo security policy plugin
sudoreplay (8)   - replay sudo session logs
visudo (8)       - edit the sudoers file
```

---

Một nguồn tài nguyên khác hữu ích để nhận trợ giúp nếu chúng ta gặp khó khăn trong việc hiểu một lệnh dài là:
🔗 [https://explainshell.com/](https://explainshell.com/)

---

Tiếp theo, chúng ta sẽ tìm hiểu nhiều lệnh, trong đó có thể có những lệnh mới đối với bạn.
Tuy nhiên, bây giờ bạn đã biết cách tìm kiếm trợ giúp với bất kỳ lệnh nào mà bạn chưa quen hoặc không chắc về các tùy chọn của nó.
Chúng tôi khuyến khích bạn hãy khám phá sự tò mò của mình, dành thời gian để thử nghiệm và tìm hiểu các công cụ được giới thiệu. Điều này luôn là thời gian xứng đáng để đầu tư.

---

## 2.3. System Information
**Thông tin Hệ thống**

Bây giờ, hãy cùng thực hành một số lệnh cơ bản để làm quen với terminal và shell.
Hãy nhớ rằng bạn luôn có thể sử dụng các lệnh **`-h`**, **`--help`**, hoặc **`man`** để nhận trợ giúp khi cần.

Vì chúng ta sẽ làm việc với nhiều hệ thống Linux khác nhau, việc hiểu cấu trúc của chúng bao gồm thông tin hệ thống, tiến trình, cấu hình mạng, cài đặt người dùng/thư mục và các tham số liên quan là rất quan trọng.
Dưới đây là danh sách các công cụ thiết yếu giúp thu thập thông tin này. Hầu hết các công cụ này đều được cài đặt sẵn.
Kiến thức này không chỉ cần cho các tác vụ Linux thường ngày mà còn đóng vai trò quan trọng trong việc đánh giá cấu hình bảo mật, xác định lỗ hổng hoặc ngăn ngừa rủi ro bảo mật tiềm ẩn trong hệ điều hành Linux.

| Lệnh         | Mô tả                                                                                        |
| ------------ | -------------------------------------------------------------------------------------------- |
| **whoami**   | Hiển thị tên người dùng hiện tại.                                                            |
| **id**       | Trả về thông tin nhận dạng của người dùng.                                                   |
| **hostname** | Thiết lập hoặc in tên của máy chủ hiện tại.                                                  |
| **uname**    | In thông tin cơ bản về tên hệ điều hành và phần cứng hệ thống.                               |
| **pwd**      | Trả về tên thư mục làm việc hiện tại.                                                        |
| **ifconfig** | Dùng để gán hoặc xem địa chỉ của giao diện mạng và/hoặc cấu hình các tham số giao diện mạng. |
| **ip**       | Hiển thị hoặc thao tác định tuyến, thiết bị mạng, giao diện và đường hầm.                    |
| **netstat**  | Hiển thị trạng thái mạng.                                                                    |
| **ss**       | Một công cụ khác để kiểm tra socket.                                                         |
| **ps**       | Hiển thị trạng thái các tiến trình.                                                          |
| **who**      | Hiển thị ai đang đăng nhập.                                                                  |
| **env**      | In biến môi trường hoặc thiết lập và thực thi lệnh.                                          |
| **lsblk**    | Liệt kê các thiết bị khối (block devices).                                                   |
| **lsusb**    | Liệt kê các thiết bị USB.                                                                    |
| **lsof**     | Liệt kê các tệp đang mở.                                                                     |
| **lspci**    | Liệt kê các thiết bị PCI.                                                                    |

---

Cuối cùng, hãy cuộn xuống cuối trang, khởi chạy máy mục tiêu, kết nối với nó bằng SSH, sau đó cố gắng làm theo và thực hiện lại càng nhiều ví dụ trong phần này càng tốt.

### Đăng nhập qua SSH

**Secure Shell (SSH)** là một giao thức cho phép các máy khách truy cập và thực thi lệnh hoặc hành động trên máy tính từ xa.
Trên các máy chủ và hệ điều hành dựa trên Unix (bao gồm Linux), SSH là một công cụ tiêu chuẩn được cài đặt sẵn và thường được quản trị viên ưa chuộng để cấu hình, quản lý máy tính từ xa.

SSH là một giao thức lâu đời, đáng tin cậy, không yêu cầu hoặc cung cấp giao diện đồ họa (GUI), hoạt động rất hiệu quả và tiêu tốn ít tài nguyên.
Vì lý do này, nó thường được dùng trong các bài thực hành để bạn có thể thử nghiệm các lệnh và thao tác trong một môi trường an toàn.

Cú pháp kết nối tới máy mục tiêu:

```bash
ssh htb-student@[IP address]
```

---

**Hostname**

Lệnh **`hostname`** sẽ in ra tên của máy tính mà chúng ta đang đăng nhập:

```bash
hostname
```

Ví dụ đầu ra:

```
nixfund
```

---

**Whoami**

Lệnh **`whoami`** cho biết tên người dùng hiện tại.
Điều này rất hữu ích trong kiểm thử bảo mật hoặc khi có quyền truy cập shell đảo ngược, giúp ta biết mình đang chạy với tư cách người dùng nào và liệu người đó có đặc quyền gì không.

```bash
whoami
```

Ví dụ đầu ra:

```
cry0l1t3
```

**Id**

Lệnh **`id`** mở rộng chức năng của `whoami` bằng cách in ra thông tin **ID người dùng (UID)**, **ID nhóm (GID)** và danh sách **các nhóm** mà người dùng thuộc về.

Điều này hữu ích cho cả kiểm thử xâm nhập (pentest) và quản trị viên hệ thống khi cần kiểm tra quyền truy cập và quyền thành viên nhóm.
Ví dụ, trong kết quả dưới đây:

* **Nhóm `hackthebox`**: là nhóm không tiêu chuẩn, có thể cho thấy quyền truy cập đặc biệt.
* **Nhóm `adm`**: cho phép đọc log hệ thống trong `/var/log`, có thể tiết lộ thông tin nhạy cảm.
* **Nhóm `sudo`**: cho phép chạy một số hoặc tất cả lệnh với quyền **root**, giúp leo thang đặc quyền.

```bash
id
```

Kết quả mẫu:

```
uid=1000(cry0l1t3) gid=1000(cry0l1t3) groups=1000(cry0l1t3),1337(hackthebox),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lpadmin),126(sambashare)
```

---

**Uname**

Lệnh **`uname`** hiển thị thông tin cơ bản về hệ điều hành và phần cứng.
Bạn có thể gõ:

```bash
man uname
```

để xem tài liệu hướng dẫn và các tùy chọn khả dụng của lệnh này.

```bash
UNAME(1)                                    User Commands                                   UNAME(1)

NAME
       uname - print system information

SYNOPSIS
       uname [OPTION]...

DESCRIPTION
       Print certain system information.  With no OPTION, same as -s.

       -a, --all
              print all information, in the following order, except omit -p and -i if unknown:

       -s, --kernel-name
              print the kernel name

       -n, --nodename
              print the network node hostname

       -r, --kernel-release
              print the kernel release

       -v, --kernel-version
              print the kernel version

       -m, --machine
              print the machine hardware name

       -p, --processor
              print the processor type (non-portable)

       -i, --hardware-platform
              print the hardware platform (non-portable)

       -o, --operating-system

```

Chạy `uname -a` sẽ in ra tất cả thông tin về máy theo một thứ tự cụ thể: tên kernel, tên máy chủ, bản phát hành kernel, phiên bản kernel, tên phần cứng của máy, và hệ điều hành. Tùy chọn `-a` sẽ bỏ qua `-p` (loại bộ xử lý) và `-i` (nền tảng phần cứng) nếu chúng không xác định được.

```
cry0l1t3@htb[/htb]$ uname -a

Linux box 4.15.0-99-generic #100-Ubuntu SMP Wed Apr 22 20:32:56 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```

Từ lệnh trên, ta có thể thấy tên kernel là **Linux**, tên máy chủ là **box**, bản phát hành kernel là **4.15.0-99-generic**, phiên bản kernel là **#100-Ubuntu SMP Wed Apr 22 20:32:56 UTC 2020**, v.v. Chạy bất kỳ tùy chọn nào riêng lẻ sẽ cho ta phần thông tin cụ thể mà ta quan tâm.

---

### Sử dụng uname để lấy bản phát hành kernel

Giả sử ta muốn in ra bản phát hành kernel để nhanh chóng tìm kiếm các khai thác kernel tiềm năng. Ta có thể gõ `uname -r` để lấy thông tin này.

```
cry0l1t3@htb[/htb]$ uname -r

4.15.0-99-generic
```

Với thông tin này, ta có thể tìm kiếm `"4.15.0-99-generic exploit"`, và kết quả đầu tiên lập tức sẽ xuất hiện hữu ích cho chúng ta.

Chúng ta nên nghiên cứu kỹ các lệnh và hiểu chúng dùng để làm gì và cung cấp thông tin gì. Dù có hơi tốn thời gian, nhưng việc nghiên cứu trang hướng dẫn (manpages) của các lệnh thông dụng sẽ giúp chúng ta học được nhiều điều mà có thể trước đây ta không nghĩ là có thể làm với một lệnh. Thông tin này không chỉ được dùng để làm việc với Linux mà còn được sử dụng sau này để phát hiện lỗ hổng và cấu hình sai trên hệ thống Linux có thể dẫn đến leo thang đặc quyền. Dưới đây là một vài bài tập tùy chọn mà chúng ta có thể giải cho mục đích thực hành, giúp chúng ta làm quen hơn với một số lệnh.


### Về các bài tập Linux

Các bài tập được cung cấp để học hệ điều hành Linux và các lệnh của nó có thể không phải lúc nào cũng rõ ràng ngay về những gì bạn cần làm, và điều đó hoàn toàn bình thường — thậm chí còn là điều không thể tránh khỏi. Như bạn đã học từ phần “Quá trình học tập”, việc học một điều mới có thể khiến bạn thấy không thoải mái và có thể gây căng thẳng. Bạn có thể hình dung điều đó giống như lần đầu tiên bạn ngồi sau tay lái và phải tự lái xe. Khi đó rất căng thẳng vì có quá nhiều thứ bạn phải tập trung cùng lúc. Nhưng bây giờ, khi đã có kinh nghiệm, việc lái xe trở nên dễ dàng hơn, dù rằng bạn không còn học được nhiều như trước. Tương tự, trong phần học này, bạn có thể thấy mình ở trong những tình huống không chắc nên làm gì, nhưng điều đó cũng không sao. Trên hành trình an ninh mạng, bạn sẽ thường xuyên gặp những khoảnh khắc như vậy, và đó là dấu hiệu tích cực cho thấy bạn đang học điều gì đó mới. Vượt qua những thử thách này sẽ giúp bạn tiến bộ, ngay cả khi bạn chưa hoàn toàn giải xong bài tập. Đó mới là mục tiêu cuối cùng — tiến bộ thông qua việc học.

Các bài tập được thiết kế có chủ đích nhằm dần dần đưa bạn ra khỏi vùng kiến thức hiện tại và bước vào lĩnh vực chưa quen thuộc. Tiến trình này được sắp đặt cẩn thận để đảm bảo rằng khi bạn tiếp tục luyện tập, kinh nghiệm và kiến thức của bạn sẽ tự nhiên mở rộng. Dù đôi khi có thể cảm thấy không thoải mái, quá trình này là cần thiết cho sự phát triển. Với mỗi thử thách mới, bạn sẽ vượt ra ngoài những gì mình đã biết, và với nỗ lực đều đặn, bạn sẽ thấy sự hiểu biết và kỹ năng của mình gần như tự động phát triển. Hãy tiếp tục luyện tập, và bạn sẽ dần tự tin hơn cũng như thành thạo hơn trong việc điều hướng những điều chưa biết.

## Các câu hỏi

**1. Find out the machine hardware name and submit it as the answer.**

>x86_64

![](./img/2_Linux_Fundamentals/2.3.1.png)

---

**2. What is the path to htb-student's home directory?**

>/home/htb-student

![](./img/2_Linux_Fundamentals/2.3.2.png)

---

**3.  What is the path to the htb-student's mail?** 

>/var/mail/htb-student

![](./img/2_Linux_Fundamentals/2.3.3.png)

---

**4.  Which shell is specified for the htb-student user?**

>/bin/bash

![](./img/2_Linux_Fundamentals/2.3.4.png)

Trường cuối cùng (/bin/bash) chính là shell được chỉ định cho user htb-student 

---

**5. Which kernel release is installed on the system? (Format: 1.22.3)**

Sử dụng các câu lệnh sau:

```uname -r
```

Hoặc

```hostnamectl
```

---

**6.  What is the name of the network interface that MTU is set to 1500?**


![](./img/2_Linux_Fundamentals/2.3.5.png)

---

# 3. Workflow

## 3.1 Navigation
>Điều hướng

Điều hướng là cần thiết, giống như làm việc với chuột như một người dùng Windows thông thường. Với nó, chúng ta di chuyển khắp hệ thống và làm việc trong các thư mục và với các tệp mà chúng ta cần và muốn. Do đó, chúng ta sử dụng các lệnh và công cụ khác nhau để in ra thông tin về một thư mục hoặc một tệp và có thể sử dụng các tùy chọn nâng cao để tối ưu hóa đầu ra theo nhu cầu của chúng ta.

Một trong những cách tốt nhất để học điều gì đó mới là thử nghiệm với nó. Ở đây, chúng ta sẽ đề cập đến các phần về điều hướng trong Linux, tạo, di chuyển, chỉnh sửa và xóa tệp cũng như thư mục, tìm chúng trong hệ điều hành, các loại tiến trình khác nhau và các bộ mô tả tệp là gì. Chúng ta cũng sẽ tìm các phím tắt để làm việc với shell dễ dàng và thoải mái hơn. Chúng tôi khuyên bạn nên thử nghiệm trên máy ảo (VM) đã cài đặt sẵn. Hãy đảm bảo rằng chúng ta đã tạo một snapshot cho VM để phòng trường hợp hệ thống của chúng ta bị hỏng bất ngờ.

Hãy bắt đầu với phần điều hướng. Trước khi chúng ta di chuyển trong hệ thống, chúng ta cần biết mình đang ở thư mục nào. Chúng ta có thể tìm ra vị trí hiện tại với lệnh `pwd`.

---

Ví dụ:

```bash
cry0l1t3@htb[-]$ pwd
/home/cry0l1t3
```

---

Chỉ cần lệnh `ls` là có thể liệt kê tất cả nội dung bên trong một thư mục. Nó có nhiều tùy chọn bổ sung có thể làm cho việc hiển thị nội dung trong thư mục hiện tại đầy đủ hơn.

---

Ví dụ:

```bash
cry0l1t3@htb[-]$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
```

---

Sử dụng nó mà không thêm tùy chọn nào sẽ chỉ hiển thị các thư mục và tệp. Tuy nhiên, chúng ta cũng có thể thêm tùy chọn `-l` để hiển thị nhiều thông tin hơn về các thư mục và tệp đó.

---

Ví dụ:

```bash
cry0l1t3@htb[-]$ ls -l
total 32
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:37 Desktop
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Documents
drwxr-xr-x 3 cry0l1t3 htbacademy 4096 Nov 13 17:34 Downloads
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Music
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Pictures
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Public
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Templates
drwxr-xr-x 2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Videos
```

Trước tiên, chúng ta thấy tổng số block (1024 byte) được các tệp và thư mục trong thư mục hiện tại sử dụng, điều này cho biết tổng dung lượng đã dùng. Điều đó có nghĩa là nó đã sử dụng 32 block \* 1024 byte/block = 32.768 byte (hay 32 KB) dung lượng đĩa. Tiếp theo, chúng ta thấy một vài cột được cấu trúc như sau:

| Nội dung cột     | Mô tả                                                                   |
| ---------------- | ----------------------------------------------------------------------- |
| **drwxr-xr-x**   | Kiểu và quyền                                                           |
| **2**            | Số lượng hard link đến tệp/thư mục                                      |
| **cry0l1t3**     | Chủ sở hữu của tệp/thư mục                                              |
| **htbacademy**   | Nhóm sở hữu của tệp/thư mục                                             |
| **4096**         | Kích thước của tệp hoặc số block được dùng để lưu trữ thông tin thư mục |
| **Nov 13 17:37** | Ngày và giờ                                                             |
| **Desktop**      | Tên thư mục                                                             |

---

Tuy nhiên, chúng ta sẽ không thấy tất cả những gì có trong thư mục này. Một thư mục cũng có thể chứa các tệp ẩn bắt đầu bằng dấu chấm ở đầu tên của nó (ví dụ: `.bashrc` hoặc `.bash_history`).

Do đó, chúng ta cần sử dụng lệnh `ls -la` để liệt kê **tất cả** các tệp trong một thư mục:

---

Ví dụ:

```bash
cry0l1t3@htb[-]$ ls -la
total 403188
drwxr-xr-x  2 cry0l1t3 htbacademy 4096 Nov 13 17:37 .bash_history
drwxr-xr-x  2 cry0l1t3 htbacademy 4096 Nov 13 17:37 .bashrc
...SNIP...
drwxr-xr-x  2 cry0l1t3 htbacademy 4096 Nov 13 17:37 Desktop
drwxr-xr-x  2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Documents
drwxr-xr-x  3 cry0l1t3 htbacademy 4096 Nov 13 03:26 Downloads
drwxr-xr-x  2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Music
drwxr-xr-x  2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Pictures
drwxr-xr-x  2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Public
drwxr-xr-x  2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Templates
drwxr-xr-x  2 cry0l1t3 htbacademy 4096 Nov 13 17:34 Videos
```
Để liệt kê nội dung của một thư mục, chúng ta không nhất thiết phải điều hướng vào đó trước. Chúng ta cũng có thể dùng lệnh `ls` để chỉ định đường dẫn nơi chúng ta muốn biết nội dung.

---

Ví dụ:

```bash
cry0l1t3@htb[-]$ ls -l /var/

total 52
drwxr-xr-x  2 root root   4096 Mai 15 18:54 backups
drwxr-xr-x 18 root root   4096 Nov 15 16:55 cache
drwxrwsrwt  2 root whoopsie 4096 Jul 25  2018 crash
drwxr-xr-x 66 root root   4096 Mai  1 03:08 lib
drwxrwsr-x  2 root staff  4096 Nov 24  2018 local
<SNIP>
```

---

Chúng ta cũng có thể làm điều tương tự để điều hướng đến thư mục. Để di chuyển qua các thư mục, chúng ta sử dụng lệnh `cd`. Hãy thử chuyển sang thư mục `/dev/shm`. Tất nhiên, chúng ta có thể vào thư mục `/dev` trước rồi mới đến `/shm`. Tuy nhiên, chúng ta cũng có thể nhập đầy đủ đường dẫn và nhảy trực tiếp đến đó.

---

Ví dụ:

```bash
cry0l1t3@htb[-]$ cd /dev/shm
cry0l1t3@htb[/dev/shm]$
```

---

Vì trước đó chúng ta ở trong thư mục home, nên có thể nhanh chóng quay lại thư mục vừa rồi bằng lệnh:

---

Ví dụ:

```bash
cry0l1t3@htb[/dev/shm]$ cd -
cry0l1t3@htb[-]$
```

---

Shell cũng cung cấp cho chúng ta chức năng tự động hoàn thành (auto-complete), giúp việc điều hướng dễ dàng hơn. Nếu bây giờ chúng ta gõ `cd /dev/s` và nhấn `[TAB]` hai lần, chúng ta sẽ nhận được tất cả các mục bắt đầu bằng chữ "s" trong thư mục `/dev/`.

---

Ví dụ:

```bash
cry0l1t3@htb[-]$ cd /dev/s [TAB 2x]
shm/  snd/
```

Nếu chúng ta thêm chữ **“h”** vào sau chữ **“s”**, shell sẽ tự động hoàn thành đầu vào bởi vì sẽ không có thư mục nào trong đường dẫn này bắt đầu bằng chữ “sh” ngoài `/shm`. Nếu bây giờ hiển thị tất cả nội dung của thư mục, chúng ta sẽ chỉ thấy những nội dung sau:

---

Ví dụ:

```bash
cry0l1t3@htb[/dev/shm]$ ls -la /dev/shm
total 0
drwxrwxrwt  2 root root   40 Mai 15 18:31 .
drwxr-xr-x 17 root root 4000 Mai 14 20:45 ..
```

---

Mục đầu tiên với dấu chấm đơn (`.`) biểu thị thư mục hiện tại mà chúng ta đang đứng. Mục thứ hai với hai dấu chấm (`..`) biểu thị thư mục cha (`/dev`). Điều này có nghĩa là chúng ta có thể quay lại thư mục cha bằng lệnh:

---

Ví dụ:

```bash
cry0l1t3@htb[/dev/shm]$ cd ..
cry0l1t3@htb[/dev]$
```

---

Vì shell của chúng ta đã chứa khá nhiều lệnh, chúng ta có thể dọn dẹp màn hình bằng lệnh `clear`. Trước hết, hãy quay lại thư mục `/dev/shm` rồi thực thi lệnh `clear` để làm sạch terminal.

---

Ví dụ:

```bash
cry0l1t3@htb[/dev]$ cd shm && clear
```

---

Một cách khác để làm sạch terminal là sử dụng tổ hợp phím **\[Ctrl] + \[L]**.
Chúng ta cũng có thể dùng các phím mũi tên (**↑ hoặc ↓**) để cuộn qua lịch sử các lệnh đã dùng trước đó. Ngoài ra, chúng ta có thể tìm kiếm trong lịch sử lệnh bằng cách dùng phím tắt **\[Ctrl] + \[R]** và nhập một phần nội dung của lệnh mà chúng ta muốn tìm.

---

### Trả lời các câu hỏi

**What is the name of the hidden "history" file in the htb-user's home directory?**

>Sử dụng lệnh `ls -a` hoặc tìm ```find ~ -type f -name "*history"```

---

**What is the index number of the "sudoers" file in the "/etc" directory?**

![](./img/2_Linux_Fundamentals/3.1.1.png)

---
