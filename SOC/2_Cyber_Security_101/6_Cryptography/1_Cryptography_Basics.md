# Cryptography Basics

## Mục lục

1. [Task 1: Introduction](#task-1-introduction)
2. [Task 2: Importance of Cryptography](#task-2-common-use-of-asymmetric-encryption)
3. [Task 3: Plaintext to Ciphertext](#task-3-plaintext-to-ciphertext)

## Nội dung

# Task 1: Introduction

**Giới thiệu**

Hãy xem xét kịch bản sau đây trong cuộc sống hàng ngày. Giả sử bạn đang gặp một đối tác kinh doanh tại quán cà phê và thảo luận về các kế hoạch kinh doanh mang tính bảo mật. Hãy cùng phân tích cuộc gặp này từ góc nhìn bảo mật.

* Bạn có thể nhìn thấy và nghe thấy người kia. Do đó, rất dễ để chắc chắn về danh tính của họ. Đó là **xác thực (authentication)**, tức là bạn đang xác nhận danh tính của người mà bạn đang nói chuyện.

* Bạn cũng có thể xác nhận rằng những gì bạn đang “nghe thấy” thực sự đến từ đối tác kinh doanh của bạn. Bạn có thể phân biệt được từ ngữ và câu nói nào đến từ đối tác và cái nào đến từ người khác. Đó là **tính xác thực (authenticity)**, tức là bạn xác minh rằng thông điệp thực sự đến từ một người gửi cụ thể. Hơn nữa, bạn biết rằng những gì họ đang nói đến được truyền đạt nguyên vẹn đến bạn, không có khả năng bị ai đó thay đổi. Đó là **tính toàn vẹn (integrity)**, tức là đảm bảo rằng dữ liệu không bị thay đổi hoặc can thiệp.

* Cuối cùng, bạn có thể chọn ngồi cách xa những khách hàng khác và nói nhỏ để chỉ đối tác của bạn có thể nghe thấy. Đó là **tính bảo mật (confidentiality)**, tức là chỉ những bên được ủy quyền mới có thể truy cập dữ liệu.

Hãy nhanh chóng so sánh điều này với việc liên lạc trong không gian mạng. Khi ai đó gửi cho bạn một tin nhắn văn bản, làm sao bạn có thể chắc chắn họ đúng là người mà họ nói? Làm sao bạn có thể chắc rằng không ai đã thay đổi nội dung khi nó truyền qua các liên kết mạng khác nhau? Khi bạn giao tiếp với đối tác kinh doanh của mình qua một nền tảng nhắn tin trực tuyến, bạn cần phải chắc chắn về những điều sau:

* **Xác thực (Authentication):** Bạn muốn chắc rằng bạn đang giao tiếp với đúng người, không phải ai đó đang giả mạo.

* **Tính xác thực (Authenticity):** Bạn có thể xác minh rằng thông tin đến từ nguồn đã được khẳng định.

* **Tính toàn vẹn (Integrity):** Bạn phải đảm bảo rằng không ai thay đổi dữ liệu mà bạn trao đổi.

* **Tính bảo mật (Confidentiality):** Bạn muốn ngăn chặn bên không được ủy quyền nghe lén các cuộc trò chuyện của bạn.

Mật mã học có thể cung cấp giải pháp để đáp ứng các yêu cầu trên, cùng với nhiều yêu cầu khác. Mật mã khóa riêng (private key cryptography), tức mã hóa đối xứng, chủ yếu bảo vệ tính bảo mật. Tuy nhiên, mật mã khóa công khai (public key cryptography), tức mã hóa bất đối xứng, đóng vai trò quan trọng trong xác thực, tính xác thực và tính toàn vẹn. Phòng này sẽ trình bày các ví dụ khác nhau về cách mật mã khóa công khai đạt được điều đó.

**Mục tiêu học tập**

Trong phần này, chúng ta sẽ tìm hiểu về nhiều hệ mật mã bất đối xứng khác nhau và các ứng dụng sử dụng chúng, chẳng hạn như:

* RSA
* Diffie-Hellman
* SSH
* Chứng chỉ SSL/TLS
* PGP và GPG


# Task 2: Importance of Cryptography
**Tầm quan trọng của Mật mã học**

Mục đích cuối cùng của mật mã học là đảm bảo **giao tiếp an toàn trong sự hiện diện của các đối thủ**. Thuật ngữ “an toàn” bao gồm tính bảo mật và toàn vẹn của dữ liệu được truyền đạt. Mật mã học có thể được định nghĩa là thực hành và nghiên cứu các kỹ thuật để giao tiếp an toàn và bảo vệ dữ liệu trong trường hợp có sự hiện diện của các đối thủ và bên thứ ba. Nói cách khác, những đối thủ này không nên có khả năng tiết lộ hoặc thay đổi nội dung của các thông điệp.

Mật mã học được sử dụng để bảo vệ tính bảo mật, toàn vẹn và xác thực. Trong thời đại này, bạn sử dụng mật mã học hằng ngày, và bạn gần như chắc chắn đang đọc nội dung này qua một kết nối được mã hóa.

Hãy xem xét các tình huống sau đây khi bạn sẽ sử dụng mật mã học:

* Khi bạn đăng nhập vào TryHackMe, thông tin đăng nhập của bạn được mã hóa và gửi đến máy chủ để không ai có thể lấy được chúng bằng cách theo dõi kết nối của bạn.
* Khi bạn kết nối qua SSH, máy khách SSH của bạn và máy chủ thiết lập một đường hầm mã hóa để không ai có thể nghe lén phiên làm việc của bạn.
* Khi bạn thực hiện giao dịch ngân hàng trực tuyến, trình duyệt của bạn kiểm tra chứng chỉ của máy chủ từ xa để xác nhận rằng bạn đang giao tiếp với máy chủ ngân hàng và không phải máy chủ của kẻ tấn công.
* Khi bạn tải xuống một tệp, làm sao bạn kiểm tra được nó có được tải đúng không? Mật mã học cung cấp giải pháp thông qua các hàm băm để xác nhận rằng tệp của bạn giống hệt tệp gốc.

Như bạn thấy, bạn hiếm khi phải tương tác trực tiếp với mật mã học, nhưng các giải pháp và tác động của nó có mặt ở khắp nơi trong thế giới số. Hãy xem xét trường hợp một công ty muốn xử lý thông tin thẻ tín dụng và xử lý các giao dịch liên quan. Khi xử lý thẻ tín dụng, công ty phải tuân thủ và thực hiện các tiêu chuẩn của PCI DSS (Tiêu chuẩn Bảo mật Dữ liệu Ngành Thẻ Thanh toán). Trong trường hợp này, PCI DSS đảm bảo một mức độ bảo mật tối thiểu để lưu trữ, xử lý và truyền dữ liệu liên quan đến thẻ tín dụng. Nếu bạn kiểm tra [PCI DSS for Large Organizations](./PCI_DSS_for_Large_Organizations_v1.pdf), bạn sẽ thấy rằng dữ liệu phải được mã hóa cả khi được lưu trữ (at rest) và khi được truyền đi (in motion).

Tương tự như việc xử lý thông tin thẻ tín dụng yêu cầu tuân thủ PCI DSS, việc xử lý hồ sơ y tế yêu cầu tuân thủ các tiêu chuẩn tương ứng của chúng. Không giống như thẻ tín dụng, các tiêu chuẩn về xử lý hồ sơ y tế khác nhau tùy theo quốc gia. Các luật và quy định ví dụ cần được cân nhắc khi xử lý hồ sơ y tế bao gồm HIPAA (Đạo luật Trách nhiệm và Khả năng Giải trình Bảo hiểm Y tế) và HITECH (Công nghệ Thông tin Y tế cho Kinh tế và Sức khỏe Lâm sàng) ở Hoa Kỳ, GDPR (Quy định Bảo vệ Dữ liệu Chung) ở EU, DPA (Đạo luật Bảo vệ Dữ liệu) ở Vương quốc Anh. Mặc dù danh sách này không đầy đủ, nó cung cấp ý tưởng về các yêu cầu pháp lý mà các nhà cung cấp dịch vụ chăm sóc sức khỏe nên xem xét tùy thuộc vào quốc gia của họ. Các luật và quy định này cho thấy rằng mật mã học là điều cần thiết và nên được hiện diện, tuy nhiên thường bị ẩn đi khỏi quyền truy cập trực tiếp của người dùng.

**Trả lời câu hỏi sau:**

**Câu hỏi:** What is the standard required for handling credit card information?

**Trả lời:** PCI DSS


# Task 3: Plaintext to Ciphertext
>Chuyển đổi văn bản thuần túy thành văn bản mã hóa

Hãy bắt đầu với một minh họa trước khi giới thiệu các thuật ngữ chính. Chúng ta bắt đầu với bản rõ (plaintext) mà ta muốn mã hóa. Bản rõ là dữ liệu có thể đọc được; nó có thể là bất cứ thứ gì từ một từ đơn giản như “hello”, một bức ảnh mèo, thông tin thẻ tín dụng hoặc hồ sơ y tế. Từ góc nhìn của mật mã học, tất cả những thứ này đều là các “bản rõ” đang chờ được mã hóa. Bản rõ được đưa qua hàm mã hóa cùng với một khóa phù hợp; hàm mã hóa sẽ trả về bản mã (ciphertext). Hàm mã hóa là một phần của thuật toán mã hóa (cipher); một cipher là một thuật toán chuyển đổi bản rõ thành bản mã và ngược lại.

![](./img/1_Cryptography_Basics/3.1.svg)

Để khôi phục bản rõ, ta phải đưa bản mã cùng với khóa phù hợp vào hàm giải mã, hàm này sẽ trả lại bản rõ ban đầu. Điều này được minh họa trong hình bên dưới.

![](./img/1_Cryptography_Basics/3.2.svg)

Chúng ta vừa được giới thiệu một số thuật ngữ mới và cần học chúng để hiểu bất kỳ văn bản nào liên quan đến mật mã học. Các thuật ngữ được liệt kê dưới đây:

* **Plaintext** là thông điệp hoặc dữ liệu gốc, có thể đọc được trước khi được mã hóa. Nó có thể là một tài liệu, hình ảnh, tệp đa phương tiện hoặc bất kỳ dữ liệu nhị phân nào khác.
* **Ciphertext** là phiên bản bị xáo trộn, không thể đọc được của thông điệp sau khi được mã hóa. Lý tưởng nhất, chúng ta không thể thu được bất kỳ thông tin nào về bản rõ ban đầu ngoại trừ kích thước xấp xỉ của nó.
* **Cipher** là một thuật toán hoặc phương pháp để chuyển đổi bản rõ thành bản mã và ngược lại. Một cipher thường được phát triển bởi các nhà toán học.
* **Key** là một chuỗi bit mà cipher sử dụng để mã hóa hoặc giải mã dữ liệu. Nói chung, thuật toán cipher được công khai; tuy nhiên, key phải được giữ bí mật trừ khi nó là khóa công khai trong mã hóa bất đối xứng. Chúng ta sẽ tìm hiểu về mã hóa bất đối xứng trong một nhiệm vụ sau.
* **Encryption** là quá trình chuyển đổi bản rõ thành bản mã bằng cách sử dụng một thuật toán mã hóa và một khóa. Không giống như khóa, thuật toán mã hóa thường được công khai.
* **Decryption** là quá trình ngược lại của mã hóa, chuyển đổi bản mã trở lại thành bản rõ bằng cách sử dụng thuật toán mã hóa và khóa. Mặc dù thuật toán mã hóa có thể là công khai, việc khôi phục bản rõ mà không có kiến thức về khóa phải là điều bất khả thi (hoặc không khả thi).

**Trả lời các câu hỏi dưới đây**

- Câu 1: Bạn gọi văn bản thuần được mã hóa là gì?

**ciphertext**

- Câu 2: Bạn gọi quá trình trả lại văn bản thuần là gì?

**decryption**

---
