# API

## API là gì?
- Về mặt kỹ thuật, API là viết tắt của Giao diện lập trình ứng dụng (Application Programming Interface).
- API là một trung gian phần mềm cho phép hai ứng dụng giao tiếp với nhau, có thể sử dụng cho web-based system, operating system, database system, computer hardware, or software library.
- Ở dạng đơn giản nhất, API là giao diện cho phép một ứng dụng giao tiếp với ứng dụng khác thông qua các lệnh đơn giản và cách các lệnh này được gửi và định dạng mà dữ liệu được truy xuất thông qua API có thể khác với API SOAP hoặc REST.

## API hoạt động như thế nào?
- API được xây dựng trên chính 2 thành phần: Request và Response

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/API/How_an_API_work.png" alt="API hoạt động như thế nào" width="1000">
</p>

### Request
**Một request đúng chuẩn cần có 4 thứ:**

1. URL
- URL là địa chỉ duy nhất cho 1 request, thường là đường dẫn tới một hàm xử lí logic.
2. Method
- HTTP request có tất cả 9 loại method , 2 loại được sử dụng phổ biến nhất là GET và POST
  - GET: Sử dụng để lấy thông tin từ server theo URI đã cung cấp.
  - HEAD: Giống với GET nhưng response trả về không có body, chỉ có header.
  - POST: Gửi thông tin tới sever thông qua các parameters HTTP.
  - PUT: Ghi đè tất cả thông tin của đối tượng với những gì được gửi lên.
  - PATCH: Ghi đè các thông tin được thay đổi của đối tượng.
  - DELETE: Xóa resource trên server.
  - CONNECT: Thiết lập một kết nối tới server theo URI.
  - OPTIONS: Mô tả các tùy chọn giao tiếp cho resource.
  - TRACE: Thực hiện một bài test loop-back theo đường dẫn đến resource.
3. Headers
- Là nơi chứa các thông tin cần thiết của 1 request nhưng end-users không biết có sự tồn tại của nó. Ví dụ: độ dài của request body, thời gian gửi request, loại thiết bị đang sử dụng, loại định dạng cái response mà client có đọc được…
4. Body
- Là nơi chứa thông tin mà client sẽ điền.

### Response

- Sau khi nhận được request từ phía client, server sẽ xử lý cái request đó và gửi ngược lại cho client 1 cái response. Cấu trúc của 1 response tương đối giống phần request nhưng Status code sẽ thay thế cho URL và Method. Tóm lại, nó có cầu trúc 3 phần:
  - Status code
  - Headers
  - Body
- Phần Header và body tương đối giống với request.

**Status code của respone**

- Status code (Mã hóa trạng thái thường được gọi là mã trạng thái) là một số nguyên 3 ký tự, trong đó ký tự đầu tiên của Status-Code định nghĩa loại Response và hai ký tự cuối không có bất cứ vai trò phân loại nào. Có 5 giá trị của ký tự đầu tiên:
  - 1xx: Information (Thông tin): Khi nhận được những mã như vậy tức là request đã được server tiếp nhận và quá trình xử lý request đang được tiếp tục.
  - 2xx: Success (Thành công): Khi nhận được những mã như vậy tức là request đã được server tiếp nhận, hiểu và xử lý thành công
  - 3xx: Redirection (Chuyển hướng): Mã trạng thái này cho biết client cần có thêm action để hoàn thành request
  - 4xx: Client Error (Lỗi Client): Nó nghĩa là request chứa cú pháp không chính xác hoặc không được thực hiện.
  - 5xx: Server Error (Lỗi Server): Nó nghĩa là Server thất bại với việc thực hiện một request nhìn như có vẻ khả thi.
## Ví dụ về request - response 
- Khi bạn sử dụng một ứng dụng trên điện thoại di động, ứng dụng kết nối Internet và gửi dữ liệu tới máy chủ. Máy chủ sau đó lấy ra dữ liệu đó, diễn giải nó, thực hiện các hành động cần thiết và gửi nó trở lại điện thoại của bạn. Ứng dụng sau đó giải thích dữ liệu đó và trình bày cho bạn thông tin bạn muốn theo cách có thể đọc được. Đây là những gì một API là – tất cả điều này xảy ra thông qua API.
- Trước khi đến với khái niệm chuyên môn, chúng ta hãy lấy một ví dụ quen thuộc. Hãy tưởng tượng bạn đang ngồi trong nhà hàng và chuẩn bị đặt món. Đầu bếp – “hệ thống” sẽ nấu thức ăn cho bạn. Cái còn thiếu là liên kết giữa bạn và đầu bếp ấy. Bạn không có khả năng biết bếp là khu nào trong nhà hàng để xông thẳng vào và gọi món.Đó là lúc bạn cần đến người phục vụ – API.
- Người bồi bàn này sẽ là người bồi bài, (hay thông thường chúng ta thường gọi là request – yêu cầu) của bạn nói với đầu bếp biết phải làm gì. Người đầu bếp – “hệ thống” biết phải nấu cho bạn cái gì và đưa cho người bồi bàn sau khi đã hoàn thành. Sau đó, người bồi bàn này sẽ mang thứ bạn cần – thức ăn/ thông tin (hay chúng ta hay gọi là response).
