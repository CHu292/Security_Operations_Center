# Nhiệm vụ 2. Truyền dữ liệu được mã hóa qua kênh liên lạc

## 2.1. Mục đích và đặc điểm ngắn gọn của công việc:


**Mục đích công việc**:  
Nghiên cứu ảnh hưởng của các đặc tính kênh truyền thông đến chất lượng truyền tín hiệu khi sử dụng các phương pháp mã hóa vật lý và logic khác nhau trong mạng truyền dữ liệu số.

**Nhiệm vụ trong quá trình thực hiện**:
- Đối với thông điệp gốc và các phương pháp mã hóa được chỉ định, tiến hành nghiên cứu chất lượng truyền tín hiệu vật lý qua kênh truyền theo các yếu tố:
  - Mức độ nhiễu trong kênh.
  - Độ lệch đồng bộ giữa máy phát và máy thu.
  - Mức điện áp biên (được coi như mức suy hao tín hiệu).
- So sánh các phương pháp mã hóa đã sử dụng.
- Chọn và giải thích phương pháp tối ưu nhất để truyền thông điệp gốc qua kênh truyền thực tế, có xét đến suy hao, nhiễu và lệch đồng bộ.

---

## 2.2 Kiến thức lý thuyết


Trong trường hợp đơn giản nhất, dữ liệu nhị phân có thể được biểu diễn dưới dạng tín hiệu hình sin, trong đó:
- Phần dương của sóng sin tương ứng với giá trị nhị phân "1".
- Phần âm của sóng sin tương ứng với giá trị nhị phân "0".

Chu kỳ của sóng sin là:

$$
T = 2t,
$$

trong đó $$t$$ là độ dài khoảng thời gian bit và được liên kết với băng thông $$C$$ của kênh qua mối quan hệ:

$$
t = \frac{1}{C}.
$$

Do đó, tần số của tín hiệu hình sin:

$$
f = \frac{C}{2}.
$$

Truyền tín hiệu qua kênh truyền ở khoảng cách lớn có một số đặc điểm như sau:

1. **Suy hao tín hiệu**:  
   Khi tín hiệu lan truyền qua kênh, công suất của nó tại điểm nhận bị giảm đi đáng kể so với công suất ban đầu. Độ giảm công suất tỉ lệ thuận với độ dài của kênh truyền.

2. **Biến dạng tín hiệu**:  
   Do nhiễu từ thiết bị tạo kênh và các yếu tố gây nhiễu khác, tín hiệu nhận được thực tế bị biến dạng nhiều so với tín hiệu ban đầu. Điều này có thể dẫn đến việc tín hiệu bị mất hoặc đọc sai giá trị.

3. **Nhiễu nội tại**:  
   Các đặc tính kỹ thuật của môi trường truyền dẫn (dây dẫn) và thiết bị tạo kênh dẫn đến sự xuất hiện của tín hiệu nền (nhiễu). Để tránh việc tín hiệu nhiễu bị nhận diện sai thành tín hiệu thông tin, trong máy thu thường có một ngưỡng biên độ tín hiệu (gọi là mức điện áp biên), tương ứng với mức nhiễu tự nhiên. Nếu công suất tín hiệu nhận được nhỏ hơn mức nhiễu, tín hiệu sẽ không được phân biệt và bị mất.

4. **Yêu cầu đồng bộ hóa**:  
   Cần phải đồng bộ hóa máy phát và máy thu để tại máy thu có thể lấy mẫu tín hiệu chính xác tại trung tâm của khoảng thời gian bit. Điều này giúp đảm bảo độ chính xác cao nhất trong việc nhận dạng giá trị tín hiệu, vì tín hiệu hình sin đạt công suất lớn nhất tại trung tâm khoảng thời gian bit.  
   Tuy nhiên, mọi đồng hồ đều có sai số, dẫn đến sự khác biệt lớn dần theo thời gian giữa đồng hồ tại nút phát và nút thu. Điều này có thể dẫn đến việc bỏ sót hoặc lặp lại một số bit tại nút thu. Để giải quyết vấn đề đồng bộ, các mã tự đồng bộ hóa được sử dụng trong mạng máy tính.

**Mã hóa tín hiệu tiềm năng**:  
Tín hiệu lý tưởng biểu diễn các giá trị nhị phân "1" và "0" có dạng hình chữ nhật, là tín hiệu lý thuyết với phổ tần vô hạn. Theo lý thuyết Fourier, tín hiệu này có thể được biểu diễn dưới dạng chuỗi Fourier gồm:
- Thành phần tần số cơ bản $$f_0$$ (còn gọi là tần số sóng mang).
- Các thành phần bậc lẻ như $$f_1 = 3f_0, f_2 = 5f_0, f_3 = 7f_0, ...$$.

Biên độ của các thành phần giảm dần:

$$
A_1 = \frac{A_0}{3}, A_2 = \frac{A_0}{5}, A_3 = \frac{A_0}{7}, ...
$$

Phổ của tín hiệu tiềm năng yêu cầu băng thông kênh vô hạn để truyền dữ liệu một cách chất lượng.  

Trong thực tế, tín hiệu có phổ giới hạn, điều này phụ thuộc vào đặc tính của các cạnh tín hiệu (cạnh lên và cạnh xuống). Do đó, phổ của tín hiệu thực tế chiếm một khoảng từ gần 0 Hz đến một giá trị tần số nhất định. Trong các ứng dụng thực tế, phổ tín hiệu thường được giới hạn ở các giá trị $$f_3, f_5$$ hoặc $$f_7$$. Các thành phần tần số cao hơn $$f_7$$ thường có thể được bỏ qua vì chúng đóng góp rất ít vào tín hiệu tổng thể (biên độ dưới 11% so với biên độ tần số cơ bản).

Lưu ý: Khi truyền dữ liệu số, để khôi phục tín hiệu ban đầu, cần ít thành phần tần số hơn so với truyền dữ liệu tương tự. Trong công nghệ truyền dẫn số, chỉ cần tần số cơ bản để khôi phục tín hiệu. Tuy nhiên, để giảm lỗi, ít nhất cần có thành phần điều hòa bậc 1, mặc dù điều này làm tăng phổ tín hiệu gấp ba lần và do đó yêu cầu băng thông lớn hơn.

---

Dưới đây là bản dịch đúng và đầy đủ nội dung từ đoạn văn bản bạn vừa cung cấp:

---

## 2.3. Các giai đoạn thực hiện công việc và các phương án bài tập

### 2.3.1 Giai đoạn 1. Làm quen với chương trình để nghiên cứu chất lượng truyền tín hiệu vật lý qua kênh truyền 

Để nghiên cứu chất lượng truyền thông điệp gốc (tín hiệu) qua kênh truyền, chương trình **"Network Fourier 2"** được sử dụng. Chương trình này được phát triển bởi sinh viên Alexey Bezgodov.

**Mục đích của chương trình.**  
Chương trình **"Network Fourier 2"** được thiết kế để mô phỏng quá trình truyền thông điệp rời rạc với phổ tín hiệu bị giới hạn, có xét đến ảnh hưởng của nhiễu, độ lệch đồng bộ và mức điện áp biên. Thông điệp có thể được mã hóa bằng bốn phương pháp mã hóa vật lý và ba phương pháp mã hóa logic.

**Mô tả giao diện.**  
Hình 2.1 minh họa giao diện người dùng (cửa sổ) của chương trình.




**Hình 2.1. Giao diện người dùng**

Các thành phần của giao diện có ý nghĩa sau:

1. Nút thoát chương trình.
2. Nút hiển thị cửa sổ "về chương trình".
3. Đồ thị của thông điệp đã được mã hóa.
4. Đồ thị biểu diễn vật lý của tín hiệu, có xét đến phổ bị giới hạn và nhiễu.
5. Đồ thị của tín hiệu được nhận và giải mã.
6. Thanh trạng thái.
7. Trường chỉnh sửa để nhập thông điệp cần mã hóa.  
   Thông điệp có thể được nhập dưới dạng ký tự ASCII hoặc dưới dạng số hệ thập lục phân.  
   - Để nhập số hệ thập lục phân, trước thông điệp cần thêm ký tự "\\".  
     Ví dụ: "\\123AB" sẽ tương ứng với số thập lục phân **123AB**.  
   - Để nhập thông điệp văn bản bắt đầu bằng ký tự "\\", cần nhập hai ký tự "\\" liên tiếp.  
     Ví dụ: "\\\\xyz" sẽ được hiểu là thông điệp văn bản **"\\xyz"**.

8. Nút chuyển tiếp thông điệp.  
9. Bộ đếm điều hòa cao nhất trong chuỗi Fourier, phạm vi [0..255].  
10. Công tắc chuyển đổi phương pháp mã hóa logic.  
11. Bộ đếm thiết lập mức độ nhiễu, phạm vi [0..2].  
12. Bộ đếm thiết lập mức độ lệch đồng bộ, phạm vi [0..1].  
13. Bộ đếm thiết lập mức điện áp biên, phạm vi [0..1].  
14. Thông tin về thông điệp được truyền: dạng ASCII và dạng thập lục phân của tín hiệu, độ dài, tốc độ truyền (bit/s).  
15. Bộ đếm điều hòa thấp nhất trong chuỗi Fourier, phạm vi [0..255].  
16. Công tắc chuyển đổi phương pháp mã hóa vật lý.  
17. Thông tin về thông điệp nhận được: số lượng bit nhận được, số bit lỗi và tỷ lệ lỗi (phần trăm).  
18. Nút đặt lại thống kê.  
19. Công tắc kiểm tra cho phép hiển thị thông tin trên đồ thị biểu diễn vật lý của tín hiệu.

**Lưu ý**: Để tăng tốc độ thiết lập giá trị mong muốn trong các thành phần điều khiển "bộ đếm", có thể sử dụng các phím "phải/trái".


**Mô tả thuật toán.**  
Thông điệp được giả định là tuần hoàn, ví dụ, thông điệp ban đầu "ABCD" sẽ được biểu diễn trong thời gian như **"…ABCDABCDABCDABCD…"**.  
Ứng dụng liên tục thực hiện việc truyền thông điệp với độ dài bằng một chu kỳ khoảng 50 lần mỗi giây và thu thập thống kê về lỗi.

Chuỗi Fourier cho hàm tuần hoàn trên đoạn có độ dài $$ 2m $$ có dạng:

$$
f(x) = \frac{a_0}{2} + \sum_{k=1}^{\infty} \left( a_k \cos \frac{k \pi x}{m} + b_k \sin \frac{k \pi x}{m} \right),
$$

trong đó các hệ số của chuỗi được tính theo công thức:

$$
a_k = \frac{1}{m} \int_{-m}^{m} f(x) \cos \frac{k \pi x}{m} dx; \quad b_k = \frac{1}{m} \int_{-m}^{m} f(x) \sin \frac{k \pi x}{m} dx, \quad (k = 0, 1, 2, \ldots).
$$

Nhiễu được biểu diễn bởi một hàm có dạng:

$$
N(x, t) = \frac{a}{2} \sum_{i=1}^{\infty} \frac{\sin (i x + i^4 t)}{i},
$$

trong đó:
- $$ a $$: biên độ,
- $$ x $$: giá trị tín hiệu (điện áp),
- $$ t $$: thời gian hệ thống (điều này tạo ra sự dịch pha ngẫu nhiên trong mô phỏng nhiễu ngẫu nhiên).

**Mức độ lệch đồng bộ** $$ \Delta x $$:  
Điều này chỉ khoảng rộng của đoạn mà tại đó giá trị tín hiệu (điện áp) được lấy mẫu. Việc tính toán giá trị tín hiệu được thực hiện như sau:

$$
x = x_0 + rand(\Delta x) - \frac{\Delta x}{2},
$$

trong đó:
- $$ rand(a) $$: một hàm trả về giá trị thực ngẫu nhiên trong khoảng [0; $$ a $$].

**Thuật toán hoạt động của mô hình.**  
Khi mô phỏng việc truyền thông điệp qua kênh trong mô hình giả lập, các bước lặp lại sau được thực hiện mỗi 20 ms:

1. Kiểm tra các thành phần điều khiển và thiết lập các tham số ban đầu.
2. Hình thành tín hiệu chưa mã hóa từ thông điệp đã nhập.
3. Mã hóa logic thông điệp.
4. Mã hóa vật lý thông điệp.
5. Tạo chuỗi Fourier với phổ được chọn.
6. Thêm hàm nhiễu.
7. Lấy mẫu tín hiệu có xét đến mức điện áp biên và độ lệch đồng bộ.
8. Giải mã vật lý tín hiệu.
9. Giải mã logic thông điệp.
10. Đếm lỗi và thu thập thống kê.


**Quy trình làm việc với chương trình.**  
Để thực hiện các thí nghiệm bằng mô hình giả lập, cần hoàn thành các bước sau:

1. Thiết lập các tham số cần thiết cho việc truyền tín hiệu: phổ, mức độ nhiễu (Noise), mức độ lệch đồng bộ (Desync) và mức điện áp biên (Voltage).  
2. Đặt giới hạn phổ dưới (lowest) và trên (highest) của phổ tín hiệu truyền (Spectrum harmonics).  
3. Chọn phương pháp mã hóa (NRZ, RZ, Manchester).  
4. Nhập thông điệp cần truyền vào trường “Enter Message” và nhấn nút “Transmit!”.  
5. Đặt lại thống kê bằng cách nhấn nút “Reset stats”.  
6. Chờ cho đến khi hoàn thành số lần truyền yêu cầu (khoảng 100.000 bit) và ghi lại phần trăm lỗi (error %).  
7. Nếu cần, lặp lại các bước 1-6 cho các tham số và phương pháp mã hóa khác.

**Yêu cầu hệ thống.**  
Để mô hình giả lập hoạt động đúng, cần có ít nhất 32 MB RAM, cùng với hệ điều hành Win98, WinXP hoặc cao hơn. Card đồ họa cần hỗ trợ tăng tốc 3D để hiển thị nhanh các thành phần giao diện người dùng. Giao diện đồ họa người dùng được phát triển bằng thư viện OpenGL.

---

### 2.3.2 Giai đoạn 2. Xác định băng thông tối thiểu của kênh truyền

Băng thông tối thiểu cần thiết của kênh truyền để truyền thông điệp (tín hiệu nhị phân) một cách chất lượng được xác định cho một kênh lý tưởng, trong đó:
- Không có nhiễu và yếu tố gây méo làm biến dạng tín hiệu;
- Các nút phát và thu tín hiệu hoàn toàn đồng bộ, tức là không có sự lệch đồng bộ giữa chúng;
- Tín hiệu không bị suy hao và không cần thiết phải thiết lập mức điện áp biên để phân biệt tín hiệu 1 và 0.

Để thực hiện, cần thiết lập giá trị bằng 0 cho các mức: nhiễu (Noise), độ lệch đồng bộ (Desync) và điện áp biên (Voltage).  
Sau đó, nhập thông điệp gốc vào trường "Enter message". Thông điệp gốc được sử dụng là bốn byte đầu tiên trong họ của sinh viên thực hiện bài tập này, như đã chỉ định trong bài tập số 1.

**Chú ý.**  
Các ký tự của thông điệp gốc được nhập dưới dạng mã thập lục phân theo thứ tự ngược lại, tức là mã thập lục phân của byte thứ tư được nhập đầu tiên, sau đó là byte thứ ba, v.v. Trước thông điệp nhập, cần thêm ký tự "\\" để đánh dấu rằng đây là mã thập lục phân.

Bằng cách thay đổi lần lượt các giá trị phổ dưới và phổ trên của tín hiệu, xác định các giá trị giới hạn mà thông điệp được truyền mà không xảy ra lỗi. Các giá trị tương ứng này đại diện cho giới hạn dưới và giới hạn trên, xác định băng thông tối thiểu của kênh truyền.


---

### 2.3.3 Giai đoạn 3. Xác định các mức tối đa cho phép của nhiễu, lệch đồng bộ và suy hao

Ở giai đoạn này, lần lượt xác định các mức tối đa cho phép của nhiễu, lệch đồng bộ và suy hao mà vẫn đảm bảo chất lượng truyền thông điệp, tức là không xuất hiện lỗi.  

Trước tiên, thay đổi mức độ nhiễu (Noise) và xác định mức tối đa cho phép của nhiễu mà thông điệp gốc vẫn được truyền không lỗi. Trong trường hợp này, các giá trị của lệch đồng bộ và điện áp biên phải bằng 0.  

Sau đó, thiết lập mức nhiễu bằng 0 và thay đổi mức lệch đồng bộ (Desync), xác định mức tối đa cho phép của lệch đồng bộ mà thông điệp gốc vẫn được nhận không lỗi.  

Cuối cùng, thiết lập mức lệch đồng bộ bằng 0 và thay đổi mức điện áp biên (Voltage), xác định mức tối đa cho phép của điện áp biên mà thông điệp gốc vẫn được nhận không lỗi.

Dưới đây là bản dịch nội dung từ hình ảnh bạn cung cấp:

---

### 2.3.4 Giai đoạn 4. Đánh giá độ chính xác của việc nhận dạng tín hiệu ở phía thu

Ở giai đoạn này, xác định phần trăm lỗi khi truyền thông điệp với các giá trị mức nhiễu, lệch đồng bộ, điện áp biên và băng thông tối thiểu của kênh truyền đã tìm được ở giai đoạn trước.  

Thiết lập các giá trị tối đa cho phép của nhiễu, lệch đồng bộ và điện áp biên đã tìm được ở giai đoạn trước và xác định phần trăm lỗi ở phía thu của kênh truyền.  

**Lưu ý.** Giai đoạn 2–4 được thực hiện theo các phương pháp mã hóa vật lý và logic do giảng viên chỉ định. Các giá trị thu được được ghi vào bảng kết quả.


---

### 2.3.5 Giai đoạn 5. Xác định các giá trị mức nhiễu, lệch đồng bộ và điện áp biên cho kênh truyền thực tế  

Tính toán các giá trị mức nhiễu, lệch đồng bộ và điện áp biên cho kênh truyền thực tế dưới dạng giá trị trung bình trên tất cả các phương pháp mã hóa đã xem xét.



---

### 2.3.6 Giai đoạn 6. Xác định băng thông cần thiết của kênh truyền thực tế

Băng thông cần thiết của kênh truyền thực tế được xác định theo điều kiện rằng việc truyền thông điệp phải diễn ra mà không bị mất dữ liệu với các mức nhiễu, lệch đồng bộ và điện áp biên đã tính toán được cho tất cả các phương pháp mã hóa đã xem xét.

- Thiết lập các giá trị đã tính toán của mức nhiễu, lệch đồng bộ và điện áp biên cho kênh truyền thực tế.
- Lần lượt thay đổi giá trị số thứ tự của điều hòa phổ dưới từ 0 và điều hòa phổ trên từ giá trị tối đa (255) trong phổ tín hiệu, xác định các giới hạn mà thông điệp được truyền không lỗi trên kênh truyền thực tế. Các giá trị tần số tương ứng xác định băng thông cần thiết của kênh truyền cho phương pháp mã hóa đã xem xét.

**Lưu ý.** Giai đoạn này được thực hiện cho tất cả các phương pháp mã hóa vật lý và logic đã xem xét. Các giá trị thu được được ghi vào bảng kết quả.


---

### 2.3.7 Giai đoạn 7. Phân tích kết quả thu được và lựa chọn phương pháp mã hóa tốt nhất cho thông điệp gốc 

Phân tích các kết quả đã thu được và lựa chọn phương pháp mã hóa tốt nhất cho thông điệp gốc từ tất cả các phương pháp đã xem xét, đồng thời đưa ra lý do giải thích cho sự lựa chọn này.

Dưới đây là bản dịch nội dung từ hình ảnh bạn cung cấp:

---

## 2.4. Trình tự thực hiện công việc

1. Làm quen với yêu cầu bài tập.  
2. Làm quen với chương trình nghiên cứu chất lượng truyền tín hiệu vật lý qua kênh truyền (giai đoạn 1).  
3. Sử dụng chương trình này để thực hiện nghiên cứu theo các giai đoạn 2–6 và ghi kết quả vào bảng 2.1.  
4. Thực hiện phân tích so sánh các phương pháp mã hóa đã xem xét và chọn phương pháp tốt nhất để truyền thông điệp gốc (giai đoạn 7).  
5. Chuẩn bị báo cáo về công việc đã thực hiện.


---

## 2.5. Yêu cầu đối với nội dung báo cáo

1. Tóm tắt ngắn gọn yêu cầu của bài tập.  
2. Thông điệp gốc và cách biểu diễn của nó dưới dạng mã thập lục phân.  
3. Ảnh chụp màn hình từ chương trình "Network Fourier 2", trong đó cần hiển thị thông điệp được truyền và các đặc tính của kênh truyền thực tế.  
4. Kết quả nghiên cứu các phương pháp mã hóa đã xem xét, được trình bày dưới dạng bảng 2.1, phân tích các kết quả thu được và lựa chọn phương pháp mã hóa tốt nhất để truyền thông điệp gốc, kèm theo giải thích.  
5. Kết luận ngắn gọn với lý giải cho phương pháp mã hóa logic và vật lý tốt nhất để truyền thông điệp gốc.  
6. Danh mục tài liệu tham khảo đã sử dụng.



## 2.6. Câu hỏi kiểm tra để tự ôn tập

Khi chuẩn bị bảo vệ bài tập số 2, cần tham khảo danh sách câu hỏi và bài tập mẫu sau đây để tự luyện tập:

1. Lợi ích của việc tính suy hao tín hiệu bằng dB là gì?  
2. Công suất tín hiệu sẽ giảm bao nhiêu lần trên khoảng cách 100 m nếu suy hao là \( d = 10 \, \text{dB/km} \)?  
3. Vẽ đồ thị tín hiệu điều hòa và biểu diễn các thông số của nó trên đồ thị. Ghi công thức mô tả tín hiệu điều hòa.  
4. Ghi và giải thích biểu diễn của hàm dữ liệu liên tục dưới dạng chuỗi Fourier.  
5. Định nghĩa tín hiệu (hàm) với phổ bị giới hạn.  
6. Phổ tần số nào đặc trưng cho tín hiệu số?  
7. Trong điều kiện nào đảm bảo truyền tín hiệu chất lượng?  
8. Mô tả trên đồ thị các giới hạn phổ của đường truyền dẫn. Kênh điện thoại có băng thông như thế nào (đường dây tương tự)?  
9. Tín hiệu số được truyền qua kênh như thế nào mà không cần điều chế (trong băng thông gốc)?  
10. Làm thế nào để truyền tín hiệu qua các kênh tốc độ cao với băng thông bị giới hạn nghiêm ngặt?  
11. Điều chế là gì và nó dùng để làm gì?  
12. Điều khiển (manipulation) khác gì so với điều chế?  
13. Giải thích nguyên lý điều chế biên độ, điều chế tần số và điều chế pha.  
14. ICM (PCM) là gì?  
15. Phân biệt giữa AIM (PCM điều chế biên độ) và ICM.  
16. Làm thế nào để đảm bảo tốc độ truyền dữ liệu 64 kbit/s (56 kbit/s) trong ICM?  
17. Giải thích nguyên lý của ICM vi sai thích ứng (adaptive differential PCM).  
18. Khác biệt giữa tín hiệu đường truyền và tín hiệu ban đầu là gì?  
19. Liệt kê các đặc tính của kênh số.  
20. Băng thông kênh phụ thuộc vào yếu tố nào?  
21. Tính băng thông tối đa có thể của kênh (Mbit/s) với băng thông là 20 MHz, tỉ lệ công suất tín hiệu trên công suất nhiễu là 3.  
22. Phân biệt băng thông với tốc độ truyền dữ liệu.  
23. Tốc độ truyền dữ liệu nào đặc trưng cho kênh điện thoại?  
24. Các phương pháp ghép kênh nào được sử dụng trong mạng máy tính?  
25. Quá trình biểu diễn dữ liệu liên tục thành tín hiệu vật lý gọi là gì?  
26. Quá trình biểu diễn dữ liệu số thành tín hiệu vật lý gọi là gì?  
27. Phổ của tín hiệu điều chế phụ thuộc vào yếu tố nào?  
28. Liệt kê yêu cầu đối với phương pháp mã hóa số.  
29. Tốc độ bit liên quan như thế nào đến phổ tín hiệu điều chế?  
30. Vấn đề đồng bộ hóa trong truyền tín hiệu số là gì?  
31. Mã tự đồng bộ hóa là gì?  
32. Phương pháp mã hóa nào giải quyết vấn đề đồng bộ hóa?  
33. Chi phí thực hiện phương pháp mã hóa phụ thuộc vào yếu tố nào?  
34. Thành phần phổ tín hiệu không đổi là gì và tại sao nó không mong muốn?  
35. Phương pháp mã hóa nào có thành phần phổ không đổi?  
36. Tại sao trong mạng viễn thông, việc đồng bộ hóa không sử dụng sơ đồ riêng lẻ?  
37. Tại sao vấn đề đồng bộ hóa trong mạng viễn thông khó hơn so với trao đổi dữ liệu giữa máy tính và máy in?

