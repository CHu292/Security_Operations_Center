# 1. Chủ đề:
 Mô hình hóa thông tin cơ sở dữ liệu bằng phương pháp mối quan hệ thực thể


# 2. Mục tiêu:
Nghiên cứu các phương pháp biểu diễn ngữ nghĩa của cơ sở dữ liệu (DB), rèn luyện kỹ năng thiết kế thông tin bằng cách sử dụng ký hiệu “thực thể-mối quan hệ”.

# 3. Nhiệm vụ:

## 3.1 Chọn chủ đề cho hệ thống thông tin (IS) mà cơ sở dữ liệu sẽ được biên soạn.

Ví dụ về hệ thống thông tin:

- Hệ thống thông tin khách sạn;
- Hệ thống thông tin trường đại học;
- Hệ thống thông tin dịch vụ sửa chữa PC

## 3.2 Sử dụng phương pháp “thực thể-mối quan hệ”, xây dựng mô hình cơ sở dữ liệu cho hệ thống thông tin đã chọn.

### 3.2.1 giai đoạn mô hình hóa. Phân tích hệ thống của hệ thống thông tin. Ở giai đoạn này, những điều sau đây được mô tả chi tiết:

- Cơ sở dữ liệu đang được phát triển cho các quy trình cụ thể nào trong IS đã chọn. Những vấn đề nào được lên kế hoạch để giải quyết bằng cách sử dụng cơ sở dữ liệu đang được phát triển.
- nguồn dữ liệu là gì, dữ liệu đến từ đâu, thông tin được nhận trong cơ sở dữ liệu ở định dạng/hình thức nào, với tần suất cập nhật;
- ai (nhóm người dùng nào) hoặc cái gì (hệ thống thông tin cấp cao hơn) là người tiêu dùng thông tin. Thông tin được trình bày dưới dạng/hình thức nào cho các tầng lớp người tiêu dùng khác nhau? Chọn ít nhất 2 loại người tiêu dùng thông tin, không tính quản trị viên cơ sở dữ liệu.
- mô tả các hạn chế đối với các thực thể và mối quan hệ trong mô hình cơ sở dữ liệu tương lai. Ví dụ: nếu cơ sở dữ liệu về IP của trường đại học đang được phát triển. Ở giai đoạn này, những hạn chế rõ ràng sau đây có thể được mô tả (trong một luồng giáo dục không thể có các lớp học ở các ngành khác nhau cùng một lúc; một giáo viên không thể dạy các lớp ở các ngành khác nhau cùng một lúc, v.v.)

### 3.2.2 Xác định các thực thể và xây dựng sơ đồ ER. 
Ở giai đoạn này, một danh sách các thực thể cho cơ sở dữ liệu đang được phát triển sẽ được tạo. Mô tả ngắn gọn nội dung mà mỗi thực thể trong mô hình IS của bạn đại diện. Nó cho biết mỗi thực thể thể hiện điều gì trong hệ thống. Tiếp theo, mối quan hệ giữa các thực thể được phân tích, chỉ ra loại mối quan hệ và loại thành viên. Kết quả của giai đoạn này sẽ là một sơ đồ ER. Số lượng mối quan hệ tối thiểu cần đạt được sau khi lập mô hình là 7. Số lượng thuộc tính (cột) tối thiểu trong các mối quan hệ là 3. Mối quan hệ giữa các bảng không được tính khi tính số lượng mối quan hệ tối thiểu được yêu cầu

### 3.2.3 Chuyển đổi sơ đồ ER thành sơ đồ mối quan hệ bằng cách sử dụng các quy tắc để hình thành các mối quan hệ sơ bộ;

### 3.2.4 Chuyển đổi quan hệ cơ sở dữ liệu sang 3NF.

### 3.2.5 Tạo ít nhất 2 chế độ xem cho mỗi người tiêu dùng thông tin từ cơ sở dữ liệu của bạn. Chế độ xem phải dựa trên truy vấn ảnh hưởng đến các thuộc tính từ 2 mối quan hệ liên quan trở lên.
