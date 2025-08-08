# Public Key Cryptography Basics

## Mục lục

1. [Task 1: Introduction](#task-1-introduction)
2. [Task 2: Common Use of Asymmetric Encryption](#task-2-common-use-of-asymmetric-encryption)
3. [Task 3: RSA](#task-3-rsa)
4. [Task 4: Diffie-Hellman Key Exchange](#task-4-diffie-hellman-key-exchange)
5. [Task 5: SSH](#task-5-ssh)
6. [Task 6: Digital Signatures and Certificates](#task-6-digital-signatures-and-certificates)
7. [Task 7: PGP and GPG](#task-7-pgp-and-gpg)

## Nội dung

# Task 1: Introduction
>Giới thiệu

Hãy xem xét kịch bản sau trong đời sống hằng ngày. Giả sử bạn đang gặp một đối tác kinh doanh để uống cà phê và thảo luận về một số kế hoạch kinh doanh mang tính bảo mật. Hãy phân tích buổi gặp này dưới góc nhìn an ninh.

* Bạn có thể nhìn và nghe người kia. Do đó, bạn dễ dàng xác minh được danh tính của họ. Đó là **xác thực (authentication)**, tức là bạn đang xác nhận danh tính của người mà bạn đang trò chuyện.

* Bạn cũng có thể xác nhận rằng những gì bạn “nghe thấy” thực sự đến từ đối tác kinh doanh. Bạn có thể phân biệt được lời nói và câu văn đến từ đối tác của mình và những gì đến từ người khác. Đó là **tính xác thực (authenticity)**, tức là bạn xác minh rằng thông điệp thực sự đến từ một người gửi cụ thể. Hơn nữa, bạn biết rằng những gì họ nói đang đến đúng người, và không có khả năng có điều gì thay đổi nội dung lời nói của họ trong quá trình truyền đạt. Đó là **tính toàn vẹn (integrity)**, tức là đảm bảo rằng dữ liệu không bị thay đổi hoặc can thiệp.

* Cuối cùng, bạn có thể chọn chỗ ngồi xa những khách hàng khác và giữ giọng nói đủ nhỏ để chỉ có đối tác của bạn nghe thấy. Đó là **tính bảo mật (confidentiality)**, tức là chỉ những người được ủy quyền mới có thể truy cập dữ liệu.

Hãy so sánh nhanh điều này với việc liên lạc trong không gian mạng. Khi ai đó gửi cho bạn một tin nhắn văn bản, làm sao bạn có thể chắc chắn rằng họ thực sự là người mà họ nói họ là? Làm sao bạn chắc rằng không có gì đã thay đổi văn bản trong quá trình nó được truyền qua nhiều liên kết mạng? Khi bạn đang liên lạc với đối tác kinh doanh của mình thông qua một nền tảng nhắn tin trực tuyến, bạn cần đảm bảo những điều sau:

* **Xác thực (Authentication):** Bạn cần chắc chắn rằng bạn đang giao tiếp với đúng người, không phải ai đó giả mạo.
* **Tính xác thực (Authenticity):** Bạn có thể xác minh rằng thông tin đến từ nguồn đáng tin cậy.
* **Tính toàn vẹn (Integrity):** Bạn phải đảm bảo rằng không ai thay đổi dữ liệu mà bạn trao đổi.
* **Tính bảo mật (Confidentiality):** Bạn muốn ngăn chặn các bên không được phép nghe lén các cuộc trò chuyện của bạn.

Mật mã học có thể cung cấp các giải pháp để đáp ứng những yêu cầu trên, cùng với nhiều yêu cầu khác. Mật mã khóa riêng (tức là mã hóa đối xứng) chủ yếu bảo vệ **tính bảo mật**. Tuy nhiên, **mật mã khóa công khai** (tức là mã hóa bất đối xứng) đóng vai trò quan trọng trong việc đảm bảo **xác thực, tính xác thực và tính toàn vẹn**. Phần sau sẽ trình bày các ví dụ về cách mà mật mã khóa công khai thực hiện được những điều đó.


### Mục tiêu học tập

Trong phần này, chúng ta sẽ tìm hiểu về các hệ mật mã bất đối xứng khác nhau và các ứng dụng sử dụng chúng, chẳng hạn như:

* RSA
* Diffie-Hellman
* SSH
* Chứng chỉ SSL/TLS
* PGP và GPG


# Task 2: Common Use of Asymmetric Encryption

>Cách sử dụng phổ biến của mã hóa bất đối xứng

Việc trao đổi khóa cho mã hóa đối xứng là một trong những cách sử dụng phổ biến của mật mã bất đối xứng. Mã hóa bất đối xứng tương đối chậm hơn so với mã hóa đối xứng; do đó, chúng ta dựa vào mã hóa bất đối xứng để đàm phán và thống nhất về thuật toán và khóa mã hóa đối xứng.

**Nhưng câu hỏi đặt ra là:** Làm thế nào để bạn có thể thống nhất về một khóa với máy chủ **mà không truyền khóa đó để người khác có thể nhìn thấy?**

### Phép ẩn dụ

Hãy tưởng tượng bạn có một **mã bí mật** để liên lạc và các hướng dẫn để sử dụng mã bí mật đó. Câu hỏi là làm sao bạn có thể gửi những hướng dẫn này cho bạn của mình mà không ai khác có thể đọc được. Câu trả lời đơn giản hơn bạn nghĩ: bạn có thể nhờ bạn mình gửi cho bạn một **ổ khóa**. Chỉ bạn của bạn mới có **chìa khóa** cho ổ khóa này, và ta giả định rằng bạn có một chiếc hộp không thể phá hủy mà bạn có thể khóa lại bằng ổ khóa đó.

Nếu bạn gửi hướng dẫn trong chiếc hộp đã khóa cho bạn mình, họ có thể mở khóa khi nhận được hộp và đọc hướng dẫn. Sau đó, hai người có thể sử dụng mã bí mật để liên lạc mà không lo bị người khác nghe lén.

Trong phép ẩn dụ này:

* **Mã bí mật** tượng trưng cho **thuật toán và khóa mã hóa đối xứng**
* **Ổ khóa** tượng trưng cho **khóa công khai của máy chủ**
* **Chìa khóa của ổ khóa** tượng trưng cho **khóa riêng của máy chủ**

| Phép ẩn dụ           | Hệ thống mật mã học                |
| -------------------- | ---------------------------------- |
| Mã bí mật(Secret Code)            | Thuật toán và khóa mã hóa đối xứng |
| Ổ khóa (Lock)               | Khóa công khai (Public Key)        |
| Chìa khóa của ổ khóa (Lock's Key) | Khóa riêng (Private Key)           |

**Kết luận:** Bạn chỉ cần sử dụng mật mã bất đối xứng một lần (để gửi khóa mã hóa đối xứng), nhờ đó sẽ không làm ảnh hưởng đến tốc độ, và sau đó có thể liên lạc riêng tư bằng mã hóa đối xứng.

### Thế giới thực

Trong thực tế, bạn cần nhiều kỹ thuật mật mã hơn để xác minh rằng người bạn đang giao tiếp thực sự là người mà họ tuyên bố. Điều này được thực hiện bằng **chữ ký số và chứng chỉ số**, những nội dung sẽ được đề cập trong phần sau.

---

**Trả lời câu hỏi dưới đây**

*Câu hỏi:* Trong phép ẩn dụ đã trình bày, đối tượng thực tế nào tương ứng với **khóa công khai**?

**Trả lời:** **Ổ khóa (Lock)**

# Task 3: RSA

[Xem lab tại đây](/ITMO/)

**RSA (Rivest-Shamir-Adleman)** là một thuật toán mã hóa sử dụng khóa công khai, cho phép truyền dữ liệu an toàn qua các kênh không bảo mật. Với một kênh không bảo mật, ta kỳ vọng sẽ có kẻ tấn công nghe trộm.

---

### Toán học giúp RSA trở nên an toàn

RSA dựa trên một bài toán toán học khó: phân tích một số lớn thành các thừa số nguyên tố. Việc nhân hai số nguyên tố lớn với nhau là thao tác đơn giản; tuy nhiên, tìm các thừa số của một số lớn thì đòi hỏi rất nhiều sức mạnh tính toán.

Bạn có thể nhân hai số nguyên tố nhỏ một cách dễ dàng, ví dụ:
113 × 127 = 14351
Thậm chí với các số nguyên tố lớn hơn, bạn vẫn có thể thực hiện bằng tay nếu cần.

Xét ví dụ sau:

* Số nguyên tố 1: 982451653031
* Số nguyên tố 2: 169743212279
* Tích của chúng:
  982451653031 × 169743212279 = **166764499494295486767649**

Tuy nhiên, nếu chỉ được cho số **166764499494295486767649**, thì việc xác định hai số nguyên tố nào đã tạo nên nó lại rất khó.

Trong các ví dụ thực tế, các số nguyên tố được sử dụng còn lớn hơn nhiều. Máy tính có thể dễ dàng phân tích số 166764499494295486767649, nhưng nếu là một số có hơn **600 chữ số**, thì việc phân tích sẽ gần như là không thể. Ngược lại, việc nhân hai số nguyên tố lớn (mỗi số có khoảng 300 chữ số) lại đơn giản hơn nhiều so với việc phân tích ngược lại.

---

### Ví dụ số học

Tiếp theo, nội dung sẽ minh họa quá trình **mã hóa, giải mã và sử dụng khóa** trong mã hóa bất đối xứng như RSA. Khóa công khai sẽ được dùng để mã hóa, còn **khóa riêng sẽ được giữ bí mật** và dùng để giải mã.

![](./img/2_Public_Key_Cryptography_Basics/3.1.png)

Trong phần **Cơ bản về Mật mã học**, ta đã giải thích phép toán modulo và vai trò quan trọng của nó trong mật mã. Dưới đây là một ví dụ số học đơn giản minh họa cách hoạt động của thuật toán **RSA**:

1. **Bob chọn hai số nguyên tố:**
   $p = 157$, $q = 199$
   Sau đó tính $n = p \times q = 31243$

2. Tính $\phi(n) = n - p - q + 1 = 31243 - 157 - 199 + 1 = 30888$
   Bob chọn $e = 163$ sao cho $e$ nguyên tố cùng nhau với $\phi(n)$.
   Tiếp theo, Bob chọn $d = 379$ sao cho $e \times d \equiv 1 \mod \phi(n)$.
   Nghĩa là $e \times d = 163 \times 379 = 61777$ và $61777 \mod 30888 = 1$
   ⇒ **Khóa công khai** là $(n, e) = (31243, 163)$
   ⇒ **Khóa bí mật** là $(n, d) = (31243, 379)$

3. Giả sử Alice muốn mã hóa giá trị $x = 13$, cô sẽ tính:
   $y = x^e \mod n = 13^{163} \mod 31243 = 16341$
   ⇒ Alice gửi **y = 16341**

4. Bob giải mã giá trị nhận được bằng cách tính:
   $x = y^d \mod n = 16341^{379} \mod 31243 = 13$
   ⇒ Bob khôi phục lại đúng giá trị mà Alice đã gửi.

---

**Lưu ý:**
Chứng minh chi tiết cho thuật toán trên có thể tìm thấy trong lĩnh vực **số học modulo (modular arithmetic)** và vượt ra ngoài phạm vi của mô-đun này. Cũng cần nhắc lại rằng, trong ví dụ này, các số nguyên tố chỉ có 3 chữ số, còn trong ứng dụng thực tế, $p$ và $q$ thường có ít nhất **300 chữ số mỗi số**.


### RSA trong các cuộc thi CTF

Các kiến thức toán học đằng sau RSA thường xuất hiện trong các cuộc thi CTF (Capture The Flag), yêu cầu bạn phải tính toán các biến hoặc phá giải một dạng mã hóa nào đó dựa trên RSA. Nhiều bài viết trên mạng giải thích rất rõ về RSA và thường cung cấp gần như đầy đủ thông tin bạn cần để hoàn thành thử thách. Một ví dụ điển hình về RSA trong CTF là phòng **Breaking RSA**.

Có một số công cụ rất tốt để phá giải thử thách RSA trong CTF. Công cụ yêu thích của tôi là **RsaCtfTool**, đã hoạt động hiệu quả nhiều lần. Tôi cũng từng thành công với **rsatool**.

---

Bạn cần biết các biến chính trong RSA dùng trong CTF, bao gồm:
$p, q, m, n, e, d, c$. Theo ví dụ số học trước:

* $p$ và $q$ là hai số nguyên tố lớn
* $n$ là tích của $p \times q$
* Khóa công khai là $(n, e)$
* Khóa bí mật là $(n, d)$
* $m$ là thông điệp gốc (plaintext)
* $c$ là bản mã (ciphertext)

---

Các thử thách RSA trong Crypto CTF thường cung cấp một tập hợp các giá trị trong số này, và bạn cần phá giải mã hóa để **giải mã thông điệp và truy xuất ra flag**.

**Trả lời các câu hỏi dưới đây**

---

**Biết rằng** $p = 4391$ và $q = 6659$.
**Hỏi:** $n$ là bao nhiêu?

**Trả lời:** **29239669**

```bash
Calculate 𝑛
Formula:n=p×q
Given values:
p=4391
q=6659
Calculation:
n=4391×6659=29239669
```

---

**Biết rằng** $p = 4391$ và $q = 6659$.
**Hỏi:** $\varphi(n)$ là bao nhiêu?

**Trả lời:** **29228620**

```bash
Calculate φ(n):
Formula: φ(n)=(p−1)×(q−1)
Calculation:
φ(n)=(4391−1)×(6659−1)=4390×6658=29228620
```

---

# Task 4: Diffie-Hellman Key Exchange

**Trao đổi khóa Diffie-Hellman**

Một trong những thách thức khi sử dụng mã hóa đối xứng là việc chia sẻ khóa bí mật. Giả sử bạn muốn gửi một tài liệu được bảo vệ bằng mật khẩu cho đối tác kinh doanh của mình để thảo luận về các chiến lược kinh doanh bảo mật. Làm thế nào bạn sẽ chia sẻ mật khẩu với họ? Sẽ là tốt nhất nếu bạn có một kênh bảo mật để gửi mật khẩu, đảm bảo rằng kẻ tấn công không thể đọc hoặc thay đổi nó.

### Trao đổi khóa Diffie-Hellman

**Trao đổi khóa** nhằm thiết lập một bí mật chung giữa hai bên. Đây là một phương pháp cho phép hai bên thiết lập một bí mật chung thông qua một kênh liên lạc không an toàn mà không cần một bí mật chung có sẵn và cũng không để cho bất kỳ bên quan sát nào có thể lấy được khóa này. Do đó, khóa chung này có thể được sử dụng để mã hóa đối xứng trong các liên lạc tiếp theo.

Hãy xem xét kịch bản sau: Alice và Bob muốn nói chuyện một cách an toàn. Họ muốn thiết lập một khóa chung cho mã hóa đối xứng nhưng không muốn sử dụng mã hóa bất đối xứng cho việc trao đổi khóa. Đây chính là lúc phương pháp Trao đổi khóa Diffie-Hellman được sử dụng.

Alice và Bob tạo ra các bí mật một cách độc lập; ta gọi các bí mật này là A và B. Họ cũng có một số dữ liệu công khai chung; ta gọi nó là C.

Chúng ta cần đưa ra một số giả định. Thứ nhất, bất cứ khi nào chúng ta kết hợp các bí mật, thì gần như không thể tách chúng ra được. Thứ hai, thứ tự kết hợp không quan trọng. Alice và Bob sẽ kết hợp bí mật của họ với dữ liệu chung để tạo thành AC và BC. Sau đó, họ gửi những phần này cho nhau và kết hợp phần nhận được với bí mật của mình để tạo ra hai khóa giống hệt nhau, tức là cả hai đều có ABC. Giờ đây, họ có thể sử dụng khóa này để liên lạc với nhau.

Nếu bạn thấy các đoạn trước quá trừu tượng, hãy cùng tìm hiểu quy trình cụ thể sau đây:

1. **Alice và Bob đồng ý về các biến công khai**: một số nguyên tố lớn $p$ và một số sinh $g$, với $0 < g < p$. Những giá trị này sẽ được công bố công khai qua kênh liên lạc. Mặc dù nhỏ và không an toàn trong thực tế, ta sẽ chọn $p = 29$ và $g = 3$ để đơn giản hóa việc tính toán.

2. **Mỗi bên chọn một số nguyên riêng**. Ví dụ cụ thể: Alice chọn $a = 13$, Bob chọn $b = 15$. Mỗi giá trị này là **khóa bí mật** và không được tiết lộ.

3. Đến lúc mỗi bên **tính toán khóa công khai** của mình bằng cách dùng khóa bí mật ở bước 2 và các biến công khai đã thống nhất ở bước 1.
   Alice tính: $A = g^a \mod p = 3^{13} \mod 29 = 19$
   Bob tính: $B = g^b \mod p = 3^{15} \mod 29 = 26$
   Đây là các **khóa công khai**.

4. **Alice và Bob gửi khóa công khai cho nhau**.
   Bob nhận được: $A = g^a \mod p = 19$, tức là khóa công khai của Alice.
   Alice nhận được: $B = g^b \mod p = 26$, tức là khóa công khai của Bob.
   Bước này gọi là **trao đổi khóa**.

5. **Alice và Bob có thể tính toán khóa bí mật chung** bằng cách dùng khóa công khai nhận được và khóa bí mật của chính họ.
   Alice tính: $B^a \mod p = 26^{13} \mod 29 = 10$
   Bob tính: $A^b \mod p = 19^{15} \mod 29 = 10$
   Cả hai phép tính cho cùng một kết quả, $g^{ab} \mod p = 10$, đây là **khóa bí mật chung**.

![](./img/2_Public_Key_Cryptography_Basics/4.1.png)

Các số được chọn quá nhỏ để cung cấp bất kỳ mức độ bảo mật nào, và trong các ứng dụng thực tế, chúng ta sẽ sử dụng những số lớn hơn nhiều.

Trao đổi khóa Diffie-Hellman thường được sử dụng cùng với mật mã khóa công khai RSA. Diffie-Hellman được dùng để thỏa thuận khóa, trong khi RSA được dùng cho chữ ký số, truyền khóa và xác thực, cùng nhiều mục đích khác. Ví dụ, RSA giúp xác minh danh tính của người mà bạn đang liên lạc thông qua việc ký số, vì bạn có thể xác nhận dựa trên khóa công khai của họ. Điều này sẽ ngăn chặn ai đó tấn công kết nối bằng một cuộc tấn công xen giữa (man-in-the-middle) chống lại Alice bằng cách giả làm Bob. Tóm lại, Diffie-Hellman và RSA được tích hợp vào nhiều giao thức và tiêu chuẩn bảo mật để cung cấp một giải pháp bảo mật toàn diện.

---

**Trả lời các câu hỏi dưới đây**

**Cho $p = 29$, $g = 5$, $a = 12$. Hỏi $A$ bằng bao nhiêu?**

**Đáp án: 7**

$$
A = 5^{12} \mod 29 = 7
$$

**Tính toán chi tiết:**

* Công thức: $A = g^a \mod p$
* Thay số: $A = 5^{12} \mod 29$
* Kết quả: $A = 7$

---

**Cho $p = 29$, $g = 5$, $b = 17$. Hỏi $B$ bằng bao nhiêu?**

**Đáp án: 9**

$$
B = 5^{17} \mod 29 = 9
$$

**Tính toán chi tiết:**

* Công thức: $B = g^b \mod p$
* Thay số: $B = 5^{17} \mod 29$
* Kết quả: $B = 9$

---

**Biết rằng $p = 29$, $a = 12$, và bạn đã có $B$ từ câu hỏi thứ hai, khóa được Bob tính là bao nhiêu?**
(**Công thức:** $\text{key} = B^a \mod p$)

**Đáp án: 24**

$$
9^{12} \mod 29 = 24
$$

**Tính toán chi tiết:**

* Công thức: $\text{Key} = B^a \mod p$
* Thay số: $\text{Key} = 9^{12} \mod 29$
* Kết quả: $\text{Key} = 24$

---

**Biết rằng $p = 29$, $b = 17$, và bạn đã có $A$ từ câu hỏi đầu tiên, khóa được Alice tính là bao nhiêu?**
(**Công thức:** $\text{key} = A^b \mod p$)

**Đáp án: 24**

$$
7^{17} \mod 29 = 24
$$

**Tính toán chi tiết:**

* Công thức: $\text{Key} = A^b \mod p$
* Thay số: $\text{Key} = 7^{17} \mod 29$
* Kết quả: $\text{Key} = 24$

# Task 5: SSH

**Xác thực máy chủ**

>Secure Shell

Nếu bạn đã từng sử dụng SSH client trước đây, bạn sẽ nhận ra lời nhắc xác nhận như hiển thị trong đầu ra terminal dưới đây.

```bash
root@TryHackMe# ssh 10.10.244.173
The authenticity of host '10.10.244.173 (10.10.244.173)' can't be established.
ED25519 key fingerprint is SHA256:llZhZc7YzRBDchm02qTX0QsLqeeiTCJg5ip0T0E/YM8.
This key is not known by any other name.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.244.173' (ED25519) to the list of known hosts.
```

Trong tương tác trên, SSH client xác nhận liệu chúng ta có nhận diện được dấu vân tay của khóa công khai của máy chủ hay không. ED25519 là thuật toán khóa công khai được sử dụng để tạo và xác minh chữ ký số trong ví dụ này. SSH client không nhận ra khóa này và đang yêu cầu xác nhận xem chúng ta có muốn tiếp tục kết nối không. Cảnh báo này xuất hiện vì có khả năng xảy ra tấn công dạng "man-in-the-middle" — một máy chủ độc hại có thể đã chặn kết nối và phản hồi, giả danh là máy chủ đích.

Trong trường hợp này, người dùng phải xác thực máy chủ, tức là xác minh danh tính của máy chủ bằng cách kiểm tra chữ ký khóa công khai. Khi người dùng trả lời “yes”, SSH client sẽ ghi nhớ khóa công khai này cho máy chủ. Lần sau, nó sẽ tự động kết nối trừ khi máy chủ trả lời bằng một khóa công khai khác.

**Xác thực máy khách**

Bây giờ khi chúng ta đã xác nhận rằng mình đang giao tiếp với đúng máy chủ, ta cần xác định danh tính và thực hiện xác thực. Trong nhiều trường hợp, người dùng SSH được xác thực bằng tên đăng nhập và mật khẩu giống như khi đăng nhập vào một máy vật lý. Tuy nhiên, do các vấn đề bảo mật vốn có của mật khẩu, phương pháp này không phải là thực hành an toàn tốt nhất.

Một lúc nào đó, bạn sẽ gặp một máy có cấu hình SSH sử dụng xác thực bằng khóa thay vì mật khẩu. Cách xác thực này sử dụng **khóa công khai và khóa riêng tư** để chứng minh rằng máy khách là người dùng hợp lệ và được ủy quyền trên máy chủ. Mặc định, các khóa SSH là khóa RSA. Bạn có thể chọn thuật toán để tạo khóa và thêm passphrase để mã hóa khóa SSH.

**`ssh-keygen`** là chương trình thường được sử dụng để tạo cặp khóa. Nó hỗ trợ nhiều thuật toán khác nhau, như được hiển thị trong trang hướng dẫn dưới đây:

```bash
root@TryHackMe# man ssh-keygen
[...]
  -t dsa | ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa
  Specifies the type of key to create. The possible values are “dsa”, “ecdsa”, “ecdsa-sk”, “ed25519”, “ed25519-sk”, or “rsa”.
[...]
```

**Các thuật toán được hỗ trợ (chỉ cần nhận diện tên tại giai đoạn này):**

* **DSA (Digital Signature Algorithm)**: Thuật toán mật mã khóa công khai chuyên dùng để tạo chữ ký số.
* **ECDSA (Elliptic Curve Digital Signature Algorithm)**: Biến thể của DSA sử dụng mật mã đường cong elliptic để tạo kích thước khóa nhỏ hơn với mức bảo mật tương đương.
* **ECDSA-SK (ECDSA with Security Key)**: Phần mở rộng của ECDSA, sử dụng khóa phần cứng để tăng cường bảo vệ khóa riêng.
* **Ed25519**: Thuật toán chữ ký số sử dụng EdDSA (Edwards-curve Digital Signature Algorithm) với Curve25519.
* **Ed25519-SK (Ed25519 with Security Key)**: Biến thể của Ed25519, tương tự ECDSA-SK, sử dụng khóa bảo mật phần cứng để bảo vệ khóa riêng mạnh hơn.

**Tạo cặp khóa SSH với tùy chọn mặc định**

Lệnh thực hiện:

```bash
ssh-keygen -t ed25519
```

![](./img/2_Public_Key_Cryptography_Basics/5.1.png)

**Diễn giải quá trình:**

* Hệ thống tạo một **cặp khóa công khai/riêng tư** sử dụng thuật toán `ed25519`.
* Tên tệp lưu khóa riêng được đề xuất là:
  `/home/strategos/.ssh/id_ed25519`
* Nếu bạn muốn đặt mật khẩu bảo vệ khóa riêng, hãy nhập **passphrase** (hoặc để trống nếu không cần).
* Khóa riêng được lưu tại:
  `/home/strategos/.ssh/id_ed25519`
* Khóa công khai được lưu tại:
  `/home/strategos/.ssh/id_ed25519.pub`

**Thông tin thêm hiển thị:**

* Dấu vân tay (fingerprint) của khóa:
  `SHA256:4S4DQVrFp52UuNwg+nNTcwlnTETJTbMcCU0N8UYC1do strategos@g5000`
* Một hình ảnh ngẫu nhiên đại diện cho khóa (random art image) giúp trực quan xác minh khóa bằng mắt.

Đây là bước đầu tiên để thiết lập xác thực bằng SSH key — sau đó bạn cần thêm khóa công khai vào máy chủ từ xa (trong tệp `~/.ssh/authorized_keys`) để có thể đăng nhập mà không cần mật khẩu.


Trong ví dụ trên, chúng ta không sử dụng passphrase để có thể xem nội dung của cặp khóa SSH đã tạo:

![](./img/2_Public_Key_Cryptography_Basics/5.2.png)

 **Khóa công khai (`id_ed25519.pub`)**

```bash
cat id_ed25519.pub
```

Nội dung:

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAInqNMqNhpXZGt6T8Q8b0pIyTeldfWq3T3RyNJTmTMJq9 strategos@g5000
```

Đây là khóa mà bạn chia sẻ với máy chủ từ xa — bạn cần thêm dòng này vào tệp `~/.ssh/authorized_keys` trên máy chủ đó để cho phép truy cập.


 **Khóa riêng (`id_ed25519`)**

```bash
cat id_ed25519
```

Nội dung:

```
-----BEGIN OPENSSH PRIVATE KEY-----
<...nội dung mã hóa của khóa riêng...>
-----END OPENSSH PRIVATE KEY-----
```

Đây là khóa phải được giữ **bí mật tuyệt đối**. Bạn không bao giờ chia sẻ khóa này — nó được dùng để xác minh bạn là chủ sở hữu hợp lệ của khóa công khai.


Việc không đặt passphrase (để trống khi tạo khóa) khiến khóa riêng không được mã hóa bằng mật khẩu, tức là **bất kỳ ai có được tệp `id_ed25519` đều có thể sử dụng nó**. Trong môi trường thực tế, nên đặt passphrase để tăng bảo mật.

Lưu ý rằng khóa riêng được chia sẻ ở trên chỉ nhằm mục đích minh họa và đã bị xóa sau đó. Việc chia sẻ khóa riêng là hành động kém an toàn nhất mà bất kỳ ai có thể mắc phải đối với bảo mật của mình. Ngoài ra, nếu chúng ta sử dụng tùy chọn `-t rsa`, thì các khóa được tạo ra sẽ dài hơn nhiều.


**Khóa riêng SSH**

Như đã đề cập, bạn nên đối xử với khóa riêng SSH như mật khẩu. **Không bao giờ chia sẻ chúng trong bất kỳ trường hợp nào**; chúng được gọi là "khóa riêng" vì một lý do. Ai đó có khóa riêng của bạn có thể đăng nhập vào các máy chủ chấp nhận khóa đó, trừ khi khóa đã được mã hóa bằng passphrase.

**Passphrase** được dùng để giải mã khóa riêng **không được gửi đến máy chủ** và **không rời khỏi hệ thống của bạn**. Nó chỉ dùng để giải mã khóa riêng.

Dùng các công cụ như **John the Ripper**, bạn có thể tấn công khóa SSH đã mã hóa để tìm passphrase — điều này nhấn mạnh tầm quan trọng của việc dùng passphrase phức tạp và giữ khóa riêng an toàn.

Khi tạo khóa SSH để đăng nhập vào máy từ xa, bạn nên tạo khóa trên máy cục bộ rồi **sao chép khóa công khai** sang máy đích bằng lệnh `ssh-copy-id`. Như vậy, khóa riêng không bao giờ tồn tại trên máy đích (trừ các trường hợp tạm thời như CTF).

**Phân quyền đúng** là bắt buộc để sử dụng khóa riêng. Nếu không, SSH client sẽ bỏ qua tệp với cảnh báo. Chỉ chủ sở hữu nên có quyền đọc/ghi khóa riêng (thường là `600` hoặc chặt hơn):

```bash
ssh -i privateKeyFileName user@host
```

Đây là cú pháp chuẩn cho SSH client của OpenSSH trên Linux.

---

**Khóa được máy chủ tin cậy**

Thư mục `~/.ssh` là nơi mặc định lưu các khóa. Tệp `authorized_keys` trong thư mục này chứa các **khóa công khai** được phép truy cập vào máy chủ nếu xác thực bằng khóa được bật.

Trên nhiều bản phân phối **Linux**, xác thực bằng khóa được bật theo mặc định vì **an toàn hơn** so với dùng mật khẩu. Chỉ nên cho phép xác thực bằng khóa nếu bạn muốn cấp quyền SSH cho người dùng `root`.

---

**Sử dụng khóa SSH để có một shell "tốt hơn"**

Trong các bài thực hành CTF, kiểm thử xâm nhập, hoặc huấn luyện đỏ xanh (red teaming), khóa SSH là cách tuyệt vời để **nâng cấp reverse shell**, miễn là tài khoản người dùng có đăng nhập được. Tài khoản như `www-data` thường không cho phép, nhưng tài khoản người dùng hoặc `root` thì có thể.

Để lại một khóa SSH trong tệp `authorized_keys` có thể được dùng như một **backdoor hữu ích**, giúp bạn **tránh các vấn đề** liên quan đến shell không ổn định (ví dụ: không dùng được Ctrl-C hoặc tab completion).

---

**Kiểm tra khóa riêng SSH trong thư mục `~/Public-Crypto-Basics/Task-5`. Thuật toán mà khóa sử dụng là gì?**

**Đáp án:** RSA

**Lệnh sử dụng để kiểm tra:**

```bash
ssh-keygen -l -f ~/Public-Crypto-Basics/Task-5
```

**Hoặc để xem nội dung khóa:**

```bash
cat ~/Public-Crypto-Basics/Task-5/id_rsa_1593558668558.id_rsa
```

Từ đó, bạn có thể xác định được loại thuật toán được sử dụng là **RSA**.

---

# Task 6: Digital Signatures and Certificates

**Chữ ký số và Chứng chỉ**

Trong thế giới **“phi số” (analogue)**, bạn thường được yêu cầu ký vào giấy tờ. Khi bạn đến ngân hàng để mở tài khoản tiết kiệm, bạn gần như chắc chắn sẽ phải ký nhiều tài liệu. Khi muốn tạo tài khoản ở thư viện địa phương, bạn sẽ được yêu cầu điền đơn và ký vào đó. Mục đích có thể khác nhau tùy theo hoàn cảnh — ví dụ như xác nhận bạn đồng ý với các điều khoản, ủy quyền giao dịch, hoặc xác nhận đã nhận hàng.

Trong thế giới **“số” (digital)**, bạn không thể sử dụng chữ ký tay, con dấu, hay dấu vân tay — bạn cần một **chữ ký số**.

---

### Chữ ký số là gì?

Chữ ký số cung cấp cách để **xác minh tính xác thực và toàn vẹn** của một thông điệp hoặc tài liệu số. Việc chứng minh tính xác thực của tệp có nghĩa là ta biết ai đã tạo hoặc sửa đổi nó.

Sử dụng **mã hóa bất đối xứng**, bạn tạo ra chữ ký bằng **khóa riêng**, có thể được xác minh bằng **khóa công khai**. Chỉ bạn mới được phép sở hữu khóa riêng, điều đó chứng minh rằng **chính bạn đã ký vào tệp**.

Tại nhiều quốc gia hiện đại, chữ ký số và chữ ký tay có **giá trị pháp lý tương đương**.

Dạng đơn giản nhất của chữ ký số là mã hóa tài liệu bằng **khóa riêng**. Ai muốn xác minh chữ ký có thể giải mã bằng **khóa công khai**, rồi so sánh nội dung để kiểm tra xem tệp có bị thay đổi không. Quy trình này được minh họa trong hình bên dưới.

![](./img/2_Public_Key_Cryptography_Basics/6.1.png)

Một số bài viết sử dụng các thuật ngữ như **chữ ký điện tử** và **chữ ký số** thay thế cho nhau. Chúng thường chỉ hành động chèn hình ảnh của chữ ký vào tài liệu. Tuy nhiên, cách này **không chứng minh được tính toàn vẹn của tài liệu**, vì ai cũng có thể sao chép và dán hình ảnh đó.

Trong nhiệm vụ này, thuật ngữ **chữ ký số** dùng để chỉ việc ký một tài liệu bằng **khóa riêng** hoặc **chứng chỉ số**. Quy trình này giống như hình minh họa trước đó — ví dụ Bob mã hóa **hàm băm (hash)** của tài liệu rồi chia sẻ cùng tài liệu gốc với Alice. Alice có thể **giải mã hàm băm** và **so sánh với hàm băm của tài liệu** cô ấy nhận được để xác thực tính toàn vẹn. Cách làm này **an toàn hơn nhiều** so với việc chỉ chèn hình chữ ký.

---

### **Chứng chỉ số: Xác minh bạn là ai**

**Chứng chỉ số (certificates)** là một ứng dụng quan trọng của mật mã khóa công khai, và cũng liên quan chặt chẽ đến chữ ký số. Một ví dụ phổ biến là khi bạn truy cập trang web qua **HTTPS** — làm sao trình duyệt biết được đó thực sự là trang *tryhackme.com*?

Câu trả lời nằm ở **chứng chỉ số**. Máy chủ web có một chứng chỉ nói rằng nó là *tryhackme.com thật sự*. Các chứng chỉ này nằm trong **chuỗi tin cậy (chain of trust)**, bắt đầu từ một **Tổ chức cấp chứng chỉ gốc (Root CA)**. Từ lúc thiết bị được cài đặt, hệ điều hành và trình duyệt web đã **tự động tin tưởng nhiều Root CA**. Một chứng chỉ chỉ được tin cậy nếu **Root CA tuyên bố rằng họ tin tưởng tổ chức đã ký** chứng chỉ đó.

Về bản chất, đây là một chuỗi:
Chứng chỉ được ký bởi một tổ chức → tổ chức đó được tin bởi một CA → CA được trình duyệt của bạn tin → do đó trình duyệt tin chứng chỉ. Các trình duyệt như Firefox hay Chrome có danh sách CA đáng tin cậy của riêng mình ([xem tại đây](https://ccadb-public.secure.force.com/mozilla/IncludedCACertificateReport) và [tại đây](https://www.chromium.org/Home/chromium-security/root-ca-policy/)).

---

### Nếu bạn có website và muốn sử dụng HTTPS:

Bạn cần **chứng chỉ TLS**. Có thể mua từ các tổ chức cấp chứng chỉ (CA) với phí hàng năm, hoặc dùng **Let’s Encrypt** để **nhận miễn phí**. Nếu bạn điều hành một trang web, thì việc thiết lập HTTPS là điều **rất nên làm**, vì gần như mọi trang hiện đại đều đã dùng.

---

**Trả lời các câu hỏi sau**

**Câu hỏi:** Máy chủ web từ xa sử dụng gì để chứng minh danh tính với máy khách?
**Trả lời:** Chứng chỉ (Certificate)

**Câu hỏi:** Bạn sẽ dùng gì để lấy chứng chỉ TLS miễn phí cho website của mình?
**Trả lời:** Let’s Encrypt

# Task 7: PGP and GPG

**PGP và GPG**

**PGP** là viết tắt của *Pretty Good Privacy* (Bảo mật khá tốt). Đây là phần mềm dùng để mã hóa file, ký số tài liệu, và nhiều chức năng khác. **GnuPG** hoặc **GPG** là phiên bản mã nguồn mở của chuẩn OpenPGP.

**GPG** thường được sử dụng trong email để bảo vệ tính riêng tư của nội dung thư. Ngoài ra, nó còn có thể được dùng để **ký vào email** nhằm xác nhận **tính toàn vẹn** của nội dung.

Dưới đây là ví dụ về quá trình tạo khóa bằng **GPG**. Bạn sẽ được hỏi về mục đích sử dụng khóa GPG — chẳng hạn để **chỉ ký số** hoặc **vừa ký vừa mã hóa**. Bên cạnh việc chọn thuật toán mã hóa, bạn cũng cần thiết lập **ngày hết hạn** cho khóa. Cuối cùng, bạn sẽ cung cấp một số thông tin cá nhân như: **tên, địa chỉ email**, và một **ghi chú** ngắn mô tả mục đích sử dụng khóa này.

```bash
gpg --full-gen-key
gpg (GnuPG) 2.4.4; Copyright (C) 2024 g10 Code GmbH
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Please select what kind of key you want:
   (1) RSA and RSA
   (2) DSA and Elgamal
   (3) DSA (sign only)
   (4) RSA (sign only)
   (9) ECC (sign and encrypt) *default*
  (10) ECC (sign only)
  (14) Existing key from card
Your selection? 9
Please select which elliptic curve you want:
   (1) Curve 25519 *default*
   (4) NIST P-384
   (6) Brainpool P-256
Your selection? 1
Please specify how long the key should be valid.
         0 = key does not expire
      <n>  = key expires in n days
      <n>w = key expires in n weeks
      <n>m = key expires in n months
      <n>y = key expires in n years
Key is valid for? (0) 
Key does not expire at all
Is this correct? (y/N) y
GnuPG needs to construct a user ID to identify your key.
Real name: strategos
Email address: strategos@tryhackme.thm
[...]
pub   ed25519 2024-08-29 [SC]
      AB7E6AA87B6A8E0D159CA7FFE5E63DBD5F83D5ED
uid                      Strategos <strategos@tryhackme.thm>
sub   cv25519 2024-08-29 [E]
```

Bạn có thể cần dùng GPG để giải mã các tệp trong các cuộc thi CTF. Với PGP/GPG, khóa riêng có thể được bảo vệ bằng passphrase (mật khẩu) — tương tự như cách bảo vệ khóa SSH riêng. Nếu khóa có đặt passphrase, bạn có thể thử dò mật khẩu bằng công cụ **John the Ripper** và **gpg2john**.

> *Lưu ý: Khóa được cung cấp trong nhiệm vụ này **không có passphrase**.*

Trang hướng dẫn (man page) của GPG có thể tìm thấy trực tuyến [tại đây](https://www.gnupg.org/gph/de/manual/r1023.html).

---

### **Ví dụ thực tế**

Khi bạn đã tạo cặp khóa GPG, bạn có thể **chia sẻ khóa công khai** với người liên hệ. Khi họ muốn gửi tin nhắn an toàn cho bạn, họ sẽ **mã hóa tin nhắn bằng khóa công khai của bạn**.
Để giải mã tin nhắn, bạn sẽ phải sử dụng **khóa riêng**.

Do tầm quan trọng của cặp khóa GPG, bạn nên **sao lưu khóa ở nơi an toàn**.

---

**Giả sử bạn dùng một máy tính mới**, bạn chỉ cần **nhập lại khóa** và bắt đầu giải mã các tin nhắn đã nhận:

* **Nhập khóa sao lưu:**

```bash
gpg --import backup.key
```

* **Giải mã tin nhắn đã nhận:**

```bash
gpg --decrypt confidential_message.gpg
```
---

**Trả lời các câu hỏi sau**

**Câu hỏi:**
Sử dụng GPG để giải mã tin nhắn trong thư mục `~/Public-Crypto-Basics/Task-7`.
Từ bí mật trong tin nhắn là gì?

**Đáp án:** Pineapple

---

**Lệnh sử dụng:**

```bash
gpg --import ~/Public-Crypto-Basics/Task-7/tryhackme.key
gpg --decrypt ~/Public-Crypto-Basics/Task-7/message.gpg
```
