# Public Key Cryptography Basics

## Mục lục

1. [Task 1: Introduction](#task-1-introduction)
2. [Task 2: Common Use of Asymmetric Encryption](#task-2-common-use-of-asymmetric-encryption)
3. [Task 3: RSA](#task-3-rsa)

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

![](./img/2_Public%20Key_Cryptography_Basics/3.1.png)

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

![](./img/2_Public%20Key_Cryptography_Basics/4.1.png)

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

