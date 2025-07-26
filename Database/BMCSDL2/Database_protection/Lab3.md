
# Báo Cáo Bài Lab 3: Bảo Mật Cơ Sở Dữ Liệu

## 1. Giám Sát Cơ Sở Dữ Liệu (Database Monitoring)

Để giám sát cơ sở dữ liệu, ta tạo một bảng log để ghi lại các thay đổi trong cơ sở dữ liệu. Sử dụng trigger để tự động cập nhật log mỗi khi có thao tác thêm, sửa, hoặc xóa trong các bảng chính.

### Tạo Bảng Log

```sql
CREATE TABLE main_log (
    log_id SERIAL PRIMARY KEY,
    operation_type TEXT,
    operation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_operator TEXT,
    changed_data JSON
);
```
Cấu trúc bảng log:
- log_id: Khóa chính, tự động tăng.
- operation_type: Loại thao tác (INSERT, UPDATE, DELETE).
- operation_date: Ngày và giờ xảy ra thay đổi.
- user_operator: Người thực hiện thao tác (tên người dùng hoặc vai trò).
- changed_data: Dữ liệu đã thay đổi, lưu ở dạng JSON để dễ dàng lưu cả dữ liệu cũ và mới.

- Ví dụ:
```sql
lab3=# CREATE TABLE main_log (
    log_id SERIAL PRIMARY KEY,
    operation_type TEXT,
    operation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    user_operator TEXT,
    changed_data JSON
);
CREATE TABLE
lab3=# \dt
                    List of relations
       Schema       |       Name       | Type  |  Owner   
--------------------+------------------+-------+----------
 coffee_shop_schema | bill             | table | postgres
 coffee_shop_schema | customer         | table | postgres
 coffee_shop_schema | employee         | table | postgres
 coffee_shop_schema | main_log         | table | postgres
 coffee_shop_schema | order_product    | table | postgres
 coffee_shop_schema | orders           | table | postgres
 coffee_shop_schema | product          | table | postgres
 coffee_shop_schema | supplier         | table | postgres
 coffee_shop_schema | supplier_product | table | postgres
 coffee_shop_schema | warehouse        | table | postgres
(10 rows)
```


### Tạo Hàm Trigger

Hàm `logging()` dưới đây sẽ ghi lại thông tin vào bảng `main_log`.

```sql
CREATE OR REPLACE FUNCTION logging() RETURNS TRIGGER AS $logging$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('D', current_user, row_to_json(OLD));
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('U', current_user, row_to_json(NEW));
    ELSIF (TG_OP = 'INSERT') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('I', current_user, row_to_json(NEW));
    END IF;
    RETURN NULL;    
END;
$logging$ LANGUAGE plpgsql;
```
- Định nghĩa hàm trigger logging(): Hàm logging() là một hàm loại trigger (kích hoạt) được viết bằng ngôn ngữ plpgsql của PostgreSQL. Hàm này sẽ thực hiện khi có thao tác thêm (INSERT), cập nhật (UPDATE) hoặc xóa (DELETE) trên các bảng đã được liên kết với trigger.

```sql
CREATE OR REPLACE FUNCTION logging() RETURNS TRIGGER AS $logging$
```
    - RETURNS TRIGGER cho biết hàm sẽ được gọi dưới dạng trigger.
    - $logging$ được sử dụng để đánh dấu phần thân của hàm bắt đầu và kết thúc.

- Kiểm tra loại thao tác với TG_OP: Bên trong hàm, TG_OP là biến hệ thống dùng để xác định loại thao tác đã kích hoạt trigger:
    - DELETE': Xóa bản ghi
    - 'UPDATE': Cập nhật bản ghi
    - 'INSERT': Thêm mới bản ghi
 
- Dựa trên giá trị của TG_OP, hàm sẽ xử lý tương ứng và lưu dữ liệu phù hợp vào bảng log.
- Lưu dữ liệu vào bảng log main_log: Với mỗi loại thao tác, hàm sẽ thực hiện một câu lệnh INSERT vào bảng main_log. Cụ thể:
    - Khi xóa dữ liệu (TG_OP = 'DELETE'):
        - Lưu loại thao tác là DELETE.
        - Ghi lại tên người dùng hiện tại thực hiện thao tác (current_user).
        - Lưu dữ liệu của bản ghi bị xóa, sử dụng row_to_json(OLD) để chuyển dữ liệu của bản ghi cũ thành định dạng JSON.

```sql
INSERT INTO main_log (operation_type, user_operator, changed_data)
VALUES ('DELETE', current_user, row_to_json(OLD));

```
- Các thao tác còn lại tương tự
- Hoàn tất hàm và trả về kết quả: Hàm logging() kết thúc bằng RETURN NULL;, để chỉ ra rằng trigger không thay đổi nội dung của bản ghi trong bảng gốc. Cuối cùng, đóng phần thân hàm với $logging$ LANGUAGE plpgsql;.
```sql
RETURN NULL;
END;
$logging$ LANGUAGE plpgsql;
```
Ví dụ:
```sql
lab3=# CREATE OR REPLACE FUNCTION logging() RETURNS TRIGGER AS $logging$
BEGIN
    IF (TG_OP = 'DELETE') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('D', current_user, row_to_json(OLD));
    ELSIF (TG_OP = 'UPDATE') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('U', current_user, row_to_json(NEW));
    ELSIF (TG_OP = 'INSERT') THEN
        INSERT INTO main_log (operation_type, user_operator, changed_data)
        VALUES ('I', current_user, row_to_json(NEW));
    END IF;
    RETURN NULL;    
END;
$logging$ LANGUAGE plpgsql;
CREATE FUNCTION
lab3=# \df
                              List of functions
       Schema       |  Name   | Result data type | Argument data types | Type 
--------------------+---------+------------------+---------------------+------
 coffee_shop_schema | logging | trigger          |                     | func
(1 row)

```

### Áp Dụng Trigger Cho Các Bảng

Áp dụng trigger cho bảng `Product`.

```sql
CREATE TRIGGER product_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```

Áp dụng trigger cho bảng `Bill`.

```sql
CREATE TRIGGER bill_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```

Áp dụng trigger cho bảng `Orders`.

```sql
CREATE TRIGGER order_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```

Áp dụng trigger cho bảng `Customer`.

```sql
CREATE TRIGGER customer_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```

Áp dụng trigger cho bảng `Employee`.

```sql
CREATE TRIGGER employee_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```

Áp dụng trigger cho bảng `Warehouse`.

```sql
CREATE TRIGGER warehouse_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```

Áp dụng trigger cho bảng `Supplier`.

```sql
CREATE TRIGGER supplier_logging
AFTER INSERT OR UPDATE OR DELETE ON Product
FOR EACH ROW EXECUTE FUNCTION logging();
```

###  Kiểm Tra Hệ Thống Log
1. Thêm dữ liệu mới vào bảng Product:
```sql
INSERT INTO product (product_category_name, price, warehouse_id) 
VALUES ('Arabica Vip Pro', 200000, 1);
```
2. Cập nhật dữ liệu trong bảng Product:
```sql
UPDATE product 
SET price = 95000 
WHERE product_id = 4;
```
3. Xóa dữ liệu trong bảng Product:
```sql
DELETE FROM product 
WHERE product_id = 6;
```
5. Kiểm tra main_log
```sql
lab3=# select * from main_log;
 log_id | operation_type |       operation_date       | user_operator |                                         changed_data                                          
--------+----------------+----------------------------+---------------+-----------------------------------------------------------------------------------------------
      1 | I              | 2024-10-26 22:14:47.801626 | postgres      | {"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
      2 | U              | 2024-10-26 22:16:57.623706 | postgres      | {"product_id":4,"product_category_name":"Typica","price":95000.00,"warehouse_id":4}
      3 | D              | 2024-10-26 22:17:26.847963 | postgres      | {"product_id":6,"product_category_name":"Arabica Vip Pro","price":200000.00,"warehouse_id":1}
```


## 2. Mã Hóa Dữ Liệu Nhạy Cảm (Data Encryption)

Để bảo mật dữ liệu nhạy cảm, ta sử dụng mã hóa đối xứng AES-256 và tạo khóa mã hóa bằng hàm băm SHA-256 từ mật khẩu.

### Tạo Bảng Chứa Dữ Liệu Nhạy Cảm

```sql
CREATE TABLE secret_data (
    id SERIAL PRIMARY KEY,
    username TEXT,
    secret_token TEXT
);
```

### Mã Hóa Dữ Liệu Sử Dụng pgcrypto
1. Tạo bảng dữ liệu nhạy cảm
- Đầu tiên, chúng ta cần tạo một bảng riêng để lưu trữ dữ liệu nhạy cảm, chẳng hạn như token hoặc khóa truy cập cho từng loại người dùng. Bảng này nên được tách biệt khỏi các bảng chính của cơ sở dữ liệu.
```sql
CREATE TABLE secret_data (
    id SERIAL PRIMARY KEY,
    username TEXT,
    secret_token TEXT
);
```
- id: Khóa chính, tự động tăng.
- username: Tên người dùng.
- secret_token: Dữ liệu nhạy cảm (token hoặc khóa truy cập) sẽ được mã hóa.

2. Mã hóa dữ liệu

Chúng ta sẽ sử dụng thuật toán mã hóa đối xứng (ví dụ: AES-256) để mã hóa dữ liệu trong bảng secret_data. Điều này đảm bảo rằng ngay cả khi dữ liệu bị rò rỉ, chúng cũng sẽ không thể đọc được nếu không có khóa mã hóa.

Chuẩn Bị Sử Dụng Mô-đun pgcrypto: PostgreSQL có mô-đun pgcrypto hỗ trợ mã hóa và giải mã dữ liệu. Đầu tiên, hãy chắc chắn rằng bạn đã cài đặt mô-đun này:

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto;
```

3. Tạo khóa mã hóa từ mật khẩu

Khóa mã hóa sẽ được tạo từ mật khẩu của superuser thông qua một hàm băm (ví dụ: SHA-256). Điều này đảm bảo rằng khóa không được lưu trữ trực tiếp trong cơ sở dữ liệu.

Ví dụ

```sql
lab3=# select encode(digest('Ch.u992mvd', 'sha256'), 'hex') as encryption_key;
                          encryption_key                          
------------------------------------------------------------------
 ca69b9601669b11f98acf29d694ec0e6d52f581bef9ffbe01bf426a3c2e6418a
(1 row)

```

4. Mã Hóa Dữ Liệu Trước Khi Chèn Vào Bảng

Khi chèn dữ liệu vào bảng secret_data, chúng ta sẽ mã hóa giá trị secret_token bằng khóa đã tạo ở bước trước.

Cú pháp:

```sql
INSERT INTO secret_data (username, secret_token)
VALUES 
    ('user1', pgp_sym_encrypt('token_user1', 'your_generated_key')),
    ('user2', pgp_sym_encrypt('token_user2', 'your_generated_key'));
```
- Thay your_generated_key bằng giá trị khóa được tạo từ mật khẩu.

Ví dụ

```sql
INSERT INTO secret_data (username, secret_token) 
VALUES 
    ('Chu', pgp_sym_encrypt('token_Chu', 'ca69b9601669b11f98acf29d694ec0e6d52f581bef9ffbe01bf426a3c2e6418a')), 
    ('postgres', pgp_sym_encrypt('token_postgres', 'ca69b9601669b11f98acf29d694ec0e6d52f581bef9ffbe01bf426a3c2e6418a'));
```

5. Chứng Minh Việc Giải Mã Dữ Liệu

Để chứng minh rằng ngay cả người có quyền quản trị cũng không thể xem dữ liệu trong bảng mà không biết mật khẩu, chúng ta sẽ sử dụng phương thức giải mã.

Giải Mã Dữ Liệu: Để giải mã dữ liệu, chúng ta cần có mật khẩu gốc. Nếu không có mật khẩu này, các quản trị viên không thể giải mã và đọc được nội dung của bảng secret_data.

```sql
lab3=# select * from secret_data;
 id | username |                                                                            secret_token                                                                            
----+----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------
  1 | Chu      | \xc30d04070302cbda441b01d7b95274d23a0167245609f84edb96a65edbde2c8b5689019035e368e08cf678485dffc70a65a79480d94e9f8b21af40531c9ce1a89ca09596e9f547218265ef
  2 | postgres | \xc30d04070302571df6bfa22c5a2064d23f01406b15d947d495bc01aeb175c38236d0b2cb584474597a12109270332cc8686d8ada1e339139e6ee48af356ada4be450c8e76f019f4d9ce3a60ea7b153d5
(2 rows)
```

Như chúng ta đã thấy, chúng ta không thể đọc được nội dung trong đó là gì

Để giải mã:

```sql
-- Giải mã dữ liệu
SELECT username, pgp_sym_decrypt(secret_token::bytea, 'your_generated_key') AS decrypted_token
FROM secret_data;
```

Ví dụ

```sql
SELECT username, pgp_sym_decrypt(secret_token::bytea, 'ca69b9601669b11f98acf29d694ec0e6d52f581bef9ffbe01bf426a3c2e6418a') AS decrypted_token
FROM secret_data;
 username | decrypted_token 
----------+-----------------
 Chu      | token_Chu
 postgres | token_postgres
(2 rows)
```


## 3. Kiểm Soát Truy Cập (Access Control)

Tạo các vai trò và phân quyền cho từng vai trò dựa trên nguyên tắc quyền hạn tối thiểu.

### Tạo Vai Trò
Trước tiên, chúng ta cần tạo ít nhất hai vai trò khác nhau cho các loại người dùng khác nhau (không tính superuser). Ví dụ, trong một hệ thống quản lý quán cà phê, bạn có thể tạo các vai trò như sales_role (vai trò nhân viên bán hàng) và warehouse_role (vai trò nhân viên kho).


```sql
-- Tạo vai trò cho nhân viên bán hàng
CREATE ROLE sales_role NOLOGIN;

-- Tạo vai trò cho nhân viên kho
CREATE ROLE warehouse_role NOLOGIN;

```


### Phân Quyền

Sau khi đã tạo các vai trò, bước tiếp theo là xác định quyền hạn cho từng vai trò dựa trên nguyên tắc quyền hạn tối thiểu. Điều này có nghĩa là bạn chỉ cấp quyền truy cập cho các bảng mà mỗi vai trò cần để thực hiện công việc của mình.

Ví dụ về Quyền Hạn:

- Nhân viên bán hàng (sales_role): Có quyền truy cập để xem các bảng liên quan đến đơn hàng và khách hàng.
- Nhân viên kho (warehouse_role): Có quyền truy cập để xem và quản lý các bảng sản phẩm và kho.

**Tuy nhiên trong lab của mình các bảng để trong schema coffee_shop_schema. Nên cần cấp quyền truy cập vào schema trước**

- Cấp Quyền Truy Cập vào Schema:

```sql
GRANT USAGE ON SCHEMA coffee_shop_schema TO sales_role;
GRANT USAGE ON SCHEMA coffee_shop_schema TO warehouse_role;
```

Câu lệnh cấp quyền:

```sql
-- Cấp quyền truy cập cho nhân viên bán hàng
GRANT SELECT ON Orders TO sales_role;
GRANT SELECT ON Customer TO sales_role;

-- Cấp quyền truy cập cho nhân viên kho
GRANT SELECT, INSERT, UPDATE ON Product TO warehouse_role;
GRANT SELECT, INSERT ON Warehouse TO warehouse_role;
```




###  Quyền Truy Cập Đến Các Bảng Log

Chỉ superuser mới có quyền xem bảng log, điều này giúp bảo vệ thông tin nhạy cảm. Bạn cần đảm bảo rằng không ai khác ngoài superuser có thể truy cập bảng log này.

Câu lệnh cấp quyền:

```sql
-- Không cấp quyền cho các vai trò khác để xem bảng log
REVOKE ALL ON main_log FROM sales_role;
REVOKE ALL ON main_log FROM warehouse_role;
```

### Thực Hiện Kiểm Tra Quyền Hạn

Để kiểm tra xem các vai trò đã được phân quyền đúng hay chưa, bạn có thể thực hiện như sau:

1. Đăng Nhập với Vai Trò sales_role:

```sql
-- Đăng nhập với vai trò nhân viên bán hàng
SET ROLE sales_role;

-- Kiểm tra quyền truy cập
SELECT * FROM Orders;  -- Nên thành công
SELECT * FROM Product;  -- Nên thất bại
```

Kết quả 
```sql
lab3=# set role sales_role;
SET
lab3=> select * from orders;
 order_id | order_date | total_amount | employee_id | customer_id 
----------+------------+--------------+-------------+-------------
        1 | 2024-10-12 |    150000.00 |           2 |           1
        2 | 2024-10-13 |    599999.00 |           2 |           2
        3 | 2024-10-13 |     70000.00 |           3 |           3
        4 | 2024-10-20 |   6699999.00 |           4 |           4
(4 rows)

lab3=> select * from product;
ERROR:  permission denied for table product
```

2. Đăng Nhập với Vai Trò warehouse_role:

```sql
-- Đăng nhập với vai trò nhân viên kho
SET ROLE warehouse_role;

-- Kiểm tra quyền truy cập
SELECT * FROM Product;  -- Nên thành công
SELECT * FROM Orders;    -- Nên thất bại
```

Kết quả:

```sql
lab3=> SET ROLE warehouse_role;
SET
lab3=> SELECT * FROM Product;
 product_id | product_category_name |   price   | warehouse_id 
------------+-----------------------+-----------+--------------
          1 | Arabica               | 100000.00 |            1
          2 | Robusta               |  90000.00 |            2
          3 | Bourbon               |  96000.00 |            3
          4 | Typica                |  95000.00 |            4
(4 rows)

lab3=> SELECT * FROM Orders; 
ERROR:  permission denied for table orders
```

3. Kiểm Tra Quyền Truy Cập Đến Bảng Log:


```sql
-- Kiểm tra quyền truy cập bảng log
SELECT * FROM main_log;  -- Nên thất bại đối với tất cả các vai trò không phải superuser
```

Kết quả:

```sql
lab3=> set role sales_role;
SET
lab3=> SELECT * FROM main_log; 
ERROR:  permission denied for table main_log
lab3=> SET ROLE warehouse_role;
SET
lab3=> SELECT * FROM main_log; 
ERROR:  permission denied for table main_log
lab3=> 
```

## Kết Luận

Qua các bước trên, chúng ta đã hoàn thành việc thiết lập hệ thống bảo mật cơ sở dữ liệu với chức năng giám sát thay đổi, mã hóa dữ liệu nhạy cảm, và phân quyền truy cập.
