# Life Cycle of a HTTP Request - Vòng đời của HTTP Request
## HTTP Request là gì?
- HTTP là từ viết tắt của Hyper Text Transfer Protocol nghĩa là Giao thức Truyền tải Siêu Văn Bản được sử dụng trong www (World Wide Web). HTTP là 1 giao thức cho phép tìm nạp tài nguyên, chẳng hạn như HTML doc. Hay hiểu đơn giản http là cách thức để website của bạn được truyền tải qua internet
## Cách thức hoạt động của HTTP Protocol
- Cuộc sống của HTTP xoay quanh cái vòng luẩn quẩn: Request và Response. Client gửi request, server gửi lại response là liệu server có thể làm được cái client muốn hay ko. Và API được xây dựng trên chính 2 thành phần: Request và Reponse. Trước tiên, ta phải hiểu cấu trúc của mỗi thành phần.
  <p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/life_cycle_of_a_HTTP_request/1.gif" alt="" width="1000">
</p>

**Request**
- Một request đúng chuẩn cần có 4 thứ:

  - URL
  - Method
  - Headers
  - Body

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/life_cycle_of_a_HTTP_request/2.gif" alt="" width="500">
</p>

**Bây giờ chúng ta sẽ đi vào chi tiết:**

1. URL là 1 cái địa chỉ duy nhất cho 1 thứ (dùng danh từ), có thể là web page, image,hoặc video. API mở rộng cái ý tưởng gốc của URL cho những thứ khác, ví dụ: customers, products. Và như thế client dễ dàng cho server biết cái nó muốn là cái gì, những cái này còn được gọi chung là “resources” – nguồn lực.
2. Method là cái hành động client muốn tác động lên “resources”, và nó thường là động từ. Có 4 loại Method hay được dùng:
  - GET: Yêu cầu server đưa lại resource: Hãy tưởng tượng ra cái cảnh vào fb, tay vuốt new feeds.
  - POST: Yêu cầu server cho tạo ra 1 resource mới. Ví dụ: đăng ký 1 chuyến đi ở GrabBike.
  - PUT: Yêu cầu server cho sửa / thêm vào resource đã có trên hệ thống. Ví dụ: Edit 1 post ở trên fb.
  - DELETE: Yêu cầu server cho xóa 1 resourse. Cái này chắc chả cần ví dụ.
3. Headers: nơi chứa các thông tin cần thiết của 1 request nhưng end-users không biết có sự tồn tại của nó. Ví dụ: độ dài của request body, thời gian gửi request, loại thiết bị đang sử dụng, loại định dạng cái response mà client có đọc được…
4. Body: nơi chứa thông tin mà client sẽ điền. Giả sử bạn đặt 1 cái bánh pizza, thì thông tin ở phần body sẽ là: Loại bánh pizza, kích cỡ, số lượng đặt.

**Response:**

- Sau khi nhận được request từ phía client, server sẽ xử lý cái request đó và gửi ngược lại cho client 1 cái response. Cấu trúc của 1 response tương đối giống phần request nhưng Status code sẽ thay thế cho URL và Method. Tóm lại, nó có cầu trúc 3 phần:
  - Status code
  - Headers
  - Body
## Vòng đời của HTTP request sẽ được hiểu như sau:

### Khởi đầu
- vòng đời yêu cầu HTTP bắt đầu khi một máy khách (thường là trình duyệt web) bắt đầu một yêu cầu(request)
- Việc bắt đầu này có thể là kết quả của nhiều tương tác khác nhau của người dùng, chẳng hạn như nhập URL vào thanh địa chỉ của trình duyệt, nhấp vào liên kết, gửi biểu mẫu hoặc thực hiện yêu cầu AJAX từ một trang web.
### URL Parsing

- Giả sử yêu cầu bắt nguồn từ hành động của người dùng như nhập URL.
- Trong trường hợp đó, máy khách sẽ phân tích cú pháp URL để trích xuất các thành phần thiết yếu, bao gồm giao thức (ví dụ: "http" hoặc "https"), tên miền (ví dụ: www.example.com), số cổng (nếu được chỉ định), đường dẫn (ví dụ: /path/to/resource), tham số truy vấn (nếu có) và mã định danh phân đoạn (ví dụ: #section).

### DNS Resolution
- Máy khách cần xác định địa chỉ IP của máy chủ web được liên kết với tên miền.
- Nó thực hiện tra cứu DNS (Domain Name System - Hệ thống tên miền) để dịch tên miền thành địa chỉ IP nếu nó vẫn cần được lưu vào bộ đệm.

### TCP Connection
- Sau khi có được địa chỉ IP, máy khách sẽ thiết lập kết nối TCP (Giao thức điều khiển truyền) tới máy chủ web trên cổng thích hợp (thường là cổng 80 cho HTTP hoặc cổng 443 cho HTTPS).
- Kết nối này cung cấp một kênh đáng tin cậy để truyền dữ liệu.

### HTTP Request Composition (các thành phần của HTTP request)
- Máy khách xây dựng một yêu cầu HTTP, bao gồm các thành phần sau: Phương thức HTTP (ví dụ: GET, POST, PUT, DELETE) chỉ định hành động sẽ được thực hiện.
- Tiêu đề yêu cầu chứa thông tin về máy khách, loại nội dung được chấp nhận và siêu dữ liệu khác.
- URL đầy đủ, bao gồm đường dẫn, tham số truy vấn và mã nhận dạng phân đoạn
- Nội dung yêu cầu tùy chọn cho các phương thức như POST và PUT, nơi dữ liệu có thể được gửi đến máy chủ.

### Request Transmission (yêu cầu truyền)
- Máy khách gửi yêu cầu HTTP đến máy chủ web qua kết nối TCP đã thiết lập.

### Server Processing
- Máy chủ web nhận và xử lý yêu cầu HTTP dựa trên phương thức, URL và tiêu đề yêu cầu.
- Các tập lệnh, ứng dụng và cơ sở dữ liệu phía máy chủ có thể liên quan đến việc tạo phản hồi.
- Máy chủ xây dựng phản hồi HTTP dựa trên yêu cầu.

### HTTP Response Composition
- Phản hồi HTTP bao gồm các thành phần chính sau: Mã trạng thái (ví dụ: 200 OK, 404 Not Found) cho biết kết quả của yêu cầu
- Tiêu đề phản hồi chứa thông tin về máy chủ, hướng dẫn bộ nhớ đệm và siêu dữ liệu (metadata).
- Nội dung phản hồi có tài nguyên được yêu cầu (ví dụ: trang HTML, hình ảnh, dữ liệu JSON).

### Response Transmission
- Máy chủ web gửi phản hồi HTTP trở lại máy khách qua cùng kết nối TCP.
- Client Processing
- Máy khách nhận được phản hồi HTTP và xử lý nó.
- Máy khách phân tích cú pháp HTML để tìm phản hồi HTML, tìm nạp các tài nguyên bổ sung (bảng định kiểu, tập lệnh, hình ảnh) và hiển thị trang web.

### JavaScript Execution (thực thi JavaScript)
- Nếu phản hồi chứa mã JavaScript, máy khách sẽ thực thi mã đó, cho phép tương tác và cập nhật động trên trang web.

### Rendering
- Máy khách hiển thị trang web đã được xử lý đầy đủ, hiển thị nó cho người dùng.

### User Interaction (tương tác người dùng)
- Người dùng có thể tương tác với trang web được hiển thị, bắt đầu các yêu cầu HTTP tiếp theo và tiếp tục chu trình bằng cách nhấp vào liên kết, gửi biểu mẫu hoặc tương tác với các ứng dụng web.
