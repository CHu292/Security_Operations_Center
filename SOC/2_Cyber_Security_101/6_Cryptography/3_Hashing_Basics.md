# Hashing Basics

## Mục lục

1. [Task 1: Introduction](#task-1-introduction)
2. [Task 2: Hash Functions](#task-2-hash-functions)


## Nội dung


# Task 1: Introduction
>Giới thiệu

Hãy tưởng tượng bạn vừa tải xuống một tệp có dung lượng 6 GB và muốn biết liệu bản sao bạn tải về có giống hệt với tệp gốc, từng bit một hay không. Làm sao để bạn kiểm tra điều đó? Hoặc giả sử ai đó tốt bụng đưa cho bạn tệp 6 GB này trong một USB — làm sao bạn có thể chắc chắn rằng nó giống hệt với tệp mà bạn định tải xuống?

Câu trả lời cho cả hai tình huống trên nằm ở việc **so sánh các giá trị băm (hash)** của hai tệp; nếu **giá trị băm** giống nhau, bạn có thể **gần như chắc chắn rằng hai tệp là giống hệt nhau**. Nhưng giá trị băm là gì?

---

Một **giá trị băm (hash value)** là một chuỗi ký tự có độ dài cố định được tính toán bởi một **hàm băm (hash function)**.
Hàm băm nhận đầu vào có kích thước bất kỳ và trả về đầu ra có độ dài cố định — tức là giá trị băm. Trong phần này, chúng ta sẽ tìm hiểu các ứng dụng thú vị và sáng tạo của hàm băm và giá trị băm.

---

**Lưu ý về thuật ngữ:**

Chúng tôi sử dụng chủ yếu hai thuật ngữ là *hàm băm* và *giá trị băm*. Tuy nhiên, đôi khi từ **hash** được dùng như:

* **Động từ:** “to hash” = tính toán giá trị băm
* **Danh từ:** “hash” = giá trị băm (thay cho “hash value”)


### **Mục tiêu học tập**

Sau khi hoàn thành phòng học này, bạn sẽ nắm được:

* Các hàm băm và hiện tượng va chạm (collisions)
* Vai trò của hàm băm trong hệ thống xác thực
* Cách nhận diện các giá trị băm đã lưu trữ
* Cách phá vỡ (crack) giá trị băm
* Việc sử dụng hàm băm để bảo vệ tính toàn vẹn dữ liệu

---

# Task 2: Hash Functions

>Hàm băm là gì?

Hàm băm khác với mã hóa. Không có khóa, và việc đi từ đầu ra quay lại đầu vào là không thể (hoặc không khả thi về mặt tính toán).

Hàm băm nhận một lượng dữ liệu đầu vào có kích thước bất kỳ và tạo ra một bản tóm tắt (digest) của dữ liệu đó. Đầu ra có kích thước cố định. Rất khó để dự đoán đầu ra cho bất kỳ đầu vào nào và ngược lại. Thuật toán băm tốt sẽ tương đối nhanh để tính toán và cực kỳ chậm để đảo ngược, tức là đi từ đầu ra và xác định đầu vào. Bất kỳ thay đổi nhỏ nào trong dữ liệu đầu vào, thậm chí chỉ một bit, đều sẽ gây ra sự thay đổi đáng kể trong đầu ra.

Hãy kiểm tra một ví dụ. Trong terminal bên dưới, chúng ta thấy hai tệp: tệp đầu tiên chứa chữ T, trong khi tệp thứ hai chứa chữ U. Nếu bạn kiểm tra T và U trong bảng mã ASCII hoặc dùng `hexdump`, bạn sẽ nhận thấy rằng hai chữ cái này chỉ khác nhau một bit.

* Chữ cái T có mã **54** ở hệ thập lục phân, tức là **01010100** ở hệ nhị phân.
* Chữ cái U có mã **55** ở hệ thập lục phân, tức là **01010101** ở hệ nhị phân.

Do đó, hai tệp này chỉ khác nhau đúng một bit. Tuy nhiên, nếu chúng ta so sánh giá trị băm **MD5** (Message-Digest Algorithm 5), **SHA1** (Secure Hash Algorithm 1), hoặc **SHA-256** (Secure Hash Algorithm 256) của chúng, ta sẽ nhận thấy rằng chúng hoàn toàn khác nhau. Chúng tôi khuyến nghị bạn tự thử các lệnh bên dưới. Các tệp nằm trong thư mục `~/Hashing-Basics/Task-2/`.

```bash
strategos@g5000 ~> cat file1.txt 
T⏎
strategos@g5000 ~> cat file2.txt 
U⏎   
strategos@g5000 ~> hexdump -C file1.txt 
00000000  54                                                |T|
00000001
strategos@g5000 ~> hexdump -C file2.txt 
00000000  55                                                |U|
00000001
strategos@g5000 ~> md5sum *.txt
b9ece18c950afbfa6b0fdbfa4ff731d3  file1.txt
4c614360da93c0a041b22e537de151eb  file2.txt
strategos@g5000 ~> sha1sum *.txt
c2c53d66948214258a26ca9ca845d7ac0c17f8e7  file1.txt
b2c7c0caa10a0cca5ea7d69e54018ae0c0389dd6  file2.txt
strategos@g5000 ~> sha256sum *.txt
e632b7095b0bf32c260fa4c539e9fd7b852d0de454e9be26f24d0d6f91d069d3  file1.txt
a25513c7e0f6eaa80a3337ee18081b9e2ed09e00af8531c8f7bb2542764027e7  file2.txt
```

Đầu ra của một hàm băm thường là các byte thô (raw bytes), sau đó được mã hóa. Các dạng mã hóa phổ biến là base64 hoặc hexadecimal. Các lệnh `md5sum`, `sha1sum`, `sha256sum` và `sha512sum` tạo ra đầu ra ở định dạng hexadecimal. Hãy nhớ rằng định dạng hexadecimal in mỗi byte thô thành hai chữ số hexadecimal.

### Tại sao băm lại quan trọng?

Băm đóng vai trò thiết yếu trong việc sử dụng Internet hàng ngày. Giống như các hàm mật mã khác, băm thường được ẩn khỏi người dùng. Băm giúp bảo vệ tính toàn vẹn của dữ liệu và đảm bảo tính bảo mật của mật khẩu.

Xem ví dụ sau về cách băm được sử dụng để bảo vệ an ninh mạng của bạn. Khi bạn đăng nhập vào TryHackMe, máy chủ sử dụng băm để xác minh mật khẩu của bạn. Thực tế, theo các thực hành bảo mật tốt, máy chủ không lưu mật khẩu của bạn; thay vào đó, nó lưu **giá trị băm** của mật khẩu. Khi bạn đăng nhập, hệ thống sẽ tính giá trị băm của mật khẩu bạn nhập và so sánh với giá trị đã lưu. Tương tự, khi bạn đăng nhập vào máy tính của mình, băm cũng đóng vai trò xác minh mật khẩu. Bạn tương tác với băm một cách gián tiếp nhiều hơn bạn nghĩ, gần như hàng ngày trong ngữ cảnh mật khẩu.

---

### Va chạm hàm băm (Hash Collision) là gì?

Va chạm hàm băm xảy ra khi **hai đầu vào khác nhau cho cùng một đầu ra**.
Hàm băm được thiết kế để tránh va chạm tốt nhất có thể, và ngăn chặn kẻ tấn công tạo (hoặc "kỹ thuật hóa") ra va chạm một cách có chủ đích. Tuy nhiên, vì số lượng đầu vào là vô hạn còn số lượng đầu ra có giới hạn, điều này dẫn đến **hiệu ứng lồng chim (pigeonhole effect)**.

Ví dụ: nếu hàm băm tạo ra giá trị băm 4 bit, thì chỉ có 16 giá trị băm khác nhau. Tổng số đầu ra có thể là $2^4 = 16$. Xác suất xảy ra va chạm là tương đối cao.

**Hiệu ứng lồng chim** (pigeonhole effect) nói rằng nếu số lượng vật (chim) lớn hơn số lượng ngăn chứa (lồng chim), thì một số ngăn phải chứa nhiều hơn một vật. Trong ngữ cảnh này, có số lượng giá trị đầu ra hữu hạn, nhưng có thể đưa vào bất kỳ đầu vào nào → một số đầu vào **bắt buộc** phải cho cùng giá trị băm. Nếu có 21 con chim và chỉ 16 cái lồng, thì một số lồng phải chứa nhiều hơn một con → va chạm là **không thể tránh khỏi**. Tuy nhiên, một hàm băm tốt sẽ khiến xác suất xảy ra va chạm **rất nhỏ**.

---

**MD5** và **SHA1** đã bị tấn công và hiện nay bị coi là **không an toàn** do có thể tạo ra va chạm.
Tuy nhiên, **chưa có cuộc tấn công nào tạo được va chạm trong cả hai thuật toán cùng lúc**.

Nếu bạn so sánh kết quả băm của MD5 và SHA1, bạn sẽ thấy chúng khác nhau. Bạn có thể xem ví dụ về va chạm của MD5 tại trang **[MD5 Collision Demo](https://www.mscs.dal.ca/~selinger/md5collision/)**, và tìm hiểu thêm về tấn công va chạm SHA1 tại **[Shattered](https://shattered.io/)**.

Vì những lý do này, bạn **không nên tin tưởng MD5 hay SHA1** để băm mật khẩu hoặc dữ liệu.

---
**Trả lời các câu hỏi sau:**

**Câu hỏi:**
SHA256 hash của tệp `passport.jpg` trong `~/Hashing-Basics/Task-2/` là gì?
**Trả lời:**
`77148c6f605a8df855f2b764bcc3be749d7db814f5f79134d2aa539a64b61f02`

Lệnh sử dụng:

```bash
sha256sum ~/Hashing-Basics/Task-2/passport.jpg
```

---

**Câu hỏi:**
Kích thước đầu ra (output size) của hàm băm MD5 là bao nhiêu byte?
**Trả lời:** 16

---

**Câu hỏi:**
Nếu đầu ra của hàm băm là 8 bit, thì có bao nhiêu giá trị băm có thể xảy ra?
**Trả lời:** 256

---
