# 5. Mô hình thực thể-liên kết: sơ đồ

## 5.1 Sơ đồ ER theo ký hiệu của Peter Chen 

### 5.1.1 Sơ đồ ER: Thực thể và các thuộc tính

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/thuc_the_thuoc_tinh_Peter_Chen.png" alt="Thực thể và các thuộc tính của Peter Chen" width="700">
</p>

- Thực thể: 
  - Các thực thể mạnh được thể hiện bằng hình chữ nhật với nét đơn.
  - Các thưc thể yếu được thể hiện bằng hình chữ nhật với nét đôi.
  - Tên các thực thể sẽ được ghi ở trong hình chữ nhật

- Thuộc tính:
  - Thuộc tính không phải là thuộc tính đa trị hay thuộc tính phức hợp được thể hiện bởi một hình ô van nét đơn và có một đường nối nối vào thực thể.
  - Bên trong hình ô van là tên thuộc tính.
  - Đối với thuộc tính khóa thì bên dưới của tên thuộc tính sẽ có một nét gạch chân.
  - Đối với thuộc tính đa trị là hình ô van nét đôi
  - Đối với thuộc tính phức hợp thì các thuộc tính được chia thành 2 mức.
    - mức thứ nhất - sẽ có đường nối vào thực thể
    - mức thứ 2 sẽ được nối vào mức thứ nhất
  - Thuộc tính suy diễn được thể hiển bằng hình ô van nét đứt
 
### 5.1.2 Sơ đồ ER: Liên kết và các ràng buộc

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/Lien_ket_Peter_.png" alt="Liên kết của Peter Chen" width="700">
</p>

- Các liên kết được thể hiện bằng hình thoi nét đơn
- Liên kết của thực thể yếu và thực thể chủ : hìn thoi nét đôi
- 3 hình cuối của sơ đồ trên biểu diễn về tham gia và ràng buộc về tỷ số lực lượng 
- Ở hình số 3: E2 tham gia toàn bộ (ký hiệu bằng nét kết nối đôi) vào liên kết R, E1 tham gia bộ phận (ký hiệu bằng nét kết nối đơn) vào liên kết R.
- Ở hình 4: Ngoài ràng buộc về sự tham gia còn có sự ràng buộc về tỉ số lực lượng. Ta có tỉ số lực lượng tham gia vào liên kết R của E1 và E2 là 1 : R. Và cả E1 và E2 đều tham gia bộ phận vào liên kết R
- Ngoài ra ta còn có ràng buộc cấu trúc min, max. Nếu min là 1 thì E tham gia toàn bộ, mếu min là 0 thì E tham gia bộ phận.

## 5.2 Ký hiệu ER theo kiểu “chân chim“ (crow’s foot)

### 5.2.1 Thực thể và liên kết

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/Thuc_the_lien_ket_crow_foot.png" alt="Thực thể và Liên kết của Crow's foot" width="700">
</p>

### 5.2.2 Thể hiện thuộc tính của thực thể

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/Thuoc_tinh_thuc_the_Crow_foot.png" alt="Thuộc tính của thực thể Crow's foot" width="700">
</p>

### 5.2.3 Ràng buộc tỷ số lực lượng và tham gia

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/Ky_hieu_crow_.png" alt="Ràng buộc của Crow's foot" width="700">
</p>

