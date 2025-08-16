# 1. Chọn hệ quản trị cơ sở dữ liệu (DBMS)

- Sử dụng PostgreSQL
- Lý do sử dụng: PostgreSQL là một hệ quản trị cơ sở dữ liệu quan hệ mạnh mẽ, mã nguồn mở và tuân thủ chuẩn SQL. Nó có khả năng xử lý các cơ sở dữ liệu phức tạp, hỗ trợ đa người dùng và tích hợp tốt với các ngôn ngữ lập trình. PostgreSQL cũng được sử dụng rộng rãi trong các dự án thực tế nhờ khả năng mở rộng và bảo mật tốt.
---
# 2. Tạo cấu trúc cơ sở dữ liệu

## Kết nối cơ sở dữ liệu:

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
---
### Tạo cơ sở dữ liệu

```SQL
create database coffee_shop_db
with
owner = postgres
encoding = 'UTF8'
tablespace = pg_default
connection limit = -1
is_template = False;
```
1. CREATE DATABASE coffee_shop_db
CREATE DATABASE coffee_shop_db: Tạo cơ sở dữ liệu mới có tên là coffee_shop_db. Đây là tên của cơ sở dữ liệu mà bạn sẽ sử dụng để lưu trữ dữ liệu của mình.
2. OWNER = postgres
OWNER = postgres: Xác định người sở hữu (owner) của cơ sở dữ liệu là người dùng postgres. Người sở hữu có toàn quyền quản lý cơ sở dữ liệu này (tạo bảng, sửa bảng, quản lý dữ liệu, v.v.).
3. ENCODING = 'UTF8'
ENCODING = 'UTF8': Xác định mã hóa ký tự mà cơ sở dữ liệu sẽ sử dụng là UTF-8. UTF-8 là một chuẩn mã hóa ký tự phổ biến, hỗ trợ hầu hết các ngôn ngữ trên thế giới. Điều này đảm bảo rằng cơ sở dữ liệu có thể lưu trữ dữ liệu tiếng Việt, tiếng Anh, tiếng Nga và nhiều ngôn ngữ khác.
4. TABLESPACE = pg_default
TABLESPACE = pg_default: Xác định không gian lưu trữ (tablespace) mặc định là pg_default. Tablespace là nơi vật lý trên đĩa mà dữ liệu của cơ sở dữ liệu sẽ được lưu trữ. Trong trường hợp này, dữ liệu sẽ được lưu trong tablespace mặc định của PostgreSQL.
5. CONNECTION LIMIT = -1
CONNECTION LIMIT = -1: Giới hạn số lượng kết nối tối đa đến cơ sở dữ liệu này là -1, nghĩa là không giới hạn số lượng kết nối. Bất kỳ số lượng người dùng nào cũng có thể kết nối vào cơ sở dữ liệu, miễn là tài nguyên hệ thống cho phép.
6. IS_TEMPLATE = False
IS_TEMPLATE = False: Đặt thuộc tính IS_TEMPLATE thành False, nghĩa là cơ sở dữ liệu này không được sử dụng làm mẫu (template) để tạo các cơ sở dữ liệu khác. Nếu bạn đặt giá trị True, cơ sở dữ liệu này có thể được dùng làm mẫu để sao chép khi tạo các cơ sở dữ liệu mới.

```SQL
postgres=# \c coffee_shop_db 
You are now connected to database "coffee_shop_db" as user "postgres".
coffee_shop_db=# 
```

- Tạo schema
```sql
coffee_shop_db=# create schema coffee_shop_schema;
CREATE SCHEMA
coffee_shop_db=# \dn
            List of schemas
        Name        |       Owner       
--------------------+-------------------
 coffee_shop_schema | postgres
 public             | pg_database_owner
(2 rows)
```
- Chỉ định schema
```sql
coffee_shop_db=# set search_path to coffee_shop_schema;
SET
coffee_shop_db=# show search_path ;
    search_path     
--------------------
 coffee_shop_schema
```
----
### Tạo bảng
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
    Employee_ID INTEGER,
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);
```

Bảng Product
```sql
CREATE TABLE Product (
    Product_ID SERIAL PRIMARY KEY,
    Product_Category_Name VARCHAR(100) NOT NULL,
    Price NUMERIC(10, 2) NOT NULL,
    Warehouse_ID INTEGER,
    FOREIGN KEY (Warehouse_ID) REFERENCES Warehouse(Warehouse_ID)
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
    Employee_ID INTEGER,
    FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID),
    FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);
```
Bảng Bill
```sql
CREATE TABLE Bill (
    Bill_ID SERIAL PRIMARY KEY,
    Amount NUMERIC(10, 2) NOT NULL,
    Payment_Method VARCHAR(50) NOT NULL,
    Order_ID INTEGER,
    FOREIGN KEY (Order_ID) REFERENCES Orders(Order_ID)
);
```

Bảng liên kết giữa bảng Orders và bảng Product
```sql
CREATE TABLE Order_Product (
    Order_ID INTEGER,
    Product_ID INTEGER,
    PRIMARY KEY (Order_ID, Product_ID),
    FOREIGN KEY (Order_ID) REFERENCES "Order"(Order_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);
```

- Bảng liên kết giữa bảng Supplier và Product
```sql
CREATE TABLE Supplier_Product (
    Supplier_ID INTEGER,
    Product_ID INTEGER,
    PRIMARY KEY (Supplier_ID, Product_ID),
    FOREIGN KEY (Supplier_ID) REFERENCES Supplier(Supplier_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID)
);
```
Ta có các bảng sau
```sql
coffee_shop_db=# \dt
                    List of relations
       Schema       |       Name       | Type  |  Owner   
--------------------+------------------+-------+----------
 coffee_shop_schema | bill             | table | postgres
 coffee_shop_schema | customer         | table | postgres
 coffee_shop_schema | employee         | table | postgres
 coffee_shop_schema | order_product    | table | postgres
 coffee_shop_schema | orders           | table | postgres
 coffee_shop_schema | product          | table | postgres
 coffee_shop_schema | supplier         | table | postgres
 coffee_shop_schema | supplier_product | table | postgres
 coffee_shop_schema | warehouse        | table | postgres
(9 rows)
```
---
### Thêm dữ liệu vào các bảng
 Thêm dữ liệu vào bảng Emloyee
 
```sql
INSERT INTO employee (name, position, phone_number, email) 
VALUES 
    ('Nguyen Van A', 'supervisor', '9312828535', 'nguyenvana123@gmail.com'),
    ('Nguyen Thi B', 'salesperson', '92537563834', 'nb4214@gmail.com'),
    ('Artom', 'salesperson', '27582473683', 'artom33@mail.ru'),
    ('Irina', 'salesperson', '8925748253', 'irina8386@mail.ru'),
    ('Tran', 'salesperson', '92846363583', 'trantran4953@gmail.com');
```
Kết quả:
```sql
coffee_shop_db=# select * from employee;
 employee_id |     name     |  position   | phone_number |          email          
-------------+--------------+-------------+--------------+-------------------------
           1 | Nguyen Van A | supervisor  | 9312828535   | nguyenvana123@gmail.com
           2 | Nguyen Thi B | salesperson | 92537563834  | nb4214@gmail.com
           3 | Artom        | salesperson | 27582473683  | artom33@mail.ru
           4 | Irina        | salesperson | 8925748253   | irina8386@mail.ru
           5 | Tran         | salesperson | 92846363583  | trantran4953@gmail.com
(5 rows)
```

Thêm dữ liệu vào bảng Supplier
```sql
INSERT INTO supplier (name, address, phone_number, email) 
VALUES 
    ('Trung Nguyen Coffee', 'Dalat city', '03873532753', 'trungnguyencoffee@gmail.com'),
    ('King Coffee', 'Ho Chi Minh city', '0385636282', 'kingcoffee@gmail.com'),
    ('G7 Coffee', 'Ha Noi', '92834772843', 'g7coffee@gmail.com');
```
Kết quả:
```sql
coffee_shop_db=# select * from supplier;
 supplier_id |        name         |     address      | phone_number |            email            
-------------+---------------------+------------------+--------------+-----------------------------
           1 | Trung Nguyen Coffee | Dalat city       | 03873532753  | trungnguyencoffee@gmail.com
           2 | King Coffee         | Ho Chi Minh city | 0385636282   | kingcoffee@gmail.com
           3 | G7 Coffee           | Ha Noi           | 92834772843  | g7coffee@gmail.com
(3 rows)
```

Thêm dữ liệu cho bảng Warehouse
```sql
INSERT INTO warehouse (address, status, employee_id) 
VALUES 
    ('Lam Ha', 'In stock', 1),
    ('Tan Ha', 'In stock', 1),
    ('Dan Phuong', 'In stock', 1),
    ('Me Linh', 'In stock', 1);
```
Kết quả
```sql
coffee_shop_db=# select * from warehouse;
 warehouse_id |  address   |  status  | employee_id 
--------------+------------+----------+-------------
            1 | Lam Ha     | In stock |           1
            2 | Tan Ha     | In stock |           1
            3 | Dan Phuong | In stock |           1
            4 | Me Linh    | In stock |           1
(4 rows)
```

Thêm dữ liệu cho bảng Product
```sql
INSERT INTO product (product_category_name, price, warehouse_id) 
VALUES 
    ('Arabica', 100000, 1),
    ('Robusta', 90000, 2),
    ('Bourbon', 96000, 3),
    ('Typica', 92000, 4);
```
Kết quả:
```sql
coffee_shop_db=# select * from product;
 product_id | product_category_name |   price   | warehouse_id 
------------+-----------------------+-----------+--------------
          1 | Arabica               | 100000.00 |            1
          2 | Robusta               |  90000.00 |            2
          3 | Bourbon               |  96000.00 |            3
          4 | Typica                |  92000.00 |            4
(4 rows)
```

Thêm dữ liệu cho bảng Customer
```sql
INSERT INTO customer (name, phone_number, email) 
VALUES 
    ('Alex', '93842727543', 'alex8888@mail.ru'),
    ('Tom', '82736464383', 'tomi7749@mail.ru'),
    ('Anton', '827364646737', 'ton@mail.ru'),
    ('Karababy', '8283747654', 'baby@mail.ru');
```
Kết quả:
```sql
coffee_shop_db=# select * from customer;
 customer_id |   name   | phone_number |      email       
-------------+----------+--------------+------------------
           1 | Alex     | 93842727543  | alex8888@mail.ru
           2 | Tom      | 82736464383  | tomi7749@mail.ru
           3 | Anton    | 827364646737 | ton@mail.ru
           4 | Karababy | 8283747654   | baby@mail.ru
(4 rows)
```
Nhập dữ liệu cho bảng Orders
```sql
INSERT INTO orders (order_date, total_amount, employee_id, customer_id) 
VALUES 
    ('2024-10-12', 150000, 2, 1),
    ('2024-10-13', 599999, 2, 2),
    ('2024-10-13', 70000, 3, 3),
    ('2024-10-20', 6699999, 4, 4);
```
Kết quả
```sql
coffee_shop_db=# select * from orders;
 order_id | order_date | total_amount | employee_id | customer_id 
----------+------------+--------------+-------------+-------------
        1 | 2024-10-12 |    150000.00 |           2 |           1
        2 | 2024-10-13 |    599999.00 |           2 |           2
        3 | 2024-10-13 |     70000.00 |           3 |           3
        4 | 2024-10-20 |   6699999.00 |           4 |           4
(4 rows)
```

Thêm dữ liệu vào bảng Bill
```sql
INSERT INTO bill (amount, payment, order_id) 
VALUES 
    (150000, 'Cash', 1),
    (599999, 'Bank Transfer', 2),
    (50000, 'Cash', 3),
    (20000, 'Online Payment', 3),
    (6699999, 'Cash', 4);
```
Kết quả:
```sql
coffee_shop_db=# select * from bill;
 bill_id |   amount   |    payment     | order_id 
---------+------------+----------------+----------
       1 |  150000.00 | Cash           |        1
       2 |  599999.00 | Bank Transfer  |        2
       3 |   50000.00 | Cash           |        3
       4 |   20000.00 | Online Payment |        3
       5 | 6699999.00 | Cash           |        4
(5 rows)
```

Thêm dữ liệu vào bảng trung gian Order_Product
```sql
INSERT INTO order_product (order_id, product_id) 
VALUES 
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4);
```
Kết quả:
```sql
coffee_shop_db=# select * from order_product ;
 order_id | product_id 
----------+------------
        1 |          1
        2 |          2
        3 |          3
        4 |          4
(4 rows)
```
Thêm dữ liệu vào bảng trung gian Supplier_Product
```sql
INSERT INTO supplier_product (supplier_id, product_id) 
VALUES 
    (1, 1),
    (1, 2),
    (2, 3),
    (3, 4);
```
Kết quả:
```sql
coffee_shop_db=# select * from supplier_product;
 supplier_id | product_id 
-------------+------------
           1 |          1
           1 |          2
           2 |          3
           3 |          4
(4 rows)
```

---

# 3. Tạo index

```sql
-- Bảng Employee
-- Tạo chỉ mục cho cột Employee_ID để tìm kiếm nhân viên
CREATE INDEX idx_employee_id ON Employee(Employee_ID);

-- Bảng Supplier
-- Tạo chỉ mục cho cột Supplier_ID để tìm kiếm nhà cung cấp
CREATE INDEX idx_supplier_id ON Supplier(Supplier_ID);

-- Bảng Product
-- Tạo chỉ mục cho cột Warehouse_ID để tăng tốc liên kết với bảng Warehouse
CREATE INDEX idx_product_warehouse_id ON Product(Warehouse_ID);

-- Bảng Customer
-- Tạo chỉ mục cho cột Customer_ID để tìm kiếm khách hàng
CREATE INDEX idx_customer_id ON Customer(Customer_ID);

-- Bảng Order
-- Tạo chỉ mục cho cột Customer_ID và Employee_ID để tăng tốc các truy vấn liên kết giữa Order và Customer, Order và Employee
CREATE INDEX idx_order_customer_id ON orders(Customer_ID);
CREATE INDEX idx_order_employee_id ON orders(Employee_ID);

-- Bảng Bill
-- Tạo chỉ mục cho cột Order_ID để tăng tốc truy vấn liên kết giữa Bill và Order
CREATE INDEX idx_bill_order_id ON Bill(Order_ID);

-- Bảng Warehouse
-- Tạo chỉ mục cho cột Employee_ID để tăng tốc truy vấn liên kết giữa Warehouse và Employee
CREATE INDEX idx_warehouse_employee_id ON Warehouse(Employee_ID);

-- Bảng liên kết Order_Product
-- Tạo chỉ mục cho cột Order_ID và Product_ID để tăng tốc truy vấn liên kết giữa Order và Product
CREATE INDEX idx_order_product_order_id ON Order_Product(Order_ID);
CREATE INDEX idx_order_product_product_id ON Order_Product(Product_ID);

-- Bảng liên kết Supplier_Product
-- Tạo chỉ mục cho cột Supplier_ID và Product_ID để tăng tốc truy vấn liên kết giữa Supplier và Product
CREATE INDEX idx_supplier_product_supplier_id ON Supplier_Product(Supplier_ID);
CREATE INDEX idx_supplier_product_product_id ON Supplier_Product(Product_ID);
```
---


# 4 Thiết lập mối quan hệ giữa các bảng:
   Các mối quan hệ chính giữa các bảng đã được thiết lập bằng cách sử dụng các khóa ngoại (foreign keys). 
   
```sql
-- Quan hệ giữa Employee và Warehouse
ALTER TABLE Warehouse
ADD CONSTRAINT fk_warehouse_employee
FOREIGN KEY (Employee_ID)
REFERENCES Employee(Employee_ID);

-- Quan hệ giữa Orders và Customer
ALTER TABLE Orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (Customer_ID)
REFERENCES Customer(Customer_ID);

-- Quan hệ giữa Orders và Employee
ALTER TABLE Orders
ADD CONSTRAINT fk_orders_employee
FOREIGN KEY (Employee_ID)
REFERENCES Employee(Employee_ID);

-- Quan hệ giữa Bill và Orders
ALTER TABLE Bill
ADD CONSTRAINT fk_bill_orders
FOREIGN KEY (Order_ID)
REFERENCES Orders(Order_ID);

-- Quan hệ giữa Product và Warehouse
ALTER TABLE Product
ADD CONSTRAINT fk_product_warehouse
FOREIGN KEY (Warehouse_ID)
REFERENCES Warehouse(Warehouse_ID);

-- Quan hệ giữa Order_Product và Orders
ALTER TABLE Order_Product
ADD CONSTRAINT fk_order_product_order
FOREIGN KEY (Order_ID)
REFERENCES Orders(Order_ID);

-- Quan hệ giữa Order_Product và Product
ALTER TABLE Order_Product
ADD CONSTRAINT fk_order_product_product
FOREIGN KEY (Product_ID)
REFERENCES Product(Product_ID);

-- Quan hệ giữa Supplier_Product và Supplier
ALTER TABLE Supplier_Product
ADD CONSTRAINT fk_supplier_product_supplier
FOREIGN KEY (Supplier_ID)
REFERENCES Supplier(Supplier_ID);

-- Quan hệ giữa Supplier_Product và Product
ALTER TABLE Supplier_Product
ADD CONSTRAINT fk_supplier_product_product
FOREIGN KEY (Product_ID)
REFERENCES Product(Product_ID);
```

# 5 Ví dụ các truy vấn thử nghiệm trong cơ sở dữ liệu:

   - **Truy vấn để lấy danh sách các đơn hàng, kèm thông tin về khách hàng và nhân viên phục vụ:**
     ```sql
     SELECT o.Order_ID, o.Order_Date, o.Total_Amount, c.Name AS Customer, e.Name AS Employee
     FROM Orders o
     JOIN Customer c ON o.Customer_ID = c.Customer_ID
     JOIN Employee e ON o.Employee_ID = e.Employee_ID;
     ```
     Truy vấn này trả về danh sách các đơn hàng, bao gồm ngày đặt hàng, tổng số tiền, tên khách hàng và nhân viên phục vụ.

   - **Truy vấn để hiển thị tất cả các sản phẩm được lưu trữ ở từng kho:**
     ```sql
     SELECT w.Address AS Warehouse, p.Product_Category_Name AS Product, p.Price
     FROM Warehouse w
     JOIN Product p ON w.Warehouse_ID = p.Warehouse_ID;
     ```
     Truy vấn này hiển thị thông tin các sản phẩm tại từng kho, bao gồm địa chỉ kho, tên loại sản phẩm và giá.

   - **Truy vấn để hiển thị danh sách các nhà cung cấp và sản phẩm mà họ cung cấp:**
     ```sql
     SELECT s.Name AS Supplier, p.Product_Category_Name AS Product
     FROM Supplier s
     JOIN Supplier_Product sp ON s.Supplier_ID = sp.Supplier_ID
     JOIN Product p ON sp.Product_ID = p.Product_ID;
     ```
     Truy vấn này trả về danh sách nhà cung cấp cùng các sản phẩm mà họ cung cấp cho cửa hàng.

   - **Truy vấn để tìm tổng tiền của tất cả các đơn hàng thanh toán bằng tiền mặt:**
     ```sql
     SELECT SUM(b.Amount) AS TotalCashPayments
     FROM Bill b
     WHERE b.Payment_Method = 'Cash';
     ```
     Truy vấn này tính tổng số tiền của các đơn hàng được thanh toán bằng tiền mặt.

   - **Truy vấn để lấy danh sách các đơn hàng có chứa một sản phẩm cụ thể, ví dụ "Arabica":**
     ```sql
     SELECT o.Order_ID, o.Order_Date, o.Total_Amount
     FROM Orders o
     JOIN Order_Product op ON o.Order_ID = op.Order_ID
     JOIN Product p ON op.Product_ID = p.Product_ID
     WHERE p.Product_Category_Name = 'Arabica';
     ```
     Truy vấn này trả về thông tin các đơn hàng có chứa sản phẩm "Arabica", bao gồm mã đơn hàng, ngày đặt hàng và tổng tiền.

### Tạo view

View dành cho Nhân viên bán hàng (Sales Employee View)
```sql
CREATE VIEW sales_employee_view AS 
SELECT 
    e.employee_ID,
    e.name AS employee_name,
    o.order_id,
    o.order_date,
    o.total_amount,
    c.customer_id,
    c.name AS customer_name,
    c.phone_number AS customer_phone,
    c.email AS customer_mail
FROM 
    employee e
JOIN 
    orders o ON e.employee_id = o.employee_id
JOIN 
    customer c ON o.customer_id = c.customer_id;
```
Kết quả
```sql
coffee_shop_db=# select * from sales_employee_view;
 employee_id | employee_name | order_id | order_date | total_amount | customer_id | customer_name | customer_phone |  customer_mail   
-------------+---------------+----------+------------+--------------+-------------+---------------+----------------+------------------
           2 | Nguyen Thi B  |        1 | 2024-10-12 |    150000.00 |           1 | Alex          | 93842727543    | alex8888@mail.ru
           2 | Nguyen Thi B  |        2 | 2024-10-13 |    599999.00 |           2 | Tom           | 82736464383    | tomi7749@mail.ru
           3 | Artom         |        3 | 2024-10-13 |     70000.00 |           3 | Anton         | 827364646737   | ton@mail.ru
           4 | Irina         |        4 | 2024-10-20 |   6699999.00 |           4 | Karababy      | 8283747654     | baby@mail.ru
(4 rows)
```

View dành cho Quản lý kho (Warehouse Manager View)
```sql
CREATE VIEW Warehouse_Manager_View AS 
SELECT
    w.warehouse_id,
    w.address AS warehouse_address,
    w.status AS warehouse_status,
    p.product_id,
    p.product_category_name,
    p.price
FROM 
    warehouse w
JOIN 
    product p ON w.warehouse_id = p.warehouse_id;
```
Kết quả
```sql
coffee_shop_db=# select * from warehouse_manager_view ;
 warehouse_id | warehouse_address | warehouse_status | product_id | product_category_name |   price   
--------------+-------------------+------------------+------------+-----------------------+-----------
            1 | Lam Ha            | In stock         |          1 | Arabica               | 100000.00
            2 | Tan Ha            | In stock         |          2 | Robusta               |  90000.00
            3 | Dan Phuong        | In stock         |          3 | Bourbon               |  96000.00
            4 | Me Linh           | In stock         |          4 | Typica                |  92000.00
(4 rows)
```

View dành cho Khách hàng (Customer View)
```sql
CREATE VIEW Customer_Order_View AS 
SELECT 
    c.customer_id,
    c.name AS customer_name,
    o.order_id,
    o.order_date,
    o.total_amount,
    b.bill_id,
    b.amount AS bill_amount,
    b.payment 
FROM 
    customer c
JOIN 
    orders o ON c.customer_id = o.customer_id
JOIN 
    bill b ON o.order_id = b.order_id;
```

Xem tất cả các view 
```sql
coffee_shop_db=# SELECT table_name 
FROM information_schema.views 
WHERE table_schema = 'coffee_shop_schema';
       table_name       
------------------------
 sales_employee_view
 warehouse_manager_view
 customer_order_view
(3 rows)
```

---








