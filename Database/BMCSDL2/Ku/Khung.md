# 1. Mô hình hóa thông tin cơ sở dữ liệu bằng phương pháp “mối quan hệ thực thể”
## 1.1 Lựa chọn chủ đề

Chủ đề: Hệ thống thông tin bán sản phẩm cà phê

Lý do chọn chủ đề: Nơi tôi sống ở Việt Nam họ trồng rất nhiều cà phê. Vì vậy tôi chọn đề tài:
“Hệ thống thông tin bán sản phẩm cà phê”

## 1.2 Sử dụng phương pháp “thực thể-mối quan hệ”, xây dựng mô hình cơ sở dữ liệu cho hệ thống thông tin đã chọn.

### 1.2.1 Phân tích hệ thống của hệ thống thông tin. 

#### 1.2.1.1 Quá trình xử lý và nhiệm vụ cơ sở dữ liệu

**Cơ sở dữ liệu sẽ hỗ trợ các quy trình chính sau:**

- Quản lý sản phẩm: Theo dõi thông tin về các loại cà phê, giá cả, kho hàng và nhà cung cấp.
- Quản lý đơn hàng: Đăng ký và xử lý đơn đặt hàng của khách hàng, bao gồm chi tiết sản phẩm, tổng giá trị và trạng thái đơn hàng.
- Quản lý khách hàng: Lưu trữ thông tin khách hàng và lịch sử mua hàng.
- Quản lý nhà cung cấp: Theo dõi các nhà cung cấp và các sản phẩm họ cung cấp.
- Quản lý kho: Quản lý vị trí kho và tình trạng lưu trữ hàng hóa.. 

**Nhiệm vụ cần giải quyết:**

- Quản lý hiệu quả hàng tồn kho.
- Tự động hóa xử lý đơn hàng và theo dõi.
- Đơn giản hóa quản lý quan hệ khách hàng và nhà cung cấp.
- Tối ưu hóa công việc nhân viên qua việc phân chia nhiệm vụ.

#### 1.2.1.2 Nguồn dữ liệu, định dạng và tần suất cập nhật 

**Nguồn dữ liệu:**

- Đơn hàng: Lấy từ hệ thống bán hàng hoặc cửa hàng trực tuyến.
- Thông tin sản phẩm: Cập nhật bởi nhà cung cấp.
- Thông tin khách hàng: Nhập liệu bởi nhân viên hoặc qua biểu mẫu đăng ký.
- Thông tin kho: Từ hệ thống quản lý kho.

**Định dạng dữ liệu:**

- Đơn hàng: Dữ liệu đơn hàng được lưu trữ trong các bản ghi có cấu trúc bao gồm sản phẩm, số lượng, giá cả và thông tin khách hàng. 
- Sản phẩm và nhà cung cấp: thông tin được trình bày dưới dạng bảng với các thuộc tính chính (tên, giá, số lượng, chi tiết liên hệ của nhà cung cấp). 

**Tần suất cập nhật:**

- Đơn hàng: Cập nhật theo thời gian thực.
- Sản phẩm và kho: Cập nhật hàng ngày hoặc khi có thay đổi.
- Khách hàng: Cập nhật khi có khách hàng mới hoặc thay đổi thông tin.

#### 1.2.1.3 Lớp người dùng

- Quản lý bán hàng: Truy cập dữ liệu khách hàng, đơn hàng, và trạng thái thanh toán.
- Nhân viên kho: Quản lý tình trạng hàng tồn kho và vị trí lưu trữ sản phẩm.

#### 1.2.1.4 Hạn chế

- Mỗi đơn hàng chỉ có thể thuộc về một khách hàng, và một khách hàng có thể có nhiều đơn hàng.
- Một sản phẩm có thể liên quan đến nhiều nhà cung cấp, nhưng phải có ít nhất một nhà cung cấp.
- Mỗi kho phải có một nhân viên quản lý duy nhất.

### 1.2.2 Xác định thực thể và xây dựng ERD

#### 1.2.2.1 Xác dựng các thực thể 

- Employee: Nhân viên
- Supplier: Nhà cung cấp
- Product: Sản phẩm
- Customer: Khách hàng
- Order: Đơn hàng
- Bill: Hóa đơn
- Warehouse: Kho hàng

#### 1.2.2.2 Mô tả thực thể

- Employee: Gồm ID, tên, chức vụ, số điện thoại và email.
- Supplier: Gồm ID, tên nhà cung cấp, địa chỉ, số điện thoại và email.
- Product: Gồm ID, tên loại sản phẩm, giá cả.
- Customer: Gồm ID, tên khách hàng, số điện thoại, email.
- Order: Gồm ID, ngày đặt hàng, tổng số tiền.
- Bill: Gồm ID, số tiền, phương thức thanh toán.
- Warehouse: Gồm ID, địa chỉ, trạng thái kho

#### 1.2.2.3 Các liên kết

1.  Nhân viên (Employee) và Đơn hàng (Order):

- Tên liên kết: "Xử lý" (Processes)
- Mô tả: Mỗi nhân viên có thể xử lý nhiều đơn hàng, nhưng mỗi đơn hàng chỉ được xử lý bởi một nhân viên duy nhất.
- Cardinality: 1 : N (Một nhân viên có thể xử lý nhiều đơn hàng, mỗi đơn hàng chỉ có một nhân viên).
- Nhân viên: Tham gia một phần (Partial Participation). Không phải tất cả nhân viên đều xử lý đơn hàng.
- Đơn hàng: Tham gia toàn phần (Total Participation). Mỗi đơn hàng đều phải được xử lý bởi một nhân viên.

2. Nhà cung cấp (Supplier) và Sản phẩm (Product):

- Tên liên kết: "Cung cấp" (Delivers)
- Mô tả: Một nhà cung cấp có thể cung cấp nhiều sản phẩm, và một sản phẩm có thể được cung cấp bởi nhiều nhà cung cấp.
- Cardinality: M : N (Nhiều nhà cung cấp có thể cung cấp nhiều sản phẩm, và nhiều sản phẩm có thể được cung cấp bởi nhiều nhà cung cấp).
- Nhà cung cấp: Tham gia một phần. Không phải nhà cung cấp nào cũng cung cấp tất cả các sản phẩm.
- Sản phẩm: Tham gia toàn phần. Mỗi sản phẩm cần có ít nhất một nhà cung cấp.

3. Sản phẩm (Product) và Đơn hàng (Order):

- Tên liên kết: "Bao gồm" (Includes)
- Mô tả: Một đơn hàng có thể bao gồm nhiều sản phẩm, và một sản phẩm có thể có trong nhiều đơn hàng.
- Cardinality: M : N (Một đơn hàng có thể chứa nhiều sản phẩm, và một sản phẩm có thể nằm trong nhiều đơn hàng).
- Sản phẩm: Tham gia toàn phần. Mỗi sản phẩm phải thuộc ít nhất một đơn hàng nếu nó đã được bán.
- Đơn hàng: Tham gia toàn phần. Mỗi đơn hàng phải chứa ít nhất một sản phẩm

4. Khách hàng (Customer) và Đơn hàng (Order):

- Tên liên kết: "Đặt hàng" (Places)
- Mô tả: Một khách hàng có thể đặt nhiều đơn hàng, nhưng mỗi đơn hàng chỉ thuộc về một khách hàng.
- Cardinality: 1 : N (Một khách hàng có thể có nhiều đơn hàng, nhưng mỗi đơn hàng chỉ thuộc về một khách hàng).
- Khách hàng: Tham gia một phần. Không phải khách hàng nào cũng đặt đơn hàng.
- Đơn hàng: Tham gia toàn phần. Mỗi đơn hàng phải thuộc về một khách hàng.

5. Đơn hàng (Order) và Hóa đơn (Bill):

- Tên liên kết: "Có" (Has)
- Mô tả: Mỗi đơn hàng chỉ có thể có nhiều hóa đơn, và mỗi hóa đơn chỉ liên quan đến một đơn hàng.
- Cardinality: 1 : N (Mỗi đơn hàng tương ứng với một hóa đơn và ngược lại).
- Đơn hàng: Tham gia toàn phần. Mỗi đơn hàng đều phải có một hoá đơn.
- Hoá đơn: Tham gia toàn phần. Mỗi hoá đơn phải gắn liền với một đơn hàng.

6. Kho hàng (Warehouse) và Sản phẩm (Product):

- Tên liên kết: "Lưu trữ" (Stores)
- Mô tả: Một kho có thể chứa nhiều sản phẩm, nhưng mỗi sản phẩm chỉ được lưu trữ tại một kho.
- Cardinality: 1 : N (Một kho có thể lưu trữ nhiều sản phẩm, mỗi sản phẩm chỉ lưu trữ tại một kho).
- Kho hàng: Tham gia một phần. Không phải tất cả các kho đều chứa sản phẩm.
- Sản phẩm: Tham gia toàn phần. Mỗi sản phẩm phải được lưu trữ tại một kho.

7. Nhân viên (Employee) và Kho hàng (Warehouse):

- Tên liên kết: "Quản lý" (Manages)
- Mô tả: Một nhân viên có thể quản lý nhiều kho, nhưng mỗi kho chỉ có một nhân viên quản lý.
- Cardinality: 1 : N (Một nhân viên có thể quản lý nhiều kho, nhưng mỗi kho chỉ có một nhân viên quản lý).
- Nhân viên: Tham gia một phần. Không phải tất cả nhân viên đều quản lý kho.
- Kho hàng: Tham gia toàn phần. Mỗi kho phải được quản lý bởi một nhân viên.

#### 1.2.2.4 Sơ đồ ER

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/So_do_ER.png" alt="Sơ đồ ER" width="700">
</p>
<p align="center"><b>Bảng 1 - Sơ đồ ER</b></p>

## 1.3 Chuyển đổi ER-diagram sang mô hình quan hệ

### 1.3.1 Xác định các thực thể trong sơ đồ ER

Trong sơ đồ ER (Hình 1), các thực thể được xác định bao gồm:

Employee: Nhân viên

- Thuộc tính: Employee_ID, Name, Position, Phone_Number, Email.
- Khóa chính (Primary Key): Employee_ID.

Warehouse: Lưu trữ hàng hóa.

- Thuộc tính: Warehouse_ID, Address, Status.
- Khóa chính: Warehouse_ID.

Supplier: Nhà cung cấp hàng hóa.

- Thuộc tính: Supplier_ID, Name, Address, Phone_Number, Email.
- Khóa chính: Supplier_ID.

Product: Sản phẩm.

- Thuộc tính: Product_ID, Product_Category_Name, Price.
- Khóa chính: Product_ID.

Customer: Khách hàng.

- Thuộc tính: Customer_ID, Name, Phone_Number, Email.
- Khóa chính: Customer_ID.

Orders: Đơn hàng được đặt bởi khách hàng.

- Thuộc tính: Order_ID, Order_Date, Total_Amount.
- Khóa chính: Order_ID.

Bill: Hóa đơn gắn với đơn hàng.

- Thuộc tính: Bill_ID, Amount, Payment.
- Khóa chính: Bill_ID.

### 1.3.2 Chuyển đổi các mối quan hệ trong sơ đồ ER

Mối quan hệ giữa Employee và Warehouse:

- Mối quan hệ 1:N (Employee quản lý nhiều Warehouse).
- Giải pháp: Thêm khóa ngoại Employee_ID vào bảng Warehouse để tham chiếu đến bảng Employee.

Mối quan hệ giữa Warehouse và Product:

- Mối quan hệ 1:N (một Warehouse chứa nhiều Product).
- Giải pháp: Thêm khóa ngoại Warehouse_ID vào bảng Product để tham chiếu đến bảng Warehouse.

Mối quan hệ giữa Supplier và Product

- Mối quan hệ N:M (một Supplier cung cấp nhiều Product, một Product được cung cấp bởi nhiều Supplier).
- Giải pháp: Tạo bảng trung gian Supplier_Product với:
  - Thuộc tính: Supplier_ID, Product_ID.
  - Khóa chính là tổ hợp của Supplier_ID và Product_ID.
  - Cả hai cột này đều là khóa ngoại tham chiếu đến bảng Supplier và Product.

Mối quan hệ giữa Customer và Orders:

- Mối quan hệ 1:N (một Customer có thể đặt nhiều Orders).
- Giải pháp: Thêm khóa ngoại Customer_ID vào bảng Orders để tham chiếu đến bảng Customer.

Mối quan hệ giữa Orders và Product:

- Mối quan hệ N:M (một Order có thể bao gồm nhiều Product, một Product có thể thuộc nhiều Order).
- Giải pháp: Tạo bảng trung gian Order_Product với:
  - Thuộc tính: Order_ID, Product_ID.
  - Khóa chính là tổ hợp của Order_ID và Product_ID.
  - Cả hai cột này đều là khóa ngoại tham chiếu đến bảng Orders và Product.
 

Mối quan hệ giữa Orders và Bill:

- Mối quan hệ 1:1 (mỗi Order có một Bill tương ứng).
- Giải pháp: Thêm khóa ngoại Order_ID vào bảng Bill để tham chiếu đến bảng Orders.

- Mỗi thực thể trong ER-diagram sẽ được chuyển thành một bảng. Các thuộc tính của thực thể sẽ trở thành các cột của bảng, và khoá chính của thực thể sẽ trở thành khoá chính của bảng.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Database/BMCSDL2/entity-relationship_method/image/mo_hinh_quan_he.png" alt="Mô hình quan hệ" width="700">
</p>
<p align="center"><b>Bảng 2 - Mô hình quan hệ</b></p>


## 1.4 Chuyển đổi quan hệ cơ sở dữ liệu sang 3NF.

**Để kiểm tra xem mô hình quan hệ đã đạt chuẩn 3NF (Third Normal Form) hay chưa, chúng ta cần xem xét các điều kiện của chuẩn 3NF:**

**- Đạt chuẩn 1NF:** Mỗi bảng trong mô hình phải có cấu trúc dạng bảng, với mỗi giá trị trong các cột phải là đơn trị (không có cột chứa các giá trị lặp hoặc nhóm giá trị lồng nhau). Đồng thời, bảng phải có khóa chính (Primary Key - PK) để đảm bảo mỗi dòng là duy nhất.

**- Đạt chuẩn 2NF:** Bảng phải đạt chuẩn 1NF và tất cả các thuộc tính không khóa phải phụ thuộc hoàn toàn vào khóa chính. Nói cách khác, không có thuộc tính không khóa nào phụ thuộc vào một phần của khóa chính (tránh phụ thuộc một phần).

**- Đạt chuẩn 3NF:** Bảng phải đạt chuẩn 2NF và không có phụ thuộc bắc cầu giữa các thuộc tính không khóa. Nghĩa là, tất cả các thuộc tính không khóa phải phụ thuộc trực tiếp vào khóa chính, không phụ thuộc vào các thuộc tính không khóa khác.

 Phân tích mô hình quan hệ để kiểm tra 3NF

Chúng ta sẽ xem xét từng bảng trong mô hình đã thiết kế để đảm bảo không vi phạm các điều kiện của chuẩn 3NF.

1. Bảng Employee

- Thuộc tính: Employee_ID (PK), Name, Position, Phone_Number, Email
- Phụ thuộc hàm: Tất cả các thuộc tính (Name, Position, Phone_Number, Email) đều phụ thuộc trực tiếp vào Employee_ID, và không có phụ thuộc bắc cầu.
- Kết luận: Đạt chuẩn 3NF.

2. Bảng Supplier

- Thuộc tính: Supplier_ID (PK), Name, Address, Phone_Number, Email
- Phụ thuộc hàm: Tất cả các thuộc tính (Name, Address, Phone_Number, Email) phụ thuộc trực tiếp vào Supplier_ID, không có phụ thuộc bắc cầu.
- Kết luận: Đạt chuẩn 3NF.

3. Bảng Product

- Thuộc tính: Product_ID (PK), Product_Category_Name, Price, Warehouse_ID (FK)
- Phụ thuộc hàm:
  -  Tất cả các thuộc tính (Product_Category_Name, Price, Warehouse_ID) đều phụ thuộc trực tiếp vào Product_ID.
  -  Không có thuộc tính nào phụ thuộc vào thuộc tính khác ngoài khóa chính.
-  Kết luận: Đạt chuẩn 3NF.

4. Bảng Customer

- Thuộc tính: Customer_ID (PK), Name, Phone_Number, Email
- Phụ thuộc hàm: Tất cả các thuộc tính phụ thuộc trực tiếp vào Customer_ID, không có phụ thuộc bắc cầu.
- Kết luận: Đạt chuẩn 3NF.

5.  Bảng Order

- Thuộc tính: Order_ID (PK), Order_Date, Total_Amount, Customer_ID (FK), Employee_ID (FK)
- Phụ thuộc hàm:
  - Tất cả các thuộc tính (Order_Date, Total_Amount, Customer_ID, Employee_ID) đều phụ thuộc trực tiếp vào Order_ID.
  - Không có thuộc tính nào phụ thuộc vào thuộc tính khác ngoài khóa chính.
- Kết luận: Đạt chuẩn 3NF.

6. Bảng Bill

- Thuộc tính: Bill_ID (PK), Amount, Payment_Method, Order_ID (FK)
- Phụ thuộc hàm:
  - Tất cả các thuộc tính (Amount, Payment_Method, Order_ID) đều phụ thuộc trực tiếp vào Bill_ID.
  - Không có thuộc tính nào phụ thuộc vào thuộc tính khác ngoài khóa chính.
- Kết luận: Đạt chuẩn 3NF.

7. Bảng Warehouse

- Thuộc tính: Warehouse_ID (PK), Address, Status, Employee_ID (FK)
- Phụ thuộc hàm:
  - Tất cả các thuộc tính (Address, Status, Employee_ID) đều phụ thuộc trực tiếp vào Warehouse_ID.
  - Không có phụ thuộc bắc cầu.
- Kết luận: Đạt chuẩn 3NF.

8. Bảng trung gian Order_Product

- Thuộc tính: Order_ID (PK, FK), Product_ID (PK, FK)
- Không có thuộc tính không khóa, bảng này chỉ chứa các khóa ngoại liên kết, nên không cần kiểm tra thêm về 3NF.

9. Bảng trung gian Supplier_Product

- Thuộc tính: Supplier_ID (PK, FK), Product_ID (PK, FK)
- Không có thuộc tính không khóa, bảng này chỉ chứa các khóa ngoại liên kết, nên không cần kiểm tra thêm về 3NF.

**Tổng kết**

Tất cả các bảng trong mô hình quan hệ trên đều đạt chuẩn 3NF. Không có bảng nào vi phạm điều kiện của chuẩn 3NF như phụ thuộc bắc cầu hoặc phụ thuộc một phần vào khóa chính.

## 1.5 Tạo chế độ xem

### 1.5.1 View dành cho Nhân viên bán hàng (Sales Employee View)

**Mục đích:**

Chế độ xem này cung cấp cho nhân viên bán hàng thông tin về các đơn hàng mà họ đã xử lý, bao gồm thông tin chi tiết về khách hàng, ngày đặt hàng, tổng số tiền đơn hàng, và trạng thái của đơn hàng. Nhân viên bán hàng có thể dùng view này để theo dõi tiến độ của các đơn hàng và liên hệ khách hàng nếu cần thiết.

*Dữ liệu hiển thị:**

- Employee_ID, Employee_Name: ID và tên của nhân viên bán hàng.
- Order_ID, Order_Date, Total_Amount: ID của đơn hàng, ngày đặt hàng, và tổng số tiền của đơn hàng.
- Customer_ID, Customer_Name, Customer_Phone, Customer_Email: ID, tên, số điện thoại và email của khách hàng.

### 1.5.2. View dành cho Quản lý kho (Warehouse Manager View)

**Mục đích:**

Chế độ xem này cho phép quản lý kho theo dõi thông tin về các sản phẩm đang được lưu trữ trong kho và tình trạng của kho. View này giúp họ kiểm soát hiệu quả việc quản lý hàng tồn kho và đánh giá tình trạng lưu trữ của sản phẩm.

**Dữ liệu hiển thị:**

- Warehouse_ID, Warehouse_Address, Warehouse_Status: ID, địa chỉ và trạng thái của kho hàng.
- Product_ID, Product_Category_Name, Price: ID sản phẩm, tên danh mục sản phẩm, và giá sản phẩm.

### 1.5.3 View dành cho Khách hàng (Customer View)

**Mục đích:**

View này cho phép khách hàng xem lịch sử mua hàng của họ, bao gồm thông tin về các đơn hàng đã đặt và chi tiết hóa đơn tương ứng. Nó giúp khách hàng theo dõi các giao dịch đã thực hiện và các phương thức thanh toán.

**Dữ liệu hiển thị:**

- Customer_ID, Customer_Name: ID và tên của khách hàng.
- Order_ID, Order_Date, Total_Amount: ID đơn hàng, ngày đặt hàng, và tổng số tiền của đơn hàng.
- Bill_ID, Bill_Amount, Payment_Method: ID hóa đơn, số tiền hóa đơn, và phương thức thanh toán.

### 1.5.4 View dành cho Quản lý nhà cung cấp (Supplier Manager View)

**Mục đích:**

View này cho phép quản lý nhà cung cấp theo dõi thông tin về các nhà cung cấp và sản phẩm mà họ cung cấp. Quản lý nhà cung cấp có thể sử dụng view này để kiểm tra thông tin về các nhà cung cấp và sản phẩm đang được nhập từ các đối tác.

**Dữ liệu hiển thị:**

- Supplier_ID, Supplier_Name, Supplier_Phone: ID, tên và số điện thoại của nhà cung cấp.
- Product_ID, Product_Category_Name, Price: ID sản phẩm, danh mục sản phẩm, và giá sản phẩm mà nhà cung cấp cung cấp.

# 2. Triển khai cơ sở dữ liệu trong DBMS

## 2.1 Chọn hệ quản trị cơ sở dữ liệu (DBMS)

- Sử dụng PostgreSQL
- Lý do sử dụng: PostgreSQL là một hệ quản trị cơ sở dữ liệu quan hệ mạnh mẽ, mã nguồn mở và tuân thủ chuẩn SQL. Nó có khả năng xử lý các cơ sở dữ liệu phức tạp, hỗ trợ đa người dùng và tích hợp tốt với các ngôn ngữ lập trình. PostgreSQL cũng được sử dụng rộng rãi trong các dự án thực tế nhờ khả năng mở rộng và bảo mật tốt.

## 2.2 Tạo cấu trúc cơ sở dữ liệu

Kết nối cơ sở dữ liệu:

```bash
sudo systemctl enable --now postgresql.service
[sudo] password for chu: 
Synchronizing state of postgresql.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable postgresql
```

```bash
sudo su postgres -c psql
psql (16.4 (Ubuntu 16.4-1.pgdg22.04+1))
```

Tạo cơ sở dữ liệu

```SQL
create database coffee_shop_db
with
owner = postgres
encoding = 'UTF8'
tablespace = pg_default
connection limit = -1
is_template = False;
```

```SQL
postgres=# \c coffee_shop_db 
You are now connected to database "coffee_shop_db" as user "postgres".
coffee_shop_db=# 
```

### 2.2.1 Code tạo các bảng 

Bảng nhân viên

```sql
CREATE TABLE Employee (
    Employee_ID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Position VARCHAR(50) NOT NULL,
    Phone_Number VARCHAR(13),
    Email VARCHAR(100)
);
```

Bảng Supplier
```sql
CREATE TABLE Supplier (
    Supplier_ID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Address VARCHAR(255),
    Phone_Number VARCHAR(13),
    Email VARCHAR(100)
);
```
Bảng Warehouse
```sql
CREATE TABLE Warehouse (
    Warehouse_ID SERIAL PRIMARY KEY,
    Address VARCHAR(255) NOT NULL,
    Status VARCHAR(50),
    Employee_ID INTEGER
);
```

Bảng Product
```sql
CREATE TABLE Product (
    Product_ID SERIAL PRIMARY KEY,
    Product_Category_Name VARCHAR(100) NOT NULL,
    Price NUMERIC(10, 2) NOT NULL,
    Warehouse_ID INTEGER
);
```
Bảng Customer
```sql
CREATE TABLE Customer (
    Customer_ID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Phone_Number VARCHAR(15),
    Email VARCHAR(100)
);
```

Bảng Orders
```sql
CREATE TABLE Orders(
    Order_ID SERIAL PRIMARY KEY,
    Order_Date DATE NOT NULL,
    Total_Amount NUMERIC(10, 2) NOT NULL,
    Customer_ID INTEGER,
    Employee_ID INTEGER
);
```
Bảng Bill
```sql
CREATE TABLE Bill (
    Bill_ID SERIAL PRIMARY KEY,
    Amount NUMERIC(10, 2) NOT NULL,
    Payment_Method VARCHAR(50) NOT NULL,
    Order_ID INTEGER
);
```

Bảng liên kết giữa bảng Orders và bảng Product
```sql
CREATE TABLE Order_Product (
    Order_ID INTEGER,
    Product_ID INTEGER,
    PRIMARY KEY (Order_ID, Product_ID)
);
```

- Bảng liên kết giữa bảng Supplier và Product
```sql
CREATE TABLE Supplier_Product (
    Supplier_ID INTEGER,
    Product_ID INTEGER,
    PRIMARY KEY (Supplier_ID, Product_ID)
);
```

Ta có các bảng như sau:

```sql
coffee_shop_db=# \dt
              List of relations
 Schema |       Name       | Type  |  Owner   
--------+------------------+-------+----------
 public | bill             | table | postgres
 public | customer         | table | postgres
 public | employee         | table | postgres
 public | order_product    | table | postgres
 public | orders           | table | postgres
 public | product          | table | postgres
 public | supplier         | table | postgres
 public | supplier_product | table | postgres
 public | warehouse        | table | postgres
(9 rows)
```

### 2.2.2 Code nhập dữ liệu vào bảng

- Bảng employee

```sql
INSERT INTO Employee (Name, Position, Phone_Number, Email) VALUES
('Алексей Иванов', 'Sales Staff', '+84410621704', 'alekseyivanov@mail.ru'),
('Дмитрий Соколов', 'Sales Staff', '+84804504364', 'dmitriysokolov@mail.ru'),
('Екатерина Смирнова', 'Sales Staff', '+84637892756', 'ekaterinasmirnova@mail.ru'),
('Анна Петрова', 'Sales Staff', '+84116278986', 'annapetrova@mail.ru'),
('Иван Васильев', 'Sales Staff', '+84463544856', 'ivanvasilev@mail.ru'),
('Мария Кузнецова', 'Sales Staff', '+84726549107', 'mariyakuznetsova@mail.ru'),
('Ольга Попова', 'Sales Staff', '+84913287564', 'olgapopova@mail.ru'),
('Сергей Федоров', 'Warehouse Manager', '+84892657481', 'sergeyfedorov@mail.ru'),
('Николай Григорьев', 'Warehouse Manager', '+84652718462', 'nikolaygrigoriev@mail.ru'),
('Владимир Николаев', 'Warehouse Manager', '+84187365942', 'vladimirnikolaev@mail.ru');
```

- Bảng supplier

```sql
INSERT INTO Supplier (Name, Address, Phone_Number, Email) VALUES
('ООО РусКофе', 'ул. 80-15, Москва, Россия', '+84867010843', 'oooruskofe@mail.ru'),
('ЗАО ЧайКофе', 'ул. 100-16, Москва, Россия', '+84625548793', 'zaochaykofe@mail.ru'),
('ИП Васильев Торг', 'ул. 25-5, Москва, Россия', '+84534269602', 'ipvasilevtorg@mail.ru'),
('ТД Бариста', 'ул. 18-45, Москва, Россия', '+84919114853', 'tdbarista@mail.ru'),
('КофеТрейд', 'ул. 97-24, Москва, Россия', '+84992880427', 'kofetreyd@mail.ru'),
('СоюзКофе', 'ул. 59-42, Москва, Россия', '+84731450928', 'soyuzkofe@mail.ru'),
('МирКофе', 'ул. 38-35, Москва, Россия', '+84713090284', 'mirkofe@mail.ru'),
('ЭспрессоЭкспорт', 'ул. 47-9, Москва, Россия', '+84890236452', 'espressoeksport@mail.ru'),
('ЗАО Черный Жемчуг', 'ул. 64-17, Москва, Россия', '+84938572461', 'zaochernyjzhemchug@mail.ru'),
('Кофейный Дом', 'ул. 29-31, Москва, Россия', '+84719530678', 'kofejnyjdom@mail.ru');
```

- Bảng warehouse

```sql
INSERT INTO Warehouse (Address, Status, Employee_ID) VALUES
('ул. 97-4, Москва, Россия', 'Inactive', 9),
('ул. 38-11, Москва, Россия', 'Active', 9),
('ул. 97-13, Москва, Россия', 'Inactive', 8),
('ул. 24-37, Москва, Россия', 'Inactive', 10),
('ул. 58-40, Москва, Россия', 'Active', 10);
```

- Bảng product

```sql
INSERT INTO Product (Product_Category_Name, Price, Warehouse_ID) VALUES
('Арабика', 481.21, 1),
('Капучино', 549.51, 1),
('Латте', 778.31, 5),
('Капучино', 114.89, 5),
('Робуста', 465.66, 5),
('Эспрессо', 982.47, 3),
('Робуста', 347.12, 2),
('Капучино', 853.89, 1),
('Арабика', 616.37, 4),
('Латте', 239.44, 3);
```

- Bảng customer

```sql
INSERT INTO Customer (Name, Phone_Number, Email) VALUES
('Иван Иванов', '+84347792080', 'ivanivanov@mail.ru'),
('Петр Петров', '+84725742192', 'petrpetrov@mail.ru'),
('Светлана Смирнова', '+84498734272', 'svetlanasmirnova@mail.ru'),
('Елена Кузнецова', '+84451098251', 'elenakuznetsova@mail.ru'),
('Александр Соколов', '+84479531226', 'aleksandrsokolov@mail.ru'),
('Мария Попова', '+84712349852', 'mariyapopova@mail.ru'),
('Николай Федоров', '+84396571482', 'nikolayfedorov@mail.ru'),
('Анна Васильева', '+84578321940', 'annavasilyeva@mail.ru'),
('Дмитрий Григорьев', '+84410239854', 'dmitriygrigorev@mail.ru'),
('Ольга Николаева', '+84765849320', 'olganikolaeva@mail.ru');
```

- Bảng orders

```sql
INSERT INTO Orders (Order_Date, Total_Amount, Customer_ID, Employee_ID) VALUES
('2024-11-08', 1039.79, 9, 5),
('2024-10-28', 1316.75, 9, 4),
('2024-10-31', 3327.25, 10, 4),
('2024-10-24', 3579.22, 9, 3),
('2024-11-08', 2161.28, 6, 6),
('2024-10-26', 3024.59, 2, 6),
('2024-11-06', 4376.18, 7, 5),
('2024-10-29', 2891.04, 3, 1),
('2024-11-04', 3561.47, 1, 7),
('2024-10-30', 4589.87, 5, 3);
```

- Bảng bill

```sql
INSERT INTO Bill (Bill_ID, Amount, Payment_Method, Order_ID) VALUES
(1, 1039.79, 'Bank Transfer', 1),
(2, 1316.75, 'Bank Transfer', 2),
(3, 3327.25, 'Credit Card', 3),
(4, 3579.22, 'Credit Card', 4),
(5, 2161.28, 'Bank Transfer', 5),
(6, 3024.59, 'Cash', 6),
(7, 4376.18, 'Credit Card', 7),
(8, 2891.04, 'Cash', 8),
(9, 3561.47, 'Credit Card', 9),
(10, 4589.87, 'Bank Transfer', 10);
```

- Bảng liên kết giữa bảng Orders và bảng Product

```sql
INSERT INTO Order_Product (Order_ID, Product_ID) VALUES
(1, 2),
(1, 4),
(2, 5),
(2, 1),
(2, 9),
(3, 7),
(3, 3),
(3, 8),
(4, 10),
(4, 6),
(4, 2),
(5, 4),
(5, 1),
(6, 3),
(6, 8),
(6, 5),
(7, 9),
(7, 2),
(7, 10),
(8, 1),
(8, 7),
(9, 6),
(9, 5),
(10, 4),
(10, 3);
```

- Bảng liên kết giữa bảng Supplier và Product

```sql
INSERT INTO Supplier_Product (Supplier_ID, Product_ID) VALUES
(1, 7),
(1, 1),
(1, 10),
(2, 7),
(2, 9),
(2, 2),
(2, 5),
(3, 8),
(3, 4),
(3, 6),
(4, 3),
(4, 1),
(4, 5),
(4, 10),
(5, 9),
(5, 4),
(5, 2),
(5, 6),
(5, 8);
```

## 2.3 Tạo index

 **Liên kết bảng** (JOIN): Thông thường là các cột `Primary Key` và `Foreign Key`.
 **Tìm kiếm hoặc lọc dữ liệu**: Các cột thường xuyên được sử dụng trong các mệnh đề `WHERE`, `ORDER BY`, hoặc `GROUP BY`.



1. Index bảng `Employee`
- **Mục tiêu**: Tăng tốc tìm kiếm theo `Employee_ID`.

```sql
CREATE INDEX idx_employee_id ON Employee (Employee_ID);
CREATE INDEX idx_employee_email ON Employee (Email);
```


2. Index bảng `Supplier`
- **Mục tiêu**: Tăng tốc truy vấn theo `Supplier_ID` và tìm kiếm qua `Name`.

```sql
CREATE INDEX idx_supplier_id ON Supplier (Supplier_ID);
CREATE INDEX idx_supplier_name ON Supplier (Name);
```


3. Index bảng `Warehouse`
- **Mục tiêu**: Tăng tốc liên kết và lọc dữ liệu theo `Employee_ID` và `Warehouse_ID`.

```sql
CREATE INDEX idx_warehouse_id ON Warehouse (Warehouse_ID);
CREATE INDEX idx_warehouse_employee_id ON Warehouse (Employee_ID);
```


4. Index bảng `Product`
- **Mục tiêu**: Tăng tốc tìm kiếm theo `Product_ID`, `Warehouse_ID`, và lọc dữ liệu theo `Price`.

```sql
CREATE INDEX idx_product_id ON Product (Product_ID);
CREATE INDEX idx_product_warehouse_id ON Product (Warehouse_ID);
CREATE INDEX idx_product_price ON Product (Price);
```


5. Index bảng `Customer`
- **Mục tiêu**: Tăng tốc tìm kiếm theo `Customer_ID` và email khách hàng.

```sql
CREATE INDEX idx_customer_id ON Customer (Customer_ID);
CREATE INDEX idx_customer_email ON Customer (Email);
```


6. Index bảng `Orders`
- **Mục tiêu**: Tăng tốc liên kết và lọc dữ liệu theo `Order_ID`, `Customer_ID`, và `Employee_ID`.

```sql
CREATE INDEX idx_orders_id ON Orders (Order_ID);
CREATE INDEX idx_orders_customer_id ON Orders (Customer_ID);
CREATE INDEX idx_orders_employee_id ON Orders (Employee_ID);
```


7. Index bảng `Bill`
- **Mục tiêu**: Tăng tốc liên kết với bảng `Orders` và tìm kiếm theo `Payment_Method`.

```sql
CREATE INDEX idx_bill_id ON Bill (Bill_ID);
CREATE INDEX idx_bill_order_id ON Bill (Order_ID);
CREATE INDEX idx_bill_payment_method ON Bill (Payment_Method);
```

8. Index bảng `Order_Product`
- **Mục tiêu**: Tăng tốc liên kết giữa `Orders` và `Product`.

```sql
CREATE INDEX idx_order_product_order_id ON Order_Product (Order_ID);
CREATE INDEX idx_order_product_product_id ON Order_Product (Product_ID);
```


9. Index bảng `Supplier_Product`
- **Mục tiêu**: Tăng tốc liên kết giữa `Supplier` và `Product`.

```sql
CREATE INDEX idx_supplier_product_supplier_id ON Supplier_Product (Supplier_ID);
CREATE INDEX idx_supplier_product_product_id ON Supplier_Product (Product_ID);
```

## 2.4 Thiết lập mối quan hệ giữa các bảng

Để thiết lập mối quan hệ giữa các bảng trong cơ sở dữ liệu PostgreSQL, chúng ta sẽ sử dụng các **Foreign Key** (khóa ngoại). Điều này giúp duy trì tính toàn vẹn dữ liệu và thể hiện các mối quan hệ giữa các bảng.


1. Mối quan hệ giữa `Warehouse` và `Employee`
- **Mô tả**: Một nhân viên (`Employee`) quản lý một hoặc nhiều kho (`Warehouse`).
- **Mối quan hệ**: 1:N.

```sql
ALTER TABLE Warehouse
ADD CONSTRAINT fk_warehouse_employee
FOREIGN KEY (Employee_ID)
REFERENCES Employee (Employee_ID)
ON DELETE SET NULL;
```


2. Mối quan hệ giữa `Product` và `Warehouse`
- **Mô tả**: Một sản phẩm (`Product`) được lưu trữ trong một kho (`Warehouse`).
- **Mối quan hệ**: 1:N.

```sql
ALTER TABLE Product
ADD CONSTRAINT fk_product_warehouse
FOREIGN KEY (Warehouse_ID)
REFERENCES Warehouse (Warehouse_ID)
ON DELETE CASCADE;
```


3. Mối quan hệ giữa `Orders` và `Customer`
- **Mô tả**: Một khách hàng (`Customer`) có thể đặt nhiều đơn hàng (`Orders`).
- **Mối quan hệ**: 1:N.

```sql
ALTER TABLE Orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (Customer_ID)
REFERENCES Customer (Customer_ID)
ON DELETE CASCADE;
```


4. Mối quan hệ giữa `Orders` và `Employee`
- **Mô tả**: Một nhân viên (`Employee`) xử lý nhiều đơn hàng (`Orders`).
- **Mối quan hệ**: 1:N.

```sql
ALTER TABLE Orders
ADD CONSTRAINT fk_orders_employee
FOREIGN KEY (Employee_ID)
REFERENCES Employee (Employee_ID)
ON DELETE SET NULL;
```


5. Mối quan hệ giữa `Bill` và `Orders`
- **Mô tả**: Một hóa đơn (`Bill`) thuộc về một đơn hàng (`Orders`).
- **Mối quan hệ**: 1:N.

```sql
ALTER TABLE Bill
ADD CONSTRAINT fk_bill_order
FOREIGN KEY (Order_ID)
REFERENCES Orders (Order_ID)
ON DELETE CASCADE;
```


6. Mối quan hệ giữa `Order_Product` và `Orders`, `Product`
- **Mô tả**: Liên kết giữa các đơn hàng (`Orders`) và sản phẩm (`Product`) thông qua bảng trung gian `Order_Product`.
- **Mối quan hệ**: N:M.

```sql
ALTER TABLE Order_Product
ADD CONSTRAINT fk_order_product_order
FOREIGN KEY (Order_ID)
REFERENCES Orders (Order_ID)
ON DELETE CASCADE;

ALTER TABLE Order_Product
ADD CONSTRAINT fk_order_product_product
FOREIGN KEY (Product_ID)
REFERENCES Product (Product_ID)
ON DELETE CASCADE;
```


7. Mối quan hệ giữa `Supplier_Product` và `Supplier`, `Product`
- **Mô tả**: Liên kết giữa các nhà cung cấp (`Supplier`) và sản phẩm (`Product`) thông qua bảng trung gian `Supplier_Product`.
- **Mối quan hệ**: N:M.

```sql
ALTER TABLE Supplier_Product
ADD CONSTRAINT fk_supplier_product_supplier
FOREIGN KEY (Supplier_ID)
REFERENCES Supplier (Supplier_ID)
ON DELETE CASCADE;

ALTER TABLE Supplier_Product
ADD CONSTRAINT fk_supplier_product_product
FOREIGN KEY (Product_ID)
REFERENCES Product (Product_ID)
ON DELETE CASCADE;
```


Ghi chú:
- **`ON DELETE CASCADE`**: Khi dữ liệu trong bảng cha bị xóa, các bản ghi liên quan trong bảng con cũng sẽ bị xóa.
- **`ON DELETE SET NULL`**: Khi dữ liệu trong bảng cha bị xóa, cột khóa ngoại trong bảng con sẽ được đặt thành `NULL`.

## 2.5 Test queries -  kiểm tra cơ sở dữ liệu

Dưới đây là một số truy vấn mẫu (test queries) để kiểm tra cơ sở dữ liệu của bạn sau khi thiết lập xong:

---

1.  Xem tất cả thông tin về nhân viên trong bảng `Employee`.

```sql
SELECT * FROM Employee;
```

```sql
coffee_shop_db=# select * from employee;
 employee_id |        name        |     position      | phone_number |           email           
-------------+--------------------+-------------------+--------------+---------------------------
           1 | Алексей Иванов     | Sales Staff       | +84410621704 | alekseyivanov@mail.ru
           2 | Дмитрий Соколов    | Sales Staff       | +84804504364 | dmitriysokolov@mail.ru
           3 | Екатерина Смирнова | Sales Staff       | +84637892756 | ekaterinasmirnova@mail.ru
           4 | Анна Петрова       | Sales Staff       | +84116278986 | annapetrova@mail.ru
           5 | Иван Васильев      | Sales Staff       | +84463544856 | ivanvasilev@mail.ru
           6 | Мария Кузнецова    | Sales Staff       | +84726549107 | mariyakuznetsova@mail.ru
           7 | Ольга Попова       | Sales Staff       | +84913287564 | olgapopova@mail.ru
           8 | Сергей Федоров     | Warehouse Manager | +84892657481 | sergeyfedorov@mail.ru
           9 | Николай Григорьев  | Warehouse Manager | +84652718462 | nikolaygrigoriev@mail.ru
          10 | Владимир Николаев  | Warehouse Manager | +84187365942 | vladimirnikolaev@mail.ru
(10 rows)
```


2. Lọc danh sách nhân viên có chức vụ là "Sales Staff"

```sql
SELECT Name, Position, Phone_Number, Email
FROM Employee
WHERE Position = 'Sales Staff';
```
```sql
        name        |  position   | phone_number |           email           
--------------------+-------------+--------------+---------------------------
 Алексей Иванов     | Sales Staff | +84410621704 | alekseyivanov@mail.ru
 Дмитрий Соколов    | Sales Staff | +84804504364 | dmitriysokolov@mail.ru
 Екатерина Смирнова | Sales Staff | +84637892756 | ekaterinasmirnova@mail.ru
 Анна Петрова       | Sales Staff | +84116278986 | annapetrova@mail.ru
 Иван Васильев      | Sales Staff | +84463544856 | ivanvasilev@mail.ru
 Мария Кузнецова    | Sales Staff | +84726549107 | mariyakuznetsova@mail.ru
 Ольга Попова       | Sales Staff | +84913287564 | olgapopova@mail.ru
(7 rows)
```

3.  Tìm danh sách các kho hàng có trạng thái "Active" cùng với tên quản lý.

```sql
SELECT w.Warehouse_ID, w.Address, w.Status, e.Name AS Manager_Name
FROM Warehouse w
JOIN Employee e ON w.Employee_ID = e.Employee_ID
WHERE w.Status = 'Active';
```
```sql
 warehouse_id |          address          | status |   manager_name    
--------------+---------------------------+--------+-------------------
            2 | ул. 38-11, Москва, Россия | Active | Николай Григорьев
            5 | ул. 58-40, Москва, Россия | Active | Владимир Николаев
(2 rows)
```

4.  Xem danh sách sản phẩm cùng với thông tin kho lưu trữ.

```sql
SELECT p.Product_ID, p.Product_Category_Name, p.Price, w.Address AS Warehouse_Address
FROM Product p
JOIN Warehouse w ON p.Warehouse_ID = w.Warehouse_ID;
```
```sql
 product_id | product_category_name | price  |     warehouse_address     
------------+-----------------------+--------+---------------------------
          1 | Арабика               | 481.21 | ул. 97-4, Москва, Россия
          2 | Капучино              | 549.51 | ул. 97-4, Москва, Россия
          3 | Латте                 | 778.31 | ул. 58-40, Москва, Россия
          4 | Капучино              | 114.89 | ул. 58-40, Москва, Россия
          5 | Робуста               | 465.66 | ул. 58-40, Москва, Россия
          6 | Эспрессо              | 982.47 | ул. 97-13, Москва, Россия
          7 | Робуста               | 347.12 | ул. 38-11, Москва, Россия
          8 | Капучино              | 853.89 | ул. 97-4, Москва, Россия
          9 | Арабика               | 616.37 | ул. 24-37, Москва, Россия
         10 | Латте                 | 239.44 | ул. 97-13, Москва, Россия
(10 rows)
```

5.  Hiển thị danh sách các đơn hàng cùng với tên khách hàng đã đặt.

```sql
SELECT o.Order_ID, o.Order_Date, o.Total_Amount, c.Name AS Customer_Name, c.Email AS Customer_Email
FROM Orders o
JOIN Customer c ON o.Customer_ID = c.Customer_ID;
```
```sql
 order_id | order_date | total_amount |   customer_name   |      customer_email      
----------+------------+--------------+-------------------+--------------------------
        1 | 2024-11-08 |      1039.79 | Дмитрий Григорьев | dmitriygrigorev@mail.ru
        2 | 2024-10-28 |      1316.75 | Дмитрий Григорьев | dmitriygrigorev@mail.ru
        3 | 2024-10-31 |      3327.25 | Ольга Николаева   | olganikolaeva@mail.ru
        4 | 2024-10-24 |      3579.22 | Дмитрий Григорьев | dmitriygrigorev@mail.ru
        5 | 2024-11-08 |      2161.28 | Мария Попова      | mariyapopova@mail.ru
        6 | 2024-10-26 |      3024.59 | Петр Петров       | petrpetrov@mail.ru
        7 | 2024-11-06 |      4376.18 | Николай Федоров   | nikolayfedorov@mail.ru
        8 | 2024-10-29 |      2891.04 | Светлана Смирнова | svetlanasmirnova@mail.ru
        9 | 2024-11-04 |      3561.47 | Иван Иванов       | ivanivanov@mail.ru
       10 | 2024-10-30 |      4589.87 | Александр Соколов | aleksandrsokolov@mail.ru
(10 rows)
```


6.  Lọc các đơn hàng do một nhân viên cụ thể xử lý (ví dụ `Employee_ID = 3`).

```sql
SELECT o.Order_ID, o.Order_Date, o.Total_Amount
FROM Orders o
WHERE o.Employee_ID = 3;
```
```sql
 order_id | order_date | total_amount 
----------+------------+--------------
        4 | 2024-10-24 |      3579.22
       10 | 2024-10-30 |      4589.87
(2 rows)
```

7.  Tìm danh sách hóa đơn thuộc về một đơn hàng cụ thể (ví dụ `Order_ID = 5`).

```sql
SELECT b.Bill_ID, b.Amount, b.Payment_Method
FROM Bill b
WHERE b.Order_ID = 5;
```
```sql
bill_id | amount  | payment_method 
---------+---------+----------------
       5 | 2161.28 | Bank Transfer
(1 row)
```

8. Tìm danh sách sản phẩm liên quan đến một đơn hàng cụ thể (ví dụ `Order_ID = 3`).

```sql
SELECT p.Product_ID, p.Product_Category_Name, p.Price
FROM Order_Product op
JOIN Product p ON op.Product_ID = p.Product_ID
WHERE op.Order_ID = 3;
```
```sql
 product_id | product_category_name | price  
------------+-----------------------+--------
          3 | Латте                 | 778.31
          7 | Робуста               | 347.12
          8 | Капучино              | 853.89
(3 rows)
```

9.  Xem danh sách nhà cung cấp và các sản phẩm họ cung cấp.

```sql
SELECT s.Name AS Supplier_Name, p.Product_Category_Name, p.Price
FROM Supplier_Product sp
JOIN Supplier s ON sp.Supplier_ID = s.Supplier_ID
JOIN Product p ON sp.Product_ID = p.Product_ID;
```
```sql
 supplier_name   | product_category_name | price  
------------------+-----------------------+--------
 ООО РусКофе      | Робуста               | 347.12
 ООО РусКофе      | Арабика               | 481.21
 ООО РусКофе      | Латте                 | 239.44
 ЗАО ЧайКофе      | Робуста               | 347.12
 ЗАО ЧайКофе      | Арабика               | 616.37
 ЗАО ЧайКофе      | Капучино              | 549.51
 ЗАО ЧайКофе      | Робуста               | 465.66
 ИП Васильев Торг | Капучино              | 853.89
 ИП Васильев Торг | Капучино              | 114.89
 ИП Васильев Торг | Эспрессо              | 982.47
 ТД Бариста       | Латте                 | 778.31
 ТД Бариста       | Арабика               | 481.21
 ТД Бариста       | Робуста               | 465.66
 ТД Бариста       | Латте                 | 239.44
 КофеТрейд        | Арабика               | 616.37
 КофеТрейд        | Капучино              | 114.89
 КофеТрейд        | Капучино              | 549.51
 КофеТрейд        | Эспрессо              | 982.47
 КофеТрейд        | Капучино              | 853.89
(19 rows)
```

10.  Tính tổng số đơn hàng và tổng giá trị.

```sql
SELECT COUNT(Order_ID) AS Total_Orders, SUM(Total_Amount) AS Total_Amount
FROM Orders;
```
```sql
 total_orders | total_amount 
--------------+--------------
           10 |     29867.44
(1 row)
```

11. Tìm các đơn hàng chứa sản phẩm có tên cụ thể (ví dụ "Арабика").

```sql
SELECT DISTINCT o.Order_ID, o.Order_Date, o.Total_Amount
FROM Orders o
JOIN Order_Product op ON o.Order_ID = op.Order_ID
JOIN Product p ON op.Product_ID = p.Product_ID
WHERE p.Product_Category_Name = 'Арабика';
```
```sql
 order_id | order_date | total_amount 
----------+------------+--------------
        2 | 2024-10-28 |      1316.75
        5 | 2024-11-08 |      2161.28
        7 | 2024-11-06 |      4376.18
        8 | 2024-10-29 |      2891.04
(4 rows)
```

12. Hiển thị danh sách các kho hoạt động cùng với số lượng sản phẩm lưu trữ.

```sql
SELECT w.Warehouse_ID, w.Address, COUNT(p.Product_ID) AS Product_Count
FROM Warehouse w
LEFT JOIN Product p ON w.Warehouse_ID = p.Warehouse_ID
WHERE w.Status = 'Active'
GROUP BY w.Warehouse_ID, w.Address;
```
```sql
 warehouse_id |          address          | product_count 
--------------+---------------------------+---------------
            2 | ул. 38-11, Москва, Россия |             1
            5 | ул. 58-40, Москва, Россия |             3
(2 rows)
```

13. Tìm danh sách khách hàng có nhiều hơn một đơn hàng.

```sql
SELECT c.Customer_ID, c.Name, COUNT(o.Order_ID) AS Order_Count
FROM Customer c
JOIN Orders o ON c.Customer_ID = o.Customer_ID
GROUP BY c.Customer_ID, c.Name
HAVING COUNT(o.Order_ID) > 1;
```
```sql
customer_id |       name        | order_count 
-------------+-------------------+-------------
           9 | Дмитрий Григорьев |           3
(1 row)
```


14. Tính tổng giá trị hóa đơn theo từng phương thức thanh toán.

```sql
SELECT b.Payment_Method, SUM(b.Amount) AS Total_Amount
FROM Bill b
GROUP BY b.Payment_Method;
```
```sql
 payment_method | total_amount 
----------------+--------------
 Credit Card    |     14844.12
 Cash           |      5915.63
 Bank Transfer  |      9107.69
(3 rows)
```

## 2.6 Tạo view



1. View dành cho Nhân viên bán hàng (Sales Employee View)
```sql
CREATE VIEW Sales_Employee_View AS
SELECT 
    e.Employee_ID, 
    e.Name AS Employee_Name,
    o.Order_ID, 
    o.Order_Date, 
    o.Total_Amount,
    c.Customer_ID, 
    c.Name AS Customer_Name, 
    c.Phone_Number AS Customer_Phone, 
    c.Email AS Customer_Email
FROM Employee e
JOIN Orders o ON e.Employee_ID = o.Employee_ID
JOIN Customer c ON o.Customer_ID = c.Customer_ID
WHERE e.Position = 'Sales Staff';
```
```sql
coffee_shop_db=# select * from sales_employee_view ;
 employee_id |   employee_name    | order_id | order_date | total_amount | customer_id |   customer_name   | customer_phone |      customer_email      
-------------+--------------------+----------+------------+--------------+-------------+-------------------+----------------+--------------------------
           7 | Ольга Попова       |        9 | 2024-11-04 |      3561.47 |           1 | Иван Иванов       | +84347792080   | ivanivanov@mail.ru
           6 | Мария Кузнецова    |        6 | 2024-10-26 |      3024.59 |           2 | Петр Петров       | +84725742192   | petrpetrov@mail.ru
           1 | Алексей Иванов     |        8 | 2024-10-29 |      2891.04 |           3 | Светлана Смирнова | +84498734272   | svetlanasmirnova@mail.ru
           3 | Екатерина Смирнова |       10 | 2024-10-30 |      4589.87 |           5 | Александр Соколов | +84479531226   | aleksandrsokolov@mail.ru
           6 | Мария Кузнецова    |        5 | 2024-11-08 |      2161.28 |           6 | Мария Попова      | +84712349852   | mariyapopova@mail.ru
           5 | Иван Васильев      |        7 | 2024-11-06 |      4376.18 |           7 | Николай Федоров   | +84396571482   | nikolayfedorov@mail.ru
           3 | Екатерина Смирнова |        4 | 2024-10-24 |      3579.22 |           9 | Дмитрий Григорьев | +84410239854   | dmitriygrigorev@mail.ru
           4 | Анна Петрова       |        2 | 2024-10-28 |      1316.75 |           9 | Дмитрий Григорьев | +84410239854   | dmitriygrigorev@mail.ru
           5 | Иван Васильев      |        1 | 2024-11-08 |      1039.79 |           9 | Дмитрий Григорьев | +84410239854   | dmitriygrigorev@mail.ru
           4 | Анна Петрова       |        3 | 2024-10-31 |      3327.25 |          10 | Ольга Николаева   | +84765849320   | olganikolaeva@mail.ru
(10 rows)
```


2. View dành cho Quản lý kho (Warehouse Manager View)
```sql
CREATE VIEW Warehouse_Manager_View AS
SELECT 
    w.Warehouse_ID, 
    w.Address AS Warehouse_Address, 
    w.Status AS Warehouse_Status,
    p.Product_ID, 
    p.Product_Category_Name, 
    p.Price
FROM Warehouse w
JOIN Product p ON w.Warehouse_ID = p.Warehouse_ID;
```
```sql
coffee_shop_db=# select * from warehouse_manager_view ;
 warehouse_id |     warehouse_address     | warehouse_status | product_id | product_category_name | price  
--------------+---------------------------+------------------+------------+-----------------------+--------
            1 | ул. 97-4, Москва, Россия  | Inactive         |          1 | Арабика               | 481.21
            1 | ул. 97-4, Москва, Россия  | Inactive         |          2 | Капучино              | 549.51
            5 | ул. 58-40, Москва, Россия | Active           |          3 | Латте                 | 778.31
            5 | ул. 58-40, Москва, Россия | Active           |          4 | Капучино              | 114.89
            5 | ул. 58-40, Москва, Россия | Active           |          5 | Робуста               | 465.66
            3 | ул. 97-13, Москва, Россия | Inactive         |          6 | Эспрессо              | 982.47
            2 | ул. 38-11, Москва, Россия | Active           |          7 | Робуста               | 347.12
            1 | ул. 97-4, Москва, Россия  | Inactive         |          8 | Капучино              | 853.89
            4 | ул. 24-37, Москва, Россия | Inactive         |          9 | Арабика               | 616.37
            3 | ул. 97-13, Москва, Россия | Inactive         |         10 | Латте                 | 239.44
(10 rows)

```

3. View dành cho Khách hàng (Customer View)**
```sql
CREATE VIEW Customer_View AS
SELECT 
    c.Customer_ID, 
    c.Name AS Customer_Name,
    o.Order_ID, 
    o.Order_Date, 
    o.Total_Amount,
    b.Bill_ID, 
    b.Amount AS Bill_Amount, 
    b.Payment_Method
FROM Customer c
JOIN Orders o ON c.Customer_ID = o.Customer_ID
JOIN Bill b ON o.Order_ID = b.Order_ID;
```
```sql
coffee_shop_db=# select * from customer_view ;
 customer_id |   customer_name   | order_id | order_date | total_amount | bill_id | bill_amount | payment_method 
-------------+-------------------+----------+------------+--------------+---------+-------------+----------------
           9 | Дмитрий Григорьев |        1 | 2024-11-08 |      1039.79 |       1 |     1039.79 | Bank Transfer
           9 | Дмитрий Григорьев |        2 | 2024-10-28 |      1316.75 |       2 |     1316.75 | Bank Transfer
          10 | Ольга Николаева   |        3 | 2024-10-31 |      3327.25 |       3 |     3327.25 | Credit Card
           9 | Дмитрий Григорьев |        4 | 2024-10-24 |      3579.22 |       4 |     3579.22 | Credit Card
           6 | Мария Попова      |        5 | 2024-11-08 |      2161.28 |       5 |     2161.28 | Bank Transfer
           2 | Петр Петров       |        6 | 2024-10-26 |      3024.59 |       6 |     3024.59 | Cash
           7 | Николай Федоров   |        7 | 2024-11-06 |      4376.18 |       7 |     4376.18 | Credit Card
           3 | Светлана Смирнова |        8 | 2024-10-29 |      2891.04 |       8 |     2891.04 | Cash
           1 | Иван Иванов       |        9 | 2024-11-04 |      3561.47 |       9 |     3561.47 | Credit Card
           5 | Александр Соколов |       10 | 2024-10-30 |      4589.87 |      10 |     4589.87 | Bank Transfer
(10 rows)
```
---

4. View dành cho Quản lý nhà cung cấp (Supplier Manager View)**
```sql
CREATE VIEW Supplier_Manager_View AS
SELECT 
    s.Supplier_ID, 
    s.Name AS Supplier_Name, 
    s.Phone_Number AS Supplier_Phone,
    p.Product_ID, 
    p.Product_Category_Name, 
    p.Price
FROM Supplier s
JOIN Supplier_Product sp ON s.Supplier_ID = sp.Supplier_ID
JOIN Product p ON sp.Product_ID = p.Product_ID;
```
```sql
coffee_shop_db=# select * from supplier_manager_view ;
 supplier_id |  supplier_name   | supplier_phone | product_id | product_category_name | price  
-------------+------------------+----------------+------------+-----------------------+--------
           1 | ООО РусКофе      | +84867010843   |          7 | Робуста               | 347.12
           1 | ООО РусКофе      | +84867010843   |          1 | Арабика               | 481.21
           1 | ООО РусКофе      | +84867010843   |         10 | Латте                 | 239.44
           2 | ЗАО ЧайКофе      | +84625548793   |          7 | Робуста               | 347.12
           2 | ЗАО ЧайКофе      | +84625548793   |          9 | Арабика               | 616.37
           2 | ЗАО ЧайКофе      | +84625548793   |          2 | Капучино              | 549.51
           2 | ЗАО ЧайКофе      | +84625548793   |          5 | Робуста               | 465.66
           3 | ИП Васильев Торг | +84534269602   |          8 | Капучино              | 853.89
           3 | ИП Васильев Торг | +84534269602   |          4 | Капучино              | 114.89
           3 | ИП Васильев Торг | +84534269602   |          6 | Эспрессо              | 982.47
           4 | ТД Бариста       | +84919114853   |          3 | Латте                 | 778.31
           4 | ТД Бариста       | +84919114853   |          1 | Арабика               | 481.21
           4 | ТД Бариста       | +84919114853   |          5 | Робуста               | 465.66
           4 | ТД Бариста       | +84919114853   |         10 | Латте                 | 239.44
           5 | КофеТрейд        | +84992880427   |          9 | Арабика               | 616.37
           5 | КофеТрейд        | +84992880427   |          4 | Капучино              | 114.89
           5 | КофеТрейд        | +84992880427   |          2 | Капучино              | 549.51
           5 | КофеТрейд        | +84992880427   |          6 | Эспрессо              | 982.47
           5 | КофеТрейд        | +84992880427   |          8 | Капучино              | 853.89
(19 rows)

```

# 3. Bảo mật cơ sở dữ liệu

## 3.1 Giám sát cơ sở dữ liệu
### 3.1.1 Tạo bảng log

Bảng Log được sử dụng để lưu lại thông tin về các thay đổi, sự kiện, lỗi, hoặc các hành động xảy ra trong cơ sở dữ liệu. Bảng này rất hữu ích cho việc kiểm tra, theo dõi hoạt động của người dùng và phân tích.

```sql
CREATE TABLE main_log (
    log_id SERIAL PRIMARY KEY,                 -- ID duy nhất cho mỗi log
    operation_type TEXT,                       -- Loại thao tác (INSERT, UPDATE, DELETE)
    operation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Thời gian thực hiện thao tác
    user_operator TEXT,                        -- Người thực hiện thao tác
    changed_data JSON                          -- Dữ liệu bị thay đổi
);

```


### 3.1.2 Hàm ghi log
Tạo hàm `log_changes()` để ghi thông tin vào bảng log. Hàm này sẽ xử lý các sự kiện `INSERT`, `UPDATE` và `DELETE`.

```sql
CREATE OR REPLACE FUNCTION logging() RETURNS TRIGGER AS $logging$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('DELETE', current_user, row_to_json(OLD));
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('UPDATE', current_user, row_to_json(NEW));
    ELSIF (TG_OP = 'INSERT') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('INSERT', current_user, row_to_json(NEW));
    END IF;
    RETURN NULL;
END;
$logging$ LANGUAGE plpgsql;


```

### 3.1.3 Tạo trigger cho từng bảng

- Trigger cho bảng `Employee`
  
```sql
CREATE TRIGGER employee_logging
AFTER INSERT OR UPDATE OR DELETE ON Employee
FOR EACH ROW EXECUTE FUNCTION logging();
```


- Trigger cho bảng `Supplier`
 
```sql
CREATE TRIGGER supplier_logging
AFTER INSERT OR UPDATE OR DELETE ON Supplier
FOR EACH ROW EXECUTE FUNCTION logging();
```


- Trigger cho bảng `Warehouse`

```sql
CREATE TRIGGER warehouse_logging
AFTER INSERT OR UPDATE OR DELETE ON Warehouse
FOR EACH ROW EXECUTE FUNCTION logging();
```


- Trigger cho bảng `Product`
```sql
CREATE TRIGGER product_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```


- Trigger cho bảng `Customer`

```sql
CREATE TRIGGER customer_logging
AFTER INSERT OR UPDATE OR DELETE ON Customer
FOR EACH ROW EXECUTE FUNCTION logging();
```


- Trigger cho bảng `Orders`

```sql
CREATE TRIGGER order_logging
AFTER INSERT OR UPDATE OR DELETE ON Orders
FOR EACH ROW EXECUTE FUNCTION logging();
```


- Trigger cho bảng `Bill`

```sql
CREATE TRIGGER bill_logging
AFTER INSERT OR UPDATE OR DELETE ON Bill
FOR EACH ROW EXECUTE FUNCTION logging();
```

### 3.1.4 Kiểm tra hoạt động của hệ thống ghi log 

Các ví dụ cụ thể cho từng loại thao tác (`INSERT`, `UPDATE`, `DELETE`) và các quan hệ trong cơ sở dữ liệu:

1. Kiểm tra ghi log cho thao tác `INSERT`**

Ví dụ: Thêm một sản phẩm mới vào bảng Product

```sql
INSERT INTO Product (Product_Category_Name, Price, Warehouse_ID)
VALUES ('Latte', 700.00, 1);
```


2. Kiểm tra ghi log cho thao tác `UPDATE`

Ví dụ: Cập nhật giá sản phẩm:

```sql
UPDATE Product
SET Price = 750.00
WHERE Product_Category_Name = 'Latte';
```

3. Kiểm tra ghi log cho thao tác `DELETE`**

Ví dụ: Xóa một sản phẩm

```sql
DELETE FROM Product
WHERE Product_Category_Name = 'Latte';
```

4. Kiểm tra bảng log


```sql
SELECT * FROM main_log ORDER BY operation_date DESC;
```

```sql
coffee_shop_db=# SELECT * FROM main_log ORDER BY operation_date DESC;
 log_id | operation_type |       operation_date       | user_operator |                                   changed_data                                    
--------+----------------+----------------------------+---------------+-----------------------------------------------------------------------------------
      3 | DELETE         | 2024-11-22 23:37:33.057911 | postgres      | {"product_id":11,"product_category_name":"Latte","price":750.00,"warehouse_id":1}
      2 | UPDATE         | 2024-11-22 23:37:20.029167 | postgres      | {"product_id":11,"product_category_name":"Latte","price":750.00,"warehouse_id":1}
      1 | INSERT         | 2024-11-22 23:37:04.072942 | postgres      | {"product_id":11,"product_category_name":"Latte","price":700.00,"warehouse_id":1}
(3 rows)
```

## 3.2 Mã hóa dữ liệu

### 3.2.1 Tạo bảng để lưu trữ dữ liệu bảo mật

- Đầu tiên, chúng ta cần tạo một bảng riêng để lưu trữ dữ liệu nhạy cảm, chẳng hạn như token hoặc khóa truy cập cho từng loại người dùng. Bảng này nên được tách biệt khỏi các bảng chính của cơ sở dữ liệu.


```sql
CREATE TABLE secret_data (
    id SERIAL PRIMARY KEY,       -- ID duy nhất cho mỗi bản ghi
    username TEXT,               -- Tên người dùng
    secret_token TEXT            -- Token hoặc khóa bảo mật
);
```

- id: Khóa chính, tự động tăng.
- username: Tên người dùng.
- secret_token: Dữ liệu nhạy cảm (token hoặc khóa truy cập) sẽ được mã hóa.

### 3.2.2 Mã hóa dữ liệu

Chúng ta sẽ sử dụng thuật toán mã hóa đối xứng (ví dụ: AES-256) để mã hóa dữ liệu trong bảng secret_data. Điều này đảm bảo rằng ngay cả khi dữ liệu bị rò rỉ, chúng cũng sẽ không thể đọc được nếu không có khóa mã hóa.

Chuẩn Bị Sử Dụng Mô-đun pgcrypto: PostgreSQL có mô-đun pgcrypto hỗ trợ mã hóa và giải mã dữ liệu. Đầu tiên, hãy chắc chắn rằng bạn đã cài đặt mô-đun này:

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

### 3.2.3 Tạo khóa từ mật khẩu

Khóa mã hóa sẽ được tạo từ mật khẩu của superuser thông qua một hàm băm (ví dụ: SHA-256). Điều này đảm bảo rằng khóa không được lưu trữ trực tiếp trong cơ sở dữ liệu.

- Tạo khóa mã hóa cho admin

```sql
coffee_shop_db=# select encode(digest('Ch.u992mvd', 'sha256'), 'hex') as encryption_key;
                          encryption_key                          
------------------------------------------------------------------
 ca69b9601669b11f98acf29d694ec0e6d52f581bef9ffbe01bf426a3c2e6418a
(1 row)
```

- Tạo khóa mã hóa cho manager

```sql
coffee_shop_db=# select encode(digest('Chumiran', 'sha256'), 'hex') as encryption_key;
                          encryption_key                          
------------------------------------------------------------------
 9f836f77a5918d1d48f774cbde22f4317f7931018ccd44e4350a441e00c6b56a
(1 row)
```

- Tạo khóa mã hóa cho user

```sql
coffee_shop_db=# select encode(digest('Chudoan', 'sha256'), 'hex') as encryption_key;
                          encryption_key                          
------------------------------------------------------------------
 9b766363aa387a7f871298d2d5273e8df0f12e997062618ec47ff14e34352ae5
(1 row)
```

### 3.2.4 Chèn dữ liệu với mã hóa

```sql
INSERT INTO secret_data (username, secret_token)
VALUES 
('admin', pgp_sym_encrypt('admin_token', 'ca69b9601669b11f98acf29d694ec0e6d52f581bef9ffbe01bf426a3c2e6418a')),
('manager', pgp_sym_encrypt('manager_token', '9f836f77a5918d1d48f774cbde22f4317f7931018ccd44e4350a441e00c6b56a')),
('user', pgp_sym_encrypt('user_token', '9b766363aa387a7f871298d2d5273e8df0f12e997062618ec47ff14e34352ae5'));
```

### 3.2.5 Chứng minh giải mã dữ liệu

Để chứng minh rằng ngay cả người có quyền quản trị cũng không thể xem dữ liệu trong bảng mà không biết mật khẩu, chúng ta sẽ sử dụng phương thức giải mã.

Giải Mã Dữ Liệu: Để giải mã dữ liệu, chúng ta cần có mật khẩu gốc. Nếu không có mật khẩu này, các quản trị viên không thể giải mã và đọc được nội dung của bảng secret_data.

```sql
coffee_shop_db=# SELECT * FROM secret_data;
 id | username |                                                                           secret_token                                                                           
----+----------+------------------------------------------------------------------------------------------------------------------------------------------------------------------
  1 | admin    | \xc30d040703020f5d604f69c6e78a67d23c0120fc2827eb39f9fff2db0261c6d8f516ccb53c7846075eef17b54ee0bdbe1c26ae946b5b904a866e424575ba74ad76797f35dbc343b1cf5fdb2e54
  2 | manager  | \xc30d04070302b9c64d64901ae9b165d23e0172c08888d2becb206f9e1e7302e3afd42f13f5626e870c9aff5d99c772cff69d137d4a1de3f6411d21a015900662461567119c3984f4fb9e994a694c26
  3 | user     | \xc30d040703028d9f757c7581acdd67d23b01fa076da8a793794d4106a1227237035ebf9cf37fe1939b5a9f6f62ef6e08ac137ed9508c7039dd0f454c196039a371b33560af372c98894dc9b2
```

Như chúng ta đã thấy, chúng ta không thể đọc được nội dung trong đó là gì

Để giải mã:

```sql
SELECT username, pgp_sym_decrypt(secret_token::bytea, 'your_generated_key') AS secret_token
FROM secret_data;
```
Thay `your_generated_key` bằng key

- Kiểm thử với fake token:

```sql
coffee_shop_db=# SELECT username, pgp_sym_decrypt(secret_token::bytea, 'fake_token') AS token
FROM secret_data ;
ERROR:  Wrong key or corrupt data
```

```sql
coffee_shop_db=# SELECT username, pgp_sym_decrypt(secret_token::bytea, '9f836f77a5918d1d48f774cbde22f4317f7931018ccd44e4350a441e00c6b56a') AS token
FROM secret_data where username = 'user';
ERROR:  Wrong key or corrupt data
```
- Kiểm thử đúng token

```sql
coffee_shop_db=# SELECT username, pgp_sym_decrypt(secret_token::bytea, '9b766363aa387a7f871298d2d5273e8df0f12e997062618ec47ff14e34352ae5') AS token
FROM secret_data where username = 'user';
 username |   token    
----------+------------
 user     | user_token
(1 row)
```

## 3.3 Kiểm Soát Truy Cập (Access Control)

Tạo các vai trò và phân quyền cho từng vai trò dựa trên nguyên tắc quyền hạn tối thiểu.

### 3.3.1 Tạo vai trò (role)


1. **role_manager**: Vai trò dành cho quản lý, có quyền truy cập vào các bảng `Orders` (Đơn hàng), `Products` (Sản phẩm) và `Customers` (Khách hàng).
2. **role_staff**: Vai trò dành cho nhân viên, chỉ có quyền truy cập vào các *view* liên quan đến sản phẩm và đơn hàng.

```sql
-- Tạo vai trò quản lý
CREATE ROLE role_manager WITH LOGIN PASSWORD 'manager_pass';

-- Tạo vai trò nhân viên
CREATE ROLE role_staff WITH LOGIN PASSWORD 'staff_pass';
```


### 3.3.2 Phân quyền

- Cấp Quyền Truy Cập vào Schema:

```sql
GRANT USAGE ON SCHEMA public TO role_manager;
GRANT USAGE ON SCHEMA public TO role_staff;
```

#### 3.3.2.1. Quyền cho vai trò `role_manager`**

Quản lý có thể:
- Xem (`SELECT`), thêm (`INSERT`), sửa (`UPDATE`), và xóa (`DELETE`) dữ liệu trong bảng `Orders`, `Products`, `Customers`.
- Không được phép truy cập bảng `main_log` hoặc các bảng liên quan đến thông tin nhạy cảm.

```sql
-- Quyền cho bảng Orders
GRANT SELECT, INSERT, UPDATE, DELETE ON Orders TO role_manager;

-- Quyền cho bảng Products
GRANT SELECT, INSERT, UPDATE, DELETE ON Product TO role_manager;

-- Quyền cho bảng Customers
GRANT SELECT, INSERT, UPDATE, DELETE ON Customer TO role_manager;

-- Từ chối quyền truy cập bảng main_log
REVOKE ALL ON main_log FROM role_manager;
```


#### 3.3.2.2. Quyền cho vai trò `role_staff`

Nhân viên có thể:
- Chỉ xem các *view* (bảng ảo) được tạo ở bài trước, ví dụ như `sales_employee_view` và `customer_view`.
- Không có quyền truy cập vào các bảng cơ sở dữ liệu chính (`Orders`, `Products`, `Customers`).

```sql
-- Quyền cho *view* sales_employee_view
GRANT SELECT ON sales_employee_view TO role_staff;

-- Quyền cho *view* customer_view
GRANT SELECT ON customer_view TO role_staff;

-- Từ chối quyền truy cập các bảng chính
REVOKE ALL ON Orders FROM role_staff;
REVOKE ALL ON Product FROM role_staff;
REVOKE ALL ON Customer FROM role_staff;

-- Từ chối quyền truy cập bảng main_log
REVOKE ALL ON main_log FROM role_staff;
```



#### 3.3.2.3. Hạn chế truy cập bảng log

Bảng `main_log` (bảng ghi log hoạt động) chỉ có thể được xem bởi **superuser**. Đảm bảo rằng các vai trò khác không thể truy cập:

```sql
-- Từ chối quyền truy cập bảng log cho tất cả người dùng
REVOKE ALL ON main_log FROM PUBLIC;

-- Chỉ cho phép superuser (ví dụ: postgres) truy cập
GRANT ALL ON main_log TO postgres; -- Thay "postgres" bằng superuser của bạn
```

---

### 3.3.3 Kiểm tra phân quyền**

#### 3.3.3.1 Kiểm tra với vai trò `role_manager`

Đăng nhập vào cơ sở dữ liệu với vai trò `role_manager`:
```bash
psql -U role_manager -d coffee_shop_db
```

Hoặc:

```sql
coffee_shop_db=# set role role_manager;
SET
```

Thực hiện các truy vấn sau:

1. **Xem bảng Orders**:
   ```sql
   SELECT * FROM Orders;
   ```

```sql
coffee_shop_db=> SELECT * FROM Orders;
 order_id | order_date | total_amount | customer_id | employee_id 
----------+------------+--------------+-------------+-------------
        1 | 2024-11-08 |      1039.79 |           9 |           5
        2 | 2024-10-28 |      1316.75 |           9 |           4
        3 | 2024-10-31 |      3327.25 |          10 |           4
        4 | 2024-10-24 |      3579.22 |           9 |           3
        5 | 2024-11-08 |      2161.28 |           6 |           6
        6 | 2024-10-26 |      3024.59 |           2 |           6
        7 | 2024-11-06 |      4376.18 |           7 |           5
        8 | 2024-10-29 |      2891.04 |           3 |           1
        9 | 2024-11-04 |      3561.47 |           1 |           7
       10 | 2024-10-30 |      4589.87 |           5 |           3
(10 rows)
```

2. **Xem bảng Products**:
   ```sql
   SELECT * FROM Product;
   ```
   
```sql
coffee_shop_db=> SELECT * FROM Product;
 product_id | product_category_name | price  | warehouse_id 
------------+-----------------------+--------+--------------
          1 | Арабика               | 481.21 |            1
          2 | Капучино              | 549.51 |            1
          3 | Латте                 | 778.31 |            5
          4 | Капучино              | 114.89 |            5
          5 | Робуста               | 465.66 |            5
          6 | Эспрессо              | 982.47 |            3
          7 | Робуста               | 347.12 |            2
          8 | Капучино              | 853.89 |            1
          9 | Арабика               | 616.37 |            4
         10 | Латте                 | 239.44 |            3
(10 rows)

```

3. **Xem bảng Customers**:
   ```sql
   SELECT * FROM Customer;
   ```
```sql
coffee_shop_db=>  SELECT * FROM Customer;
 customer_id |       name        | phone_number |          email           
-------------+-------------------+--------------+--------------------------
           1 | Иван Иванов       | +84347792080 | ivanivanov@mail.ru
           2 | Петр Петров       | +84725742192 | petrpetrov@mail.ru
           3 | Светлана Смирнова | +84498734272 | svetlanasmirnova@mail.ru
           4 | Елена Кузнецова   | +84451098251 | elenakuznetsova@mail.ru
           5 | Александр Соколов | +84479531226 | aleksandrsokolov@mail.ru
           6 | Мария Попова      | +84712349852 | mariyapopova@mail.ru
           7 | Николай Федоров   | +84396571482 | nikolayfedorov@mail.ru
           8 | Анна Васильева    | +84578321940 | annavasilyeva@mail.ru
           9 | Дмитрий Григорьев | +84410239854 | dmitriygrigorev@mail.ru
          10 | Ольга Николаева   | +84765849320 | olganikolaeva@mail.ru
(10 rows)
```

4. **Thử truy cập bảng main_log**:
   ```sql
   SELECT * FROM main_log;
   ```
```sql
coffee_shop_db=> SELECT * FROM main_log;
ERROR:  permission denied for table main_log
```

**Kết quả mong đợi**:
- Vai trò `role_manager` có thể truy cập các bảng `Orders`, `Products`, và `Customers`.
- Truy cập bảng `main_log` sẽ bị từ chối với lỗi: `ERROR: permission denied`.


#### 3.3.3.2 Kiểm tra với vai trò `role_staff`

Đăng nhập với vai trò `role_staff`:
```bash
psql -U role_staff -d coffee_shop_db
```

Hoặc:

```sql
coffee_shop_db=> set role role_staff;
SET
```

Thực hiện các truy vấn sau:

1. **Xem *view* sales_employee_view**:
   ```sql
   SELECT * FROM sales_employee_view;
   ```
```sql
offee_shop_db=> SELECT * FROM sales_employee_view;
 employee_id |   employee_name    | order_id | order_date | total_amount | customer_id |   customer_name   | customer_phone |      customer_email      
-------------+--------------------+----------+------------+--------------+-------------+-------------------+----------------+--------------------------
           7 | Ольга Попова       |        9 | 2024-11-04 |      3561.47 |           1 | Иван Иванов       | +84347792080   | ivanivanov@mail.ru
           6 | Мария Кузнецова    |        6 | 2024-10-26 |      3024.59 |           2 | Петр Петров       | +84725742192   | petrpetrov@mail.ru
           1 | Алексей Иванов     |        8 | 2024-10-29 |      2891.04 |           3 | Светлана Смирнова | +84498734272   | svetlanasmirnova@mail.ru
           3 | Екатерина Смирнова |       10 | 2024-10-30 |      4589.87 |           5 | Александр Соколов | +84479531226   | aleksandrsokolov@mail.ru
           6 | Мария Кузнецова    |        5 | 2024-11-08 |      2161.28 |           6 | Мария Попова      | +84712349852   | mariyapopova@mail.ru
           5 | Иван Васильев      |        7 | 2024-11-06 |      4376.18 |           7 | Николай Федоров   | +84396571482   | nikolayfedorov@mail.ru
           3 | Екатерина Смирнова |        4 | 2024-10-24 |      3579.22 |           9 | Дмитрий Григорьев | +84410239854   | dmitriygrigorev@mail.ru
           4 | Анна Петрова       |        2 | 2024-10-28 |      1316.75 |           9 | Дмитрий Григорьев | +84410239854   | dmitriygrigorev@mail.ru
           5 | Иван Васильев      |        1 | 2024-11-08 |      1039.79 |           9 | Дмитрий Григорьев | +84410239854   | dmitriygrigorev@mail.ru
           4 | Анна Петрова       |        3 | 2024-10-31 |      3327.25 |          10 | Ольга Николаева   | +84765849320   | olganikolaeva@mail.ru
(10 rows)
```

2. **Xem *view* customer_view**:
   ```sql
   SELECT * FROM customer_view;
   ```
```sql
coffee_shop_db=> SELECT * FROM customer_view;
 customer_id |   customer_name   | order_id | order_date | total_amount | bill_id | bill_amount | payment_method 
-------------+-------------------+----------+------------+--------------+---------+-------------+----------------
           9 | Дмитрий Григорьев |        1 | 2024-11-08 |      1039.79 |       1 |     1039.79 | Bank Transfer
           9 | Дмитрий Григорьев |        2 | 2024-10-28 |      1316.75 |       2 |     1316.75 | Bank Transfer
          10 | Ольга Николаева   |        3 | 2024-10-31 |      3327.25 |       3 |     3327.25 | Credit Card
           9 | Дмитрий Григорьев |        4 | 2024-10-24 |      3579.22 |       4 |     3579.22 | Credit Card
           6 | Мария Попова      |        5 | 2024-11-08 |      2161.28 |       5 |     2161.28 | Bank Transfer
           2 | Петр Петров       |        6 | 2024-10-26 |      3024.59 |       6 |     3024.59 | Cash
           7 | Николай Федоров   |        7 | 2024-11-06 |      4376.18 |       7 |     4376.18 | Credit Card
           3 | Светлана Смирнова |        8 | 2024-10-29 |      2891.04 |       8 |     2891.04 | Cash
           1 | Иван Иванов       |        9 | 2024-11-04 |      3561.47 |       9 |     3561.47 | Credit Card
           5 | Александр Соколов |       10 | 2024-10-30 |      4589.87 |      10 |     4589.87 | Bank Transfer
(10 rows)

```

3. **Thử truy cập bảng Products**:
   ```sql
   SELECT * FROM Product;
   ```
```sql
coffee_shop_db=> SELECT * FROM Product;
ERROR:  permission denied for table product
```

4. **Thử truy cập bảng main_log**:
   ```sql
   SELECT * FROM main_log;
   ```
```sql
coffee_shop_db=> SELECT * FROM main_log;
ERROR:  permission denied for table main_log
```
**Kết quả mong đợi**:
- Vai trò `role_staff` chỉ có thể truy cập *view* `customer_view` và `sales_employee_view`.
- Truy cập các bảng cơ sở dữ liệu chính (`Orders`, `Products`, `Customers`) và bảng `main_log` sẽ bị từ chối với lỗi: `ERROR: permission denied`.

---

#### 3.3.3.3 Kiểm tra từ chối truy cập

Nếu vai trò `role_staff` thử thêm dữ liệu vào bảng `Orders`, ví dụ:
```sql
INSERT INTO Orders (Order_Date, Total_Amount, Customer_ID, Employee_ID)
VALUES ('2024-11-22', 1000.00, 1, 1);
```

```sql
coffee_shop_db=> INSERT INTO Orders (Order_Date, Total_Amount, Customer_ID, Employee_ID)
VALUES ('2024-11-22', 1000.00, 1, 1);
ERROR:  permission denied for table orders
```


