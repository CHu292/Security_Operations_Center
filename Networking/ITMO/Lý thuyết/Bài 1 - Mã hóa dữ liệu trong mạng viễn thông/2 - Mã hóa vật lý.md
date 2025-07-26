
# 2. Phương pháp mã hóa vật lý
## 2.1 NRZ - Non Return to Zero

Phương pháp mã hóa nhị phân đơn giản và rõ ràng nhất là phương pháp mã hóa tiềm năng không quay về mức 0 – NRZ (Non Return to Zero), trong đó bit "1" tương ứng với mức điện thế cao, còn bit "0" tương ứng với mức điện thế thấp
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/ITMO/K%E1%BB%B3%205/M%E1%BA%A1ng%20m%C3%A1y%20t%C3%ADnh/ITMO/image/1/NRZ.png" alt="Alt text" width="500">
</p>
- Ví dụ: Trong chuỗi "1010", mã NRZ sẽ giữ mức điện áp cao cho "1", chuyển xuống thấp cho "0", rồi lại chuyển lên cao cho "1", và cuối cùng xuống thấp cho "0".


Để xác định giới hạn tần số trên, cần tìm thành phần tần số cao nhất trong phổ của thông điệp được truyền. Trong mã NRZ, thành phần tần số cao nhất xuất hiện khi truyền các giá trị 0 và 1 luân phiên, trong đó chu kỳ của sóng sin (tín hiệu điều hòa) được sử dụng để truyền tín hiệu hình chữ nhật 0 và 1 sẽ bằng gấp đôi độ dài của khoảng thời gian bit $$T$$:

$$
T = 2T_b
$$

Trong đó $$T_b$$ được xác định là giá trị nghịch đảo của tốc độ truyền dữ liệu (băng thông kênh):

$$
T_b = \frac{1}{C}
$$

Từ đó, giới hạn tần số trên sẽ bằng:

$$
f_{\text{top}} = \frac{C}{2}
$$

Với băng thông kênh truyền $$C$$, tần số điều hòa cơ bản sẽ bằng:

$$
f_0 = \frac{C}{2}
$$

Trong trường hợp mã hóa bất kỳ thông điệp nào bằng phương pháp NRZ, tần số lớn nhất (giới hạn trên) sẽ đạt được khi truyền các giá trị 0 và 1 luân phiên, còn tần số nhỏ nhất (giới hạn dưới) sẽ đạt được khi truyền các chuỗi dài (vô hạn) các giá trị 0 hoặc 1, làm cho tần số giới hạn dưới gần bằng 0:

$$
f_{\text{lower}} \approx 0
$$

Do đó, trong trường hợp lý tưởng, độ rộng phổ sẽ bằng:

$$
\Delta f = f_{\text{top}} - f_{\text{lower}} = \frac{C}{2}
$$

Mặt khác, khi truyền thông điệp cụ thể, tần số giới hạn dưới luôn lớn hơn 0 và phụ thuộc vào độ dài tối đa của chuỗi các giá trị 0 hoặc 1. Trong thông điệp được mã hóa theo phương pháp NRZ, như minh họa trên hình 1.1a, thành phần tần số thấp được tạo ra khi truyền 4 số 1 liên tiếp và 4 số 0 liên tiếp. Chu kỳ của tín hiệu hình sin khi truyền những chuỗi này sẽ bằng 8 khoảng thời gian bit, và giới hạn tần số dưới sẽ bằng:

$$
f_{\text{lower}} = \frac{C}{8}
$$

Do đó, độ rộng phổ khi truyền thông điệp này bằng mã NRZ sẽ bằng:

$$
\Delta f = f_{\text{top}} - f_{\text{lower}} = \frac{C}{2} - \frac{C}{8} = \frac{3C}{8}
$$

Lưu ý rằng các giá trị tần số giới hạn dưới và phổ thu được chỉ đúng cho thông điệp cụ thể này. Khi truyền các thông điệp khác, các giá trị này sẽ khác nhau.

Vì vậy, có thể khẳng định rằng khi mã hóa theo phương pháp NRZ, độ rộng phổ của tín hiệu sẽ nằm trong khoảng:

$$
f_{\text{lower}} \leq f_{\text{signal}} \leq f_{\text{lower}}
$$

Giá trị trung bình của tần số thông điệp được truyền sẽ nằm trong khoảng:

$$
f_{\text{average}} = \frac{f_{\text{lower}} + f_{\text{top}}}{2}
$$

Nó cho biết những tần số nào (cao hay thấp) chiếm ưu thế trong phổ của tín hiệu được truyền.

Để tính giá trị trung bình của tần số thông điệp được truyền, cần xác định tần số tương ứng cho từng khoảng thời gian bit, cộng chúng lại và chia cho tổng số khoảng thời gian bit. Trong trường hợp của chúng ta, tần số điều hòa cơ bản $$f_0$$ tương ứng với 7 khoảng thời gian bit, 4 khoảng thời gian bit tương ứng với tần số thấp hơn gấp đôi so với tần số điều hòa cơ bản, tức là:

$$
f_{\text{lower}} = \frac{f_0}{2}
$$

và 8 khoảng thời gian bit tương ứng với tần số:

$$
f_{\text{lower}} = \frac{f_0}{4}
$$

Khi đó, tần số trung bình của thông điệp này sẽ bằng:

$$
f_{\text{average}} = \frac{1}{19} \left( 7f_0 + 4 \cdot \frac{f_0}{2} + 8 \cdot \frac{f_0}{4} \right) = 0.58 f_0 \approx 0.58 C
$$

Vì vậy, phổ của tín hiệu không có sự khác biệt lớn giữa tần số thấp và tần số cao:

$$
f_{\text{lower}} < \frac{f_{\text{average}}}{2}
$$

Để truyền tín hiệu nhị phân qua kênh truyền thực và để nhận dạng chúng với số lỗi tối thiểu, lý tưởng nhất là tín hiệu ở phía phát cần được định dạng gần giống dạng sóng hình chữ nhật. Tuy nhiên, phổ của các tín hiệu như vậy quá rộng. Trong khi đó, để nhận dạng tín hiệu chất lượng ở phía nhận khi truyền các giá trị luân phiên 0 và 1, chỉ cần tín hiệu chứa 4 điều hòa đầu tiên (vì các điều hòa có tần số cao hơn ít ảnh hưởng đến tín hiệu tổng) với các tần số:

$$
f_{\text{top}} = 7f_0
$$

Do đó, băng thông cần thiết để truyền thông điệp này bằng mã NRZ sẽ bằng:

$$
\Delta f = 6C/4
$$

Ưu điểm của mã NRZ là:

- Đơn giản và chi phí thấp do chỉ có hai mức điện thế.
- Phổ tín hiệu hẹp hơn so với các phương pháp mã hóa khác: $$\Delta f = 0.5C$$, trong đó $$C$$ là tốc độ truyền dữ liệu [bit/s].

Tuy nhiên, mã NRZ không được sử dụng trong các mạng máy tính do các nhược điểm sau:

- Thiếu đồng bộ hóa, điều này có thể dẫn đến mất đồng bộ giữa đồng hồ của bộ nhận và bộ phát khi truyền chuỗi dài các giá trị 0 hoặc 1.
- Không thể sử dụng trong các kênh truyền điện có các mạch cách ly bằng điện giữa bộ phát và bộ nhận.

Tuy nhiên, các biến thể của mã NRZ được sử dụng, trong đó thành phần cố định được loại bỏ bằng các phương pháp mã hóa logic, cụ thể là mã hóa dư thừa.

## 2.2 Return to Zero (RZ) Mã xung lưỡng cực

Bit "1" được biểu diễn bằng một xung có cực dương (tín hiệu điện áp cao), nhưng chỉ tồn tại trong nửa đầu của khoảng thời gian bit. Trong nửa sau, tín hiệu trở về mức không.
Bit "0" được biểu diễn bằng một xung có cực âm (tín hiệu điện áp thấp), và cũng chỉ tồn tại trong nửa đầu của khoảng thời gian bit, sau đó cũng trở về mức không.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/ITMO/K%E1%BB%B3%205/M%E1%BA%A1ng%20m%C3%A1y%20t%C3%ADnh/ITMO/image/1/RZ.png" alt="Alt text" width="500">
</p>

Mỗi xung kéo dài một nửa khoảng thời gian bit. Giữa khoảng thời gian bit, tín hiệu quay trở lại mức 0.

**Ưu điểm của mã RZ bao gồm:**

- Có khả năng tự đồng bộ: Tín hiệu để đồng bộ hóa đồng hồ của bộ nhận là sự quay về mức 0 giữa mỗi khoảng thời gian bit.
- Không có thành phần cố định.

**Nhược điểm của mã RZ là:**

- Có ba mức tín hiệu, điều này đòi hỏi tăng công suất của bộ phát để đảm bảo độ tin cậy của việc nhận tín hiệu, dẫn đến tăng chi phí thực hiện.
- Phổ tín hiệu rộng hơn so với các mã tiềm năng: Khi truyền chuỗi các bit "0" hoặc "1", giới hạn tần số trên sẽ là $$f_{\text{top}} = C$$ Hz, và giới hạn tần số dưới khi truyền các bit "0" và "1" xen kẽ sẽ là $$f_{\text{ниж}} = \frac{C}{4}$$, điều này làm tăng phổ tín hiệu lên 1.5 lần so với mã NRZ:

$$
S = f_{\text{top}} - f_{\text{lower}} = 0.75C
$$

Do những nhược điểm này, mã xung lưỡng cực "RZ" hiếm khi được sử dụng.

## 2.3. Alternate Mark Inversion - Mã lưỡng cực với đảo cực xen kẽ (AMI)

Mã lưỡng cực với đảo cực xen kẽ (Alternate Mark Inversion, AMI) là một biến thể của phương pháp mã hóa RZ. Trong AMI cũng sử dụng ba mức điện thế: dương, trung tính và âm. Bit "0" nhị phân được mã hóa bằng điện thế trung tính, còn bit "1" nhị phân được mã hóa bằng điện thế dương hoặc âm, trong đó điện thế của bit "1" kế tiếp luôn ngược với điện thế của bit "1" trước đó.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/ITMO/K%E1%BB%B3%205/M%E1%BA%A1ng%20m%C3%A1y%20t%C3%ADnh/ITMO/image/1/AMI.png" alt="Alt text" width="500">
</p>

**Các ưu điểm chính của phương pháp AMI bao gồm:**

- Không có thành phần cố định, và có khả năng đồng bộ hóa giữa bộ phát và bộ nhận khi truyền các chuỗi dài bit "1", vì trong trường hợp này tín hiệu sẽ là một chuỗi các xung có cực tính đối lập nhau.
- Phổ tín hiệu khi mã hóa AMI nói chung nhỏ hơn so với mã hóa RZ, điều này giúp tăng dung lượng kênh truyền thông. Đặc biệt, khi truyền các chuỗi bit "1" và "0" luân phiên, giới hạn tần số trên sẽ giống như khi truyền các bit luân phiên trong mã NRZ, với giới hạn tần số trên là $$f_{\text{top}} = \frac{C}{2}$$ Hz, và độ rộng phổ tín hiệu là $$S < \frac{C}{2}$$.
- Khả năng phát hiện các tín hiệu lỗi (bị cấm) khi có sự vi phạm thứ tự đảo cực của các tín hiệu trong quá trình truyền các bit "1", ví dụ như khi sau một bit "1" xuất hiện một bit "1" cùng cực tính.

**Nhược điểm của phương pháp AMI bao gồm:**

- Sự tồn tại của ba mức tín hiệu yêu cầu tăng công suất của bộ phát, điều này dĩ nhiên làm tăng chi phí.
- Khi truyền các chuỗi dài bit "0", trong tín hiệu xuất hiện thành phần cố định, dịch chuyển phổ tín hiệu vào dải tần số thấp.
## 2.4 NRZ-I (Non - Return to Zero Inverted)
Mã tiềm năng với đảo chiều tại bit "1" (NRZI - Non-Return to Zero Inverted) là một biến thể của mã NRZ (Non-Return to Zero). Trong phương pháp mã hóa này, chỉ có hai mức điện áp được sử dụng, và tín hiệu được thay đổi dựa trên bit "1", cụ thể:
- Khi truyền một bit "0", mức điện áp không thay đổi. Nghĩa là tín hiệu sẽ giữ nguyên trạng thái điện áp từ bit trước đó.
- Khi truyền một bit "1", mức điện áp sẽ đảo chiều. Nếu trước đó tín hiệu ở mức cao, nó sẽ chuyển xuống mức thấp, và ngược lại.
  
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/ITMO/K%E1%BB%B3%205/M%E1%BA%A1ng%20m%C3%A1y%20t%C3%ADnh/ITMO/image/1/NRZI.png" alt="Alt text" width="500">
</p>

**Ưu điểm của mã NRZI:**

- Sử dụng hai mức điện áp: Điều này giúp mã NRZI đơn giản hơn trong việc thực hiện so với các phương pháp yêu cầu ba mức điện áp (như mã AMI).
- Hỗ trợ đồng bộ hóa: Mã NRZI cải thiện đồng bộ hóa hơn so với NRZ thông thường, đặc biệt khi có sự xuất hiện của nhiều bit "1". Mỗi lần truyền bit "1", tín hiệu sẽ đảo chiều, giúp dễ dàng nhận biết khi nào bit "1" được truyền.

**Nhược điểm của mã NRZI:**

- Không xử lý tốt các chuỗi dài của bit "0": Giống như NRZ, mã NRZI không thay đổi điện áp khi truyền chuỗi dài các bit "0", điều này có thể gây ra lỗi đồng bộ hóa nếu không có sự thay đổi tín hiệu trong một thời gian dài.

  ## 2.5. Mã Manchester

Mã Manchester đã tìm thấy ứng dụng rộng rãi trong các mạng cục bộ Ethernet. Để mã hóa, hai mức tín hiệu được sử dụng, trong đó để đại diện cho các số nhị phân 1 và 0, có sự chuyển đổi tín hiệu ở giữa mỗi khoảng thời gian bit:

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/ITMO/K%E1%BB%B3%205/M%E1%BA%A1ng%20m%C3%A1y%20t%C3%ADnh/ITMO/image/1/Manchester.png" alt="Alt text" width="500">
</p>

- Bit "1" nhị phân tương ứng với sự chuyển từ mức tín hiệu cao sang mức tín hiệu thấp;
- Bit "0" nhị phân tương ứng với sự chuyển từ mức tín hiệu thấp sang mức tín hiệu cao.

Trong trường hợp có một chuỗi dài các số 1 hoặc 0, ở đầu mỗi khoảng thời gian bit sẽ xảy ra một chuyển đổi tín hiệu bổ sung.

**Ưu điểm của mã Manchester bao gồm:**

- Tự đồng bộ hóa: Sự thay đổi tín hiệu ở giữa mỗi khoảng thời gian bit có thể được sử dụng làm tín hiệu để đồng bộ hóa giữa bộ nhận và bộ phát.
- Phổ tín hiệu nhỏ hơn so với mã lưỡng cực (AMI) trong trung bình là 1,5 lần: Giới hạn tần số trên khi truyền chuỗi các số 1 hoặc 0 là \( f_{\text{верх}} = C \) Hz, và giới hạn tần số dưới khi truyền các số 1 và 0 xen kẽ là $$f_{\text{top}} = \frac{C}{2}$$, do đó độ rộng phổ là $$S = f_{\text{top}} - f_{\text{lower}} = \frac{C}{2}$$).
- Chỉ có hai mức điện thế;
- Không có thành phần cố định.

**Nhược điểm của mã Manchester là:**

- Phổ tín hiệu rộng hơn so với mã NRZ và AMI.

## 2.6 Manchester vi sai
Mã Manchester vi sai là một biến thể của mã Manchester, được sử dụng trong các mạng như Token Ring. Phương pháp mã hóa này vẫn sử dụng hai mức điện áp và có sự chuyển đổi tín hiệu trong mỗi khoảng bit, nhưng nó khác so với mã Manchester chuẩn ở cách mã hóa các bit:

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/ITMO/K%E1%BB%B3%205/M%E1%BA%A1ng%20m%C3%A1y%20t%C3%ADnh/ITMO/image/1/Manchester_vi_sai.png" alt="Alt text" width="500">
</p>

- Bit "0" được mã hóa bằng cách chuyển đổi điện áp ở đầu khoảng bit (không phải giữa khoảng bit như trong mã Manchester chuẩn).
- Bit "1" được mã hóa bằng cách giữ nguyên mức điện áp từ bit trước đó, tức là không có sự thay đổi ở đầu khoảng bit.
Dù vậy, trong cả hai trường hợp, mã Manchester vi sai luôn có sự chuyển đổi tín hiệu ở giữa mỗi khoảng bit để hỗ trợ đồng bộ hóa tín hiệu giữa máy phát và máy thu.

### 2.6.1 Chuyển đổi tín hiệu ở giữa mỗi khoảng bit
- Trong mã Manchester vi sai, ở giữa mỗi khoảng bit luôn có sự chuyển đổi từ mức điện áp này sang mức điện áp khác (từ dương sang âm hoặc ngược lại). Điều này đảm bảo rằng tín hiệu có tính đồng bộ hóa cao, giúp máy thu dễ dàng xác định ranh giới của các bit và giải mã chính xác dữ liệu.
- Việc chuyển đổi tín hiệu ở giữa mỗi khoảng bit là một đặc trưng quan trọng của mã Manchester nói chung (cả vi sai và chuẩn), vì nó giúp duy trì sự đồng bộ hóa tín hiệu giữa máy phát và máy thu, ngăn chặn sự mất tín hiệu khi truyền các chuỗi dài bit giống nhau.
### 2.6.2 Ký hiệu "J" và "K"
- Ngoài các bit "0" và "1", mã Manchester vi sai còn có thể truyền các ký hiệu đặc biệt “J” và “K”. Đây là các ký hiệu không tuân theo quy tắc chuyển đổi tín hiệu ở giữa mỗi khoảng bit:
“J” và “K” là các ký hiệu mà không có sự thay đổi tín hiệu ở giữa khoảng bit.
- Chúng thường được sử dụng để đánh dấu điểm bắt đầu và kết thúc của một khung (frame) dữ liệu. Điều này rất quan trọng trong truyền thông, vì máy thu cần biết khi nào bắt đầu và khi nào kết thúc một khung dữ liệu.

  **Ưu điểm**
  
- Khả năng chịu lỗi tốt hơn:
Điểm mạnh chính của mã Manchester vi sai so với mã Manchester chuẩn là khả năng chống lại sự đảo ngược tín hiệu. Nếu tín hiệu bị đảo ngược toàn bộ (tức là điện áp cao trở thành điện áp thấp và ngược lại), mã Manchester vi sai vẫn có thể giải mã chính xác. Điều này giúp nó có khả năng chịu lỗi cao hơn trong môi trường truyền tín hiệu không ổn định.
- Tự đồng bộ hóa:
Cũng giống như mã Manchester chuẩn, mã Manchester vi sai có sự thay đổi tín hiệu ở giữa mỗi khoảng bit, giúp đảm bảo tín hiệu có tính tự đồng bộ hóa giữa máy phát và máy thu.

**Nhược điểm**

- Phổ tín hiệu rộng:
Giống với mã Manchester chuẩn, mã Manchester vi sai cũng yêu cầu băng thông lớn để truyền tín hiệu, vì nó tạo ra sự chuyển đổi tín hiệu liên tục trong suốt quá trình truyền.
- Độ phức tạp cao hơn:
Mặc dù mã Manchester vi sai có ưu điểm về khả năng chống lỗi, nhưng nó yêu cầu phần cứng phức tạp hơn để thực hiện mã hóa và giải mã so với các phương pháp đơn giản hơn như NRZ hoặc AMI.

## 2.7 MLT-3 (Multi-Level Transmit - 3)  -  Mã hóa truyền 3 mức
MLT-3 (Multi-Level Transmit - 3) là một phương pháp mã hóa tín hiệu ba mức điện áp, được sử dụng trong các hệ thống truyền dữ liệu tốc độ cao, như Fast Ethernet (100BASE-TX). Mã hóa này sử dụng ba mức điện áp khác nhau: dương, không và âm, để truyền tín hiệu số.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/ITMO/K%E1%BB%B3%205/M%E1%BA%A1ng%20m%C3%A1y%20t%C3%ADnh/ITMO/image/1/MLT-3.png" alt="Alt text" width="500">
</p>

**Nguyên tắc hoạt động của mã MLT-3:**

Trong MLT-3, tín hiệu không thay đổi giá trị với mỗi bit dữ liệu "1", mà thay đổi theo một chu kỳ gồm bốn bước:
- Từ mức 0 lên mức dương.
- Từ mức dương xuống mức 0.
- Từ mức 0 xuống mức âm.
- Từ mức âm lên mức 0.
Mỗi lần có bit "1" trong chuỗi dữ liệu, tín hiệu sẽ chuyển sang bước tiếp theo trong chu kỳ này. Nếu bit "0" được truyền, tín hiệu sẽ giữ nguyên ở mức hiện tại mà không thay đổi.

**Những nhược điểm của phương pháp mã hóa này bao gồm:**

- Thiếu khả năng tự đồng bộ;
- Có ba mức tín hiệu;
- Sự tồn tại của thành phần cố định trong tín hiệu khi truyền chuỗi dài các bit "0"

## 2.7 PAM-5 (Pulse Amplitude Modulation - 5 level) - Mã năm mức PAM-5
PAM-5 (Pulse Amplitude Modulation - 5 level) là một phương pháp mã hóa tín hiệu dựa trên điều chế biên độ xung với năm mức điện áp khác nhau, được sử dụng trong các hệ thống truyền dẫn tốc độ cao như Gigabit Ethernet (1000BASE-T). Mã PAM-5 sử dụng các mức điện áp khác nhau để đại diện cho các giá trị nhị phân, trong đó mỗi mức điện áp có thể biểu diễn nhiều bit thông tin hơn so với các mã nhị phân thông thường.

**Nguyên tắc hoạt động của mã PAM-5:**

Trong PAM-5, tín hiệu có thể có năm mức điện áp: -2, -1, 0, +1, +2. Mỗi mức điện áp này đại diện cho một tổ hợp bit nhị phân nhất định:
Mức -2 có thể đại diện cho một tổ hợp bit (ví dụ: 00).
Mức -1 đại diện cho tổ hợp bit khác (ví dụ: 01).
Mức 0 cho tổ hợp khác (ví dụ: 10).
Mức +1 và +2 đại diện cho các tổ hợp khác nhau (ví dụ: 11).
Nhờ việc sử dụng năm mức điện áp, mã PAM-5 có khả năng truyền nhiều bit thông tin hơn trong mỗi xung tín hiệu so với các mã nhị phân chỉ sử dụng hai mức (0 và 1).

**Ưu điểm của mã PAM-5:**

Tăng hiệu quả truyền dữ liệu:
Với năm mức điện áp, mã PAM-5 có thể mã hóa nhiều bit thông tin hơn trong mỗi khoảng thời gian tín hiệu, điều này giúp tăng hiệu suất truyền dữ liệu. Ví dụ, thay vì chỉ truyền một bit tại mỗi xung như trong mã nhị phân, PAM-5 có thể truyền nhiều bit hơn, giúp nâng cao tốc độ truyền.
Sử dụng hiệu quả băng thông:
Bằng cách truyền nhiều bit thông tin hơn trong mỗi xung, PAM-5 sử dụng băng thông hiệu quả hơn. Điều này rất hữu ích trong các hệ thống tốc độ cao như Gigabit Ethernet, nơi cần tối ưu hóa việc sử dụng băng thông để đạt được tốc độ truyền cao.

**Nhược điểm của mã PAM-5:**

Yêu cầu chất lượng kênh truyền tốt:
Vì mã PAM-5 sử dụng nhiều mức điện áp, tín hiệu có thể bị ảnh hưởng bởi nhiễu và suy hao tín hiệu trong quá trình truyền qua kênh. Điều này đòi hỏi kênh truyền phải có chất lượng tốt để đảm bảo các mức điện áp khác nhau có thể được nhận dạng chính xác.
Phức tạp trong giải mã:
So với các mã nhị phân, PAM-5 yêu cầu thiết bị thu phải phân biệt được năm mức điện áp khác nhau, điều này làm tăng độ phức tạp trong quá trình giải mã tín hiệu. Điều này cũng đòi hỏi các bộ xử lý tín hiệu phức tạp hơn.
