# Bash Scripting
> Cơ bản về những tập lệnh bash

![](./img/4_Bash_Scripting/bashs.jpg)

# Mục Lục

1. [Task 1: Introduction](#task-1-introduction)  
2. [Task 2: Our first simple bash scripts](#task-2-our-first-simple-bash-scripts)  
3. [Task 3: Variables](#task-3-variables)  
4. [Task 4: Parameters](#task-4-parameters)  
5. [Task 5: Arrays](#task-5-arrays)  
6. [Task 6: Conditionals](#task-6-conditionals)  
7. [Task 7: Further reading](#task-7-further-reading)

## Nội dung

# Task 1: Introduction

---

### Bash là gì?

Bash là một ngôn ngữ kịch bản (scripting language) chạy trong terminal trên hầu hết các bản phân phối Linux, cũng như trên MacOS. Shell script là một chuỗi các lệnh bash nằm trong một tệp, kết hợp lại với nhau để thực hiện các tác vụ phức tạp hơn so với các lệnh một dòng đơn giản, và đặc biệt hữu ích khi cần tự động hóa các tác vụ quản trị hệ thống như sao lưu dữ liệu.

Dưới đây là một vài nội dung  sẽ học:

* Bash syntax
* Variables
* Using parameters
* Arrays
* Conditionals

Trang web hữu ích học Bash: [https://devhints.io/bash](https://devhints.io/bash)

Trang web tra cứu chức năng của các lệnh: [https://explainshell.com/](https://explainshell.com/)

---

# Task 2: Our first simple bash scripts

---

Một file bash script thường có đuôi `.sh`

Trước tiên, hãy trình bày cấu trúc của chúng ta.

Một bash script luôn bắt đầu với dòng mã sau ở đầu tập tin:

```
#!/bin/bash
```

![](./img/4_Bash_Scripting/2.1.png)

Dòng này giúp shell của bạn (bất kể loại shell nào) biết rằng nó cần phải chạy tập tin của bạn bằng bash trong terminal.

---

Hãy cùng bắt đầu với một vài ví dụ cơ bản.

```bash
#!/bin/bash
echo "Hello World!"
```
![](./img/4_Bash_Scripting/2.2.png)

Lệnh này sẽ in ra chuỗi “Hello World!”.
Lệnh `echo` được dùng để xuất văn bản ra màn hình, tương tự như lệnh `print` trong Python.

---

Chúng cũng có thể thực thi các lệnh Linux thông thường bên trong bash script, và chúng sẽ được chạy nếu bạn định dạng đúng.
Ví dụ, chúng ta có thể chạy lệnh `ls` bên trong bash script và sẽ thấy kết quả khi chạy file đó. 

```bash
#!/bin/bash
echo "Hello World"
whoami
id
```
![](./img/4_Bash_Scripting/2.3.png)

---

Trong đoạn script trên:

* `whoami` sẽ in ra tên người dùng hiện tại.
* `id` sẽ hiển thị thông tin UID, GID, và nhóm của người dùng.

---

Bây giờ để chạy một bash script, trước tiên ta cần cấp quyền thực thi cho nó:

```
chmod +x yourfile.sh
```

Sau đó ta chạy nó bằng cách sử dụng:

```
./
```

Ví dụ:

```bash
./first_bash_script.sh 
Hello World
chu
uid=1000(chu) gid=1000(chu) groups=1000(chu),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),109(kvm),119(vboxusers),122(lpadmin),134(lxd),135(sambashare),139(wireshark),140(docker),143(ubridge),145(libvirt)
```

Ta có thể thấy script đã xuất ra kết quả của các lệnh `whoami` và `id`.

---

**Hãy trả lời các câu hỏi bên dưới**

**Câu hỏi: Dòng mã nào có thể được chèn vào đầu dòng để biến dòng đó thành chú thích trong code?**

<details>
  <summary>Hiển thị đáp án</summary>
  Đáp án: `#`
</details>

---

**Câu hỏi: Đoạn script sau sẽ in ra màn hình nội dung gì? Dòng lệnh: `echo "BishBashBosh"`**

<details>
  <summary>Hiển thị đáp án</summary>
  Đáp án: `BishBashBosh`
</details>

# Task 3: Variables

---

Bây giờ chúng ta sẽ chuyển sang phần **Variables**,
trong bash thì việc này khá đơn giản và chúng ta khai báo biến như sau:

```bash
name="Sun"
```

![](./img/4_Bash_Scripting/3.1.png)

Ở đây, chúng ta gán giá trị `"Sun"` cho biến có tên là `name`.

Lưu ý: để biến hoạt động đúng trong bash, bạn **không được để khoảng trắng** giữa tên biến, dấu `=` và giá trị. Biến không được chứa khoảng trắng.

Vậy làm sao để sử dụng biến vừa tạo? Điều đó cũng rất đơn giản — ta sẽ xem ngay sau đây.

Chúng ta cần thêm dấu **`$`** phía trước tên biến để sử dụng nó.

```bash
name="Sun"
echo $name
```
![](./img/4_Bash_Scripting/3.2.png)

Nếu chúng ta thử điều này trong terminal của mình, kết quả sẽ giống như sau:

Lệnh này sẽ in ra chữ **Sun** trên màn hình.

```bash
 ./variables.sh
Sun
```

---

Biến giúp việc lưu trữ dữ liệu trở nên dễ dàng hơn rất nhiều. Thay vì phải gõ đi gõ lại cùng một nội dung ở nhiều nơi, chúng ta có thể đơn giản chèn biến với cú pháp `$var` và gán cho nó một giá trị cụ thể — điều này giúp dễ dàng thay đổi sau này nếu cần.
Vậy làm thế nào để gỡ lỗi (debug) mã của chúng ta?

---

**Gỡ lỗi là một phần rất quan trọng trong lập trình**, vì vậy chúng ta nên làm quen với việc giải quyết vấn đề và sửa lỗi càng sớm càng tốt.
Bash có một số tính năng tích hợp sẵn giúp việc này đơn giản hơn.

Khi chạy lệnh trên dòng lệnh, bạn có thể dùng:

```bash
bash -x ./file.sh
```

Ví dụ:

![](./img/4_Bash_Scripting/3.3.png)

Bạn có thể tạo một bash script đơn giản (giờ bạn đã biết cú pháp cơ bản) và cố ý viết sai để kiểm tra.
Sau đó chạy chương trình của bạn với chế độ gỡ lỗi (debug) và xem nó trông như thế nào khi xảy ra lỗi!

---

Lệnh này cho bạn biết dòng nào đang hoạt động và dòng nào không.
Nếu bạn muốn gỡ lỗi tại một điểm cụ thể trong script, bạn có thể chèn lệnh `set -x` vào script, và dùng `set +x` để kết thúc phần đó, như sau:

```bash
echo "hi"

set -x
# đoạn này sẽ được gỡ lỗi
set +x
```

![](./img/4_Bash_Scripting/3.4.png)

---

Với cách này, chỉ phần nằm giữa `set -x` và `set +x` sẽ được theo dõi chi tiết khi chạy.

---

Hãy xem một ví dụ. Đây là script mà ta đã viết trước đó, được chạy bằng lệnh:

```bash
 bash -x ./first_bash_script.sh 
+ echo 'Hello World'
Hello World
+ whoami
chu
+ id
uid=1000(chu) gid=1000(chu) groups=1000(chu),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),109(kvm),119(vboxusers),122(lpadmin),134(lxd),135(sambashare),139(wireshark),140(docker),143(ubridge),145(libvirt)
```

Bạn có thể thấy đầu ra có dấu `+` phía trước mỗi lệnh, sau đó là kết quả thực thi của lệnh đó.
Nếu có lỗi xảy ra, dòng đó sẽ hiển thị với dấu `-`, điều này giúp bạn dễ dàng phát hiện chỗ sai để sửa lỗi.

Dưới đây là bản dịch tiếng Việt của nội dung trong ảnh:

---

Chúng ta cũng có thể sử dụng **nhiều biến** trong một câu lệnh `echo`. Bạn không bị giới hạn chỉ dùng 1 biến đâu!

```bash
#!/bin/bash
name="Sun"
age=23

echo "$name is $age years old"
```
Kết quả:

```bash
 ./print_name_age.bash 
Sun is 23 years old
```

---

**Trả lời các câu hỏi sau** và sử dụng đoạn mã dưới đây để hỗ trợ bạn:

```bash
name="Jammy"
age=21
echo "$name is $age years old"

city="Paris"
country="France"
```

---

**Câu hỏi: Đoạn mã trên sẽ trả về gì?**

<details>
  <summary>Hiển thị đáp án</summary>
  Đáp án: Jammy is 21 years old
</details>

---

**Câu hỏi: Làm thế nào để in tên thành phố ra màn hình?**

<details>
  <summary>Hiển thị đáp án</summary>
  Đáp án: echo $city
</details>

---

**Câu hỏi: Làm thế nào để in tên quốc gia ra màn hình?**

<details>
  <summary>Hiển thị đáp án</summary>
  Đáp án: echo $country
</details>

---

# Task 4: Parameters

Bây giờ chúng ta sẽ tìm hiểu một trong những tính năng chính của bash — đó là **sử dụng tham số (parameters)**.

Trước tiên, ta sẽ xem xét các tham số được chỉ định thông qua dòng lệnh khi chạy file. Những tham số này có thể có nhiều dạng, nhưng thường có tiền tố `$` vì tham số cũng là một biến.

Hãy bắt đầu bằng cách khai báo một tham số sẽ là đối số (argument) đầu tiên khi chạy bash script:

```bash
#!/bin/bash
name=$1
echo $name
```

Sau đó, ta chạy script với:

```bash
./parameters_1.sh Sun
Sun
```

Và đúng như mong đợi, ta nhận được kết quả là `"Sun"`.

Vậy nếu ta muốn sử dụng đối số thứ hai thì sao? Quá trình cũng rất đơn giản, chỉ cần thay `$1` thành `$2`, ví dụ:

```bash
#!/bin/bash
name=$2
echo $name
```

Sau đó chạy:

```bash
./parameters_2.sh Sun Moon
Moon
```

Theo bạn, nó sẽ trả về gì? — Nó sẽ trả về `"Moon"`.

---

Nhưng nếu ta **không muốn truyền tham số từ dòng lệnh**, mà muốn cho người dùng **nhập tên tương tác trực tiếp**, ta có thể dùng lệnh `read`:

```bash
#!/bin/bash
echo Enter your name
read name
echo "Your name is $name"
```

Khi chạy đoạn code này, chương trình sẽ tạm dừng để bạn nhập tên vào, ví dụ:

```bash
./parameters_3.sh 
Enter your name:
Sun
Your name is Sun
```

Và ta thấy rằng nó hoạt động!

---

### **Tham số trong Shell**

| **Tham số**    | **Chức năng**                                                             |
| -------------- | ------------------------------------------------------------------------- |
| `$1`–`$9`      | Đại diện cho các tham số vị trí (positional parameters) từ đối số 1 đến 9 |
| `${10}`–`${n}` | Đại diện cho các tham số vị trí từ đối số thứ 10 trở đi                   |
| `$0`           | Đại diện cho tên của script                                               |
| `$*`           | Đại diện cho tất cả các đối số dưới dạng một chuỗi duy nhất               |
| `$@`           | Tương tự như `$*`, nhưng khác biệt khi đặt trong dấu ngoặc kép `(")`      |
| `$#`           | Đại diện cho tổng số đối số được truyền vào                               |
| `$$`           | PID (Process ID) của script                                               |
| `$?`           | Đại diện cho mã trả về (return code) cuối cùng của lệnh vừa thực hiện     |

---

**Hãy trả lời các câu hỏi bên dưới**

**Câu hỏi: Làm thế nào để lấy số lượng đối số được truyền vào một script?**

<details>
  <summary>Hiển thị đáp án</summary>
  Đáp án: `$#`
</details>

---

**Câu hỏi: Làm thế nào để lấy tên file script hiện tại (tức là đối số đầu tiên)?**

<details>
  <summary>Hiển thị đáp án</summary>
  Đáp án: `$0`
</details>

---

**Câu hỏi: Làm thế nào để lấy đối số thứ 4 được truyền vào script?**

<details>
  <summary>Hiển thị đáp án</summary>
  Đáp án: `$4`
</details>

---

**Câu hỏi: Nếu script yêu cầu nhập dữ liệu, làm sao để lưu đầu vào đó vào biến có tên là `test` bằng lệnh `read`?**

<details>
  <summary>Hiển thị đáp án</summary>
  Đáp án: `read test`
</details>

---

**Câu hỏi: Lệnh `echo "$1 $3"` sẽ in ra gì nếu script được chạy với `./script.sh hello hola aloha`?**

<details>
  <summary>Hiển thị đáp án</summary>
  Đáp án: `hello aloha`
</details>
