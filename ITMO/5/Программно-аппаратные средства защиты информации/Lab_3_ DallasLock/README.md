
### **Цели лабораторной работы (Лабораторная работа №3)**

#### **Основные цели**
1. **Обеспечить знакомство с системой защиты Dallas Lock 8.0-K**:  
   - Познакомиться с системой защиты информации Dallas Lock 8.0-K и её возможностями в обеспечении защиты от несанкционированного доступа.  
   - Làm quen với hệ thống bảo vệ Dallas Lock 8.0-K và khả năng của nó trong việc bảo vệ thông tin khỏi truy cập trái phép.

2. **Изучить основные механизмы работы системы**:  
   - Изучить основные механизмы работы системы, включая:  
     - Разграничение прав доступа к файлам.  
     - Контроль целостности.  
     - Аудит и ведение журналов.  
   - Nghiên cứu các cơ chế chính của hệ thống, bao gồm:  
     - Phân quyền truy cập tệp.  
     - Kiểm tra tính toàn vẹn.  
     - Nhật ký kiểm toán.  

3. **Освоить работу с политиками аудита и управления доступом**:  
   - Научиться настраивать и проверять политики аудита и разграничения доступа.  
   - Làm quen với cách thiết lập và kiểm tra chính sách kiểm toán và phân quyền truy cập.

#### **Конкретные задачи**
- Настроить политику аудита для двух различных пользователей.  
  - Thiết lập chính sách kiểm toán cho hai người dùng khác nhau.

- Настроить и сохранить журналы аудита, применив фильтр событий за неделю, месяц или год.  
  - Cấu hình và lưu trữ nhật ký kiểm toán, bao gồm áp dụng bộ lọc sự kiện theo tuần, tháng, hoặc năm.

- Предоставить полномочия одного пользователя другому с использованием функционала Dallas Lock.  
  - Cấp quyền của một người dùng cho người khác bằng chức năng Dallas Lock.

- Настроить контроль целостности для устройств, таких как жёсткий диск, USB-устройства, папка и файл.  
  - Cấu hình kiểm tra tính toàn vẹn cho các thiết bị như ổ cứng, thiết bị USB, thư mục và tệp tin.

- Удалить информацию о сохранённых журналах с помощью системы Dallas Lock.  
  - Xóa thông tin nhật ký đã lưu bằng hệ thống Dallas Lock.
 
---

**Báo cáo Thực hành số 3. Hệ thống bảo đảm an ninh thông tin trước truy cập trái phép. DallasLock.**

**1. Mục đích và khả năng của hệ thống DALLAS LOCK 8.0-K**

**1.1 Mô tả tổng quan hệ thống**

Hệ thống bảo vệ thông tin khỏi truy cập trái phép (sau đây gọi là hệ thống SZI từ NSD) "Dallas Lock 8.0-K" được thiết kế để bảo vệ máy tính cá nhân:
- Khỏi việc truy cập vào thông tin vi phạm thẩm quyền của nhân viên;
- Khỏi việc truy cập thông tin bị cấm công khai từ các cá nhân không được phép;
- Khỏi việc truy cập thông tin vượt quá mức cần thiết cho các nhiệm vụ công việc.

Sử dụng hệ thống SZI NSD Dallas Lock 8.0-K trong các dự án bảo vệ thông tin hạn chế quyền truy cập (thông tin bảo mật, bao gồm cả dữ liệu cá nhân) cho phép hệ thống tự động hóa đáp ứng các yêu cầu của luật pháp Liên bang Nga, các tiêu chuẩn và tài liệu chỉ đạo.

Hệ thống Dallas Lock 8.0-K là một tổ hợp phần mềm bảo vệ thông tin trong các hệ thống tự động hóa dựa trên máy tính cá nhân. Hệ thống SZI NSD Dallas Lock 8.0-K bảo vệ thông tin trước truy cập trái phép trên máy tính cá nhân trong mạng LAN thông qua các kênh vào cục bộ, mạng và điều khiển từ xa. Hệ thống này còn cung cấp phân quyền truy cập của người dùng vào hệ thống tệp và các tài nguyên khác của máy tính. 

**1.2 Cấu trúc và các mô-đun thành phần**

Hệ thống bảo vệ Dallas Lock 8.0-K bao gồm các thành phần chính sau:
- **Trình điều khiển bảo vệ:** Là lõi của hệ thống bảo vệ, thực hiện các chức năng chính của SZI NSD. 
- **Phụ hệ tích hợp vào giao diện Windows Explorer:** Hiển thị các mục menu cần thiết cho cấu hình SZI NSD trong menu ngữ cảnh của các đối tượng hệ thống tệp.
- **Phụ hệ quản lý cục bộ:** Cung cấp tất cả các tùy chọn để quản lý SZI NSD, kiểm tra và cấu hình hệ thống.
- **Phụ hệ quản lý truy cập:** Bao gồm các phần:
  - Phân hệ đầu vào: Cung cấp nhận diện và xác thực người dùng cục bộ, miền, điều khiển từ xa.
  - Phân hệ kiểm soát truy cập tùy chọn: Quản lý quyền truy cập các đối tượng.
  - Phân hệ nhận diện phần cứng: Hỗ trợ làm việc với các dạng nhận diện phần cứng khác nhau.
  
**1.3 Khả năng**

Hệ thống bảo vệ thông tin Dallas Lock 8.0-K cung cấp các khả năng như:
- Cấm truy cập của người dùng không có tài khoản trên máy tính.
- Cho phép sử dụng các thiết bị nhận diện người dùng như: USB-Flash, khóa điện tử Touch Memory, khóa USB Aladdin eToken Pro/Java.
- Cho phép giới hạn phạm vi các đối tượng tệp tin có sẵn cho người dùng.
  
**Yêu cầu thực hành cho báo cáo số 3**

1. Cấu hình chính sách kiểm toán cho 2 người dùng, lấy tham số từ giảng viên.
2. Xem và lưu các nhật ký kiểm toán. Cấu hình bộ lọc để xem các sự kiện của tuần, tháng, năm hiện tại.
3. Chuyển quyền của một người dùng cho một người dùng khác, sử dụng tính năng của Dallas Lock.
4. Thiết lập kiểm soát toàn vẹn cho đĩa cứng, thiết bị USB, thư mục, tệp.
5. Xóa và làm sạch thông tin về nhật ký lưu trữ bằng Dallas Lock.
6. Cấm chuyển đổi người dùng mà không khởi động lại.
7. Tạo thư mục, tệp và mã hóa chúng, sử dụng các thuật toán mã hóa tích hợp.
8. Chặn hoạt động của các tệp mp3, mpeg, docx, djvu cho các nhóm người dùng khác nhau.
9. Tạo báo cáo về quyền và cấu hình của Dallas Lock.
10. Tạo bản sao lưu các tệp của SZI từ NSD Dallas Lock.
11. Kiểm tra chức năng của Dallas Lock.
