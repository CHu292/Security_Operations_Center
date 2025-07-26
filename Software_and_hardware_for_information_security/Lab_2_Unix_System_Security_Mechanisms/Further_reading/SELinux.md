# Cài đặt SELinux



Security-Enhanced Linux (SELinux) là một phương pháp mới để kiểm soát truy cập trong Linux dựa trên mô-đun hạt nhân Linux Security (LSM). SELinux được kích hoạt theo mặc định trong nhiều bản phân phối dựa trên Red Hat sử dụng cơ sở gói rpm, chẳng hạn như Fedora, CentOS, v.v.

Trong bài viết này, chúng ta sẽ xem xét cách cài đặt SELinux. Chúng ta sẽ không đề cập đến việc tạo chính sách mới mà sẽ cố gắng tiếp cận hệ thống từ một góc độ khác, xem nó có thể hữu ích như thế nào đối với người dùng Linux thông thường, xem xét những điều cơ bản về cách hoạt động của nó, cũng như cách bật, tắt và thay đổi trạng thái. Hệ thống được sử dụng để thực hiện các ví dụ là CentOS 8.

## Nội dung bài viết

1. Những điều cơ bản về SELinux
2. Cài đặt SELinux
   1. Trạng thái
   2. Chế độ hoạt động
   3. Lựa chọn chính sách
   4. Xem ngữ cảnh
   5. Thay đổi ngữ cảnh
   6. Sửa đổi chính sách
   7. Nhật ký
   8. Mô-đun
   9. Cờ
3. Kết luận
