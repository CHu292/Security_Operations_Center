# 1. Xây dựng chương trình bảo vệ file
```python
import os
import hashlib
import fnmatch
import stat
import subprocess

TEMPLATE_FILE = 'template.tbl'

# Hàm để đọc file template.tbl
def read_template_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    hashed_password = lines[0].strip()  # Dòng đầu tiên chứa mật khẩu đã được băm
    forbidden_files = [line.strip() for line in lines[1:]]  # Danh sách các tệp bị cấm
    return hashed_password, forbidden_files

# Hàm để băm mật khẩu
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Hàm kiểm tra mật khẩu người dùng
def check_password(hashed_password, input_password):
    return hashed_password == hash_password(input_password)

# Hàm kiểm tra xem tệp có bị cấm hay không
def is_forbidden_file(filename, forbidden_files):
    for pattern in forbidden_files:
        if fnmatch.fnmatch(filename, pattern):
            return True
    return False

# Hàm bảo vệ tệp (cấm đọc, ghi, xóa, di chuyển)
def protect_file(filepath):
    # Đặt quyền không đọc, ghi và thực thi cho tất cả người dùng
    os.chmod(filepath, 0)
    # Sử dụng chattr để ngăn chặn xóa và di chuyển tệp (immutable)
    subprocess.run(['sudo', 'chattr', '+i', filepath])
    print(f"Tệp đã được bảo vệ: {filepath}")

# Hàm gỡ bảo vệ tệp (cho phép đọc, ghi, xóa, di chuyển)
def unprotect_file(filepath):
    # Gỡ thuộc tính immutable (cho phép xóa tệp)
    subprocess.run(['sudo', 'chattr', '-i', filepath])
    # Khôi phục quyền đọc, ghi và thực thi cho chủ sở hữu
    os.chmod(filepath, stat.S_IRWXU)
    print(f"Quyền truy cập tệp đã được khôi phục: {filepath}")

# Hàm bảo vệ hoặc gỡ bảo vệ các tệp trong thư mục hiện tại
def protect_files(directory, forbidden_files, enable=True):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if is_forbidden_file(file, forbidden_files):
                filepath = os.path.join(root, file)
                if enable:
                    protect_file(filepath)
                else:
                    unprotect_file(filepath)

# Hàm bật/tắt chế độ bảo vệ
def toggle_protection(template_file, enable=True):
    hashed_password, forbidden_files = read_template_file(template_file)
    
    input_password = input("Nhập mật khẩu để bật/tắt bảo vệ: ")
    
    if check_password(hashed_password, input_password):
        if enable:
            print("Mật khẩu đúng! Bắt đầu bảo vệ các tệp.")
        else:
            print("Mật khẩu đúng! Đang gỡ bảo vệ các tệp.")
        current_directory = os.getcwd()  # Thư mục hiện tại
        protect_files(current_directory, forbidden_files, enable)
    else:
        print("Mật khẩu sai! Không thể bật/tắt chế độ bảo vệ.")

# Chạy chương trình
if __name__ == "__main__":
    choice = input("Nhập 'on' để bật bảo vệ hoặc 'off' để tắt bảo vệ: ").strip().lower()
    if choice == 'on':
        toggle_protection(TEMPLATE_FILE, enable=True)
    elif choice == 'off':
        toggle_protection(TEMPLATE_FILE, enable=False)
    else:
        print("Lựa chọn không hợp lệ.")
```

## 1.1 Xử lý tệp tin (File Handling)

### 1.1.1 Open Files
Trước khi làm việc với bất cứ file nào, bạn phải mở file đó. Để mở một file, Python cung cấp hàm `open()`. Nó trả về một đối tượng file mà được sử dụng với các hàm khác. Với file đã mở, bạn có thể thực hiện các hoạt động như đọc, ghi mới, ghi thêm … trên file đó.
- Cú pháp:
`file object = open(file_name [, access_mode][, buffering])`
Trong đó:
- **filename**: Đối số file_name là một giá trị chuỗi chứa tên của các file mà bạn muốn truy cập.
- **access_mode**: Các access_mode xác định các chế độ của file được mở ra như read, write, append,... Đây là thông số tùy chọn và chế độ truy cập file mặc định là read (r).
- **buffering**: Nếu buffer được thiết lập là 0, nghĩa là sẽ không có trình đệm nào diễn ra. Nếu xác định là 1, thì trình đệm dòng được thực hiện trong khi truy cập một File. Nếu là số nguyên lớn hơn 1, thì hoạt động đệm được thực hiện với kích cỡ bộ đệm đã cho. Nếu là số âm, thì kích cỡ bộ đệm sẽ là mặc định.
  
| MODE  | MÔ TẢ |
|-------|-------|
| ‘r’   | Chế độ chỉ được phép đọc. |
| ‘r+’  | Chế độ được phép đọc và ghi. |
| ‘rb’  | Mở file chế độ đọc cho định dạng nhị phân. Con trỏ tại phần bắt đầu của file. |
| ‘rb+’ | Mở file để đọc và ghi trong định dạng nhị phân. Con trỏ tại phần bắt đầu của file. |
| ‘r+b’ | Mở file để đọc và ghi trong định dạng nhị phân. Con trỏ tại phần bắt đầu của file. |
| ‘w’   | Mở file để ghi. Nếu file không tồn tại thì sẽ tạo mới file và ghi nội dung, nếu file đã tồn tại thì sẽ bị cắt bớt (truncate) và ghi đè lên nội dung cũ. |
| ‘w+’  | Mở file để đọc và ghi. Nếu file không tồn tại thì sẽ tạo mới file và ghi nội dung, nếu file đã tồn tại thì sẽ bị cắt bớt (truncate) và ghi đè lên nội dung cũ. |
| ‘wb’  | Mở file để ghi cho dạng nhị phân. Nếu file không tồn tại thì sẽ tạo mới file và ghi nội dung, nếu file đã tồn tại thì sẽ bị cắt bớt (truncate) và ghi đè lên nội dung cũ. |
| ‘wb+’ | Mở file để đọc và ghi cho dạng nhị phân. Nếu file không tồn tại thì sẽ tạo mới file và ghi nội dung, nếu file đã tồn tại thì sẽ bị cắt bớt (truncate) và ghi đè lên nội dung cũ. |
| ‘w+b’ | Mở file để đọc và ghi cho dạng nhị phân. Nếu file không tồn tại thì sẽ tạo mới file và ghi nội dung, nếu file đã tồn tại thì sẽ bị cắt bớt (truncate) và ghi đè lên nội dung cũ. |
| ‘a’   | Mở file chế độ ghi tiếp. Nếu file đã tồn tại rồi thì nó sẽ ghi tiếp nội dung vào cuối file, nếu file không tồn tại thì tạo một file mới và ghi nội dung vào đó. |
| ‘a+’  | Mở file chế độ đọc và ghi tiếp. Nếu file đã tồn tại rồi thì nó sẽ ghi tiếp nội dung vào cuối file, nếu file không tồn tại thì tạo một file mới và ghi nội dung vào đó. |
| ‘ab’  | Mở file chế độ ghi tiếp ở dạng nhị phân. Nếu file đã tồn tại rồi thì nó sẽ ghi tiếp nội dung vào cuối file, nếu file không tồn tại thì tạo một file mới và ghi nội dung vào đó. |
| ‘ab+’ | Mở file chế độ đọc và ghi tiếp ở dạng nhị phân. Nếu file đã tồn tại rồi thì nó sẽ ghi tiếp nội dung vào cuối file, nếu file không tồn tại thì tạo một file mới và ghi nội dung vào đó. |
| ‘a+b’ | Mở file chế độ đọc và ghi tiếp ở dạng nhị phân. Nếu file đã tồn tại rồi thì nó sẽ ghi tiếp nội dung vào cuối file, nếu file không tồn tại thì tạo một file mới và ghi nội dung vào đó. |
| ‘x’   | Mở file chế độ ghi. Tạo file độc quyền mới (exclusive creation) và ghi nội dung, nếu file đã tồn tại thì chương trình sẽ báo lỗi. |
| ‘x+’  | Mở file chế độ đọc và ghi. Tạo file độc quyền mới (exclusive creation) và ghi nội dung, nếu file đã tồn tại thì chương trình sẽ báo lỗi. |
| ‘xb’  | Mở file chế độ ghi dạng nhị phân. Tạo file độc quyền mới và ghi nội dung, nếu file đã tồn tại thì chương trình sẽ báo lỗi. |
| ‘xb+’ | Mở file chế độ đọc và ghi dạng nhị phân. Tạo file độc quyền mới và ghi nội dung, nếu file đã tồn tại thì chương trình sẽ báo lỗi. |
| ‘b’   | Mở file ở chế độ nhị phân. |
| ‘t’   | Mở file ở chế độ văn bản (mặc định). |

Tuy nhiên, chế độ mặc định khi mở file là text, nên nếu mục đích là mở đúng loại này, chúng ta không cần ghi loại file mà chỉ cần ghi chế độ mở là được.

- Thuộc tính của File
  
| Thuộc tính   | Mô tả                                                            |
|--------------|------------------------------------------------------------------|
| `file.closed`| Trả về `True` nếu file đã đóng, ngược lại là `False`.            |
| `file.mode`  | Trả về chế độ của file đang được mở.                             |
| `file.name`  | Trả về tên của file.                                             |


Ví dụ tôi có file với nội dung sau:

```bash
$ cat test.txt 
Hello World
```

Trong chương trình Python ta thực hiện như sau:

```python
f = open("test.txt", 'r')
```

Lưu ý là file chương trình Python và file chứa dữ liệu phải nằm cùng thư mục, nếu chúng nằm khác thư mục, chúng ta phải dùng đường dẫn tuyệt đối trong phần tên file.

Khi làm việc với các tệp ở chế độ văn bản, bạn nên chỉ định loại mã hóa:

```python
f = open("test.txt", mode='r', encoding='utf-8')
```


### 1.1.2 Đọc Tệp (Read Files)

- **Cú pháp:**
```python
fileObject.read([size])
```
Phương thức này trả về một chuỗi có kích thước bằng `size`. Nếu không truyền `size` thì toàn bộ nội dung của file sẽ được đọc.

**Ví dụ:**
```python
>>> f = open("test.txt", 'r')
>>> f.read()
'Hello World\n'
```

### 1.1.3 Phương thức readline

- **Cú pháp:**
```python
fileObject.readline()
```
Phương thức này cho phép đọc một dòng trong file và trả về chuỗi.

**Ví dụ:**
```python
>>> f = open("test.txt", 'r')
>>> line_1 = f.readline()
>>> line_2 = f.readline()
>>> print('Line 1: ', line_1)
Line 1:  Hello World

>>> print('Line 2: ', line_2)
Line 2:  Hello World x2
```

### 1.1.4 Writting Files
Tương tự đọc file, để ghi một file ta cần mở file bằng cú pháp để ghi và sử dụng phương thức write để ghi vào.
**- Cú pháp: **  
`fileObject.write(string)`  
Phương thức này cho phép ghi một chuỗi có nội dung là string vào vị trí của con trỏ trong file.

```python
>>> f = open("test.txt", 'a')
>>> f.write("Hello World x3")
14
>>> f.close()
```
---------------------
```bash
$ cat test.txt 
Hello World
Hello World x2
Hello World x3
```

### 1.1.5 Rename File
Phương thức `rename()` trong module `os` được sử dụng để thay tên file. Phương thức này nhận hai tham số là tên file cũ và tên file mới.  
**- Cú pháp:**  
`os.rename("<tên file hiện tại>", "<tên file mới>")`

```python
>>> import os
>>> os.rename("test.txt", "t.txt")
```
-----------------------------------
```bash
$ ls 
t.txt
```

### 1.1.6 Remove File
Bạn có thể sử dụng phương thức `remove()` của module `os` để xóa các file với tham số là tên file bạn cần xóa.  
**- Cú pháp:**  
`os.remove("<tên file>")`

```python
>>> import os
>>> os.remove("t.txt")
```

### 1.1.7 Vị trí File
Phương thức `tell()` sẽ nói cho bạn biết vị trí hiện tại bên trong file. Nói cách khác, việc đọc và ghi tiếp theo sẽ diễn ra trên các byte đó.  
Phương thức `seek(offset[, from])` thay đổi vị trí hiện tại bên trong file.  
- Tham số `offset` là chỉ số byte để được di chuyển.  
- Tham số `from` xác định vị trí tham chiếu mà từ đó byte được di chuyển.  
    - Nếu `from` là 0 thì sử dụng phần đầu file như là vị trí tham chiếu.  
    - Nếu `from` là 2 thì sử dụng phần cuối file như là vị trí tham chiếu.
 
      
## 1.2 Hashing mật khẩu
**Tham khảo**
[Tham khảo tại đây](https://www.phamduytung.com/blog/2020-01-13-hash-in-python/#md5-16-bytes128-bit)

### 1.2.1 Built-In Hashing
Python có xây dựng sẵn cho chúng ta một hàm hash, chúng ta cứ việc gọi ra và sử dụng.  
Một lưu ý nhỏ là giá trị của hàm hash sẽ khác nhau giữa các phiên bản python.

```python
>>> hash("Chu Van Doan")
-3236864219615152728
```

### 1.2.2 Checksums
Chúng ta có thể sử dụng checksums để hash dữ liệu. Checksum được sử dụng trong thuật toán nén file ZIP để đảm bảo toàn vẹn dữ liệu sau khi nén. Thư viện `zlib` của python hỗ trợ 2 hàm tính checksum là `adler32` và `crc32`. Để đảm bảo tốc độ chương trình và chỉ cần lấy hash đơn giản, chúng ta có thể sử dụng hàm `Adler32`. Tuy nhiên, nếu bạn muốn chương trình có độ tin cậy cao hoặc đơn giản là checksums, hãy sử dụng `crc32`. 

```python
>>> import zlib
>>> zlib.adler32(b"Chu Van Doan")
426902536
>>> zlib.crc32(b"Chu Van Doan")
2282271133
```

### 1.2.3 Secure Hashing
Mã hóa an toàn (Secure Hashing) và bảo mật dữ liệu đã được nghiên cứu và ứng dụng từ nhiều năm về trước. Tiền thân là thuật toán MD5 đến SHA1, SHA256, SHA512…. Mỗi thuật toán ra đời sau sẽ cải tiến độ bảo mật và giảm đụng độ của các thuật toán trước đó.

#### 1.2.3.1 MD5 – 16 bytes/128 bit
Chuỗi đầu ra của MD5 có kích thước 16 bytes hay 16 * 8 = 128 bits. Ở thời điểm hiện tại MD5 không còn là thuật toán phổ biến và không được khuyến khích dùng bởi các tổ chức bảo mật.

```python
>>> import hashlib
>>> hashlib.md5(b"Chu Van Doan").hexdigest()
'99264990b92549a660c7d15244b01d5c'
>>> len(hashlib.md5(b"Chu Van Doan").digest())
16  # Chiều dài của đầu ra là 16 bytes
```

Chú ý: Hàm `hexdigest` biểu diễn một byte thành một ký tự hex (2 ký tự đầu `58` của ví dụ trên là giá trị hex của số 88 trong hệ thập phân).

#### 1.2.3.2 SHA1 – 20 bytes/160 bits
Đầu ra của SHA1 có chiều dài là 20 bytes tương ứng với 160 bit. Cũng giống như MD5, SHA1 cũng không được khuyến khích sử dụng ở trong các ứng dụng bảo mật.

```python
>>> import hashlib
>>> hashlib.sha1(b"Chu Van Doan").hexdigest()
'49dfdffe3846ac7150beec6d050681629d2f0349'
>>> len(hashlib.sha1(b"Chu Van Doan").digest())
20
```

#### 1.2.3.3 SHA256 – 32 bytes/256 bit và SHA512 – 64 bytes/512 bit
Đây là hai hàm hash được khuyên là nên dùng ở thời điểm hiện tại.

```python
>>> hashlib.sha256(b"Chu Van Doan").hexdigest()
'6be137c0c870a79df2e3e435917275276033e1945c3701f88fb7a346d67ba82a'
>>> len(hashlib.sha256(b"Chu Van Doan").digest())
32
>>> hashlib.sha512(b"Chu Van Doan").hexdigest()
'4c011d3c5e34191afee863293529a681051a6fd870742bd70c347ef3315f30e8cd33c08e5566149f54fa88b2c202455e5a4a87bc744ff003a0a88fc35602aa37'
>>> len(hashlib.sha512(b"Chu Van Doan").digest())
64
```
## 1.3 Khớp mẫu tên tệp Unix trong Python

### fnmatch – So khớp mẫu tên tệp kiểu Unix trong Python

Module `fnmatch` trong Python được dùng để so khớp tên tệp với các ký tự đại diện kiểu Unix. Hàm `fnmatch()` so sánh tên tệp với mẫu và trả về giá trị TRUE nếu khớp, ngược lại trả về FALSE. Việc so sánh phân biệt hoa thường nếu hệ điều hành sử dụng hệ thống tệp có phân biệt hoa thường.

Các ký tự đặc biệt và chức năng của chúng bao gồm:

- `*`: Khớp với mọi thứ
- `?`: Khớp với bất kỳ một ký tự nào
- `[seq]`: Khớp với bất kỳ ký tự nào trong chuỗi `seq`
- `[!seq]`: Khớp với ký tự không thuộc chuỗi `seq`

Nếu muốn khớp ký tự đặc biệt theo nghĩa đen, các ký tự đó phải được đặt trong dấu ngoặc vuông. Ví dụ, `'[?]'` khớp với ký tự `?`.

### Các hàm được cung cấp bởi module `fnmatch`

- **fnmatch.fnmatch(filename, pattern)**: Hàm này kiểm tra xem chuỗi tên tệp đã cho có khớp với chuỗi mẫu hay không và trả về giá trị boolean. Nếu hệ điều hành không phân biệt hoa thường, cả hai tham số sẽ được chuyển thành dạng chữ thường hoặc chữ hoa trước khi so sánh.

Ví dụ: Tìm tất cả các tệp bắt đầu bằng `fnmatch` và kết thúc bằng `.py`.

```python
import fnmatch
import os

pattern = '*.py'
print('Pattern:', pattern)
print()

files = os.listdir('.')
for name in files:
	print(f"Filename: {name: <25} {'True' if fnmatch.fnmatch(name, pattern) else 'False'}")
```

Kết quả:

```
Pattern: *.py

Filename: 2.png                     False
Filename: check_type_file.py        True
Filename: test                      False
```

- **fnmatch.fnmatchcase(filename, pattern)**: Hàm này thực hiện so sánh phân biệt hoa thường và kiểm tra xem chuỗi tên tệp có khớp với mẫu đã cho hay không, trả về giá trị boolean.

Ví dụ: So sánh có phân biệt hoa thường bất kể thiết lập của hệ thống tệp và hệ điều hành.

```python
import fnmatch
import os
  
pattern = 'FNMATCH_*.PY'
print('Pattern:', pattern)  
print() 
  
files = os.listdir('.')  
  
for name in files:  
    print(f"Filename: {name:<25} {'True' if fnmatch.fnmatchcase(name, pattern) else 'False'}")
```

Kết quả:

```
Pattern : FNMATCH_*.PY

Filename: __init__.py               False
Filename: fnmatch_filter.py         False
Filename: FNMATCH_FNMATCH.PY        True
Filename: fnmatch_fnmatchcase.py    False
Filename: fnmatch_translate.py      False
Filename: index.rst                 False
```

- **fnmatch.filter(names, pattern)**: Hàm này trả về một tập hợp con của danh sách tên tệp khớp với mẫu đã cho.

Ví dụ: Lọc các tệp theo nhiều phần mở rộng.

```python
import fnmatch
import os
  
pattern = 'fnmatch_*.py'
print('Pattern:', pattern) 
  
files = os.listdir('.')  
print('Files:', files)  
  
print('Matches:', fnmatch.filter(files, pattern))
```

Kết quả:

```python
Pattern : fnmatch_*.py
Files   : ['__init__.py', 'fnmatch_filter.py', 'fnmatch_fnmatch.py', 
           'fnmatch_fnmatchcase.py', 'fnmatch_translate.py', 'index.rst']
Matches : ['fnmatch_filter.py', 'fnmatch_fnmatch.py', 
           'fnmatch_fnmatchcase.py', 'fnmatch_translate.py']
```

- **fnmatch.translate(pattern)**: Hàm này chuyển mẫu shell-style thành biểu thức chính quy để sử dụng với `re.match()` (chỉ khớp từ đầu chuỗi).

Ví dụ:

```python
import fnmatch, re
  
regex = fnmatch.translate('*.txt')
reobj = re.compile(regex)
  
print(regex)  
print(reobj.match('foobar.txt'))
```

Kết quả:

```
'(?s:.*\.txt)\Z'
<_sre.SRE_Match object; span=(0, 10), match='foobar.txt'>
```


## 1.4 Quản lý quyền truy cập tệp (File Permissions)

### Hiển thị thư mục hiện tại
Phương thức `getcwd()` hiển thị thư mục đang làm việc hiện tại, trả về kết quả dưới dạng một chuỗi.

Chúng ta cũng có thể sử dụng phương thức `getcwdb()` để nhận về kết quả dưới dạng byte.

```python
>>> import os
>>> os.getcwd()
'C:\\Program Files\\PyScripter'
>>> os.getcwdb()
b'C:\\Program Files\\PyScripter'
```

### Thay đổi thư mục hiện tại
Thư mục làm việc hiện tại có thể được thay đổi bằng phương thức `chdir()`.

`chdir()` nhận một tham số là tên thư mục bạn muốn tới từ thư mục hiện tại. Có thể sử dụng cả dấu gạch chéo (`/`) hoặc dấu gạch chéo ngược (`\`) để tách các phần tử trong đường dẫn, nhưng tốt nhất vẫn nên sử dụng dấu gạch ngược (`\`).

```python
>>> os.chdir('C:\\Python33')
>>> print(os.getcwd())
C:\\Python33
```

### Danh sách thư mục và file
Bạn có thể liệt kê tất cả các tệp và thư mục con bên trong một thư mục bằng cách sử dụng phương thức `listdir()`.

Phương thức này nhận một đường dẫn và trả về danh sách thư mục con và các file trong đường dẫn đó.

Nếu không có đường dẫn nào được chỉ định, kết quả trả về sẽ truy xuất từ thư mục làm việc hiện tại.

```python
>>> print(os.getcwd())
C:\\Python33
>>> os.listdir()
['DLLs','Doc','include','Lib','libs','LICENSE.txt','NEWS.txt','python.exe','pythonw.exe','README.txt','Scripts','tcl','Tools']
>>> os.listdir('G:\\')
['$RECYCLE.BIN','Movies','Music','Photos','Series','System Volume Information']
```

### Tạo một thư mục mới
Để tạo các thư mục mới, bạn sử dụng phương thức `mkdir()` của Module os.

Bạn có thể chọn nơi chứa thư mục mới bằng cách ghi đầy đủ đường dẫn tới nơi muốn tạo. Nếu đường dẫn đầy đủ không được chỉ định, thư mục mới sẽ được tạo trong thư mục làm việc hiện tại.

```python
>>> os.mkdir('test')
>>> os.listdir()
['test']
```

### Đổi tên thư mục hoặc tên file
Bạn sử dụng phương thức `rename()` để đổi tên một thư mục hoặc một tập tin.

```python
>>> os.listdir()
['test']
>>> os.rename('test','new_one')
>>> os.listdir()
['new_one']
```

### Xóa bỏ thư mục hoặc file
Để gỡ bỏ một file, bạn sử dụng phương thức `remove()`

Tương tự nhưng để xóa toàn bộ thư mục, sử dụng `rmdir()`

```python
>>> os.listdir()
['new_one', 'old.txt']
>>> os.remove('old.txt')
>>> os.listdir()
['new_one']
>>> os.rmdir('new_one')
>>> os.listdir()
[]
```
Lưu ý rằng phương thức `rmdir()` chỉ có thể xóa các thư mục rỗng.

Vậy để loại bỏ một thư mục không rỗng, chúng ta có thể sử dụng phương thức `rmtree()` bên trong module `shutil`.

```python
>>> os.listdir()
['test']
>>> os.rmdir('test')
Traceback (most recent call last):
...
OSError: [WinError 145] The directory is not empty: 'test'
>>> import shutil
>>> shutil.rmtree('test')
>>> os.listdir()
[]
```


## 1.5 Thực thi hệ thống - Subprocess 

Subprocess trong Python là một mô-đun được sử dụng để chạy các code và ứng dụng mới bằng cách tạo các process mới. Nó cho phép bạn bắt đầu các ứng dụng mới ngay từ chương trình Python mà bạn hiện đang viết. Nếu bạn muốn chạy các chương trình bên ngoài từ kho lưu trữ git hoặc mã từ chương trình C hoặc C++, bạn có thể sử dụng Subprocess trong Python. Bạn cũng có thể lấy exit code và đường dẫn input, output hoặc lỗi bằng cách sử dụng Subprocess trong Python.

Subprocess trong Python có thể hữu ích nếu bạn từng có ý định hợp lý hóa tập lệnh dòng lệnh của mình hoặc sử dụng Python cùng với các ứng dụng dòng lệnh—hoặc bất kỳ ứng dụng nào. Mô-đun Subprocess của Python có thể trợ giúp mọi thứ, từ khởi động giao diện GUI đến thực thi các lệnh terminal và chương trình dòng lệnh.

### Bắt đầu một Process trong Python

Để bắt đầu một Subprocess mới trong Python, bạn cần sử dụng lệnh gọi hàm `Popen`. Có thể truyền hai tham số trong lời gọi hàm. Tham số đầu tiên là chương trình bạn muốn bắt đầu và tham số thứ hai là đối số tệp. Ví dụ:

```python
from subprocess import Popen, PIPE

# Tạo process gọi lệnh cat đọc file example.py
process = Popen(['cat', 'example.py'], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()

# Xuất kết quả
print(stdout)
```

Trong đoạn mã trên, `process.communicate()` là lệnh gọi chính đọc tất cả đầu vào và đầu ra của process. “Stdout” xử lý đầu ra của process và “stderr” dùng để xử lý bất kỳ loại lỗi nào.

### Subprocess Call()

Phương thức `call()` của Subprocess trong Python được sử dụng để khởi tạo chương trình. Cú pháp:

```python
subprocess.check_call(args, *, stdin=None, stdout=None, stderr=None, shell=False)
```

Ví dụ gọi lệnh Unix tích hợp `ls -l`:

```python
import subprocess
subprocess.call(["ls", "-l"])
```

### Lưu kết quả process

Để lưu trữ đầu ra của process, bạn có thể sử dụng hàm `check_output`. Cú pháp:

```python
subprocess.check_output(args, *, stdin=None, stderr=None, shell=False, universal_newlines=False)
```

Ví dụ:

```python
import subprocess

# Gọi hàm echo và lưu trữ kết quả
s = subprocess.check_output(["echo", "Hello World!"])

print(s)
```

## 1.6 Duyệt qua các file trong một thư mục


### 1.6.1 Sử dụng os.listdir

- Câu lệnh sau sẽ lấy danh mục các file trong thư mục

```python
>>> import os
>>> path = "~/Documents/SOC/ITMO/Kỳ 5/Phương pháp lập trình/Lab 1/Lab1_a"
>>> os.listdir(os.path.expanduser(path))
['pass.txt', 'template.tbl', 'main.py']
>>> 
```

- os.listdir chỉ cho bạn tên file hoặc thư mục nằm trong đường dẫn đó. Ví dụ:

# Bảo vệ trang web

```javascript html css
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bảo vệ Nội dung</title>

  <style>
    /* Căn giữa toàn bộ nội dung */
    body, html {
      height: 100%;
      margin: 0;
      font-family: Arial, sans-serif;
      display: flex;
      justify-content: center;  /* Căn giữa theo trục ngang */
      align-items: center;      /* Căn giữa theo trục dọc */
      background-size: cover;
      background-position: center;
    }   

    /* Căn giữa hộp nội dung */
    #main-content {
      background-color: rgba(255, 255, 255, 0.8); /* Nền trắng mờ để dễ đọc nội dung */
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
      text-align: center;
    }

    /* CSS để vô hiệu hóa chọn nội dung và nhấn chuột phải khi chế độ bảo vệ được bật */
    .protected-content {
      -webkit-user-select: none;  /* Safari */
      -moz-user-select: none;     /* Firefox */
      -ms-user-select: none;      /* Internet Explorer/Edge */
      user-select: none;          /* Non-prefixed version */
      pointer-events: none;       /* Vô hiệu hóa các sự kiện chuột */
    }

    /* CSS cho phần hiển thị tùy chọn bật/tắt bảo vệ */
    #protection-options {
      margin: 20px;
    }

    #password-section {
      margin-top: 10px;
    }

    button {
      padding: 10px 20px;
      margin: 5px;
      font-size: 16px;
      cursor: pointer;
      background-color: #4CAF50;
      color: white;
      border: none;
      border-radius: 5px;
      transition: background-color 0.3s;
    }

    button:hover {
      background-color: #45a049;
    }

    input[type="password"] {
      padding: 10px;
      font-size: 16px;
      margin-right: 10px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
  </style>
</head>
<body>
  <!-- Hộp chứa nội dung chính -->
  <div id="main-content">
    <!-- Nội dung được bảo vệ -->
    <div id="content" class="protected-content">
        <h1>Bảo vệ Chống Sao Chép</h1>
      <p>Nội dung này được bảo vệ chống sao chép và chụp ảnh màn hình nếu chế độ bảo vệ được bật.</p>
    </div>

    <!-- Phần hiển thị tùy chọn bật/tắt bảo vệ -->
    <div id="protection-options">
      <button onclick="promptPassword('enable')">Bật chế độ bảo vệ</button>
      <button onclick="promptPassword('disable')">Tắt chế độ bảo vệ</button>
    </div>

    <!-- Form nhập mật khẩu để bật/tắt bảo vệ -->
    <div id="password-section" style="display: none;">
      <input type="password" id="password" placeholder="Nhập mật khẩu">
      <button onclick="handlePassword()">Xác nhận</button>
    </div>
  </div>

  <script>
    // Mã băm SHA256 của mật khẩu
    const hashedPassword = "9f836f77a5918d1d48f774cbde22f4317f7931018ccd44e4350a441e00c6b56a";

    // Biến trạng thái yêu cầu bật/tắt
    let protectionAction = "";

    // Hiển thị form nhập mật khẩu tùy vào hành động
    function promptPassword(action) {
      protectionAction = action;
      document.getElementById("password-section").style.display = "block";
    }

    // Hàm xử lý nhập mật khẩu
    async function handlePassword() {
      const inputPassword = document.getElementById("password").value;

      // Hàm băm SHA256 mật khẩu nhập vào
      const inputHashed = await sha256(inputPassword);

      if (inputHashed === hashedPassword) {
        if (protectionAction === 'enable') {
          enableProtection();
          alert("Chế độ bảo vệ đã được bật. Bạn chỉ có thể in trang và tắt chế độ bảo vệ.");
        } else if (protectionAction === 'disable') {
          disableProtection();
          alert("Chế độ bảo vệ đã được tắt. Bạn có thể thao tác trên trang.");
        }
        document.getElementById("password-section").style.display = "none";  // Ẩn form mật khẩu sau khi xác thực
      } else {
        alert("Sai mật khẩu!");
      }
    }

    // Bật chế độ bảo vệ
    function enableProtection() {
      // Vô hiệu hóa chỉ phần nội dung, ngoại trừ các nút bảo vệ
      document.getElementById("content").classList.add("protected-content");  
    }

    // Tắt chế độ bảo vệ
    function disableProtection() {
      // Cho phép tương tác lại với nội dung
      document.getElementById("content").classList.remove("protected-content");  
    }

    // Hàm băm SHA256 (sử dụng SubtleCrypto API của trình duyệt)
    async function sha256(message) {
      const msgBuffer = new TextEncoder().encode(message);
      const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
      const hashArray = Array.from(new Uint8Array(hashBuffer));
      return hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    }
  </script>
</body>
</html>

  
