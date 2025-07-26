# 3. Mã hóa logic
Mã hóa logic được sử dụng để cải thiện mã tiềm năng AMI, NRZI hoặc MLT-3 bằng cách loại bỏ các chuỗi dài gồm các số 1 hoặc 0 dẫn đến điện thế không đổi. Mã hóa logic bao gồm mã hóa dự phòng và xáo trộn.
## 3.1. Mã hóa dư thừa

Trong mã hóa dư thừa, mã nhị phân ban đầu được biểu diễn dưới dạng các chuỗi nhiều bit, mỗi chuỗi được thay thế bằng một chuỗi mới, có số bit nhiều hơn chuỗi ban đầu.

Các phương pháp mã hóa dư thừa bao gồm: 4B/5B, 5B/6B, 8B/10B, 64B/66B.

Chữ "B" trong tên mã chỉ ra rằng tín hiệu cơ bản có 2 trạng thái (binary – nhị phân), và các con số cho biết số lượng bit trong một chuỗi mã ban đầu và mã kết quả tương ứng. Ví dụ, phương pháp 4B/5B có nghĩa là mỗi 4 bit trong mã ban đầu được thay thế bằng 5 bit trong mã kết quả. Để thực hiện điều này, một bảng mã hóa (bảng 1.1) được sử dụng để xác định sự tương ứng giữa các chuỗi bốn bit ban đầu và các chuỗi năm bit kết quả.

Kết quả của sự thay thế này là số lượng chuỗi mã kết quả nhiều hơn số lượng chuỗi ban đầu. Trong mã 4B/5B, số chuỗi kết quả là $$2^5 = 32$$, trong khi số chuỗi ban đầu là $$2^4 = 16$$. Do đó, số lượng mã dư thừa (bị cấm) là: $$32 - 16 = 16$$. Sự xuất hiện của các ký hiệu bị cấm có nghĩa là có lỗi trong dữ liệu được truyền.

Trong số các chuỗi kết quả, có 16 chuỗi được chọn sao cho bất kỳ sự kết hợp nào cũng chứa trong trường hợp xấu nhất 8 bit "1" liên tiếp.

### Bảng 1.1. Bảng mã hóa dư thừa 4B/5B

| **Ký tự ban đầu** | **Ký tự kết quả** | **Ký tự ban đầu** | **Ký tự kết quả** |
|-----------------------|-----------------------|-----------------------|-----------------------|
| 0000                  | 11110                 | 1000                  | 10010                 |
| 0001                  | 01001                 | 1001                  | 10011                 |
| 0010                  | 10100                 | 1010                  | 10110                 |
| 0011                  | 10101                 | 1011                  | 10111                 |
| 0100                  | 01010                 | 1100                  | 11010                 |
| 0101                  | 01011                 | 1101                  | 11011                 |
| 0110                  | 01110                 | 1110                  | 11100                 |
| 0111                  | 01111                 | 1111                  | 11101                 |


**Ưu điểm**

- đặc tính tự đồng bộ hóa xuất hiện do các chuỗi số 0 và số 1 dài biến mất; 
- phổ tín hiệu bị thu hẹp do thiếu thành phần không đổi; 
- có thể phát hiện lỗi do sự hiện diện của các ký tự bị cấm; 
- thực hiện đơn giản dưới dạng bảng tra cứu.

**Nhược điểm**

- Giảm băng thông hữu ích của kênh truyền, vì một phần băng thông bị tiêu tốn để truyền các bit dư thừa;
- Xuất hiện thêm chi phí thời gian tại các nút mạng để thực hiện mã hóa logic.

Nhược điểm chính của mã hóa dư thừa là sự xuất hiện của "bit thừa", tương ứng với 4 bit thông tin, tức là độ dư thừa của mã 4B/5B là 25% $$(1/4 = 0.25)$$. Điều này có nghĩa là băng thông thực tế của kênh sẽ thấp hơn 20% so với băng thông danh nghĩa. Để duy trì băng thông nhất định, cần tăng tần số đồng hồ của bộ phát lên 25%, điều này sẽ dẫn đến việc mở rộng phổ tín hiệu.

Trong phương pháp mã hóa logic 8B/6T, để mã hóa 8 bit (B) của thông điệp gốc, sử dụng mã từ 6 ký hiệu ba trạng thái (T). Số lượng mã dư thừa (bị cấm) là:

$$
3^6 - 2^8 = 729 - 256 = 473.
$$

Do đó, trong 8B/6T, tỷ lệ mã bị cấm cao hơn so với 4B/5B (65% so với 50%), điều này làm tăng hiệu quả phát hiện lỗi.

## 3.2. Mã hóa Scrambling


Mã hóa Scrambling là quá trình chuyển đổi mã nhị phân ban đầu theo một thuật toán xác định, nhằm loại bỏ hoặc ít nhất là giảm thiểu các chuỗi dài chứa toàn số 0 hoặc số 1.

Ví dụ, thuật toán chuyển đổi có thể có dạng:

$$
B_i = A_i \oplus B_{i-3} \oplus B_{i-5} \quad (i = 1, 2, …)
$$

Trong đó $$A_i$$ và $$B_i$$ là giá trị của chữ số thứ $$i$$ của mã gốc và mã kết quả tương ứng; $$B_{i-3}$$ và $$B_{i-5}$$ là giá trị của chữ số tương ứng ở vị trí $$(i-3)$$ và $$(i-5)$$ của mã kết quả; $$\oplus$$ là phép toán XOR (phép cộng theo modulo 2).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/ITMO/K%E1%BB%B3%205/M%E1%BA%A1ng%20m%C3%A1y%20t%C3%ADnh/ITMO/image/1/XOR.png" alt="Alt text" width="500">
</p>

Đối với chuỗi ban đầu $$A = 110110000001$$, việc sử dụng bộ mã hóa như vậy sẽ cho kết quả như sau:

$$
\begin{align*}
B_1 &= A_1 = 1; \\
B_2 &= A_2 = 1; \\
B_3 &= A_3 = 0; \\
B_4 &= A_4 \oplus B_1 = 1 \oplus 1 = 0; \\
B_5 &= A_5 \oplus B_2 = 1 \oplus 1 = 0; \\
B_6 &= A_6 \oplus B_3 \oplus B_1 = 0 \oplus 0 \oplus 1 = 1; \\
B_7 &= A_7 \oplus B_4 \oplus B_2 = 0 \oplus 0 \oplus 1 = 1; \\
B_8 &= A_8 \oplus B_5 \oplus B_3 = 0 \oplus 0 \oplus 0 = 0; \\
B_9 &= A_9 \oplus B_6 \oplus B_4 = 0 \oplus 1 \oplus 0 = 1; \\
B_{10} &= A_{10} \oplus B_7 \oplus B_5 = 0 \oplus 1 \oplus 0 = 1; \\
B_{11} &= A_{11} \oplus B_8 \oplus B_6 = 0 \oplus 0 \oplus 1 = 1; \\
B_{12} &= A_{12} \oplus B_9 \oplus B_7 = 1 \oplus 1 \oplus 1 = 1. \\
\end{align*}
$$

Như vậy, mã kết quả $$B$$ sẽ là $$110001101111$$, trong đó không có chuỗi nào dài hơn sáu số 0, mà có mặt trong mã gốc.

Bộ giải mã phục hồi mã gốc bằng cách sử dụng mối quan hệ đảo ngược:

$$
C_i = B_i \oplus B_{i-3} \oplus B_{i-5} \quad (i = 1, 2, …).
$$

Dễ dàng nhận thấy rằng mã được phục hồi trùng khớp với mã gốc, tức là $$C_i = A_i$$.

Các thuật toán mã hóa Scrambling khác nhau có thể khác nhau về số lượng hạng tử để xác định giá trị của chữ số trong mã kết quả và kích thước dịch chuyển giữa các hạng tử. Ví dụ, kích thước dịch chuyển có thể là 5 và 23 vị trí hoặc bất kỳ giá trị nào khác.

**Ưu điểm chính của mã hóa Scrambling** so với mã hóa dư thừa là việc giữ nguyên băng thông hữu ích của kênh truyền, vì không có bit dư thừa.

**Nhược điểm của mã hóa Scrambling** bao gồm:

- Chi phí bổ sung (overhead) tại các nút mạng để thực hiện thuật toán mã hóa và giải mã;
- Không đảm bảo 100% việc loại bỏ các chuỗi dài 0 hoặc 1, cũng như khả năng xuất hiện các chuỗi 0 hoặc 1 khác trong mã kết quả.





