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

Trong suốt quá trình học, bạn có thể làm theo cùng với tôi! Bạn có thể thử các lệnh được trình bày hoặc tích hợp chúng vào các dự án riêng của mình, sau khi bạn học bằng cách thực hành và áp dụng những gì đã học vào các tình huống thực tế. Hãy chắc chắn rằng bạn đã khởi động "tryhackme attackbox" hoặc sử dụng terminal của riêng bạn.

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

Dưới đây là bản dịch tiếng Việt của nội dung trong ảnh:

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
  Đáp án: `Jammy is 21 years old`
</details>

---

**Câu hỏi: Làm thế nào để in tên thành phố ra màn hình?**

<details>
  <summary>Hiển thị đáp án</summary>
  Đáp án: `echo $city`
</details>

---

**Câu hỏi: Làm thế nào để in tên quốc gia ra màn hình?**

<details>
  <summary>Hiển thị đáp án</summary>
  Đáp án: `echo $country`
</details>
