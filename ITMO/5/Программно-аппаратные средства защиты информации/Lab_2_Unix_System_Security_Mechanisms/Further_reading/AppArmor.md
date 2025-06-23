# AppArmor

## 1. Giới thiệu
AppArmor là một hệ thống bảo mật Kiểm Soát Truy Cập Bắt Buộc (Mandatory Access Control-MAC). Mục tiêu của AppArmor là cung cấp một hệ thống bảo mật dễ sử dụng, tập trung vào việc bảo vệ các ứng dụng riêng lẻ bằng cách xác định và giới hạn những tài nguyên mà một ứng dụng có thể truy cập và chia sẻ. Khác với các công nghệ container khác (chroot, lxc containers), AppArmor tập trung vào việc chia sẻ và kiểm soát tại chỗ để thực thi bảo mật, thay vì sao chép toàn bộ hệ thống nhằm đạt được sự cách ly hoàn toàn. Ngoài việc kiểm soát các tài nguyên hệ thống tiêu chuẩn (tệp, mạng, các quyền hạn,...), AppArmor còn mở rộng đến các dịch vụ và daemon của hệ thống (như dbus, gsettings, X,...) cho phép tích hợp thực thi chính sách vượt qua giới hạn mà sự cách ly mang lại. 

Cụ thể, AppArmor là một biến thể của Domain Type Enforcement (DTE), vốn là một biến thể của Type Enforcement (TE). AppArmor 4 mở rộng AppArmor thành một dạng lai giữa DTE và hệ thống quyền hạn. Dù AppArmor có khả năng cung cấp chính sách toàn hệ thống, chính sách của nó được thiết kế và tập trung xung quanh mô hình ứng dụng (domain), cho phép dễ dàng nhắm mục tiêu đến các ứng dụng hoặc người dùng cụ thể. Do không yêu cầu chính sách toàn hệ thống, AppArmor dễ dàng triển khai chọn lọc chỉ trong vài giờ.

Đơn vị cơ bản của sự hạn chế trong AppArmor là hồ sơ (profile), là một tệp văn bản mô tả quyền và truy cập mà một ứng dụng hoặc dịch vụ có được, dưới dạng danh sách trắng. Tệp văn bản hồ sơ này được biên dịch bởi trình biên dịch chính sách (apparmor_parser) và được tải vào nhân, nơi mô-đun bảo mật AppArmor (một mô-đun Bảo Mật Linux) thực thi tất cả các quyền hạn dựa trên nhân. Mô-đun nhân AppArmor cung cấp giao diện và API để các Trusted Helpers (dịch vụ hệ thống hỗ trợ thực thi chính sách của AppArmor) có thể thực thi phần chính sách mà họ chịu trách nhiệm.

AppArmor cho phép các hồ sơ có chế độ khác nhau được kết hợp, cho phép một số hồ sơ thực thi chính sách trong khi một số khác đang được phát triển ở chế độ phàn nàn (complain mode). AppArmor sử dụng các tệp bao gồm (include files) để dễ dàng phát triển và có rào cản gia nhập thấp hơn nhiều so với các hệ thống MAC phổ biến khác. 

Các đặc điểm của AppArmor bao gồm:

- Hồ sơ là các tệp văn bản đơn giản.
- Hỗ trợ ghi chú trong hồ sơ.
- Các đường dẫn tuyệt đối và khả năng sử dụng ký tự đại diện cho phép khi chỉ định truy cập tệp.
- Có các kiểm soát truy cập khác nhau cho tệp.
- Kiểm soát truy cập cho mạng.
- Cụ thể trong việc khớp quy tắc, ví dụ, quy tắc cụ thể nhất sẽ được áp dụng.
- Hỗ trợ tệp bao gồm để đơn giản hóa và phát triển hồ sơ.
- Biến có thể được định nghĩa và điều chỉnh ngoài hồ sơ.
- Hồ sơ AppArmor dễ đọc và kiểm tra.
- Chính sách AppArmor có thể được đọc và kiểm tra trên cơ sở từng hồ sơ ứng dụng.

AppArmor là một công nghệ đã được thiết lập, lần đầu tiên xuất hiện trong Immunix và sau đó được tích hợp vào Ubuntu, Novell/SUSE, và Mandriva. Chức năng cốt lõi của AppArmor đã có trong nhân Linux chính từ phiên bản 2.6.36 trở đi; công việc vẫn đang được AppArmor, Ubuntu và các nhà phát triển khác tiếp tục để hợp nhất thêm các tính năng của AppArmor vào nhân chính. Tập hợp chính xác các tính năng và quyền có sẵn sẽ thay đổi theo phiên bản AppArmor được cài đặt, phiên bản của nhân Linux, và những dịch vụ hệ thống mà bản phân phối Linux đã kích hoạt (ví dụ: Để thực thi trung gian dbus của AppArmor, tùy chọn này phải được kích hoạt trong daemon dbus của bản phân phối).

## 2. Profiles

### Nơi lấy hồ sơ AppArmor

**Sản phẩm**  
Các hồ sơ AppArmor sẵn sàng cho sản phẩm nên được gói bởi bản phân phối của bạn, bằng cách thêm hồ sơ cụ thể vào gói ứng dụng hoặc bằng cách phân phối một gói chứa tất cả các hồ sơ AppArmor.

**Phát triển**  
Phát triển các hồ sơ AppArmor mới được thực hiện trong kho lưu trữ này. Kho lưu trữ chứa các hồ sơ đang trong quá trình phát triển, dự kiến sẽ được phân phối bởi các bản phân phối khi chúng hoàn thiện. Mọi người đều có thể đóng góp vào các hồ sơ ở đây, lưu ý rằng chúng dùng cho mục đích chung và cần tương thích với cài đặt mặc định của bản phân phối mà chúng sẽ được đưa vào. Khi đại diện của bản phân phối quyết định hồ sơ đã sẵn sàng để sử dụng trong sản phẩm, nó sẽ được thêm vào gói chính của bản phân phối. Hồ sơ trong kho lưu trữ sẽ được thay thế bằng tệp văn bản mô tả vị trí mới của hồ sơ và cách báo lỗi với hồ sơ đó. Xem tệp README để biết thêm thông tin.

**Hồ sơ Mẫu**  
Các công cụ không gian người dùng của AppArmor chứa một số hồ sơ mẫu chung. Những hồ sơ này chưa được tùy chỉnh cho các bản phân phối cụ thể, chỉ dùng để tham khảo.

### Cách lấy hồ sơ phát triển AppArmor  (Development AppArmor profiles)

Các hồ sơ phát triển của AppArmor có trong kho lưu trữ Bazaar. Sau khi cài đặt gói Bazaar của bản phân phối, bạn có thể tải chúng bằng lệnh sau:

```bash
git clone git://git.launchpad.net/apparmor-profiles
```

Tìm thư mục con phù hợp với bản phân phối và phiên bản của bạn và tìm kiếm các hồ sơ hiện đang trong quá trình phát triển. Bạn có thể sử dụng một hồ sơ bằng cách sao chép nó vào `/etc/apparmor.d` và khởi động lại AppArmor:

```bash
/etc/init.d/apparmor restart
# hoặc
restart apparmor  # nếu sử dụng upstart, với initscripts đã cập nhật để hỗ trợ upstart
```

### Cách tạo hoặc sửa đổi hồ sơ AppArmor  
Xem các trang wiki sau:

- Tạo và sửa đổi chính sách AppArmor bằng công cụ hỗ trợ
- Tạo và sửa đổi chính sách AppArmor thủ công
- Tài liệu AppArmor

### Cách đóng góp hồ sơ AppArmor  
Các bản vá và hồ sơ mới có thể được đóng góp bằng cách đăng lên danh sách gửi thư để được xem xét. Vui lòng xem `CommitPolicy` và `Versioning` trước khi gửi bản vá. Nếu bạn là người dùng launchpad hoặc muốn tham gia launchpad, launchpad cho phép tạo các nhánh tùy chỉnh của kho lưu trữ `apparmor-profiles`, và bạn có thể gửi yêu cầu hợp nhất từ nhánh tùy chỉnh của mình (xem `Sử dụng Launchpad với AppArmor`).

## 3. Documentation

### 3.1 GettingStarted

#### Tổng Quan Nhanh
AppArmor là một hệ thống bảo mật giống như Kiểm Soát Truy Cập Bắt Buộc (MAC) cho Linux. AppArmor giới hạn các chương trình riêng lẻ với các tệp, quyền hạn, truy cập mạng và rlimits, được gọi chung là chính sách AppArmor cho chương trình, hoặc đơn giản là hồ sơ (profile). Chính sách mới hoặc đã sửa đổi có thể được áp dụng cho hệ thống đang chạy mà không cần khởi động lại. AppArmor nhằm mục đích dễ hiểu và sử dụng cho các yêu cầu phổ biến nhất bằng cách trình bày các hồ sơ của nó bằng ngôn ngữ thân thiện với quản trị viên.

AppArmor chọn lọc trong việc giới hạn các chương trình, cho phép một số chương trình trên hệ thống bị giới hạn, trong khi các chương trình khác thì không. Sự giới hạn chọn lọc này giúp quản trị viên linh hoạt tắt một hồ sơ gặp vấn đề để khắc phục sự cố, trong khi vẫn giữ các phần khác của hệ thống bị giới hạn. Các chương trình không bị giới hạn sẽ chạy dưới quyền bảo mật Kiểm Soát Truy Cập Tuỳ Ý (DAC) tiêu chuẩn của Linux. AppArmor bổ sung cho DAC truyền thống ở chỗ các chương trình bị giới hạn sẽ được đánh giá dưới DAC truyền thống trước, và nếu DAC cho phép hành vi đó, thì chính sách AppArmor sẽ được tham khảo.

AppArmor hỗ trợ chế độ học hỏi (complain) cho từng hồ sơ để giúp người dùng viết và duy trì chính sách. Chế độ học hỏi cho phép tạo hồ sơ bằng cách chạy chương trình bình thường và ghi nhận hành vi của nó. Sau khi AppArmor đã học đủ về hành vi, hồ sơ có thể được chuyển sang chế độ thực thi. Mặc dù hồ sơ tạo từ chế độ học có thể rộng rãi hơn so với hồ sơ được tạo thủ công cho một môi trường và ứng dụng cụ thể, chế độ học hỏi có thể giúp giảm đáng kể công sức và kiến thức cần thiết để sử dụng AppArmor và thêm một lớp bảo mật quan trọng.

#### Các Phiên Bản của AppArmor
Có ba phiên bản chính của AppArmor: dòng 2.x (cũ nhưng vẫn được hỗ trợ), dòng 3.x (hiện tại), và dòng 4.x (đang phát triển). Dòng 2.x đã có những cải tiến từng bước trong suốt thời gian tồn tại với các thay đổi nhỏ về tương thích ngữ nghĩa. Dòng 3.x là một sự mở rộng quan trọng của AppArmor, cho phép chính sách mở rộng và kiểm soát chi tiết hơn. Dòng 4.x tiếp tục xu hướng này, duy trì khả năng tương thích ngược trong khi giới thiệu nhiều tính năng mới cho ngôn ngữ chính sách.

### 3.2 QuickProfileLanguage
