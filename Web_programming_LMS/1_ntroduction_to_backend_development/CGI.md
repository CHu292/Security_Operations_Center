# CGI (Common Gateway Interface)
## CGI là gì ?
Common Gateway Interface hoặc CGI là một chuẩn cho các chương trình gateway để giao tiếp thông tin với các server như là HTTP server

## Web browsing
- Để hiểu hơn về khái niệm của CGI, ta hãy xem chuyện gì xảy ra khi click vào một hyper link trong trình duyệt ở một trang web hoặc một URL.
  - Trình duyệt sẽ kết nối với HTTP web server và yêu cầu URL, filename...
  - Web server sẽ phân tích cú pháp URL và tìm kiếm filename. Nếu nó tìm thấy file đó sau đó gửi chúng quay ngược lại cho trình duyệt, nếu không thì chúng sẽ gửi một thông báo lỗi mô tả request đến file bị sai
  - Trình duyệt nhận phản hồi từ web serrver và hiển thị file nhận được hoặc nhận một thông báo lỗi
- Tuy nhiên, có thể cài đặt máy chủ HTTP để bất cứ khi nào một tệp trong thư mục chỉ định được request không được gửi trở lại, thay vào đó nó được thực hiện như một chương trình và bất kì output nào của chương trình đó được gửi lại để trình duyệt hiển thị. Chức năng này được gọi là Common Gateway Interface hay CGI và chương trình đó được gọi là CGI scripts. Các chương trình này có thể là Python Script, Perl script, C or C++.

## Sơ đồ kiến trúc CGI 

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/CGI/CGI_Architecture_Diagram.png" alt="Sơ đồ kiến trúc CGI" width="500">
</p>
<p align="center"><b>Sơ đồ kiến trúc CGI</b></p>

##  CGI hoạt động như thế nào?

CGI là một giao thức trao đổi giữa máy chủ web và các ứng dụng cổng (gateway application) như PHP, Python,…

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Web_programming_LMS/1_ntroduction_to_backend_development/image/CGI/How_does_CGI_work.jpeg" alt="Cách CGI hoạt động " width="500">
</p>
<p align="center"><b>Cách CGI hoạt động </b></p>

**Trong thực tế CGI sẽ hoạt động như sau:**

1. Máy trạm gửi yêu cầu đến máy chủ web, máy chủ web nhận yêu cầu và chuyển tiếp cho ứng dụng cổng. CGI sẽ thực thi một câu lệnh tương ứng phù hợp với ứng dụng đó.
2. Các thông tin chi tiết về yêu cầu được ứng dụng truyền qua bằng các biến môi trường, trong khi đó dữ liệu bằng các phương pháp POST hoặc PUT sẽ được truyền qua các cổng nhập tiêu chuẩn. Tức là CGI xử lý dữ liệu của nó song song với dữ liệu chính.
3. Ứng dụng sẽ viết nội dung cần trả lời để máy chủ trả thông tin về cho người yêu cầu.

**Nghe quá trình này khá đơn giản và hiệu quả. Tuy nhiên, hình thức này dần bộc lộ một số hạn chế như:**

- Một yêu cầu sẽ tạo ra một tiến trình làm việc độc lập. Bộ nhớ và các thông tin không được lưu lại sau mỗi phiên, sẽ được tạo lại sao mỗi phiên.
- Một tiến trình mới sẽ tiêu tốn rất nhiều tài nguyên của hệ thống. Nếu trong một thời điểm một loạt yêu cầu được sinh ra sẽ làm máy chủ quá tải ngay lập tức.
- Trong trường hợp máy chủ một nơi, ứng dụng nằm trên một máy tính khác sẽ tạo ra nhiều khó khăn.
