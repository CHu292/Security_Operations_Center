# Tạo các thành phần cơ bản của cơ sở dữ liệu

## 1. Kết nối dữ liệu bằng máy khách psql

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

## 2. Tạo cơ sở dữ liệu:
**Cú pháp**

```bash
CREATE DATABASE <tên_cơ_sở_dữ_liệu>;
```

```bash
postgres=# create database n3347_22;
CREATE DATABASE
```

**Kiểm tra**

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

*tùy chọn \l trong PostgreSQL là một lệnh được sử dụng để hiển thị danh sách các đối tượng trong cơ sở dữ liệu hiện tại, bao gồm bảng, lược đồ, view, v.v.*

**Cú pháp xóa cơ sở dữ liệu:**

```sql
DROP DATABASE <tên_cơ_sở_dữ_liệu>;
```
**Cú pháp đổi tên cơ sở dữ liệu:**

```sql
ALTER DATABASE <tên_cơ_sở_dữ_liệu_cũ> RENAME TO <tên_cơ_sở_dữ_liệu_mới>;
```

## 3. Tạo lược đồ - SCHEMA
- Đầu tiên ta cần truy cập vào cơ sở dữ liệu
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

- Lược đồ schema đóng vai trò quan trọng trong việc quản lý và truy cập dữ liệu trong cơ sở dữ liệu.
- Cú pháp:

```sql
CREATE SCHEMA <tên_lược_đồ>;
```
**ví dụ**

```sql
create schema n3247_22_schema_lab1;
```

- Cách đổi tên schema
```sql
ALTER SCHEMA tên_schema_cũ RENAME TO tên_schema_mới;
```

- Cách xem các schema đã tạo: sử dụng ```\dn```
```sql
n3347_22=# \dn
 n3247_22_schema_lab1 | postgres
 public               | pg_database_owner
```

- Xóa schema:
```sql
DROP SCHEMA tên_schema;
```
- Phân quyền cho schema (Grant permission Schema)

**Cấp quyền:**
```sql
GRANT quyền_truy_cập ON SCHEMA tên_schema TO tên_người_dùng;
```
**Xóa quyền**

```sql
DENY SELECT, INSERT, UPDATE, DELETE ON SCHEMA :: news TO  postgres
```

## 4. Tạo bảng
