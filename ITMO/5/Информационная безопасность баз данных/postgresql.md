# 1. Kết nối dữ liệu bằng máy khách psql

```bash
sudo systemctl enable --now postgresql.service
```

```bash
sudo su postgres -c psql
```
**Giải thích tập lệnh:**
- Câu lệnh "sudo systemctl enable --now postgresql.service" được sử dụng để cài đặt và kích hoạt dịch vụ "PostgreSQL", đồng thời đảm bảo rằng dịch vụ này sẽ được khởi động tự động ngay lập tức và sau mỗi lần khởi động hệ thống.
- sudo: Được sử dụng để thực thi câu lệnh với quyền hạn của người dùng root hoặc một người dùng khác có quyền hạn tương đương.
- systemctl: Là một công cụ trong hệ thống systemd để quản lý các dịch vụ, thiết bị và các thành phần hệ thống khác.
- enable: Kích hoạt dịch vụ để khởi động cùng với hệ thống. Nó thêm một liên kết tới dịch vụ trong các thư mục systemd để đảm bảo rằng dịch vụ sẽ được khởi động tự động khi hệ thống khởi động.
- --now: Khi kết hợp với enable, sự kết hợp này đảm bảo rằng dịch vụ sẽ được khởi động ngay lập tức sau khi được kích hoạt.
- postgresql.service: Là tên của dịch vụ PostgreSQL. Trong trường hợp này, câu lệnh đang làm việc với dịch vụ PostgreSQL, có thể là một cơ sở dữ liệu quan hệ mạnh mẽ và phổ biến được sử dụng trong nhiều ứng dụng.
- su postgres: Lệnh này thay đổi người dùng hiện tại thành postgres.
- -c psql: Lệnh này chạy chương trình psql với các quyền của người dùng postgres.

# 2. Thao tác với cơ sở dữ liệu:

#### 2.1 Tạo cơ sở dữ liệu

```bash
CREATE DATABASE <tên_cơ_sở_dữ_liệu>;
```

```bash
postgres=# create database n3347_22;
CREATE DATABASE
```

#### 2.2 Xóa cơ sở dữ liệu

```sql
DROP DATABASE <tên_cơ_sở_dữ_liệu>;
```
#### 2.3 Đổi tên cơ sở dữ liệu

```sql
ALTER DATABASE <tên_cơ_sở_dữ_liệu_cũ> RENAME TO <tên_cơ_sở_dữ_liệu_mới>;
```

#### 2.4 Liệt kê tất cả các sơ sở dữ liệu

```\l```

*tùy chọn \l trong PostgreSQL là một lệnh được sử dụng để hiển thị danh sách các đối tượng trong cơ sở dữ liệu hiện tại, bao gồm bảng, lược đồ, view, v.v.*

``` bash
postgres=# \l
                                                          List of databases
      Name      |  Owner   | Encoding | Locale Provider |   Collate   |    Ctype    | ICU Locale | ICU Rules |   Access privileges   
----------------+----------+----------+-----------------+-------------+-------------+------------+-----------+-----------------------
 coffee_shop_db | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | 
 my_data        | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | =Tc/postgres         +
                |          |          |                 |             |             |            |           | postgres=CTc/postgres+
                |          |          |                 |             |             |            |           | chu=CTc/postgres
 n3347_22       | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | 
 postgres       | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | 
 template0      | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | =c/postgres          +
                |          |          |                 |             |             |            |           | postgres=CTc/postgres
 template1      | postgres | UTF8     | libc            | en_US.UTF-8 | en_US.UTF-8 |            |           | =c/postgres          +
                |          |          |                 |             |             |            |           | postgres=CTc/postgres
(6 rows)
```

#### 2.5 Kết nối với cơ sở dữ liệu
- Cú pháp:
```bash
\c <cơ sở dữ liệu bạn muốn kết nối
```
- Ví dụ:
```bash
postgres=# \c n3347_22 
You are now connected to database "n3347_22" as user "postgres".
n3347_22=# 
```

#### 2.6 Xem tất cả các người dùng

```\du```

```sql
n3347_22=# \du
 chu       | Superuser, Create role, Create DB
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS
```

# 3 Thao tác với schema  
#### 3.1 Xem các schema đã tạo:

```bash
\dn
```

```sql
n3347_22=# \dn
 n3247_22_schema_lab1 | postgres
 public               | pg_database_owner
```

#### 3.2 Tạo Schema
```sql
CREATE SCHEMA <tên_lược_đồ>;
```
**ví dụ**

```sql
create schema n3247_22_schema_lab1;
```

#### 3.3 Đổi tên schema
```sql
ALTER SCHEMA tên_schema_cũ RENAME TO tên_schema_mới;
```

#### 3.4 Xóa schema
```sql
DROP SCHEMA tên_schema;
```
#### 3.5 Phân quyền cho schema (Grant permission Schema)

**Bạn có thể cấp các quyền truy cập sau cho schema:**

- USAGE: Cho phép người dùng truy cập vào schema, nhưng không thể tạo đối tượng mới trong schema.
- CREATE: Cho phép người dùng tạo đối tượng mới (như bảng, chỉ mục) trong schema.
- Cú pháp:
```sql
GRANT quyền_truy_cập ON SCHEMA tên_schema TO tên_người_dùng;
```
- Cho phép người dùng chu có quyền truy cập (usage) vào schema n3247_22_schema_lab1:
```sql
n3347_22=# grant usage on schema n3247_22_schema_lab1 to chu;
GRANT
```
- Cho phép người dùng chu có quyền tạo đối tượng (create) trong schema n3247_22_schema_lab1:

```sql
n3347_22=# grant create on schema n3247_22_schema_lab1 to chu;
GRANT
```
- ấp cả quyền truy cập và tạo đối tượng cho người dùng chu
```sql
n3347_22=# grant usage, create on schema n3247_22_schema_lab1 to chu;
GRANT
```

#### 3.6 Phân quyền cho các đối tượng trong schema

**Bạn cũng có thể cấp quyền truy cập vào các đối tượng bên trong schema, như bảng hoặc hàm:**

- SELECT: Cho phép người dùng đọc dữ liệu từ bảng.
- INSERT: Cho phép người dùng thêm dữ liệu vào bảng.
- UPDATE: Cho phép người dùng cập nhật dữ liệu trong bảng.
- DELETE: Cho phép người dùng xóa dữ liệu từ bảng.
- ALL PRIVILEGES: Cấp tất cả các quyền cho đối tượng
- Cú pháp:
```sql
GRANT quyền_truy_cập ON đối_tượng (bảng/hàm) TO tên_người_dùng;
```
- Ví dụ:
```sql
n3347_22=# grant select on n3247_22_schema_lab1.my_table to chu;
GRANT
```
#### 3.7 Xóa quyền trên schema
- Cú pháp:
```sql
REVOKE quyền_truy_cập ON SCHEMA tên_schema FROM tên_người_dùng;
```
- Ví dụ:
```sql
n3347_22=# revoke usage on schema n3247_22_schema_lab1 from chu;
REVOKE
```
#### 3.8  Xóa quyền trên các đối tượng trong schema (bảng, hàm)
- Cú pháp
```sql
REVOKE quyền_truy_cập ON đối_tượng (bảng/hàm) FROM tên_người_dùng;
```
- Ví dụ:
```sql
n3347_22=# revoke select on n3247_22_schema_lab1.my_table from chu;
REVOKE
```
#### 3.9  Xóa quyền trên tất cả các đối tượng hiện tại và tương lai trong schema
- Nếu bạn đã cấp quyền cho tất cả các đối tượng bên trong schema, và muốn xóa chúng, bạn có thể sử dụng lệnh như sau:
```sql
REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA tên_schema FROM tên_người_dùng;
```
- Ví dụ:
```sql
n3347_22=# revoke all privileges on all tables in schema n3247_22_schema_lab1 from chu;
REVOKE
```

# 4 Thao tác với bảng
### 4.1 Tạo bảng (create table)
- Cú pháp:
```sql
CREATE TABLE tên_bảng (
    tên_cột kiểu_dữ_liệu [ràng buộc],
    ...
);
```
- Ví dụ:
```sql
n3347_22=# CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(50),
    salary NUMERIC(10, 2)
);
CREATE TABLE
```
- Khi bạn tạo một bảng trong PostgreSQL mà không chỉ định schema, bảng đó sẽ được tạo trong schema mặc định của phiên làm việc, thường là schema public. Schema public là schema mặc định mà PostgreSQL thiết lập khi bạn tạo cơ sở dữ liệu mới, và tất cả người dùng đều có quyền truy cập vào nó trừ khi bạn thay đổi quyền.
- Xác định schema hiện tại:
```bash
SHOW search_path;
```
```sql
n3347_22=# SHOW search_path;
 "$user", public
```
### 4.2 Tạo bảng trong schema cụ thể:
- Cú pháp:
```sql
CREATE TABLE tên_schema.tên_bảng (
    tên_cột kiểu_dữ_liệu [ràng buộc],
    ...
);
```
### 4.3 Thay đổi search_path để sử dụng schema khác:
- Cú pháp
```sql
SET search_path TO tên_schema;
```
- Ví dụ:
```sql
n3347_22=# SHOW search_path;
 "$user", public

n3347_22=# set search_path to n3247_22_schema_lab1;
SET
n3347_22=# show search_path;
 n3247_22_schema_lab1
```
### 4.4 Thêm cột vào bảng (Add Column)
- Cú pháp:
```sql
ALTER TABLE tên_bảng ADD COLUMN tên_cột kiểu_dữ_liệu [ràng buộc];
```
- Ví dụ:
```sql
n3347_22=# ALTER TABLE employees ADD COLUMN hire_date DATE;
ALTER TABLE
```
### 4.5 Xóa cột khỏi bảng (Drop Column)
- Cú pháp:
```sql
ALTER TABLE tên_bảng DROP COLUMN tên_cột;
```
- Ví dụ:
```sql
n3347_22=# ALTER TABLE employees DROP COLUMN hire_date;
ALTER TABLE
```
### 4.6 Đổi tên bảng (Rename Table)
- Cú pháp:
```sql
ALTER TABLE tên_bảng_cũ RENAME TO tên_bảng_mới;
```
- Ví dụ:
```sql
n3347_22=# ALTER TABLE employees RENAME TO staff;
ALTER TABLE
```
### 4.7 Đổi tên cột (Rename Column)
- Cú pháp:
```sql
ALTER TABLE tên_bảng RENAME COLUMN tên_cột_cũ TO tên_cột_mới;
```
- Ví dụ:
```sql
n3347_22=# alter table staff rename column id to staff_id;
ALTER TABLE
```
### 4.8 Sửa kiểu dữ liệu của cột (Alter Column Data Type)
- Cú pháp:
```sql
ALTER TABLE tên_bảng ALTER COLUMN tên_cột SET DATA TYPE kiểu_dữ_liệu_mới;
```
- Ví dụ:
```sql
n3347_22=# alter table staff alter column salary set data type decimal(12,2);
ALTER TABLE
```

### 4.9  Xóa bảng (Drop Table)

- Cú pháp:
```sql
DROP TABLE tên_bảng;
```
- Ví dụ:
```sql
n3347_22=# drop table my_table;
DROP TABLE
```
### 4.10 Chèn dữ liệu vào bảng (Insert Data)
- Cú pháp:
```sql
INSERT INTO tên_bảng (cột1, cột2, ...) VALUES (giá_trị1, giá_trị2, ...);
```
- Ví dụ:
```sql
n3347_22=# insert into employee (staff_id, name, salary) values (1, 'Chu', 500000);
INSERT 0 1
```
### 4.11  Cập nhật dữ liệu (Update Data)
-  Cú pháp:
```sql
UPDATE tên_bảng SET cột1 = giá_trị_mới WHERE điều_kiện;
```
- Ví dụ:
```sql
n3347_22=# update employee set salary = 10000000 where name = 'Chu';
UPDATE 1
```
### 4.12 Truy vấn dữ liệu (Select Data)
- Cú pháp xem tất cả dữ liệu:
```sql
SELECT * FROM tên_bảng;
```
```sql
n3347_22=# select * from employee;
        1 | Chu  |          | 10000000.00
```

- Cú pháp xem một số cột cụ thể:
```sql
SELECT cột1, cột2, ... FROM tên_bảng;
```
```sql
n3347_22=# select name, salary from employee;
 Chu  | 10000000.00
```
- Cú pháp xem dữ liệu với điều kiện:
```sql
SELECT cột1, cột2, ... FROM tên_bảng WHERE điều_kiện;
```
- Xem số lượng hàng trong bảng (Row Count)
```sql
SELECT COUNT(*) FROM tên_bảng;
```
-  Xem cấu trúc bảng và chỉ mục (Indexes)
```sql
\d+ tên_bảng
```

# 5 Kiểu dữ liệu
### 5.1 Kiểu dữ liệu tổng hợp (Composite Type)
- Trong PostgreSQL, kiểu tổng hợp (composite type) là kiểu dữ liệu mà bạn có thể định nghĩa, bao gồm nhiều trường với các kiểu dữ liệu khác nhau, giống như một bản ghi (record) hay một hàng trong bảng.

- Cú pháp tạo kiểu tổng hợp 
```sql
CREATE TYPE tên_kiểu AS (
    tên_trường1 kiểu_dữ_liệu1,
    tên_trường2 kiểu_dữ_liệu2,
    ...
);
```

- Ví dụ
```sql
CREATE TYPE employee_info AS (
    name VARCHAR(100),
    age INTEGER,
    position VARCHAR(50)
);
```

- Sử dụng kiểu tổng hợp
- Khai báo cột sử dụng kiểu tổng hợp: Sau khi tạo kiểu tổng hợp, bạn có thể sử dụng nó trong định nghĩa bảng như một cột.
```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    info employee_info -- Cột sử dụng kiểu tổng hợp
);
```
```sql
n3347_22=# \d employees
 id     | integer       |           | not null | nextval('employees_id_seq'::regclass)
 info   | employee_info |           |          | 
```
- Chèn dữ liệu vào bảng với kiểu tổng hợp: Để chèn dữ liệu vào cột kiểu tổng hợp, bạn cần sử dụng cú pháp phù hợp cho composite type.
```sql
n3347_22=# insert into employees (info) values (row('Chu', 30, 'Manager'));
INSERT 0 1
```
- Truy vấn dữ liệu từ bảng với kiểu tổng hợp: Bạn có thể truy vấn và truy cập các trường trong kiểu tổng hợp bằng cách sử dụng dấu chấm ```.```.
```sql
n3347_22=# SELECT (info).name, (info).age, (info).position FROM employees;
 Chu  |  30 | Manager
```
- Cập nhật dữ liệu trong kiểu tổng hợp: Để cập nhật một phần của kiểu tổng hợp, bạn có thể thực hiện như sau:

```sql
n3347_22=# update employees set info = row('Chu', 22, 'Senior Manager') where id = 1;
UPDATE 1
n3347_22=# SELECT (info).name, (info).age, (info).position FROM employees;
 Chu  |  22 | Senior Manager
```
- Hoặc chỉ cập nhật một trường trong kiểu tổng hợp:
 ```sql
n3347_22=# update employees set info.age = 21 where id = 1;
UPDATE 1
n3347_22=# SELECT (info).name, (info).age, (info).position FROM employees;
 Chu  |  21 | Senior Manager
```
- Xóa kiểu tổng hợp
```sql
DROP TYPE tên_kiểu;
```

### 5.2 Kiểu liệt kê (ENUM)
- Trong PostgreSQL, kiểu dữ liệu liệt kê (ENUM) cho phép bạn xác định một tập hợp các giá trị hợp lệ và chỉ cho phép các giá trị đó xuất hiện trong cột của bảng. Nó rất hữu ích khi bạn muốn giới hạn các giá trị của cột vào một danh sách cố định, ví dụ như trạng thái, phân loại, hoặc các loại dữ liệu khác có số lượng hữu hạn các lựa chọn.
- Cú pháp tạo kiểu liệt kê (ENUM)
```sql
CREATE TYPE tên_kiểu AS ENUM ('giá_trị1', 'giá_trị2', ..., 'giá_trịN');
```
- Ví dụ
```sql
n3347_22=# create type job_status as enum ('active', 'inactive', 'on_leave');
CREATE TYPE
```

- Sử dụng kiểu liệt kê trong bảng: Tạo bảng employees với một cột sử dụng kiểu liệt kê:

```sql
n3347_22=# create table employees (id serial primary key, name varchar(100), status job_status);
CREATE TABLE
n3347_22=# \d employees
 id     | integer                |           | not null | nextval('employees_id_seq'::regclass)
 name   | character varying(100) |           |          | 
 status | job_status             |           |          | 

```
- Chèn dữ liệu vào cột kiểu ENUM:

```sql
n3347_22=# insert into employees (name, status) values ('Chu', 'active'), ('Miran', 'inactive');
INSERT 0 2
```
- Truy vấn dữ liệu từ bảng có kiểu ENUM:
```sql
n3347_22=# select name, status from employees where status = 'active';
 Chu  | active
```
- Cập nhật giá trị của cột kiểu ENUM:

```sql
n3347_22=# update employees set status = 'on_leave' where name = 'Chu';
UPDATE 1
n3347_22=# select name, status from employees where status = 'on_leave';
 Chu  | on_leave
```
- Xóa kiểu ENUM:
```sql
DROP TYPE tên_kiểu;
```
### 5.3 Tạo tên miền
- Trong PostgreSQL, tên miền (domain) là một cách để tạo ra một kiểu dữ liệu mới dựa trên kiểu dữ liệu hiện có, nhưng với các ràng buộc bổ sung. Nó giúp tạo các kiểu dữ liệu tái sử dụng có tính nhất quán và hợp lệ trên nhiều bảng, tương tự như việc mở rộng một kiểu dữ liệu với các quy tắc riêng.

- Cú pháp tạo tên miền (Domain)
```sql
CREATE DOMAIN tên_tên_miền AS kiểu_dữ_liệu
    [ DEFAULT giá_trị_mặc_định ]
    [ CONSTRAINT tên_ràng_buộc ràng_buộc ];
```
  - tên_tên_miền: Tên của tên miền.
  - kiểu_dữ_liệu: Kiểu dữ liệu cơ sở (ví dụ: VARCHAR, INTEGER, v.v.).
  - DEFAULT: Giá trị mặc định cho tên miền (tùy chọn).
  - CONSTRAINT: Ràng buộc (constraint) để kiểm soát tính hợp lệ của dữ liệu.

- Ví dụ: Giả sử bạn muốn tạo một tên miền cho số điện thoại, là chuỗi ký tự có độ dài tối đa 10 ký tự và không được phép chứa giá trị NULL.

```sql
n3347_22=# create domain phone_number as varchar(10) check (value ~ '^[0-9]+$') not null;
CREATE DOMAIN
```
  - Tên miền phone_number có kiểu dữ liệu cơ sở là VARCHAR(10).
  - Ràng buộc CHECK đảm bảo rằng giá trị phải chỉ bao gồm các chữ số từ 0 đến 9.
  - NOT NULL đảm bảo không có giá trị NULL được chấp nhận.

- Sử dụng tên miền trong bảng

```sql
n3347_22=# CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone phone_number -- Sử dụng tên miền
);
CREATE TABLE
```
- Chèn dữ liệu vào bảng có tên miền:
```sql
n3347_22=# INSERT INTO employees (name, phone)
VALUES ('Sun', '0123456789'),
       ('Miran', '0987654321');
INSERT 0 2
```

- Sửa đổi tên miền:

```sql
n3347_22=# ALTER DOMAIN phone_number SET DEFAULT '0000000000';
ALTER DOMAIN
```
- Xóa tên miền
```sql
DROP DOMAIN tên_tên_miền;
```
### 5.4 Chỉ mục (index)

- Trong PostgreSQL, chỉ mục (index) là một cấu trúc dữ liệu giúp tăng tốc độ truy vấn và tìm kiếm dữ liệu trong bảng. Khi bạn tạo một chỉ mục trên một hoặc nhiều cột của bảng, PostgreSQL sẽ duy trì một bản sao đã sắp xếp của dữ liệu trong các cột đó, cho phép truy cập nhanh hơn. Tuy nhiên, việc tạo chỉ mục cũng có chi phí về dung lượng và tốc độ ghi dữ liệu (INSERT/UPDATE/DELETE).
- Cú pháp tạo chỉ mục (Index)

```sql
CREATE [UNIQUE] INDEX tên_chỉ_mục
    ON tên_bảng (cột1 [ASC|DESC], cột2 [ASC|DESC], ...);
```
  - UNIQUE: Tùy chọn để đảm bảo rằng các giá trị trong cột được chỉ mục là duy nhất.
  - ASC|DESC: Tùy chọn để xác định thứ tự sắp xếp tăng dần (ASC) hoặc giảm dần (DESC).
  - tên_bảng: Tên bảng mà bạn muốn tạo chỉ mục.
  - cột1, cột2: Các cột bạn muốn chỉ mục

- Ví dụ 1: Tạo chỉ mục cơ bản
- Bây giờ PostgreSQL sẽ sử dụng chỉ mục này khi bạn truy vấn bảng employees với điều kiện dựa trên cột name.
```sql
n3347_22=# create index idx_employee_name on employees (name);
CREATE INDEX
n3347_22=# select * from employees where name = 'Sun';
 id | name |   phone    
----+------+------------
  1 | Sun  | 0123456789
(1 row)
```
- Ví dụ 2: Tạo chỉ mục đa cột
- Tạo chỉ mục trên nhiều cột, ví dụ: name và position, để tối ưu hóa truy vấn có điều kiện trên cả hai cột.
```sql
n3347_22=# create index inx_employee_name_position on employees (name, position);
CREATE INDEX
```
- Ví dụ 3: Tạo chỉ mục duy nhất (UNIQUE)
- Nếu bạn muốn đảm bảo rằng giá trị của cột được chỉ mục là duy nhất, bạn có thể thêm từ khóa UNIQUE.
```sql
n3347_22=# create unique index idx_employee_phone on employees (phone);
CREATE INDEX
```
-> Điều này đảm bảo rằng không có hai nhân viên nào có cùng số điện thoại trong cột phone.
- Ví dụ 4: Chỉ mục với thứ tự sắp xếp
- Bạn có thể chỉ định thứ tự sắp xếp của cột trong chỉ mục bằng ASC (tăng dần) hoặc DESC (giảm dần). Điều này có thể hữu ích trong các trường hợp truy vấn cụ thể.
```sql
n3347_22=# create index idx_emloyee_salary_desc on employees (salary desc);
CREATE INDEX
```
- Truy vấn sử dụng chỉ mục với sắp xếp giảm/tăng dần:

```sql
n3347_22=# SELECT name, salary
FROM employees
ORDER BY salary DESC;
 name  |   salary   
-------+------------
 Sun   | 2532252.00
 Miran | 2522115.00
(2 rows)

n3347_22=# CREATE INDEX idx_employee_salary_asc
    ON employees (salary ASC);
CREATE INDEX
n3347_22=# SELECT name, salary
FROM employees
ORDER BY salary ASC;
 name  |   salary   
-------+------------
 Miran | 2522115.00
 Sun   | 2532252.00
(2 rows)
```
- Kiểm tra chỉ mục hiện có
```sql
\d tên_bảng
```
- Xóa chỉ mục
```sql
DROP INDEX tên_chỉ_mục;
```

# 6 Chế độ xem view
- Trong PostgreSQL, View (chế độ xem) là một bảng ảo được định nghĩa bằng một truy vấn SQL. View không lưu trữ dữ liệu thực tế mà lưu trữ kết quả của truy vấn SQL đã định nghĩa. View giúp tổ chức các truy vấn phức tạp, bảo mật dữ liệu, và cung cấp cách tiếp cận nhất quán cho dữ liệu từ nhiều bảng khác nhau.

### 6.1 Cú pháp tạo View
```sql
CREATE VIEW tên_view AS
SELECT cột1, cột2, ...
FROM bảng
WHERE điều_kiện;
```
  - tên_view: Tên của view bạn muốn tạo.
  - SELECT: Truy vấn SQL xác định nội dung của view. Nó có thể là bất kỳ truy vấn hợp lệ nào trong PostgreSQL.

**- Xem view đã có**
```sql
SELECT table_name 
FROM information_schema.views 
WHERE table_schema = 'tên schema';
```
ví dụ:
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

### 6.2 Ví dụ 1: Tạo view đơn giản
- Giả sử bạn có bảng employees với các cột như id, name, salary, và position. Bạn muốn tạo một view chỉ hiển thị các nhân viên có lương cao hơn 50,000.

```sql
3347_22=# CREATE VIEW high_salary_employees AS
SELECT id, name, salary
FROM employees
WHERE salary > 50000;
CREATE VIEW
n3347_22=# SELECT * FROM high_salary_employees;
 id | name  |   salary   
----+-------+------------
  1 | Sun   | 2532252.00
  2 | Miran | 2522115.00
(2 rows)
```

### 6.3 Ví dụ 2: Tạo view phức tạp với JOIN
- Bạn cũng có thể tạo view từ nhiều bảng với các truy vấn phức tạp, chẳng hạn như kết hợp các bảng bằng cách sử dụng JOIN.

- Giả sử bạn có hai bảng employees và departments:

  - employees có cột: id, name, salary, department_id.
```sql
n3347_22=# select * from employees;
 id | name  |   phone    |    position    |   salary   | department_id 
----+-------+------------+----------------+------------+---------------
  1 | Sun   | 0123456789 | senior Manager | 2532252.00 |             1
  2 | Miran | 0987654321 | Manager        | 2522115.00 |             2
(2 rows)
```
  - departments có cột: department_id, department_name.
```sql
n3347_22=# select * from departments;
 department_id | department_name 
---------------+-----------------
             1 | Vingroup
             2 | SaiGon
(2 rows)
```
Bạn muốn tạo một view hiển thị tên nhân viên cùng với tên phòng ban của họ:
```sql
n3347_22=# CREATE VIEW employee_department_view AS
SELECT e.id, e.name, e.salary, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;
CREATE VIEW
```
- Bây giờ, bạn có thể truy vấn employee_department_view để xem nhân viên cùng với tên phòng ban:

```sql
n3347_22=# SELECT * FROM employee_department_view;
 id | name  |   salary   | department_name 
----+-------+------------+-----------------
  1 | Sun   | 2532252.00 | Vingroup
  2 | Miran | 2522115.00 | SaiGon
(2 rows)
```

### 6.4 Ví dụ 3: Tạo view có ràng buộc bảo mật

- Giả sử bạn không muốn người dùng nhìn thấy mức lương của nhân viên, bạn có thể tạo một view chỉ hiển thị tên và phòng ban:

```sql
n3347_22=# CREATE VIEW employee_public_view AS
SELECT e.name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;
CREATE VIEW
n3347_22=# select * from employee_public_view;
 name  | department_name 
-------+-----------------
 Sun   | Vingroup
 Miran | SaiGon
(2 rows)
```
-> Người dùng chỉ có thể truy cập thông tin thông qua view này mà không thấy mức lương.

- Xóa view
```sql
DROP VIEW tên_view;
```

