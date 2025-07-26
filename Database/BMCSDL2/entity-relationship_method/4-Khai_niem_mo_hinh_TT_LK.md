# 4. Mô hình thực thể-liên kết: Các khái niệm

## 4.1 Mô hình thực thể-liên kết là gì

- Mô hình thực thể-liên kết (Entity-Relationship, viết tắt ER) là một mô hình dữ liệu mức quan niệm nhằm mô tả các đối tượng trong thế giới thực và quan hệ giữa chúng 
- Thực thể là một đối tượng trong thế giới thực, có sự tồn tại độc lập: 
  - Thực thể cụ thể: có thể cảm nhận bằng giác quan, ví dụ xe đạp, bàn, ghế 
  - Thực thể trừu tượng: có thể nhận biết bằng nhận thức

## 4.2  Thuộc tính của thực thể

- Mỗi một thực thể có các thuộc tính, đó là các đặc trưng cụ thể mô tả thực thể đó; chẳng hạn màu sơn của xe ô tô, số nhân viên một công ty là các thuộc tính 
- Phân loại các thuộc tính: 
  - Thuộc tính đơn là thuộc tính không thể phân chia ra được thành các thành phần nhỏ hơn 
  - Thuộc tính phức hợp là thuộc tính có thể phân chia được thành các thành phần nhỏ hơn, biểu diễn các thuộc tính cơ bản hơn với các ý nghĩa độc lập 
  - Những thuộc tính có giá trị duy nhất cho một thực thể cụ thể gọi là các thuộc tính đơn trị 
  - Một thuộc tính có thể có một tập giá trị cho cùng một thực thể: thuộc tính đa trị
  - Ví dụ:
      - Một thực thể là công ty, công ty này có thuộc tính là địa chỉ. Vậy thuộc tính địa chỉ là thuộc tính đa trị, vì một công ty có thể có nhiều chi nhánh, có nhiều địa chỉ khác nhau. 
      - Tiếp theo là thuộc tính tên công ty là thuộc tính đơn trị, vì công ty chỉ có thể có một tên duy nhất.
  - Thuộc tính có giá trị có thể tính được thông qua giá trị của các thuộc tính khác gọi là thuộc tính suy diễn được 
  - ví dụ: Đối với thực thể người, thuộc tính tuổi có thể suy ra từ thuộc tính ngày tháng năm sinh. 
  - Trong một số trường hợp, một số thuộc tính của một thực thể cụ thể không xác định được giá trị. Trong trường hợp như vậy, ta phải tạo ra một giá trị đặc biệt gọi là giá trị null. Các thuộc tính nói trên là thuộc tính có thể nhận giá trị null
  - ví dụ: thuộc tính số điện thoại của thực thể nhân viên sẽ không có giá trị đối với các nhân viên không có số điện thoại.
    
## 4.3 Thuộc tính của kiểu thực thể: Định nghĩa hình thức

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/thuoc_tinh_kieu_thuc_the.png" alt="Thuộc tính thực thể" width="700">
</p>

## 4.4 Kiểu thực thể và tập thực thể

- Một kiểu thực thể là một nhóm các thực thể có các thuộc tính như nhau được mô tả bằng tên và các thuộc tính. Ví dụ: NHÂNVIÊN (Họ tên, Tuổi, Lương) là một kiểu thực thể 
- Một tập hợp các thực thể của một kiểu thực thể trong cơ sở dữ liệu tại một thời điểm bất kỳ được gọi là một tập thực thể

## 4.5 Khóa và tập giá trị

- Thuộc tính mà các giá trị của nó là khác nhau đối với mỗi thực thể riêng biệt trong một tập thực thể gọi là thuộc tính khóa → khóa dùng để phân biệt hai thực thể 
- Nhiều thuộc tính kết hợp với nhau tạo thành một khóa phức hợp. Khóa phức hợp phải tối thiểu 
- Một kiểu thực thể có thể có nhiều hơn một khóa 
-  Ví dụ:
  - Thực thể người có các thuộc tính: số cccd, họ tên, ngày sinh, giới tính
  - Vậy số cccd là khóa, vì mỗi người sẽ có một số cccd khác nhau. 
- Kiểu thực thể không có khóa gọi là kiểu thực thể yếu 
- Mỗi thuộc tính đơn của một kiểu thực thể được kết hợp với một miền giá trị

## 4.6 Kiểu liên kết, tập liên kết và các thể hiện

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/Kieu_lien_ket.png" alt="Thuộc tính thực thể" width="700">
</p>

**Ví dụ thể hiện liên kết**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/vi_du_kieu_lien_ket.png" alt="Ví dụ thể hiện kiểu liên kết" width="700">
</p>

- Trong ví dụ trên chúng ta có 2 thực thể: Nhân viên và đơn vị
- Và một kiểu liên kết là làm việc mô tả quan hệ giữa 2 thực thể nhân viên và đơn vị
- Chúng ta có các thể hiện liên kết là r1, r2, .... -> đợc gọi là tập thể hiện các liên kết
- Xét ví dụ cụ thể: 
  - Thể hiện liên kết r1 cho biết nhân viên e1 đang làm việc cho đơn ị d1
  - Thể hiện liên kết r3 cho biết nhân viên e3 đang làm việc cho đơn vị d1

## 4.7 Cấp liên kết, tên vai trò và kiểu dữ liệu đệ quy

- Cấp của một kiểu liên kết là số các kiểu thực thể tham gia vào kiểu liên kết đó. 
  - Ví dụ ở trên ta thấy thể hiện liên kết làm việc có 2 thực thể tham gia vào kiểu liên kết này, vì vậy cấp của kiểu liên kết làm việc là cấp 2
- Tên vai trò dùng để chỉ rõ vai trò của các kiểu thực thể tham gia liên kết 
- Trong nhiều trường hợp, các vai trò là rõ ràng và không cần chỉ ra 
- Khi một kiểu thực thể có thể tham gia vào một kiểu liên kết với nhiều vai trò khác nhau, tên vai trò là cần thiết để phân biệt ý nghĩa của việc tham gia. Các kiểu liên kết như vậy gọi là kiểu liên kết đệ quy
  
### 4.7.1 Ví dụ thể hiện liên kết cấp 3

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/vi_du_lien_ket_cap_3.png" alt="Ví dụ thể hiện kiểu liên kết cấp 3" width="700">
</p>

- Ở ví dụ trê chúng ta có 3 thực thể: Nhà cung cấp, dự án, vật tư; và liên kết là cung cấp
- Xét thể hiện liên kết r1 cho ta thấy: Nhà cung cấp s1 cung cấp vật tư p1 cho dự án j1

### 4.7.2 Ví dụ thể hiện liên kết đệ quy

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/vi_du_lien_ket_de_quy.png" alt="Ví dụ thể hiện kiểu liên kết đệ quy" width="700">
</p>

- Ở ví dụ trên chúng ta chỉ có duy nhất một thực thể nhân viên và tập thể hiện liên kết giám sát. Với quy ước: 1 có vai trò là giám sát, 2 là bị giám sát
- Xét thể hiện liên kết r1: nhân viên e5 giám sát nhân viên e1, hoặc nhân viên e1 bị nhân viên e5 giám sát

## 4.8 Các ràng buộc trên các kiểu liên kết

- Các kiểu liên kết thường có một số ràng buộc để chỉ ra số tổ hợp có thể của các thực thể tham gia trong tập hợp các thể hiện liên kết. Có hai loại ràng buộc chính: 
  - Tỷ số lực lượng 
  - Sự tham gia
    
### 4.8.1 Ràng buộc tỷ số lực lượng

- Tỷ số lực lượng cho một kiểu liên kết chỉ ra số các thể hiện liên kết mà một thực thể có thể tham gia. 
- Với các kiểu liên kết cấp 2, có thể ba kiểu tỷ số lực lượng 1 : 1, 1 : N, và M : N
  - Kiểu 1 : 1 - có nghĩa là trong kiểu liên kết đó, một thực thể của kiểu A chỉ liên kết với một thực thể của  kiểu B và ngược lại. 
  - Kiểu 1 : N - có nghĩa là một thực thể của kiểu A có thể liên kết với N thực thể của kiểu B. Và Các thực thể của kiểu B chỉ liên kết với một thực thể của kiểu A.
  - Kiểu M : N - có nghĩa là mỗi thực thể của kiểu A có thể liên kết với từng thực thể của kiểu B và ngược lại

## 4.8.2 Ràng buộc tham gia

- Các ràng buộc tham gia và sự phụ thuộc tồn tại: các thực thể của một kiểu thực thể có phải tham toàn bộ vào các thể hiện liên kết hay không. Có hai kiểu ràng buộc tham gia: 
  - Ràng buộc tham gia toàn bộ (phụ thuộc tồn tại) 
  - Ràng buộc tham gia bộ phận
  
 **Ví dụ 1**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/vd_1_rang_buoc.png" alt="Ví dụ về ràng buộc" width="700">
</p>

- Ở ví dụ trên chúng ta có hai kiểu thực thể là: Nhân viên và đơn vị. Và kiểu liên kết là quản lý
- Mỗi nhân viên chỉ được quản lý một đơn vị duy nhất và ngược lại một đơn vị chỉ được quản lý bởi 1 nhân viên duy nhất.
- Ta thấy đơn vị bắt buộc phải được quản lý, nhưng không phải nhân viên nào cũng được tham gia quản lý
- Ở trong ví dụ này ta có ràng bụôc về tỷ số lực lượng là 1 : 1 và ràng buộc tham gia ở phía đơn vị là ràng buộc tham gia toàn bộ (nghĩa là đơn vị nào cũng cần phải có nhân viên quản lý). Về phía nhân viên là ràng buộc tham gia bộ phận ( nghĩa là ko phải nhân viên nào cũng đc tham gia quản lý)

  **Ví dụ 2**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/vd_2_rang_buoc.png" alt="Ví dụ về ràng buộc" width="700">
</p>

- Ở ví dụ trên chúng ta có hai thực thể là nhân viên và dự án, liên kết là làm việc.
- Ta thấy một nhân viên được phép làm việc với nhiều dự án. Và mỗi một dự án có thể được tham gia bởi nhiều nhân viên. 
- Vì vậy ràng buộc tỷ số lực lược là M : N
- Ràng buộc tham gia đối với dự án là toàn bộ, ràng buộc tham gia bộ phận đối với phía nhân viên. 
- Xét thể hiện liên kết r4 cho thấy nhân viên e3 làm việc cho dự án p2 ......

## 4.9 Thuộc tính của các kiểu liên kết

- Các kiểu liên kết cũng có các thuộc tính, giống như các thuộc tính của các kiểu thực thể 
- Ví dụ: Kiểu liên kết LAMVIEC giữa các thực thể NHANVIEN và DUAN có thể có thuộc tính SoGio, để ghi lại số giờ làm việc của một nhân viên trên một dự án

## 4.10 Cách xác định kiểu thực thể

- Các kiểu thực thể không có thuộc tính khóa được gọi là kiểu thực thể yếu (W ) 
- Các kiểu thực thể có thuộc tính khóa được gọi là kiểu thực thể mạnh 
- Các thực thể của một kiểu thực thể yếu được xác định (phân biệt) bằng cách liên kết với các thực thể của một kiểu thực thể mạnh (S) khác Kiểu thực thể mạnh S còn được gọi là
 kiểu thực thể chủ của W 
- Ví dụ: TREEM là một kiểu thực thể yếu, cần được xác định dựa vào kiểu thực thể chủ NHANVIEN với liên kết CON
