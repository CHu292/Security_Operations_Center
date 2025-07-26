# 1.3 Các bước thực hiện công việc và các tùy chọn bài tập 

## Bước 1. Hình thành thông điệp

Sử dụng họ và tên viết tắt của sinh viên thực hiện bài tập làm thông điệp ban đầu để truyền tải. Để biểu diễn thông điệp này dưới dạng số, hãy sử dụng mã hệ thập lục phân theo bảng mã (xem Bảng 1.2).

Ghi lại thông điệp ban đầu bằng mã thập lục phân và mã nhị phân. Xác định độ dài của thông điệp.

Dưới đây là nội dung của **Bảng 1.2** từ tài liệu "Задачи_сети.pdf" đã được dịch sang tiếng Việt:

---

 Bảng 1.2

| Ký hiệu | Mã  | Ký hiệu | Mã  | Ký hiệu | Mã  | Ký hiệu | Mã  | Ký hiệu | Mã  |
|---------|-----|---------|-----|---------|-----|---------|-----|---------|-----|
| А       | C0  | Р       | D0  | а       | E0  | р       | F0  | khoảng trắng | 20  |
| Б       | C1  | С       | D1  | б       | E1  | с       | F1  | ,       | 2C  |
| В       | C2  | Т       | D2  | в       | E2  | т       | F2  | .       | 2E  |
| Г       | C3  | У       | D3  | г       | E3  | у       | F3  | 0       | 30  |
| Д       | C4  | Ф       | D4  | д       | E4  | ф       | F4  | 1       | 31  |
| Е       | C5  | Х       | D5  | е       | E5  | х       | F5  | 2       | 32  |
| Ж       | C6  | Ц       | D6  | ж       | E6  | ц       | F6  | 3       | 33  |
| З       | C7  | Ч       | D7  | з       | E7  | ч       | F7  | 4       | 34  |
| И       | C8  | Ш       | D8  | и       | E8  | ш       | F8  | 5       | 35  |
| Й       | C9  | Щ       | D9  | й       | E9  | щ       | F9  | 6       | 36  |
| К       | CA  | Ъ       | DA  | к       | EA  | ъ       | FA  | 7       | 37  |
| Л       | CB  | Ы       | DB  | л       | EB  | ы       | FB  | 8       | 38  |
| М       | CC  | Ь       | DC  | м       | EC  | ь       | FC  | 9       | 39  |
| Н       | CD  | Э       | DD  | н       | ED  | э       | FD  |         |     |
| О       | CE  | Ю       | DE  | о       | EE  | ю       | FE  |         |     |
| П       | CF  | Я       | DF  | п       | EF  | я       | FF  |         |     |

Bảng này hiển thị các mã thập lục phân cho từng ký tự chữ cái trong bảng chữ cái Cyrillic, cùng với một số ký hiệu đặc biệt và số.

--- 

Thông điệp ban đầu: `Чу В.Д.`

Mã thập lục phân (hexadecimal code): `D7 F3 20 C2 2E C4 2E`

Code để chuyển từ hex sang bin:

```python
def hex_to_bin(hex_code):
    # Xóa khoảng trắng khỏi chuỗi hexadecimal
    hex_code = hex_code.replace(" ", "")
    
    # Chuyển mã hexadecimal sang số nhị phân
    bin_code = bin(int(hex_code, 16))[2:]
    
    # Đảm bảo độ dài nhị phân bằng 4 lần số chữ số của mã hexadecimal
    return bin_code.zfill(len(hex_code) * 4)

# Ví dụ sử dụng
hex_code = input("Nhập mã hexadecimal: ")
bin_code = hex_to_bin(hex_code)
print(f"Mã nhị phân tương ứng: {bin_code}")
```
Mã nhị phân: `11010111111100110010000011000010001011101100010000101110`

Độ dài thông điệp: 7 byte (56 bit)

Băng thông của kênh truyền là $C = 1$ Gbit/s.

Bốn byte đầu tiên của chuỗi nhị phân là: `11010111 11110011 00100000 11000010`.

## Bước 2. Mã hóa vật lý thông điệp ban đầu

---

**Ký hiệu:**
- tần số cơ bản $$f_0$$;
- giới hạn tần số trên trong thông điệp truyền $$f_upper$$;
- giới hạn tần số dưới trong thông điệp truyền $$f_lower$$;
- giá trị trung bình của tần số trong phổ của tín hiệu truyền $$f_{avg}$$;
- băng thông cần thiết để truyền thông điệp này chất lượng $$S$$;


- **$$f_0$$**: Fundamental frequency
- **$$f_upper$$**: Upper frequency limit
- **$$f_lower$$**: Lower frequency limit
- **$$f_{avg}$$**: Average frequency in spectrum
- **$$S$$**: Required bandwidth for quality transmission
---

### 1. Mã hóa NRZ:

Phương pháp mã hóa nhị phân đơn giản và rõ ràng nhất là phương pháp mã hóa tiềm năng không quay về mức 0 – NRZ (Non Return to Zero), trong đó bit "1" tương ứng với mức điện thế cao, còn bit "0" tương ứng với mức điện thế thấp


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/ITMO/Lab_1/img/1_NRZ.png" alt="NRZ" width="1000">
</p>
<p align="center"><b>Mã hóa NRZ</b></p>

#### 1.1 Tần số cơ bản
Trong mã hóa NRZ, mỗi bit được biểu diễn bởi một mức điện áp cố định trong suốt khoảng thời gian bit mà không quay về mức 0 giữa các bit. Điều này dẫn đến tần số cơ bản của tín hiệu NRZ bằng một nửa tốc độ bit (bit rate).

Tần số cơ bản (hay còn gọi là tần số cơ sở) là tần số thấp nhất của tín hiệu được biểu diễn.

Công thức tính thời gian truyền 1 bit

$$
t = \frac{1}{C}
$$

Trong đó:

- $$t$$: Khoảng thời gian cần để truyền 1 bit (đơn vị: giây).
- $$C$$: Tốc độ truyền dữ liệu (đơn vị: bps - bits per second).

 **Tần số cơ bản $$f_0$$** được tính bằng công thức:
  
$$
  f_0 = \frac{1}{T_0} = \frac{1}{2t} = \frac{C}{2}= \frac{1 \text{ Gbps}}{2} = 0.5 \text{ GHz} = 500 \text{ MHz}
$$

#### 1.2 giới hạn tần số trên 

 Dựa vào chuỗi bit và hình ảnh trên ta thấy chuỗi có 6 lần truyền với tần số $$f_0$$

$$f_{\text{upper}}$$ có thể được ước tính bằng công thức:

$$
f_{\text{upper}} = 6 \times f_0 = 6*500 = 3000 \text{ MHz}
$$

#### 1.3 Giới hạn tần số dưới  

Là chuỗi bit liên tiếp dài nhất chỉ gồm toàn 0 hoặc toàn 1

 Dựa vào hình ta thấy có chuỗi `1100` là chuỗi có các bit 1 và 0 liên tiếp nhiều nhất

$$
T_{\text{lower}} = 4t
$$

$$
f_{\text{lower}} = \frac{1}{T_{\text{lower}}} = \frac{1}{4t} = \frac{C}{4} = \frac{f_0}{2} = 250  \text{MHz}
$$

#### 1.4 Tần số trung bình

Chúng ta sẽ phân tích các chuỗi liên tiếp khác nhau trong tín hiệu, đại diện cho mức đóng góp tần số từ các chuỗi đó. Những thành phần này tính đến sự xuất hiện của các chuỗi liên tiếp khác nhau, từ đó tính toán ảnh hưởng của chúng đến tần số trung bình của toàn bộ tín hiệu.


$$
f_{\text{avg}} = \frac{1}{32} \left( 6 f_0 + \frac{10}{2} f_0 + \frac{4}{4} f_0 + \frac{5}{5} f_0 + \frac{7}{7} f_0 \right) = \frac{14}{32} f_0 = 218.75 \text{ MHz}
$$

Để hiểu cách công thức này hoạt động, chúng ta sẽ phân tích từng thành phần.

 Các Thành Phần Của Công Thức
- **Tần số cơ bản ($$f_0$$)**: Đây là tần số cơ bản của tín hiệu, phụ thuộc vào băng thông của kênh. Với băng thông $$1 \text{ Gbit/s}$$, tần số cơ bản của tín hiệu NRZ là $$f_0 = 500 \text{ MHz}$$.
  
- **Phân tích chuỗi nhị phân và chuỗi không đổi**:
 
  - Trong công thức này, chúng ta chia tổng của các giá trị bằng tổng độ dài của chuỗi bit ($$32$$). Điều này là để tính ra giá trị trung bình của tần số trong toàn bộ chuỗi.
  

  - Mỗi thành phần của công thức đều biểu diễn sự đóng góp của tần số từ một nhóm chuỗi nhất định trong tín hiệu.
  - Ví dụ, **$$6 f_0$$** đại diện cho tần số từ nhóm có 1 bit không thay đổi.
  - **$$\frac{10}{2} f_0$$** đại diện cho đóng góp tần số từ nhóm chuỗi có 2 bit liên tiếp ko đổi
  - Tương tự, **$$\frac{4}{4} f_0$$**, **$$\frac{5}{5} f_0$$**, và **$$\frac{7}{7} f_0$$** cũng biểu thị sự đóng góp từ các nhóm chuỗi với tỉ lệ khác nhau.


#### 1.5 Băng thông cần thiết để truyền

$$
S = f_{\text{upper}} - f_{\text{lower}} = 3500 - 250 = 3250 \, \text{MHz}
$$

Trong đó $$S$$: Băng thông tín hiệu.

---

#### Bước 3. Phân tích phổ tần số

Xác định giới hạn tần số trên và dưới trong phổ của tín hiệu đã truyền, giá trị trung bình của tần số, và băng thông cần thiết để truyền thông điệp này một cách chất lượng.

#### Bước 4. Mã hóa logic thông điệp

Thực hiện mã hóa logic cho thông điệp ban đầu bằng một hoặc hai phương pháp đã chọn. Mô tả chi tiết quá trình mã hóa và các đặc điểm chính của mỗi phương pháp.

#### Bước 5. So sánh các phương pháp mã hóa

So sánh các phương pháp mã hóa đã sử dụng ở các bước trước và đưa ra nhận xét về ưu điểm và nhược điểm của từng phương pháp. Trình bày kết quả so sánh dưới dạng bảng tóm tắt.

---

Phần dịch này cung cấp chi tiết các bước để sinh viên thực hiện bài tập liên quan đến mã hóa và truyền tín hiệu, với các tiêu chuẩn đánh giá từ điểm "đạt" đến "giỏi" dựa trên số lượng và sự phù hợp của các phương pháp mã hóa được áp dụng
