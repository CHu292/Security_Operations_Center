# Web Application Basics


## Mục lục

1. [Task 1: Introduction](#task-1-introduction)
2. [Task 2: Web Application Overview](#task-2-web-application-overview)

## Nội dung


# Task 1: Introduction
**Giới thiệu**

Chào mừng đến với *Web Application Basics*! Trong phòng học này, chúng ta sẽ đi qua các yếu tố chính của một ứng dụng web, chẳng hạn như URL, các yêu cầu HTTP và phản hồi. Đây là nội dung hoàn hảo nếu bạn mới bắt đầu và muốn nắm bắt những kiến thức cơ bản, hoặc nếu bạn muốn xây dựng hay làm việc với các ứng dụng web.

---

**Mục tiêu học tập**

Sau khi hoàn thành phòng học này, bạn sẽ:

* Hiểu ứng dụng web là gì và cách nó chạy trong trình duyệt web.
* Phân tích các thành phần của một URL và thấy cách nó giúp truy cập tài nguyên web.
* Học cách hoạt động của các yêu cầu (request) và phản hồi (response) HTTP.
* Làm quen với các loại phương thức yêu cầu HTTP khác nhau.
* Hiểu ý nghĩa của các mã phản hồi HTTP khác nhau.
* Tìm hiểu cách các header HTTP hoạt động và tại sao chúng quan trọng đối với bảo mật.

---

# Task 2: Web Application Overview

Hãy tưởng tượng một phép so sánh: một ứng dụng web giống như một hành tinh. Phi hành gia du hành đến hành tinh để khám phá bề mặt của nó, tương tự như cách ai đó sử dụng trình duyệt web để khám phá hoặc duyệt một ứng dụng web. Mặc dù chúng ta chỉ thấy bề mặt của hành tinh, nhưng bên dưới bề mặt có rất nhiều hoạt động. Bạn có thể hình dung toàn bộ hành tinh giống như một web server với nhiều thứ diễn ra bên dưới, nhưng tất cả những gì chúng ta thường thấy chỉ là bề mặt của các trang web hoặc ứng dụng. Giờ đây chúng ta sẽ khám phá các thành phần cấu thành một ứng dụng web.

---

## Front End

**Front End** có thể được coi giống như bề mặt của hành tinh, nơi mà phi hành gia có thể nhìn thấy và tương tác theo các quy luật tự nhiên. Một ứng dụng web sẽ có giao diện người dùng tương tác với nó và sử dụng nhiều công nghệ như **HTML, CSS và JavaScript** để thực hiện điều đó.

---

**HTML** (Hypertext Markup Language) là nền tảng cơ bản của ứng dụng web. Đây là tập hợp các chỉ dẫn hoặc đoạn mã hướng dẫn trình duyệt web hiển thị nội dung gì và hiển thị như thế nào. Nó có thể được so sánh với những sinh vật đơn giản sống trên hành tinh; các sinh vật này có **DNA**, chính là tập hợp hướng dẫn cách chúng được tạo ra.

---

**CSS** (Cascading Style Sheets) trong ứng dụng web mô tả giao diện chuẩn, chẳng hạn như màu sắc, kiểu chữ, bố cục. Tiếp tục với phép so sánh DNA, CSS có thể được coi như những phần DNA mô tả màu sắc, hình dạng, kích thước và kết cấu của sinh vật đơn giản.

---

**JS** (JavaScript) là một phần của front end trong ứng dụng web, cho phép thực hiện các hoạt động phức tạp hơn trong trình duyệt. Trong khi HTML được coi là tập chỉ dẫn đơn giản về những gì cần hiển thị, thì JavaScript là một tập chỉ dẫn nâng cao hơn, cho phép đưa ra lựa chọn và quyết định về những gì sẽ hiển thị. Trong phép so sánh hành tinh, JavaScript có thể được coi là bộ não của một sinh vật tiên tiến, cho phép đưa ra quyết định dựa trên việc có cái gì và cách cái đó tương tác với nó.

## Back End

**Back End** của một ứng dụng web là những thứ bạn không nhìn thấy trong trình duyệt web nhưng lại rất quan trọng để ứng dụng hoạt động. Trên một hành tinh, đó là những thứ không thể nhìn thấy như: các cấu trúc giúp tòa nhà đứng vững, không khí, và lực hấp dẫn giữ cho con người đứng trên mặt đất.

---

**Database**
Là nơi thông tin có thể được lưu trữ, chỉnh sửa và truy xuất. Một ứng dụng web có thể cần lưu và lấy lại thông tin về sở thích của người dùng — ví dụ: hiển thị hay không hiển thị một nội dung nào đó; thông tin này sẽ được lưu trong cơ sở dữ liệu. Trên hành tinh, có thể có những cư dân tiên tiến hơn lưu trữ thông tin về vị trí bản đồ, viết nhật ký hoặc lưu trữ sách trong thư viện, hồ sơ trong tủ tài liệu.

---

**Infrastructure**
Có nhiều thành phần hạ tầng khác hỗ trợ ứng dụng web, chẳng hạn như web server, application server, lưu trữ, các thiết bị mạng, và phần mềm khác hỗ trợ ứng dụng. Trên hành tinh, chúng có thể được ví như những con đường, những chiếc xe chạy trên đường, và nhiên liệu để xe vận hành.

---

**WAF** (Web Application Firewall)
Là một thành phần tùy chọn của ứng dụng web. Nó giúp lọc các yêu cầu nguy hiểm trước khi đến Web Server và cung cấp một lớp bảo vệ. Điều này có thể được so sánh với khí quyển của hành tinh, nơi bảo vệ cư dân khỏi các tia UV có hại.

---

## Tóm tắt

Có nhiều thành phần tham gia vào việc triển khai một ứng dụng web. Các thành phần **Front End** như HTML, CSS, và JavaScript tập trung vào trải nghiệm bên trong trình duyệt. Các thành phần **Back End** như Web Server, Database hay WAF là động cơ bên dưới bề mặt, cho phép ứng dụng web hoạt động. Phần giới thiệu đơn giản này sẽ được mở rộng thêm trong các nhiệm vụ tiếp theo.

## Câu hỏi

**Trả lời các câu hỏi dưới đây**

1. Thành phần nào trên máy tính chịu trách nhiệm lưu trữ và cung cấp nội dung cho các ứng dụng web?

   → **web server** (máy chủ web)

2. Công cụ nào được sử dụng để truy cập và tương tác với các ứng dụng web?

   → **web browser** (trình duyệt web)

3. Thành phần nào hoạt động như một lớp bảo vệ, lọc lưu lượng truy cập đến để chặn các cuộc tấn công độc hại và đảm bảo an ninh cho ứng dụng web?

   → **web application firewall** (tường lửa ứng dụng web)
