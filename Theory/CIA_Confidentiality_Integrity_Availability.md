# Tam Giác Bảo Mật CIA (Confidentiality, Integrity, Availability)

### Mục lục

1. [3 yếu tố bảo mật “tính bảo mật”, “tính toàn vẹn” và “tính sẵn sàng” là gì?](#3-yếu-tố-bảo-mật-tính-bảo-mật-tính-toàn-vẹn-và-tính-sẵn-sàng-là-gì)
2. [Tính bảo mật: Confidentiality là gì?](#tính-bảo-mật-confidentiality-là-gì)
   - [Tài sản thông tin cần được bảo mật](#tài-sản-thông-tin-cần-được-bảo-mật)
     - [Thông tin cá nhân](#thông-tin-cá-nhân)
     - [Bí mật kinh doanh](#bí-mật-kinh-doanh)
     - [Thông tin hợp đồng](#thông-tin-hợp-đồng)
     - [Thông tin tài chính](#thông-tin-tài-chính)
     - [Thông tin pháp lý và luật định](#thông-tin-pháp-lý-và-luật-định)
     - [Thông tin bảo mật](#thông-tin-bảo-mật)
   - [Các biện pháp cụ thể](#các-biện-pháp-cụ-thể)
     - [Kiểm soát truy cập](#kiểm-soát-truy-cập)
     - [Mã hóa](#mã-hóa)
     - [Phân loại dữ liệu](#phân-loại-dữ-liệu)
     - [Giáo dục và đào tạo về an toàn thông tin](#giáo-dục-và-đào-tạo-về-an-toàn-thông-tin)
     - [An ninh vật lý](#an-ninh-vật-lý)
     - [Thiết lập chính sách và quy trình an toàn thông tin](#thiết-lập-chính-sách-và-quy-trình-an-toàn-thông-tin)
     - [Kiểm tra và đánh giá bảo mật](#kiểm-tra-và-đánh-giá-bảo-mật)
3. [Tính toàn vẹn: Integrity là gì?](#tính-toàn-vẹn-integrity-là-gì)
   - [Tài sản thông tin cần duy trì tính toàn vẹn](#tài-sản-thông-tin-cần-duy-trì-tính-toàn-vẹn)
     - [Thông tin tài chính](#thông-tin-tài-chính-1)
     - [Thông tin khách hàng](#thông-tin-khách-hàng)
     - [Thông tin nhân viên](#thông-tin-nhân-viên)
     - [Thông tin sản phẩm và dịch vụ](#thông-tin-sản-phẩm-và-dịch-vụ)
     - [Thông tin liên quan đến pháp luật và quy định](#thông-tin-liên-quan-đến-pháp-luật-và-quy-định)
     - [Tài sản trí tuệ](#tài-sản-trí-tuệ)
     - [Thông tin kế toán và tài chính](#thông-tin-kế-toán-và-tài-chính)
   - [Các biện pháp cụ thể](#các-biện-pháp-cụ-thể)
     - [Kiểm soát truy cập](#kiểm-soát-truy-cập)
     - [Sao lưu dữ liệu](#sao-lưu-dữ-liệu)
     - [Tổng kiểm và hàm băm](#tổng-kiểm-và-hàm-băm)
     - [Xác minh nhập và chỉnh sửa dữ liệu](#xác-minh-nhập-và-chỉnh-sửa-dữ-liệu)
4. [Tính sẵn sàng: Availability là gì?](#tính-sẵn-sàng-availability-là-gì)
   - [Tài sản thông tin cần duy trì tính sẵn sàng](#tài-sản-thông-tin-cần-duy-trì-tính-sẵn-sàng)
     - [Cơ sở dữ liệu khách hàng](#cơ-sở-dữ-liệu-khách-hàng)
     - [Thông tin tài chính](#thông-tin-tài-chính-2)
     - [Tài liệu nội bộ](#tài-liệu-nội-bộ)
     - [Hệ thống và ứng dụng](#hệ-thống-và-ứng-dụng)
     - [Email](#email)
   - [Các biện pháp cụ thể](#các-biện-pháp-cụ-thể-2)
     - [Dự phòng](#dự-phòng)
     - [Sao lưu](#sao-lưu)
     - [Bảo trì](#bảo-trì)
     - [Giám sát](#giám-sát)
5. [Cách phân loại mức độ của CIA (Confidentiality, Integrity, Availability)](#cách-phân-loại-mức-độ-của-cia-confidentiality-integrity-availability)
6. [Cách áp dụng CIA vào hoạt động kinh doanh](#cách-áp-dụng-cia-vào-hoạt-động-kinh-doanh)
   - [Tính bảo mật (Confidentiality)](#tính-bảo-mật-confidentiality)
   - [Tính toàn vẹn (Integrity)](#tính-toàn-vẹn-integrity)
   - [Tính sẵn sàng (Availability)](#tính-sẵn-sàng-availability)
7. [Sự cân bằng quan trọng giữa tính bảo mật, tính toàn vẹn và tính sẵn sàng](#sự-cân-bằng-quan-trọng-giữa-tính-bảo-mật-tính-toàn-vẹn-và-tính-sẵn-sàng)
8. [Bốn tính chất mới trong khái niệm an ninh thông tin](#bốn-tính-chất-mới-trong-khái-niệm-an-ninh-thông-tin)
   - [Tính xác thực (Authenticity)](#tính-xác-thực-authenticity)
   - [Tính đáng tin cậy (Reliability)](#tính-đáng-tin-cậy-reliability)
   - [Tính trách nhiệm (Accountability)](#tính-trách-nhiệm-accountability)
   - [Tính không thể chối bỏ (Non-repudiation)](#tính-không-thể-chối-bỏ-non-repudiation)


### Nội dung

<h1 id="3-yếu-tố-bảo-mật-tính-bảo-mật-tính-toàn-vẹn-và-tính-sẵn-sàng-là-gì">Phần 1: 3 yếu tố bảo mật “tính bảo mật”, “tính toàn vẹn” và “tính sẵn sàng” là gì?</h1>

SMS (ISO 27001) yêu cầu xây dựng một hệ thống có thể duy trì 3 yếu tố “tính bảo mật”, “tính toàn vẹn” và “tính sẵn sàng”. Đây là 3 yếu tố ngăn chặn việc làm sai lệch, thất thoát, mất mát, hư hỏng các thông tin quan trọng và xử lý thông tin một cách an toàn.

Ba yếu tố bảo mật, toàn vẹn và sẵn sàng thường được gọi bằng từ viết tắt tiếng Anh là “CIA”.

- “Tính bảo mật”: confidentiality
- “Tính toàn vẹn”: integrity
- “Tính sẵn sàng”: availability

<h1 id="tính-bảo-mật-confidentiality-là-gì">Phần 2: Tính bảo mật: Confidentiality là gì?</h1>

Tính bảo mật tức là, đảm bảo thông tin chỉ được phép truy cập bởi những đối tượng được cấp phép, hay nói cách khác, là việc đảm bảo thông tin được bảo vệ sao cho không bị tiết lộ cho những đối tượng không được cấp phép.

Tính bí mật của thông tin có thể đạt được bằng cách sử dụng các biện pháp như xác thực, giới hạn truy cập và mã hóa.

Nếu tính bảo mật của thông tin được đảm bảo, thì có thể ngăn chặn sự xâm nhập từ bên ngoài và giảm thiểu khả năng rò rỉ, mất mát, thất thoát hoặc hư hỏng thông tin.

<h2 id="tài-sản-thông-tin-cần-được-bảo-mật">2.1 Tài sản thông tin cần được bảo mật</h2>


### Thông tin cá nhân

Thông tin cá nhân của khách hàng và nhân viên, bao gồm địa chỉ, số điện thoại, địa chỉ email và thông tin nhận dạng cá nhân khác, phải được bảo vệ dưới góc độ quyền riêng tư.

### Bí mật kinh doanh

Thông tin liên quan đến bí mật thương mại cần được bảo vệ, bao gồm:
- Nghiên cứu và phát triển
- Thông tin kỹ thuật
- Chiến lược kinh doanh
- Thông tin về sản phẩm và dịch vụ mới

### Thông tin hợp đồng

Các thông tin liên quan đến hợp đồng cần được bảo mật, bao gồm:
- Hợp đồng với đối tác kinh doanh và công ty đối tác
- Thông tin dự án trong quá trình đàm phán kinh doanh

### Thông tin tài chính

Thông tin liên quan đến tình hình tài chính của một tổ chức cần được giữ bí mật, bao gồm:
- Dữ liệu kế toán
- Ngân sách và dự toán
- Kế hoạch tài trợ

### Thông tin pháp lý và luật định

Thông tin cần bảo vệ bao gồm các yêu cầu pháp lý và luật định, chẳng hạn như:
- Tài liệu pháp lý
- Thông tin kiện tụng
- Báo cáo kiểm toán

### Thông tin bảo mật

Tính bảo mật rất quan trọng đối với các thông tin sau:
- Sơ đồ cấu hình mạng
- Thông tin lỗ hổng hệ thống
- Mật khẩu

<h2 id="các-biện-pháp-cụ-thể">2.2 Các biện pháp cụ thể</h2>

### Kiểm soát truy cập

Giới hạn quyền truy cập thông tin chỉ cho những người có quyền hạn tối thiểu cần thiết, nhằm ngăn chặn truy cập trái phép và rò rỉ thông tin.  
Áp dụng danh sách kiểm soát truy cập (ACL) và chỉ cho phép truy cập đối với người dùng cụ thể hoặc nhóm cụ thể.

### Mã hóa

Áp dụng công nghệ mã hóa cho việc truyền tải và lưu trữ dữ liệu, nhằm đảm bảo rằng thông tin không thể đọc được ngay cả khi xảy ra truy cập trái phép hoặc rò rỉ.  
Nên sử dụng các phương pháp mã hóa phù hợp như mã hóa toàn bộ thiết bị hoặc mã hóa tệp tin.

### Phân loại dữ liệu

Phân loại tài sản thông tin theo mức độ bảo mật và áp dụng các biện pháp bảo vệ phù hợp cho mỗi mức độ.  
Lập chính sách phân loại dữ liệu và thông báo rõ ràng cho nhân viên.

### Giáo dục và đào tạo về an toàn thông tin

Tổ chức các chương trình giáo dục và đào tạo về an toàn thông tin nhằm nâng cao nhận thức của nhân viên.  
Thực hiện đào tạo nâng cao kiến thức định kỳ và liên tục, nhằm cải thiện liên tục các biện pháp bảo mật.

### An ninh vật lý

Lưu trữ tài sản thông tin trong các cơ sở và phòng được áp dụng biện pháp bảo mật, nhằm ngăn chặn truy cập trái phép và mất mát do trộm cắp.  
Nên áp dụng các biện pháp bảo mật vật lý như camera an ninh và thẻ truy cập.

### Thiết lập chính sách và quy trình an toàn thông tin

Xây dựng chính sách an toàn thông tin cho toàn bộ tổ chức và đề ra các quy trình và quy tắc cụ thể.  
Thường xuyên xem lại và cải thiện chính sách để thích nghi với tình hình an ninh.

### Kiểm tra và đánh giá bảo mật

Thực hiện kiểm tra và đánh giá bảo mật định kỳ để xác minh hiệu quả của các biện pháp bảo mật thông tin.

<h1 id="tính-toàn-vẹn-integrity-là-gì">Phần 3: Tính toàn vẹn: Integrity là gì?</h1>

Tính toàn vẹn là trạng thái mà thông tin được lưu trữ hoặc truyền tải một cách chính xác và nhất quán. Điều này giúp ngăn chặn việc dữ liệu bị thay đổi sai hoặc bị sửa đổi một cách trái phép. Khi tính toàn vẹn không được đảm bảo, độ chính xác và đáng tin cậy của thông tin sẽ bị mất đi.

Nói một cách đơn giản, việc duy trì sự chính xác, sự cập nhật và sự đầy đủ trong thông tin là mục tiêu của tính toàn vẹn.

Ví dụ, nếu áp dụng vào tính toán lương, khi tính toàn vẹn không được đảm bảo, có thể xảy ra các vấn đề sau:

– Số tiền lương sai lệch: Nếu thời gian làm việc và thời gian làm thêm của nhân viên không được ghi chính xác, có thể dẫn đến sai sót trong tính toán lương. Điều này có thể ảnh hưởng đến động lực làm việc và gánh nặng trong cuộc sống của nhân viên, gây ảnh hưởng tiêu cực đến năng suất của tổ chức.

– Vi phạm pháp luật: Một số trường hợp sẽ bị quy cho là không tuân thủ các quy định pháp luật về mức lương tối thiểu hoặc giới hạn thời gian làm việc đã được quy định. Điều này không chỉ khiến công ty bị xử phạt mà danh tiếng của công ty cũng sẽ bị tổn hại.

<h2 id="tài-sản-thông-tin-cần-duy-trì-tính-toàn-vẹn">3.1 Tài sản thông tin cần duy trì tính toàn vẹn</h2>

### Thông tin tài chính
Thông tin liên quan đến giao dịch tài chính như thông tin tài khoản ngân hàng, thông tin thẻ tín dụng, lịch sử thanh toán, cần phải đảm bảo tính toàn vẹn vì sự thay đổi hoặc sửa đổi sai sót có thể dẫn đến thiệt hại lớn.

### Thông tin khách hàng
Thông tin về cá nhân khách hàng, lịch sử giao dịch, nội dung hợp đồng và các thông tin liên quan đến khách hàng đòi hỏi tính chính xác để duy trì mối quan hệ tin cậy.

### Thông tin nhân viên
Thông tin về cá nhân nhân viên, quản lý chấm công, thông tin về lương và các thông tin liên quan đến nhân viên yêu cầu tính toàn vẹn để đảm bảo độ chính xác và đáng tin cậy của dữ liệu liên quan đến nhân viên.

### Thông tin sản phẩm và dịch vụ
Thông tin về thông số kỹ thuật sản phẩm, giá cả, thông tin kho hàng và các chi tiết khác liên quan trực tiếp đến hoạt động kinh doanh cần đảm bảo tính chính xác.

### Thông tin liên quan đến pháp luật và quy định
Thông tin liên quan đến pháp luật, quy định và tuân thủ pháp lý yêu cầu tính toàn vẹn để thực hiện hoạt động đúng quy định.

### Tài sản trí tuệ
Thông tin về tài sản trí tuệ như bằng sáng chế, quyền tác giả, quyền thương hiệu là quan trọng cho sự cạnh tranh của công ty, và do đó, yêu cầu tính toàn vẹn.

### Thông tin kế toán và tài chính
Sổ sách kế toán, báo cáo tài chính, ngân sách và các thông tin tài chính khác ảnh hưởng đến quản lý doanh nghiệp, yêu cầu tính chính xác và đáng tin cậy.

<h2 id="các-biện-pháp-cụ-thể">3.2 Các biện pháp cụ thể</h2>

### Kiểm soát truy cập
Quản lý quyền truy cập thông tin và ngăn chặn sự thay đổi hoặc sửa đổi trái phép.

### Sao lưu dữ liệu
Thực hiện sao lưu định kỳ dữ liệu để khôi phục thông tin chính xác trong trường hợp dữ liệu bị hỏng.

### Tổng kiểm và hàm băm
Xác minh tính toàn vẹn của dữ liệu bằng cách tổng kiểm tra và sử dụng hàm băm.

### Xác minh nhập và chỉnh sửa dữ liệu
Đảm bảo rằng dữ liệu được nhập và chỉnh sửa chính xác bằng cách thiết lập các kiểm tra hợp lệ trên biểu mẫu nhập liệu, theo dõi và kiểm tra lịch sử thay đổi của dữ liệu để bảo đảm tính toàn vẹn.

<h1 id="tính-sẵn-sàng-availability-là-gì">Phần 4: Tính sẵn sàng: Availability là gì?</h1>

Tính sẵn sàng đề cập đến khả năng của một hệ thống thông tin được truy cập vào đúng thời điểm, bởi đúng người và được cung cấp đúng các tài nguyên cần thiết.

Tính sẵn sàng được định nghĩa là:

1. Thời gian ngừng hoạt động của hệ thống ở mức tối thiểu.
2. Hệ thống hoạt động với hiệu suất phù hợp.
3. Dữ liệu có thể được truy cập vào những thời điểm thích hợp.
4. Mạng và các dịch vụ hoạt động bình thường.
5. Có kế hoạch phục hồi dự phòng để đối phó với thiên tai và sự cố.

Ví dụ: đối với bộ nhớ dùng chung và bộ nhớ đám mây: Ổ đĩa dùng chung và bộ nhớ đám mây nơi lưu trữ các tệp và tài liệu được chia sẻ trong công ty phải luôn có thể truy cập được mà không gặp sự cố hoặc suy giảm hiệu suất.

<h2 id="tài-sản-thông-tin-cần-duy-trì-tính-sẵn-sàng">4.1 Tài sản thông tin cần duy trì tính sẵn sàng</h2>

### Cơ sở dữ liệu khách hàng
Cơ sở dữ liệu chứa thông tin quan trọng về khách hàng, chẳng hạn như thông tin khách hàng và lịch sử giao dịch, đóng vai trò quan trọng trong các hoạt động kinh doanh như bán hàng và hỗ trợ khách hàng.

### Thông tin tài chính
Thông tin quan trọng liên quan đến quản lý doanh nghiệp, chẳng hạn như tình hình tài chính và các chỉ số quản lý của công ty, đóng một vai trò quan trọng trong việc ra quyết định và xây dựng chiến lược.

### Tài liệu nội bộ
Các tài liệu cần thiết cho việc thực hiện kinh doanh, chẳng hạn như hướng dẫn thủ tục và quy trình kinh doanh nội bộ, hợp đồng và báo cáo, là cần thiết để đảm bảo việc thực hiện kinh doanh suôn sẻ và tuân thủ.

### Hệ thống và ứng dụng
Các hệ thống và ứng dụng kinh doanh nội bộ là cần thiết để thực hiện kinh doanh hiệu quả và chia sẻ thông tin. Điều quan trọng là các hệ thống và ứng dụng này phải hoạt động tốt và người cần truy cập có thể truy cập được.

### Email
Thư điện tử là tài sản thông tin không thể thiếu để liên lạc trong nội bộ và với bên ngoài. Tốc độ đường truyền khi gửi và nhận email phải được đảm bảo và người cần truy cập có thể truy cập được.

<h2 id="các-biện-pháp-cụ-thể">4.2 Các biện pháp cụ thể</h2>

### Dự phòng
Nên thực hiện dự phòng cho máy chủ và thiết bị mạng. Cho các thiết bị và hệ thống dự phòng hoạt động từ thời điểm mọi thứ diễn ra bình thường, để đảm bảo hệ thống vẫn hoạt động liên tục khi xảy ra sự cố.

### Sao lưu
Thực hiện sao lưu dữ liệu và hệ thống đều đặn, nhằm đảm bảo khả năng khôi phục nhanh chóng khi xảy ra sự cố hoặc mất dữ liệu.

### Bảo trì
Thực hiện bảo trì định kỳ cho hệ thống và mạng, nhằm ngăn chặn sự suy giảm hiệu suất và xảy ra sự cố từ trước.

### Giám sát
Theo dõi tình trạng hệ thống và mạng theo thời gian thực, và đối phó nhanh chóng khi phát hiện sự bất thường.

<h1 id="cách-phân-loại-mức-độ-của-cia-confidentiality-integrity-availability">Phần 5: Cách phân loại mức độ của CIA (Confidentiality, Integrity, Availability)</h1>

ISMS (ISO 27001) yêu cầu phải thực hiện đánh giá rủi ro tài sản.

Khi đánh giá rủi ro, các tài sản thông tin sẽ được xác định giá trị dựa trên mức độ CIA (Confidentiality, Integrity, Availability).

Có nhiều công ty xác định mức độ của tài sản thông tin bằng cách áp dụng các tiêu chí sau.

| Level   | Tính bảo mật                | Tính toàn vẹn                    | Tính sẵn sàng                |
|---------|-----------------------------|-----------------------------------|------------------------------|
| Level 3 | Tính bảo mật cao            | Tính toàn vẹn cao                | Tính sẵn sàng cao            |
| Level 2 | Tính bảo mật ở mức trung bình | Tính toàn vẹn ở mức trung bình    | Tính sẵn sàng ở mức trung bình |
| Level 1 | Tính bảo mật thấp           | Tính toàn vẹn thấp               | Tính sẵn sàng thấp           |

  
<h1 id="cách-áp-dụng-cia-vào-hoạt-động-kinh-doanh">Phần 6: Cách áp dụng CIA vào hoạt động kinh doanh</h1>

Để có thể áp dụng tam giác bảo mật CIA (Confidentiality, Integrity, Availability) vào hoạt động kinh doanh, doanh nghiệp cần nâng cao chất lượng và hiệu suất công việc bằng cách duy trì mức độ bảo mật CIA một cách thích hợp.

<h2 id="các-biện-pháp-cụ-thể">6.1 Tính bảo mật (Confidentiality)</h2>

Giới hạn quyền truy cập đối với các tài sản thông tin có tính bảo mật cao như thông tin khách hàng và bí mật công ty để giảm thiểu rủi ro truy cập trái phép và rò rỉ thông tin.

Khi trao đổi thông tin nội bộ và bên ngoài công ty, việc sử dụng công nghệ mã hóa có thể giảm thiểu rủi ro rò rỉ thông tin cho bên thứ ba.

<h2 id="tính-toàn-vẹn-integrity">6.2 Tính toàn vẹn (Integrity)</h2>

Để ngăn chặn sự thay đổi hoặc hư hỏng dữ liệu, cần thiết lập các quyền liên quan đến việc nhập, chỉnh sửa và xóa dữ liệu một cách chính xác và ngăn chặn sự giả mạo dữ liệu do hành động trái phép.

Thực hiện sao lưu dữ liệu định kỳ và đảm bảo rằng dữ liệu có thể được khôi phục chính xác và hoàn chỉnh trong trường hợp xảy ra sự cố.

<h2 id="tính-sẵn-sàng-availability">6.3 Tính sẵn sàng (Availability)</h2>

Thực hiện vận hành và quản lý máy chủ và mạng một cách hợp lý, duy trì trạng thái truy cập hệ thống và dịch vụ thông tin cần thiết cho công việc vào thời điểm thích hợp.

Lên kế hoạch đối phó với thiên tai và lập kế hoạch dự phòng để đảm bảo khả năng tiếp tục hoạt động của doanh nghiệp trong trường hợp xảy ra sự cố hệ thống hoặc thiên tai.
  
<h1 id="sự-cân-bằng-quan-trọng-giữa-tính-bảo-mật-tính-toàn-vẹn-và-tính-sẵn-sàng">Phần 7: Sự cân bằng quan trọng giữa tính bảo mật, tính toàn vẹn và tính sẵn sàng</h1>

Việc cân bằng 3 yếu tố tính bảo mật (C), tính toàn vẹn (I) và tính sẵn sàng (A) đã đề cập ở trên mới là quan trọng.

Ví dụ, nếu bạn ưu tiên quá nhiều vào tính bảo mật, các biện pháp hạn chế truy cập thông tin có thể dẫn đến sự suy giảm của tính sẵn sàng. Tương tự, nếu bạn quá ưu tiên tính toàn vẹn, việc quản lý thông tin quá đà sẽ làm giảm hiệu suất công việc.

Bằng cách vận dụng CIA một cách cân bằng và phù hợp, bạn có thể bảo vệ tài sản thông tin một cách hiệu quả, cải thiện tính ổn định và tính đáng tin cậy của công việc.

Do đó, doanh nghiệp nên cân bằng và đánh giá rủi ro 3 yếu tố tính bảo mật (C), tính toàn vẹn (I) và tính sẵn sàng (A); và xem xét các yếu tố ảnh hưởng xã hội và ảnh hưởng kinh tế.

<h1 id="bốn-tính-chất-mới-trong-khái-niệm-an-ninh-thông-tin">Phần 8: Bốn tính chất mới trong khái niệm an ninh thông tin</h1>

Trong thời gian gần đây, ngoài tính bảo mật (C), tính toàn vẹn (I) và tính sẵn sàng (A), còn có thêm 4 tính chất mới được chú trọng, đó là:

<h2 id="tính-xác-thực-authenticity">Tính xác thực (Authenticity)</h2>

Đảm bảo rằng các tổ chức hoặc cá nhân truy cập thông tin có quyền truy cập. Không cấp quyền truy cập cho người không mong đợi.

<h2 id="tính-đáng-tin-cậy-reliability">Tính đáng tin cậy (Reliability)</h2>

Đảm bảo dữ liệu và hệ thống hoạt động mà không có lỗi do con người hoặc lỗi trong chương trình (lỗi phần mềm) và thực hiện đúng ý đồ mong muốn.

<h2 id="tính-trách-nhiệm-accountability">Tính trách nhiệm (Accountability)</h2>

Theo dõi hoạt động của các công ty hoặc cá nhân. Điều này giúp xác định nguyên nhân và hành vi của người dùng trong trường hợp có mối đe dọa truy cập trái phép vào thông tin.

<h2 id="tính-không-thể-chối-bỏ-non-repudiation">Tính không thể chối bỏ (Non-repudiation)</h2>

Chứng minh rằng thông tin không thể bị phủ nhận sau này. Điều này đảm bảo rằng thông tin không bị sửa đổi hoặc chối bỏ sau khi được sử dụng. Việc ghi log hệ thống là một biện pháp phòng ngừa chống lại sự chối bỏ.

[Bài viết được tham khảo tại đây](https://3ac.vn/tam-giac-bao-mat-cia-tinh-bao-mat-tinh-toan-ven-tinh-san-sang-la-gi/#1_Tai_san_thong_tin_can_duoc_bao_mat)
