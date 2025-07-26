# 2. Hệ quản trị cơ sở dữ liệu

## 2.1 Khái niệm

- Một hệ quản trị cơ sở dữ liệu (Database management system – DBMS) là một tập hợp các chương trình giúp cho người sử dụng tạo ra, duy trì và khai thác CSDL một cách dễ dàng: 
- Nhiệm vụ của hệ quản trị cơ sở dữ liệu:
  - Định nghĩa CSDL: Đặc tả các kiểu dữ liệu, các cấu trúc và các ràng buộc 
  - Xây dựng CSDL: là quá trình lưu trữ dữ liệu trên các phương tiện lưu trữ được hệ quản trị CSDL kiểm soát 
  - Thao tác trên CSDL: truy vấn CSDL, cập nhật dữ liệu và tạo ra các báo cáo 
  - Các hệ quản trị CSDL có thể là phổ dụng hoặc chuyên dụng 
- Hệ cơ sở dữ liệu (database systems) = Cơ sở dữ liệu + hệ quản trị cơ sở dữ liệu
  
## 2.2 Chức năng của một hệ quản trị cơ sở dữ liệu

- Lưu trữ các định nghĩa, các mối liên kết dữ liệu (gọi là siêu dữ liệu - metadata) vào trong một từ điển dữ liệu 
- Tạo ra các cấu trúc phức tạp theo yêu cầu để lưu trữ dữ liệu 
- Biến đổi các dữ liệu được nhập vào để phù hợp với các cấu trúc dữ liệu ở điểm trên 
- Tạo ra một hệ thống bảo mật và áp đặt tính bảo mật và riêng tư trong cơ sở dữ liệu 
- Tạo ra các cấu trúc phức tạp cho phép nhiều người sử dụng truy cập đến dữ liệu 
- Cung cấp các thủ tục sao lưu và phục hồi dữ liệu để đảm bảo sự an toàn và toàn vẹn dữ liệu 
- Thực hiện các quy tắc an toàn để đảm bảo toàn vẹn dữ liệu 
- Cung cấp việc truy cập dữ liệu thông qua một ngôn ngữ truy vấn
  
## 2.3 Ngôn ngữ và giao diện cơ sở dữ liệu

- Các ngôn ngữ của hệ quản trị cơ sở dữ liệu: 
  - Ngôn ngữ định nghĩa dữ liệu (data definition language – DDL): Dùng để định nghĩa các lược đồ 
  - Ngôn ngữ thao tác dữ liệu (data manipulation language – DML): Dùng để thao tác cơ sở dữ liệu
  
- Các loại giao diện hệ quản trị cơ sở dữ liệu 
  - Giao diện dựa trên bảng chọn (Menu) 
  - Giao diện dựa trên mẫu biểu 
  - Giao diện đồ hoạ (Graphic User Interface - GUI) 
  - Giao diện cho người quản trị hệ thống
    
## 2.4  Các đặc trưng của giải pháp cơ sở dữ liệu

- Khả năng tự mô tả của hệ cơ sở dữ liệu 
- Tính độc lập của chương trình và dữ liệu 
- Hỗ trợ nhiều khung nhìn khác nhau đối với dữ liệu 
- Cho phép nhiều người sử dụng đồng thời trên một CSDL
