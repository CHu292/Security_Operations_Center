# 3 Lớp vật lý của mô hình OSI
Lớp vật lý (Physical) là lớp thấp nhất trong mô hình OSI. Nó thực hiện việc truyền một luồng bit nhận được từ lớp liên kết (Data Link) thông qua môi trường vật lý dưới dạng tín hiệu điện, quang học hoặc vô tuyến. Lớp vật lý chịu trách nhiệm thiết lập, duy trì và hủy kích hoạt kênh giữa các hệ thống đầu cuối, xác định các kênh, thông báo về việc xảy ra lỗi và lỗi, đồng thời, nếu cần, lắng nghe các kênh để xác định hoạt động trong đó. Liên minh Viễn thông Quốc tế (International Telecommunication Union - ITU) đã áp dụng một số tiêu chuẩn lớp vật lý. Các tiêu chuẩn lớp vật lý do Liên minh Công nghiệp Điện tử (Electronics Industries Alliance- EIA) và Hiệp hội Công nghiệp Viễn thông (Telecommunications Industry Association, - TIA) phát triển được biết đến và sử dụng rộng rãi. Thông số kỹ thuật của lớp vật lý mô tả chi tiết các giao diện cơ, quang, điện, chức năng với môi trường truyền dẫn: điện áp, tần số, bước sóng, đầu nối, số lượng và chức năng của các tiếp điểm, sơ đồ mã hóa tín hiệu, v.v. Lớp vật lý cũng xem xét các vấn đề liên quan đến cấu trúc liên kết vật lý của mạng.


## 3.1 Khái niệm về đường truyền và kênh liên lạc

Đường truyền thông được sử dụng để truyền tín hiệu giữa các hệ thống tương tác trong mạng máy tính.

Theo nghĩa hẹp, thuật ngữ liên kết truyền tải hoặc **đường truyền** (transmission link, link) dùng để chỉ môi trường vật lý mà qua đó tín hiệu được truyền giữa hai hệ thống đầu cuối. Tín hiệu được tạo ra bằng các phương tiện kỹ thuật đặc biệt (máy phát, bộ khuếch đại, bộ ghép kênh, v.v.) liên quan đến thiết bị mạng.

**Môi trường truyền dẫn (transmission medium)** hoặc môi trường vật lý là một chất liệu mà qua đó tín hiệu được truyền đi.

Mạng máy tính sử dụng hai loại phương tiện truyền dẫn: cáp và không dây.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_1_Types_of_transmission_media.png" alt="Hình 3.1 - Các loại phương tiện truyền dẫn" width="1000">
</p>
<p align="center"><b>Hình 3.1 - Các loại phương tiện truyền dẫn"</b></p>

Cơ sở của phương tiện truyền dẫn không dây là bầu khí quyển của trái đất hoặc không gian bên ngoài mà sóng điện từ lan truyền qua đó. Phương tiện truyền dẫn cáp sử dụng nhiều loại cáp: cáp đồng trục, cáp quang, cáp xoắn đôi. Việc truyền dữ liệu tới chúng được thực hiện bằng tín hiệu điện (dòng điện) hoặc tín hiệu quang (ánh sáng).

Theo nghĩa rộng, thuật ngữ “đường truyền - communication line” trong lĩnh vực mạng máy tính dùng để chỉ một kênh liên lạc.

**Kênh liên lạc (channel, data link)** là một tập hợp gồm một hoặc nhiều phương tiện truyền dẫn vật lý và thiết bị tạo kênh (mạng) cung cấp khả năng truyền dữ liệu giữa các hệ thống tương tác dưới dạng tín hiệu tương ứng với loại phương tiện vật lý.

Trong bối cảnh này, thuật ngữ "đường truyền" và "kênh liên lạc" là đồng nghĩa.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_2_Communication_channel.png" alt="Hình 3.2 - Kênh liên lạc" width="1000">
</p>
<p align="center"><b>Hình 3.2 - Kênh liên lạc</b></p>

Có các kênh **vật lý (physical link)** và **kênh logic (logical link)**. Kênh liên lạc vật lý là phương tiện truyền tín hiệu giữa các hệ thống tương tác. Tùy thuộc vào loại tín hiệu truyền và môi trường vật lý được sử dụng để phân phối, các kênh vật lý được chia thành điện (cặp xoắn, cáp đồng trục), quang (cáp quang) và không dây (kênh vô tuyến, kênh hồng ngoại, v.v.).

Các kênh logic được thiết lập giữa các giao thức của bất kỳ lớp nào trong mô hình OSI của các hệ thống tương tác và xác định đường dẫn dữ liệu được truyền từ nguồn đến máy thu thông qua một hoặc một chuỗi các kênh vật lý.

Khi đặt một số kênh logic trong một kênh vật lý, tài nguyên của kênh vật lý được phân phối giữa các kênh logic bằng phương pháp ghép kênh.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_3_Physical_and_logical_communication_channels.png" alt="Hình 3.3 - Các kênh truyền thông vật lý và logic" width="1000">
</p>
<p align="center"><b>Hình 3.3 - Các kênh truyền thông vật lý và logic</b></p>


Các kênh truyền liên lạc (đường truyền) có thể được phân loại dựa trên các đặc điểm sau:

- theo loại môi trường vật lý;
- theo kiểu trình bày thông tin được truyền đi;
- theo hướng truyền dữ liệu;
- theo thời gian tồn tại;
- bằng phương thức kết nối;
- về mặt băng thông.

Tùy thuộc vào loại trình bày thông tin được truyền, các kênh được chia thành kênh analog (liên tục), dành cho việc truyền tín hiệu liên tục và **rời rạc**, được sử dụng để truyền tín hiệu rời rạc (kỹ thuật số).

Tùy thuộc vào hướng truyền dữ liệu, các kênh được phân biệt:

- đơn giản (**simplex**), là chế độ truyền tín hiệu đơn giản và hiệu quả, được sử dụng trong các ứng dụng yêu cầu giao tiếp một chiều.
- bán song công (**half-duplex**),  là chế độ truyền tín hiệu hiệu quả, được sử dụng trong các ứng dụng yêu cầu giao tiếp hai chiều nhưng không đồng thời.
- song công (**full duplex**), là chế độ truyền tín hiệu hiệu suất cao, được sử dụng trong các ứng dụng yêu cầu giao tiếp hai chiều đồng thời.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_4_Simplex.png" alt="Hình 3.4 - Simplex" width="700">
</p>
<p align="center"><b>"Hình 3.4 - Simplex</b></p>


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_5_half_duplex.png" alt="Hình 3.5 - Half Duplex" width="700">
</p>
<p align="center"><b>"Hình 3.5 - Half Duplex</b></p>

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_6_Full_Duplex.png" alt="Hình 3.6 - Full Duplex" width="700">
</p>
<p align="center"><b>"Hình 3.6 - Full Duplex</b></p>


Các kênh cũng có thể được phân loại theo thời gian sẵn có của người đăng ký. Các kênh giữa các hệ thống đầu cuối có sẵn để truyền dữ liệu dài hạn nhờ kết nối cố định với các đặc tính cụ thể được gọi là **kênh chuyên dụng (dedicated)** hoặc **kênh không chuyển mạch (non-switched)**. Các kênh liên lạc chỉ có thể truyền dữ liệu sau khi thiết lập kết nối giữa các hệ thống tương tác được gọi là **kênh chuyển mạch (switched)** hoặc **kênh tạm thời (temporary)**. Kênh này chỉ tồn tại trong suốt phiên kết nối, tức là chỉ trong thời gian cần thiết để truyền dữ liệu.

Theo phương thức kết nối, các kênh được chia thành: “điểm-điểm” **(point-to-point)**, “điểm-đa điểm” **(point-to-multipoint)**, “đa điểm” **(multipoint)**. Liên kết point-to-point chỉ kết nối hai nút hoặc hai hệ thống truyền thông. Liên kết point-to-multipoint kết nối một hệ thống trung tâm node (nút) với một nhóm các hệ thống node (nút) khác. Liên kết multipoint cho phép một nhóm nút hoặc hệ thống kết nối với nhau.

Một đặc tính quan trọng của kênh liên lạc là **băng thông (bandwidth)** của nó. Tùy thuộc vào băng thông (sự khác biệt giữa tần số cắt của băng thông) và phương thức truyền tín hiệu, các kênh được chia thành kênh **băng thông cơ sở (baseband channel)** và kênh **băng thông rộng (broadband channel)**.

Kênh băng thông cơ sở được đặc trưng bởi sự đơn giản và chi phí triển khai thấp và do đó được sử dụng rộng rãi trong các mạng cục bộ (từ “BASE” trong tên của các thông số kỹ thuật của lớp vật lý Ethernet (ví dụ: 10BASE-T, 100BASE-FX, 1000BASE-SX ) biểu thị việc truyền băng cơ sở). Tín hiệu qua kênh băng thông cơ sở được truyền trong tần số cở bản, tức là không điều chế sóng mang, với toàn bộ băng thông chỉ được sử dụng để truyền một tín hiệu.

Không giống như kênh băng thông cơ sở, toàn bộ băng thông của kênh băng rộng được phân chia giữa một số kênh logic bằng kỹ thuật ghép kênh, cho phép tín hiệu được truyền đồng thời và độc lập giữa nhiều cặp hệ thống liên lạc. Các công nghệ truy cập băng thông rộng (ví dụ: xDSL, PowerLine (PLC), 3G (UMTS), 4G (LTE)) được sử dụng để tổ chức kết nối với một loạt dịch vụ do các nhà khai thác viễn thông cung cấp.


## 3.2 Tín Hiệu

Việc truyền dữ liệu qua các kênh liên lạc được thực hiện bằng cách sử dụng biểu diễn vật lý của chúng - tín hiệu điện (dòng điện), quang (ánh sáng) hoặc điện từ.

Nếu chúng ta coi tín hiệu là hàm của thời gian thì nó có thể là:

- analog (liên tục) - giá trị của nó thay đổi liên tục theo thời gian;
- kỹ thuật số (rời rạc) - có số lượng giá trị hữu hạn, thường nhỏ.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_7_Analog_signal.png" alt="Hình 3.7 - Analog Signal" width="700">
</p>
<p align="center"><b>"Hình 3.7 - Analog Signal</b></p>

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_8_Digital_signal.png" alt="Hình 3.8 - Digital Signal" width="700">
</p>
<p align="center"><b>"Hình 3.8 - Digital Signal</b></p>

Loại tín hiệu đơn giản nhất là tín hiệu tuần hoàn **(periodic signal)**. Dạng đơn giản nhất của tín hiệu tuần hoàn là tín hiệu điều hòa **(harmonic signal)**.

**Tín hiệu tuần hoàn** là một loại ảnh hưởng khi hình dạng tín hiệu được lặp lại sau một khoảng thời gian T nhất định, được gọi là một khoảng thời gian.

**Tín hiệu điều hòa** là một dao động điều hòa lan truyền trong không gian theo thời gian, mang theo thông tin hoặc một số loại dữ liệu.

**Dao động điều hòa** là dao động trong đó một đại lượng vật lý (hoặc bất kỳ đại lượng nào khác) thay đổi theo thời gian theo định luật hình sin hoặc cosin.

Nói chung, tín hiệu điều hòa có thể được xác định bởi ba tham số: biên độ cực đại A, pha φ và tần số ƒ. Biên độ cực đại là giá trị hoặc cường độ tối đa của tín hiệu theo thời gian; nó thường được đo bằng vôn. Tần số là số dao động xảy ra trong một đơn vị thời gian. Đơn vị của tần số là Hz. Pha là thước đo sự dịch chuyển thời gian tương đối trong một khoảng thời gian tín hiệu cụ thể. Pha được đo bằng radian hoặc độ.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_9_Harmonic_signal.png" alt="Hình 3.9 - Tín hiệu điều hòa" width="700">
</p>
<p align="center"><b>"Hình 3.9 - Tín hiệu điều hòa</b></p>

Tín hiệu analog cơ bản là sóng hình sin. Nói chung, các dao động điều hòa thay đổi theo định luật hình sin có thể được biểu diễn dưới dạng sau:

$$ 
y(t) = A \sin(\omega t + \varphi_0) = A \sin(2 \pi f t + \varphi_0), (3.1)
$$

Trong đó:
- $$A$$ là biên độ tín hiệu;
- $$\omega$$ là tần số góc: $$\omega = 2 \pi f$$;
- $$f$$ là tần số, được tính bằng $$f = \frac{1}{T}$$, nghịch đảo của chu kỳ $$T$$;
- $$\varphi_0$$ là pha ban đầu của tín hiệu điều hòa;
- $$t$$ là thời gian.

Giả sử rằng tín hiệu thực được truyền qua kênh liên lạc là tín hiệu tuần hoàn. Trong trường hợp này, nó có thể được biểu diễn dưới dạng chuỗi Fourier,tức là phân tích thành các thành phần hình sin:

$$
x(t) = C_0 + \sum_{i=1}^{\infty} \left( A_i \cos(i \omega_1 t) + B_i \sin(i \omega_1 t) \right) = C_0 + \sum_{i=1}^{\infty} C_i \cos(i \omega_1 t - \varphi_i), (3.2)
$$

Trong đó:
- $$i$$ — số thứ tự của điều hòa;  
- $$C_i = \sqrt{A_i^2 + B_i^2}$$ — biên độ,  
- $$\varphi_i$$ — pha ban đầu của điều hòa thứ $$i$$;  
- $$\omega_1 = 2 \pi f = \frac{2 \pi}{T}$$ — tần số cơ bản;  
- $$t$$ — thời gian.

Nhà khoa học người Pháp J.B. Fourier đã chứng minh rằng bất kỳ sự thay đổi thời gian nào của một hàm số nào đó đều có thể được tính gần đúng như một tổng hữu hạn hoặc vô hạn của một chuỗi dao động điều hòa có biên độ, tần số và pha ban đầu khác nhau.

Nói cách khác, bất kỳ tín hiệu tuần hoàn nào (analog hoặc digital signal) được mô tả bằng hàm phức tạp của thời gian đều có thể được biểu diễn dưới dạng tổng vô hạn hoặc hữu hạn của các hình sin có tần số là bội số của tần số cơ bản $$\omega_1$$ và với biên độ và pha ban đầu được chọn đúng. Các thuật ngữ riêng lẻ được gọi là sóng điều hòa. Dao động của tần số cơ bản $$\omega_1$$ được gọi là sóng điều hòa đầu tiên hay sóng điều hòa cơ bản của tín hiệu; sóng điều hòa bậc hai gọi là dao động có tần số $$2\omega_1$$; sóng điều hòa thứ ba là dao động có tần số $$3\omega_1$$, v.v.

Thành phần hằng số $$C_0$$ đơn giản là giá trị trung bình của hàm x(t) và thường không có trong thực tế.

Từ tập hợp các sóng điều hòa tạo nên tín hiệu, biên độ và phổ pha được tách biệt và phân biệt. Phổ biên độ là tập hợp các giá trị $$C_1$$. Về mặt đồ họa, phổ được biểu diễn theo tọa độ $$C_i$$ và $$\omega$$, như trong Hình 3.10. Độ dài của các đoạn thẳng đứng biểu thị biên độ của các sóng điều hòa tương ứng; những đoạn này được gọi là vạch quang phổ. Biên độ và phổ pha xác định duy nhất tín hiệu. Tuy nhiên, đối với nhiều bài toán thực tế, chỉ cần giới hạn ở phổ biên độ là đủ, để cho ngắn gọn gọi là phổ.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_10_Signal_spectrum.png" alt="Hình 3.10 - Phổ" width="700">
</p>
<p align="center"><b>"Hình 3.10 - Sự hình thành tín hiệu từ tổng của 4 sóng điều hòa đầu tiên và sơ đồ biên độ phổ của tín hiệu tuần hoàn</b></p>

Trong trường hợp tổng quát, tổng công thức (3.2) biểu thị một chuỗi vô hạn. Nhưng thực tế không có tín hiệu nào trong tự nhiên có phổ vô hạn. Phần năng lượng chiếm ưu thế của tín hiệu thực tập trung ở một vùng (dải) tần số giới hạn và bản thân tín hiệu đó được biểu diễn dưới dạng tổng hữu hạn của các dao động điều hòa, bởi vì biên độ của các sóng điều hòa, bắt đầu từ một số n nhất định, nhỏ đến mức có thể bỏ qua. Vì vậy, trong thực tế, tín hiệu được biểu diễn bằng các hàm có phổ giới hạn. Khoảng trên thang tần số chứa phổ giới hạn được gọi là **độ rộng phổ**.

Khi truyền tín hiệu qua kênh liên lạc, hình dạng của nó bị biến dạng do sự biến dạng không đồng đều của các sóng điều hòa ở các tần số khác nhau. Điều này xảy ra do các thông số vật lý của kênh liên lạc khác với các thông số lý tưởng.Tín hiệu bị ảnh hưởng bởi các yếu tố như suy giảm, tiếng ồn và nhiễu. Tuy nhiên, yếu tố chính ảnh hưởng đến hình dạng tín hiệu là băng thông của kênh truyền thông. Để truyền tín hiệu mà không bị biến dạng đáng kể, kênh liên lạc phải có băng thông không nhỏ hơn độ rộng phổ của tín hiệu được truyền.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_11_The_influence_of_physical_parameters_of_the_transmission_medium_on_the_signal.png" alt="Hình 3.11 - Ảnh hưởng của các thông số vật lý của môi trường truyền dẫn đến tín hiệu" width="700">
</p>
<p align="center"><b>"Hình 3.11 - Ảnh hưởng của các thông số vật lý của môi trường truyền dẫn đến tín hiệu</b></p>


## 3.3 Đặc điểm chính của kênh liên lạc

Các đặc điểm chính của kênh liên lạc (đường truyền), ảnh hưởng đáng kể đến chất lượng truyền tín hiệu, bao gồm:

- băng thông (bandwidth);
- suy giảm (attenuation);
- khả năng chống ồn (noise immunity);
- thông lượng (noise immunity);
- độ tin cậy của việc truyền dữ liệu (data transmission reliability).

### 3.3.1 Băng thông - Bandwidth

**Băng thông** là dải tần trong đó đáp ứng tần số biên độ (amplitude-frequency response - AFC) của kênh liên lạc (đường truyền) đủ đồng nhất để đảm bảo truyền tín hiệu mà không bị biến dạng đáng kể về hình dạng của nó.

Băng thông F được định nghĩa là sự chênh lệch giữa tần số trên $$f_{upper}$$ và tần số dưới $$f_{lower}$$ của phần đáp ứng tần số mà tại đó công suất tín hiệu giảm không quá 2 lần so với giá trị cực đại: $$F=f_P{upper}-f_{lower}$$ (xấp xỉ tương ứng với −3 dB).

Băng thông được đo bằng (Hz).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_12_Bandwidth_of_the_communication_channel.png" alt="Hình 3.12  Băng thông kênh liên lạc" width="700">
</p>
<p align="center"><b>"Hình 3.12 -  Băng thông kênh liên lạc</b></p>

Băng thông ảnh hưởng rất lớn đến tốc độ truyền dữ liệu tối đa có thể qua kênh truyền thông và phụ thuộc vào loại môi trường truyền dẫn cũng như sự hiện diện của các bộ lọc tần số trong kênh.

Các tín hiệu bao gồm một tập hợp lớn các sóng điều hòa, nhưng máy thu chỉ có thể nhận được những sóng điều hòa có tần số nằm trong băng thông của kênh. Băng thông của kênh càng rộng, tốc độ truyền dữ liệu có thể càng cao và các sóng hài tần số cao của tín hiệu càng có thể truyền được. Nếu các sóng hài có biên độ đóng góp chính vào tín hiệu kết quả rơi vào băng thông của kênh, hình dạng tín hiệu sẽ thay đổi không đáng kể và tín hiệu sẽ được nhận diện đúng bởi máy thu.

Ngược lại, hình dạng tín hiệu sẽ bị méo đáng kể, dẫn đến giảm tốc độ truyền thông qua kênh do gặp vấn đề trong việc nhận diện tín hiệu, gây ra lỗi liên lạc và yêu cầu truyền lại.



<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_13_The_influence_of_bandwidth_on_the_signal.png" alt="Hình 3.13 Ảnh hưởng của băng thông đến tín hiệu" width="700">
</p>
<p align="center"><b>"Hình 3.13 Ảnh hưởng của băng thông đến tín hiệu</b></p>

### 3.3.2 Suy giảm

Khi truyền tín hiệu qua kênh liên lạc, tín hiệu sẽ bị suy giảm dần, điều này do các đặc tính vật lý và kỹ thuật của môi trường truyền dẫn và các thiết bị mạng được sử dụng. Để tín hiệu có thể được nhận diện chính xác tại điểm tiếp nhận, mức suy giảm này không được vượt quá một giá trị ngưỡng nhất định.

Suy giảm (attenuation) là độ lớn cho thấy mức độ giảm của công suất (biên độ) tín hiệu tại đầu ra của kênh truyền so với công suất (biên độ) tín hiệu tại đầu vào. Hệ số suy giảm $$d$$ được đo bằng decibel (dB) trên một đơn vị chiều dài và được tính theo công thức sau:

$$
d \, [\text{dB}] = 10 \log \frac{P_{\text{out}}}{P_{\text{in}}} (3.3)
$$


trong đó $$P_{\text{out}}$$ là công suất tín hiệu đầu ra (out signal); $$P_{\text{in}}$$ là công suất tín hiệu đầu vào (P_in signal).

Suy giảm đặc trưng cho cả tín hiệu analog và tín hiệu số (digital). Mức độ suy giảm tăng lên khi tần số của tín hiệu tăng: tần số càng cao thì tín hiệu càng dễ bị suy giảm. Vì lý do này, các thiết bị thu của các thiết bị tốc độ cao sẽ gặp khó khăn đáng kể hơn trong việc nhận diện tín hiệu gốc.

Suy giảm tín hiệu ảnh hưởng đến khoảng cách mà tín hiệu có thể đi qua giữa hai điểm mà không cần khuếch đại hoặc phục hồi. Suy giảm là một trong những thông số quan trọng được xác định cho các loại cáp (cặp xoắn, cáp quang, cáp đồng trục). Cáp có độ suy giảm càng thấp thì chất lượng càng cao. Do đó, khi thiết kế các kênh truyền dẫn có dây, cần xem xét các đặc tính của cáp và sử dụng các loại cáp có độ suy giảm thấp nhất để đạt được chiều dài kênh tối đa.

### 3.3.3 Khả năng chống nhiễu

Trong kênh liên lạc thực tế, có tồn tại nhiễu, do các đặc tính của môi trường truyền dẫn, thiết bị tạo kênh, và tác động của các trường điện từ từ các thiết bị điện tử khác nhau. Do ảnh hưởng của các nhiễu này, các lỗi xuất hiện trong kênh truyền.

Một trong những chỉ số quan trọng nhất của kênh liên lạc là khả năng chống nhiễu của nó, được hiểu là khả năng của kênh trong việc chống lại tác động của nhiễu. Khả năng chống nhiễu dựa trên khả năng phân biệt tín hiệu với nhiễu với độ tin cậy nhất định. Vì vậy, khi xây dựng kênh liên lạc, cần phải xem xét các nhiễu có thể xảy ra và tối đa hóa sự khác biệt giữa chúng và tín hiệu.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_14_The_influence_of_interference_on_the_communication_channel.png" alt="Hình 3.14 Ảnh hưởng của nhiễu lên kênh truyền thông" width="700">
</p>
<p align="center"><b>"Hình 3.14 Ảnh hưởng của nhiễu lên kênh truyền thông</b></p>


Tùy thuộc vào nguồn gốc phát sinh và đặc tính tác động của chúng, nhiễu được chia thành nhiễu bên trong, nhiễu bên ngoài và nhiễu tương hỗ. 

**Nhiễu bên trong**, hay còn gọi là nhiễu nội tại, phát sinh từ các nguồn bên trong kênh này và xuất hiện ngay sau khi thiết bị liên lạc được bật lên. Chúng chủ yếu bao gồm nhiễu nhiệt, nhiễu chập, nhiễu tiếp xúc và nhiễu xung, và hầu như không thể loại bỏ được.

**Nhiễu bên ngoài** được chia thành nhiễu công nghiệp, nhiễu vô tuyến, nhiễu khí quyển và nhiễu vũ trụ. 
-  Nhiễu công nghiệp (giao thoa điện từ, hay còn gọi là EMI - Electro Magnetic Interference) được tạo ra do tác động của các trường điện từ từ các thiết bị điện khác nhau đến kênh liên lạc: đèn huỳnh quang, thiết bị gia dụng, máy tính, hệ thống vô tuyến, đường dây điện, thiết bị điện của các xí nghiệp công nghiệp, thiết bị y tế, mạng tiếp xúc của các phương tiện giao thông điện (như tàu điện, xe buýt điện v.v.), quảng cáo đèn neon và nhiều thiết bị tương tự. 
- Nhiễu vô tuyến (nhiễu tần số vô tuyến, RFI - Radio Frequency Interference) phát sinh từ bức xạ của các đài phát thanh với các mục đích khác nhau, có phổ tần vì một lý do nào đó trùng lên phổ tín hiệu hữu ích của kênh liên lạc.
- Nhiễu khí quyển bao gồm các nhiễu do hiện tượng khí quyển khác nhau gây ra: bão từ, cực quang, sấm sét, v.v. - Nhiễu vũ trụ bao gồm các nhiễu điện từ được tạo ra từ bức xạ của Mặt Trời, các ngôi sao nhìn thấy và không nhìn thấy, các tinh vân trong các dải tần số tương ứng.


**Nhiễu tương hỗ** (hay nhiễu xuyên âm, crosstalk) xảy ra khi truyền thông tin qua các kênh liền kề - tín hiệu truyền qua một kênh liên lạc gây ra hiệu ứng không mong muốn ở kênh khác (xuất hiện nhiễu tín hiệu).

Các kênh liên lạc không dây là những kênh ít được bảo vệ nhất khỏi ảnh hưởng của nhiễu. Chúng chịu tác động của cả nhiễu bên ngoài và nhiễu xuyên âm. Trong các mạng không dây gia đình, nhiễu bên ngoài phát sinh từ các thiết bị như lò vi sóng, máy tính, điện thoại di động, v.v. Còn nhiễu xuyên âm liên quan đến nhiễu từ các thiết bị không dây khác hoạt động trên cùng tần số. Điều này đặc biệt phổ biến ở các tòa nhà chung cư, nơi các mạng gia đình chủ yếu được xây dựng bằng công nghệ không dây.


Trong số các kênh cáp, kênh sử dụng cáp điện dễ bị ảnh hưởng bởi nhiễu nhất. Để chống lại nhiễu, các nhà sản xuất cáp điện áp dụng các biện pháp như che chắn (shielding) và xoắn cặp dây dẫn. Che chắn được sử dụng để bảo vệ khỏi nhiễu điện từ và nhiễu vô tuyến. Lớp che chắn là một lớp lưới kim loại hoặc lá kim loại bao quanh từng dây hoặc nhóm dây trong cáp, đóng vai trò như một rào cản ngăn chặn các tín hiệu tương tác.

Bản thân cáp điện cũng là nguồn phát bức xạ điện từ, có thể gây ra nhiễu xuyên âm. Trong các loại cáp xoắn đôi, nhiễu này được biết đến với tên gọi nhiễu xuyên âm đầu gần (NEXT - Near End Cross Talk) và nhiễu xuyên âm đầu xa (FEXT - Far End Cross Talk), phát sinh từ sự ảnh hưởng lẫn nhau của các trường điện từ của tín hiệu được truyền qua các cặp dây dẫn khác nhau. Để giảm thiểu các trường điện từ này, cặp dây dẫn trong cáp xoắn đôi được xoắn lại với nhau.


Các kênh quang học là loại được bảo vệ tốt nhất khỏi nhiễu. Cáp quang không bị ảnh hưởng bởi nhiễu điện từ (EMI), nhiễu tần số vô tuyến (RFI), sét và các xung điện áp cao. Ngoài ra, cáp quang cũng không tạo ra bất kỳ nhiễu điện từ hay nhiễu tần số vô tuyến nào.

Để nhiễu không làm giảm đáng kể chất lượng truyền dẫn, cần phải hạn chế ảnh hưởng của nó. Các phương pháp chống nhiễu nhằm đảm bảo mức độ tín hiệu tại nơi nhận sao cho đáp ứng được chất lượng tín hiệu yêu cầu.

Một trong những thông số quan trọng của kênh truyền dẫn, cho phép đánh giá tác động gây nhiễu của nhiễu lên tín hiệu, là tỷ lệ tín hiệu trên nhiễu (SNR, Signal-to-Noise Ratio). Tỷ lệ này được xác định là tỷ số giữa công suất của tín hiệu $$P_s$$ và công suất của nhiễu (nhiễu) $$P_n$$. Để thuận tiện, biểu thức này thường được biểu diễn bằng decibel (dB).


$$
\text{SNR} \, [\text{dB}] = 10 \cdot \log \left( \frac{P_s}{P_n} \right) (3.4)
$$


trong đó $$P_s$$ là công suất tín hiệu (signal power); $$P_n$$ là công suất nhiễu -noise power (nhiễu loạn).

Khi tỷ lệ tín hiệu trên nhiễu càng lớn, nhiễu càng ít ảnh hưởng đến tín hiệu hữu ích khi nó được truyền qua kênh liên lạc và giúp máy thu nhận diện tín hiệu tốt hơn.

Để tăng khả năng chống nhiễu của kênh truyền, các phương pháp sau đây được áp dụng:

- Tăng tỷ lệ tín hiệu trên nhiễu;
- Mở rộng phổ tín hiệu;
- Tăng độ dư thừa thông tin;
- Sử dụng mã chống nhiễu;
- Lọc tín hiệu hữu ích.

### 3.3.4 Thông lượng  
Thông lượng (throughput) của kênh truyền là tốc độ truyền thông tin tối đa có thể qua kênh, được xác định bởi các giới hạn của nó. Thông lượng được đo bằng bit trên giây (bit/s hoặc bps — bits per second) và các đơn vị dẫn xuất khác.  

Mối quan hệ giữa thông lượng tối đa và băng thông của kênh truyền đã được Claude Shannon xác định:

$$
C = F \log_2 \left(1 + \frac{P_s}{P_n}\right),
$$


Trong đó $$C$$ là thông lượng tối đa của kênh (bit/s); $$F$$ là băng thông của kênh (Hz); $$P_s$$ là công suất tín hiệu và $$P_n$$ là công suất nhiễu.  

Như có thể thấy từ công thức, thông lượng tối đa của kênh có thể được tăng lên bằng cách mở rộng băng thông $$F$$ hoặc giảm công suất nhiễu trên đường truyền.  

Thuật ngữ "thông lượng" có thể mang ý nghĩa lý thuyết và thực tiễn. Thông thường, nó được sử dụng theo nghĩa thực tế và là thước đo lượng dữ liệu hữu ích được truyền qua một kênh truyền nhất định trong một khoảng thời gian xác định, dưới những điều kiện nhất định. Thông lượng lý thuyết bị giới hạn bởi băng thông hoặc tốc độ truyền dữ liệu của công nghệ cụ thể. Ví dụ, trong đặc tả của Gigabit Ethernet, tốc độ được xác định là 1 Gbit/s. Đối với mạng Gigabit Ethernet, giá trị này sẽ là giới hạn trên của thông lượng. Tuy nhiên, thông lượng thực tế của mạng luôn nhỏ hơn thông lượng lý thuyết, vì nó phụ thuộc vào các tham số của thiết bị kênh truyền, cách tổ chức truyền dữ liệu, số lượng nút được kết nối với kênh truyền. Ngoài ra, thông lượng cũng bị giảm do chi phí quản lý liên quan đến việc truyền các gói tin điều khiển cần thiết cho hoạt động của các giao thức mạng.

Hãy xem các ví dụ liên quan đến công thức Shannon.

**Ví dụ 1.** Phổ của kênh chiếm dải từ 5 MHz đến 15 MHz. Tỷ lệ tín hiệu/nhiễu (SRN) là 24,1 dB. Xác định thông lượng của kênh truyền.

1. Xác định băng thông của kênh (Hz). $$F = 15 \, \text{MHz} - 5 \, \text{MHz} = 10 \, \text{MHz} = 10 \times 10^6 \, \text{Hz}$$.

2. Thực hiện chuyển đổi tỷ lệ tín hiệu/nhiễu từ decibel sang đơn vị thông thường. $$24,1 = 10 \lg(x) \Rightarrow x = 10^{\frac{24,1}{10}} \approx 257$$.

3. Sử dụng công thức Shannon để xác định thông lượng của kênh truyền.

$$
C = 10 \times 10^6 \times \log_2 \left(1 + 257\right) \approx 10 \times 10^6 \times 8,011 \approx 80,11 \, \text{Mbit/s}.
$$

Công thức và tính toán trên cho thấy cách xác định thông lượng kênh dựa trên băng thông và tỷ lệ tín hiệu/nhiễu.



**Ví dụ 2.** Phổ của kênh chiếm dải từ 2401 MHz đến 2423 MHz. Công suất tín hiệu là 150 mW, công suất nhiễu là 10 mW. Xác định thông lượng của kênh truyền.

1. Xác định băng thông của kênh (Hz). $$F = 2423 \, \text{MHz} - 2401 \, \text{MHz} = 22 \, \text{MHz} = 22 \times 10^6 \, \text{Hz}$$.

2. Sử dụng công thức Shannon để xác định thông lượng của kênh truyền.
 
$$
C = 22 \times 10^6 \times \log_2 \left(1 + \frac{150}{10}\right) = 22 \times 10^6 \times 4 = 88 \, \text{Mbit/s}.
$$

Bài toán trên minh họa cách tính thông lượng kênh dựa trên băng thông và tỷ lệ công suất tín hiệu/nhiễu.

**Ví dụ 3.** Độ rộng băng thông của kênh truyền là 100 MHz. Công suất tín hiệu - 20 dBm, công suất nhiễu - 3 dBm. Xác định khả năng truyền tải của kênh liên lạc.

1. Xác định tỷ lệ tín hiệu/nhiễu và thực hiện chuyển đổi giữa decibel và tỷ lệ. $$20 - 3 = 10 \cdot \lg(x) \Rightarrow x = 50$$.

   Cách thứ hai để tính tỷ lệ tín hiệu/nhiễu là chuyển đổi công suất tín hiệu từ dBm sang mW. Có thể sử dụng bảng hoặc tự tính như sau: 20 dBm = 100 mW, 3 dBm = 2.0 mW. Do đó, SRN = $$\frac{100}{2} = 50$$.

2. Theo công thức của Shannon, xác định khả năng truyền tải của kênh liên lạc. 

$$
C = 100 \times 10^6 \times \log_2(1 + 50) \approx 100 \times 10^6 \times 5.672 = 567,2 \, \text{Mbit/s}.
$$

Cần hiểu rõ sự khác biệt giữa tốc độ truyền dữ liệu và tốc độ ký hiệu. **Tốc độ truyền dữ liệu** (information rate, data rate) là tốc độ truyền các bit, đo bằng bit/s và các đơn vị phát sinh khác.$$

**Tốc độ ký hiệu** (symbol rate) hay **tốc độ điều chế** là tốc độ thay đổi các ký hiệu, đo bằng baud hoặc ký hiệu mỗi giây. Mỗi ký hiệu đại diện cho một hoặc nhiều bit thông tin tùy thuộc vào phương pháp mã hóa được chọn.


### 3.3.5 Độ tin cậy của truyền dữ liệu

Chất lượng thông tin được truyền qua kênh liên lạc thường được đánh giá dựa trên độ tin cậy của truyền dữ liệu, tức là mức độ tương ứng giữa thông tin nhận được và thông tin đã truyền. **Độ tin cậy của truyền dữ liệu** được đặc trưng bởi xác suất lỗi trong quá trình nhận mỗi bit dữ liệu truyền, tức là tần suất xuất hiện của các bit bị lỗi. Đôi khi chỉ số này còn được gọi là **tỷ lệ lỗi bit** (Bit Error Rate, BER).

BER được xác định bằng tỷ lệ giữa số bit nhận bị lỗi với tổng số bit đã truyền.

Thông thường, các lỗi xuất hiện chủ yếu do nhiễu và tiếng ồn trong kênh. Đối với các kênh truyền mà không có phương tiện bảo vệ bổ sung, giá trị BER nằm trong khoảng từ $$10^{-4}$$ đến $$10^{-6}$$, còn trong các kênh quang học, BER có thể đạt đến $$10^{-9}$$. Giá trị độ tin cậy của truyền dữ liệu, ví dụ như $$10^{-4}$$, cho biết trung bình cứ 10.000 bit thì có một bit bị sai lệch.

Có thể tăng độ tin cậy của dữ liệu truyền bằng cách nâng cao khả năng chống nhiễu của kênh liên lạc.


## 3.4 Các phương pháp sử dụng chung môi trường truyền tải của kênh liên lạc

Trong thực tế, thường phải thực hiện việc truyền các luồng dữ liệu từ nhiều người dùng qua môi trường truyền tải chung (shared medium), vì việc lắp đặt một kênh liên lạc riêng cho mọi hệ thống tương tác quá đắt đỏ, phức tạp hoặc không khả thi. Thông thường, điều này liên quan đến các hạn chế như mạng điện thoại đã có sẵn, các kênh truyền tải đã được thiết lập, tài nguyên tần số vô tuyến bị phân bổ, hoặc khó khăn trong việc xây dựng các kênh truyền tải mới do cấu trúc đô thị.

Để có thể truyền tải nhiều tín hiệu từ các người dùng khác nhau đồng thời qua cùng một cáp hoặc kênh không dây, người ta sử dụng các phương pháp **ghép kênh** (multiplexing).

**Ghép kênh** (multiplexing) là công nghệ truyền tải dữ liệu của nhiều kênh với thuông lượng thấp hơn qua một kênh có thông lượng cao hơn.

Nhiệm vụ của ghép kênh là phân bổ cho mỗi kênh một khoảng thời gian, tần số và/hoặc mã với sự can thiệp tối thiểu và tận dụng tối đa các đặc điểm của môi trường truyền tải chung.

Kết quả của ghép kênh là trong một kênh vật lý tạo ra một nhóm các kênh logic. Khi đó, **thông lượng** của kênh vật lý được chia sẻ giữa các kênh logic và cần đủ để đảm bảo tốc độ truyền dữ liệu cần thiết cho các kênh logic.

Ghép kênh được thực hiện bằng chương trình hoặc thiết bị gọi là **bộ ghép kênh** (multiplexer, MUX). Bộ ghép kênh kết nối nhóm các kênh tốc độ thấp với một kênh vật lý tốc độ cao.

Quá trình ngược lại của ghép kênh được gọi là **tách kênh** (demultiplexing), và thiết bị hoặc chương trình thực hiện quá trình này gọi là **bộ tách kênh** (demultiplexer, DEMUX). Bộ tách kênh phân phối dữ liệu nhận được từ kênh vật lý chung đến nhóm các kênh đầu ra.

Trong các mạng máy tính, các loại ghép kênh chủ yếu bao gồm:

- ghép kênh theo thời gian (TDM);
- ghép kênh theo tần số (FDM);
- ghép kênh theo bước sóng (WDM);
- ghép kênh với phân chia theo mã (CDM).


### 3.4.1 Ghép kênh theo phân chia thời gian

**Ghép kênh theo phân chia thời gian** (*Time Division Multiplexing, TDM*) hay ghép kênh tạm thời là quá trình chia sẻ băng thông của kênh giữa các hệ thống tương tác trong một khoảng thời gian ngắn. Nói cách khác, tất cả các người gửi sử dụng cùng một dải tần số của kênh chung tại các thời điểm khác nhau. Công nghệ TDM thường được sử dụng trong các kênh truyền dẫn kỹ thuật số.

Mỗi kênh đầu vào được cấp một khoảng thời gian, gọi là *thời gian khe* hoặc *khe thời gian* - Time slot, để truyền tải dữ liệu. Thời gian khe có thể là khoảng thời gian cần thiết để truyền một bit, byte, khung, hoặc gói tin.

Có hai loại ghép kênh theo phân chia thời gian: *đồng bộ* và *không đồng bộ*.

Trong chế độ đồng bộ (*Synchronous Time Division Multiplexing*), thời gian hoạt động của kênh được chia thành các chu kỳ lặp lại, bao gồm các khung TDM. Mỗi khung TDM bắt đầu bằng một chuỗi đồng bộ hóa và được chia thành các khe thời gian có độ dài bằng nhau, mỗi khe dành riêng cho một kênh logic. Các khe thời gian được phân bổ cho tất cả các kênh đầu vào được kết nối với bộ ghép kênh, được đánh số và sắp xếp trong khung TDM theo thứ tự cố định.

Các kênh đầu vào lần lượt truyền các khối dữ liệu có kích thước bằng nhau trong mỗi khe thời gian của mỗi chu kỳ. Hình 3.15 minh họa chế độ ghép kênh theo phân chia thời gian đồng bộ, đảm bảo truyền tải dữ liệu giữa bốn cặp thiết bị. Khối dữ liệu từ cổng 1 của bộ ghép kênh sẽ được truyền trong khe thời gian 1 cho kết nối A1–A2. Khối dữ liệu từ cổng 2 sẽ được truyền trong khe thời gian 2 cho kết nối B1–B2. Khối dữ liệu từ cổng 3 sẽ được truyền trong khe thời gian 3 cho kết nối C1–C2. Cuối cùng, khối dữ liệu từ cổng 4 sẽ được truyền trong khe thời gian 4 cho kết nối D1–D2.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_15_Synchronous_Time_Division_Multiplexing.png" alt=Hình 3.15 Ghép kênh phân chia thời gian đồng bộ" width="700">
</p>
<p align="center"><b>Hình 3.15 Ghép kênh phân chia thời gian đồng bộ</b></p>


Việc sử dụng phương pháp này có thể dẫn đến tình trạng trong cùng một chu kỳ, một hệ thống không có dữ liệu để truyền, trong khi hệ thống khác lại không đủ thời gian được phân bổ. Khi một thiết bị không có dữ liệu để truyền, khe thời gian được phân cho nó sẽ vẫn trống và không thể được sử dụng bởi thiết bị khác.

Để bộ giải ghép kênh ở đầu kia của kênh truyền có thể đọc chính xác các khối dữ liệu và phân phối chúng vào các kênh đầu ra tương ứng, thứ tự của các khe thời gian trong khung TDM phải được tuân thủ nghiêm ngặt. Mỗi kênh đầu vào trong TDM đồng bộ được nhận dạng bởi vị trí thời gian của nó trong khung, tức là bằng số thứ tự của khe thời gian. Vị trí này được sử dụng làm thông tin địa chỉ.

Để bên nhận có thể xác định điểm bắt đầu của khe thời gian tiếp theo trong khung TDM, cần phải có sự đồng bộ hóa. Đồng bộ hóa có thể thực hiện bằng nhiều cách. Ví dụ, một trong những cách là truyền một chuỗi đồng bộ hóa ở đầu khung TDM, giúp phân biệt giữa các khung với nhau. Việc mất đồng bộ dẫn đến việc bên nhận không thể phân phối chính xác luồng dữ liệu đến các kênh, vì vị trí tương đối của các khe thời gian thay đổi, và do đó thông tin địa chỉ bị mất.


TDM đồng bộ được sử dụng trong các mạng chuyển mạch kênh. Hai kiến trúc cơ bản dựa trên TDM đồng bộ là hệ thống phân cấp số không đồng bộ (*PDH*, *Plesiochronous Digital Hierarchy*), được sử dụng để truyền tín hiệu số của nhiều cuộc gọi điện thoại qua các kênh T1 (1,544 Mbps) và E1 (2 Mbps), và các hệ thống truyền dẫn số *SDH/SONET*, cung cấp khả năng truyền tín hiệu số qua cả dây đồng và cáp quang. Các giao diện *BRI* (*Basic Rate Interface*) và *PRI* (*Primary Rate Interface*) của mạng *ISDN* (*Integrated Services Digital Network*) cũng được sử dụng để vận chuyển dữ liệu dựa trên TDM đồng bộ.

Thông lượng của kênh chung trong TDM đồng bộ được xác định bằng tổng thông lượng của tất cả các kênh đầu vào cộng thêm một số chi phí quản lý. Một trong những nhược điểm chính của chế độ đồng bộ là sự ràng buộc giữa các kênh đầu vào và các khe thời gian. Nếu một thiết bị không có dữ liệu để truyền, thiết bị khác không thể truyền dữ liệu trong khe thời gian đó. Điều này dẫn đến việc sử dụng băng thông không hiệu quả và làm giảm thông lượng của kênh truyền.

Một ưu điểm của TDM đồng bộ là tính minh bạch đối với các giao thức tầng trên, vì nó được thực hiện ở tầng vật lý của mô hình OSI. Trong các khe thời gian, có thể truyền nhiều loại lưu lượng khác nhau: dữ liệu, thoại, video. Vì các hệ thống tương tác nhận được khe thời gian với cùng một số thứ tự trong mỗi chu kỳ, các khối dữ liệu được truyền đi sẽ xuất hiện ở bên nhận trong khoảng thời gian bằng nhau và đến với cùng độ trễ. Do đó, không cần sử dụng bộ đệm, vì luồng dữ liệu được truyền và nhận với cùng một tốc độ.



**Bộ đệm - Buffer** là một vùng nhớ nơi thiết bị mạng tạm thời lưu trữ dữ liệu đang được truyền.

Thay thế cho **ghép kênh theo thời gian đồng bộ** là **ghép kênh không đồng bộ** (Asynchronous TDM, ATDM) hoặc **ghép kênh thống kê** (Statistical TDM). Ghép kênh thống kê khác biệt ở chỗ người gửi chỉ nhận **khoảng thời gian** (time-slot) khi họ có dữ liệu để truyền. Các khoảng thời gian không có độ dài cố định (kích thước của khối dữ liệu truyền có thể thay đổi), không gắn liền với một kênh đầu vào cụ thể mà được cấp phát động, theo thống kê về nhu cầu của các kênh. Nếu người gửi không có dữ liệu để truyền, khoảng thời gian đó sẽ không bị bỏ trống mà được truyền cho thiết bị khác sẵn sàng truyền dữ liệu. Hơn nữa, người gửi, tùy thuộc vào lượng dữ liệu họ có, có thể nhận không chỉ một mà nhiều khoảng thời gian liên tiếp.

**Băng thông của kênh truyền chung** sẽ được xác định bởi băng thông trung bình của các kênh đầu vào được kết nối.

Khác với **TDM đồng bộ**, nơi thông tin địa chỉ được biểu thị bằng vị trí của khoảng thời gian trong khung TDM, trong **TDM thống kê**, khối dữ liệu truyền phải chứa thông tin địa chỉ chính xác để đảm bảo dữ liệu được truyền đến đúng người nhận.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_16_Asynchronous_Time_Division_Multiplexing.png" alt=Hình 3.16 Ghép kênh không đồng bộ với phân chia theo thời gian" width="900">
</p>
<p align="center"><b>Hình 3.16 Ghép kênh không đồng bộ với phân chia theo thời gian</b></p>


Thông thường, các thiết bị mạng tương tác một cách ngẫu nhiên, vì không phải tất cả các thiết bị đều có dữ liệu để truyền cùng lúc. Nếu dữ liệu đến cùng lúc từ nhiều cổng đầu vào, thì chỉ một cặp thiết bị có thể sử dụng kênh chung để truyền dữ liệu. Các dữ liệu khác, từ các cổng khác của bộ ghép kênh, sẽ được đưa vào bộ đệm và chờ đợi đến khi kênh chung được giải phóng. Nếu không, chúng có thể bị mất. Để giải quyết vấn đề khi nhiều người gửi muốn sử dụng kênh chung cùng lúc, các **phương pháp truy cập đa người dùng** (multiple access) được áp dụng, được thực hiện ở tầng liên kết của mô hình OSI.

Một cặp thiết bị tương tác không thể chiếm giữ độc quyền kênh chung để truyền dữ liệu, vì điều này có thể dẫn đến tình trạng đầy bộ đệm của bộ ghép kênh (tắc nghẽn mạng). Để ngăn chặn tình trạng đầy bộ đệm, các phương pháp **kiểm soát luồng** (flow control) đặc biệt được sử dụng.

Thông thường, các khối dữ liệu được lưu trong bộ đệm sẽ được truyền qua cổng ra của bộ ghép kênh theo thứ tự mà chúng đã đến, tức là theo nguyên tắc **“vào trước, ra trước”** (FIFO - First Input, First Output). Tuy nhiên, có thể tổ chức truyền dữ liệu phân biệt hoặc đảm bảo cho các khối dữ liệu, từ đó đảm bảo **chất lượng dịch vụ** (Quality of Service, QoS).

Thuật ngữ **“chất lượng dịch vụ”** không ám chỉ “tốc độ” mà các gói tin được truyền từ người gửi đến người nhận, mà là cách thức chúng được truyền. Các gói tin có thể được truyền qua các tuyến đường khác nhau, có thể được đưa vào bộ đệm của thiết bị mạng và chờ đợi lâu hoặc được truyền trước các gói tin khác, thậm chí có thể bị loại bỏ. Lưu lượng của các ứng dụng khác nhau yêu cầu băng thông khác nhau. Các chức năng QoS trong mạng hiện đại nhằm đảm bảo mức dịch vụ đảm bảo hoặc phân biệt cho lưu lượng mạng. Chi tiết về các chức năng chất lượng dịch vụ có thể tham khảo trong khóa học “Công nghệ chuyển mạch của các mạng Ethernet hiện đại”.

**Ghép kênh thống kê** được sử dụng trong các mạng chuyển mạch gói và mạng chuyển mạch tế bào. Khác với TDM đồng bộ, nó không “trong suốt” đối với các giao thức, vì nó được thực hiện ở tầng liên kết và các tầng cao hơn trong mô hình OSI. Các nút cuối và thiết bị mạng phải hỗ trợ các giao thức giống nhau. Ví dụ về ứng dụng của TDM không đồng bộ bao gồm các giao thức trong họ Ethernet, giao thức IP, các giao thức TCP và UDP, giao thức ATM (Asynchronous Transfer Mode).


### 3.4.2 Ghép kênh phân chia theo tần số

Trong ghép kênh tần số hoặc ghép kênh phân chia theo tần số (Frequency Division Multiplexing - FDM), băng thông rộng của kênh vật lý $$F$$ được chia thành $$n$$ dải tần số hẹp $$f \ll F$$, trong mỗi dải tần này tạo ra một kênh logic. Kích thước của các dải tần số $$f$$ có thể khác nhau. Mỗi hệ thống tương tác được chỉ định một dải tần riêng (kênh logic). Các bộ phát có thể gửi tín hiệu đồng thời. Tín hiệu truyền qua các kênh logic khác nhau được đặt trên các tần số sóng mang khác nhau và do đó trong miền tần số không nên chồng chéo nhau. Để loại bỏ ảnh hưởng lẫn nhau của các tín hiệu truyền qua các kênh logic khác nhau, các dải bảo vệ được hình thành giữa chúng, đóng vai trò là biên giới giữa các kênh.

Tuy nhiên, mặc dù có các dải bảo vệ, các thành phần phổ của tín hiệu vẫn có thể vượt quá giới hạn của kênh logic và gây nhiễu cho kênh logic lân cận.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_17_Frequency_Division_Multiplexing.png" alt="Hình 3.17 Ghép kênh phân chia theo tần số" width="900">
</p>
<p align="center"><b>Hình 3.17 Ghép kênh phân chia theo tần số</b></p>


Ưu điểm của ghép kênh tần số là cho phép truyền đồng thời các tín hiệu bởi nhiều hệ thống tương tác. Tuy nhiên, vì mỗi hệ thống được chỉ định một kênh riêng biệt theo cách tĩnh, điều này dẫn đến việc sử dụng không hiệu quả băng thông của kênh truyền chung. Tại một thời điểm, một hệ thống có thể không có dữ liệu để truyền và kênh sẽ để trống, trong khi các hệ thống khác có thể thiếu tài nguyên từ các kênh logic được phân bổ cho chúng. Ngoài ra, sự tồn tại của các dải bảo vệ giữa các kênh logic làm giảm băng thông có sẵn để truyền.

Ghép kênh phân chia theo tần số là một phương pháp ghép kênh được sử dụng rộng rãi trong phát thanh và truyền hình cũng như trong truyền thông di động. Nó cũng được sử dụng trong các mạng dựa trên công nghệ xDSL.

Tuy nhiên, trong ghép kênh tần số, có thể chia băng thông thành các kênh mà không cần sử dụng dải bảo vệ. 

Trong ghép kênh phân chia theo tần số trực giao (Orthogonal Frequency Division Multiplexing - OFDM), toàn bộ băng thông của kênh vật lý được chia thành nhiều tần số con (subcarriers) hoặc các kênh con. Các tần số con này có thể lên đến hàng chục, thậm chí hàng nghìn. Mỗi bộ phát được chỉ định để truyền trên một số tần số con nhất định, được chọn từ nhiều tần số con theo một quy luật xác định. Các tần số con này là trực giao với nhau, nghĩa là việc truyền thông tin trên mỗi tần số con không ảnh hưởng đến các tần số con lân cận. Như được thể hiện trong Hình 3.18, các trung tâm của tần số con được đặt sao cho mức năng lượng tối đa của một tần số con trùng với mức năng lượng tối thiểu của các tần số con khác, mặc dù tín hiệu của chúng chồng chéo nhau trong phổ tần số. Cách sắp xếp này cho phép sử dụng băng thông có sẵn một cách hiệu quả hơn.

Truyền dẫn được thực hiện đồng thời trên tất cả các tần số con. Luồng dữ liệu tốc độ cao ở đầu phát được chia thành $$n$$ luồng tốc độ thấp (với $$n$$ là số lượng tần số con được chỉ định cho bộ phát đó), mỗi luồng trong số đó được điều chế trên một tần số con riêng biệt. Phân bổ các tần số con có thể thay đổi động trong quá trình hoạt động.

Để truyền một tín hiệu phức tạp, bao gồm nhiều tần số con, phép biến đổi Fourier ngược nhanh (IFFT) được sử dụng. Bộ phát sẽ lấy các tín hiệu điều chế từ mỗi kênh con, cộng chúng lại để tạo thành một tín hiệu tổng hợp. Tín hiệu OFDM tổng hợp có thể được xem như một tập hợp các tín hiệu hẹp băng được điều chế chậm, thay vì một tín hiệu rộng băng được điều chế nhanh. Khi nhận tín hiệu, phép biến đổi Fourier nhanh (FFT) sẽ được thực hiện. Tất cả các tần số con được tách ra đồng thời và các thông số mang thông tin của từng tần số con (biên độ và/hoặc pha) được xác định.

Ngoài việc sử dụng băng thông hiệu quả, OFDM còn giúp giảm các hiệu ứng tiêu cực nổi tiếng của hiện tượng đa đường và nhiễu liên ký tự. Tín hiệu OFDM kết hợp nhiều kênh con hẹp băng, mỗi kênh có thể truyền ở tốc độ thấp. Do đó, hệ thống chỉ gặp phải nhiễu liên ký tự ở mức tối thiểu, điều mà các hệ thống tốc độ cao dễ bị ảnh hưởng.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_18_Orthogonal_Frequency_Division_Multiplexing.png" alt="Hình 3.18 Ghép kênh phân chia theo tần số trực giao" width="700">
</p>
<p align="center"><b>Hình 3.18 Ghép kênh phân chia theo tần số trực giao</b></p>



OFDM không phải là một công nghệ mới. Phần lớn các nghiên cứu cơ bản mô tả hoạt động của nó xuất hiện vào những năm 1960. Nó được sử dụng rộng rãi trong mạng không dây chuẩn 802.11, mạng truyền hình cáp, mạng dựa trên dây điện, mạng dựa trên công nghệ xDSL và mạng truyền dữ liệu di động thế hệ thứ 4 (LTE).



### 3.4.3 Ghép Kênh Phân Chia Theo Bước Sóng

**Ghép kênh phân chia theo bước sóng** (Wavelength Division Multiplexing, WDM) hoặc **ghép kênh theo bước sóng** được sử dụng trong các kênh truyền dẫn quang và là một biến thể của ghép kênh phân chia tần số. Công nghệ WDM cho phép truyền đồng thời và độc lập hai hoặc nhiều tín hiệu quang qua một sợi quang bằng cách sử dụng các bước sóng khác nhau. Công nghệ này cũng cho phép truyền dẫn hai chiều qua một sợi quang (truyền trên một bước sóng và nhận trên một bước sóng khác).

Các tín hiệu từ mỗi kênh đầu vào được mang trong một dải tần riêng biệt. Sau đó, chúng được tập hợp lại trong bộ ghép kênh và truyền qua một sợi quang, tạo thành một kênh băng thông rộng. Phân chia tần số trong sợi quang được thực hiện bằng cách truyền các tia sáng với các bước sóng khác nhau: mỗi bộ phát laser sẽ phát ánh sáng ở một tần số xác định (tần số trong dải ánh sáng) vào một sợi quang. Ánh sáng của mỗi nguồn sẽ đi qua sợi quang một cách độc lập. Do đó, nhiều kênh độc lập được tạo ra song song trong cùng một sợi, giúp tăng băng thông của hệ thống truyền dẫn tổng thể.

Ở phía nhận, bộ tách sóng phân chia các tần số của tín hiệu bằng các bộ lọc.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_19_Wavelength_division_multiplexing.png" alt="Hình 3.19 Ghép kênh phân chia bước sóng" width="800">
</p>
<p align="center"><b>Hình 3.19 Ghép kênh phân chia bước sóng</b></p>


**Công nghệ WDM** được triển khai ở tầng vật lý của mô hình OSI nên nó **trong suốt đối với các giao thức tầng trên**. Phần lớn các hệ thống WDM sử dụng các cáp quang đơn mode có đường kính sợi 9/125 µm.

Cách triển khai đơn giản và rẻ nhất của công nghệ WDM sử dụng hai kênh – một kênh có bước sóng 1310 nm và kênh còn lại là 1550 nm. Để tạo ra hệ thống WDM loại này, có thể sử dụng các bộ thu phát quang mà không cần kiểm soát chặt chẽ các bước sóng.

**Công nghệ CWDM** (Coarse WDM, ghép kênh phân chia bước sóng thưa) là sự phát triển của công nghệ WDM, cho phép sử dụng tối đa 18 kênh quang (như quy định trong ITU-T G.694.2) với khoảng cách giữa các bước sóng là 20 nm để truyền tín hiệu quang. Các kênh quang nằm trong dải từ 1271 đến 1611 nm. Do độ suy hao cao trong dải từ 1271–1451 nm, hầu hết các hệ thống CWDM chỉ sử dụng 8 kênh trong khoảng từ 1471–1611 nm. Dữ liệu trên mỗi kênh có thể truyền với tốc độ lên tới 10 Gbps.

Để tạo hệ thống CWDM, người ta sử dụng các bộ thu phát quang, các bộ ghép kênh và tách kênh với các bước sóng xác định, nhưng vì các bước sóng này không cần phải kiểm soát chặt chẽ, nên chi phí thiết bị này thấp hơn so với thiết bị của hệ thống DWDM.

**Công nghệ Dense WDM** (DWDM, ghép kênh phân chia bước sóng dày đặc) cũng là một biến thể của công nghệ WDM và cho phép truyền 40, 80 và thậm chí 160 kênh quang trong dải hẹp giữa 1525–1565 nm hoặc 1570–1610 nm (lưới tần số DWDM được quy định trong ITU-T G.694.1-2012). Các kênh quang cách nhau khoảng 0,8 nm, 0,4 nm hoặc 0,2 nm. Dữ liệu trên mỗi kênh có thể truyền với tốc độ 10 Gbps, với khả năng nâng cấp lên dịch vụ 40 Gbps và 100 Gbps.

Công nghệ DWDM phức tạp hơn so với CWDM và yêu cầu kiểm soát chặt chẽ các bước sóng và ổn định nhiệt độ của thiết bị — bao gồm các bộ thu phát quang, các bộ ghép kênh và tách kênh.

Công ty D-Link cung cấp các bộ thu phát quang SFP, XFP và SFP+ để tạo hệ thống WDM và CWDM. Bài giảng 5 sẽ giới thiệu về các bộ thu phát quang này.

**Công nghệ WDM** chủ yếu được sử dụng trên các tuyến truyền dẫn dài, nơi yêu cầu băng thông lớn. Việc sử dụng WDM giúp tránh phải lắp đặt thêm các cáp quang mới trong mạng hiện tại và tăng băng thông của kênh quang sẵn có bằng cách tăng số lượng kênh logic (các bước sóng phát ra từ các bộ phát laser). Điều này đặc biệt quan trọng khi lưu lượng dữ liệu ngày càng tăng, cho phép các nhà cung cấp dịch vụ cung cấp thêm dịch vụ cho khách hàng. Một dịch vụ mới có thể được thêm vào trên hệ thống cáp quang hiện có mà không làm gián đoạn dịch vụ cho khách hàng.

Bên cạnh việc cung cấp các dịch vụ, việc sử dụng WDM cũng cho phép các nhà khai thác dịch vụ viễn thông cung cấp dịch vụ cho thuê “sợi quang ảo”, tức là cho thuê từng bước sóng riêng lẻ.

Phương pháp ghép kênh theo tần số (bước sóng) và ghép kênh theo thời gian có thể được sử dụng đồng thời. Trong trường hợp này, các băng tần được chia sẻ trong một kênh vật lý. Trong bất kỳ băng tần nào, mỗi hệ thống đều được cung cấp các khoảng thời gian nhất định để truyền dữ liệu.

Ví dụ về kết hợp giữa ghép kênh theo tần số và ghép kênh theo thời gian là **hệ thống thông tin di động GSM** (Global System for Mobile Communications).

---

### 3.4.4 Ghép kênh phân chia theo mã

**Ghép kênh phân chia theo mã (Code Division Multiplexing, CDM)** khác biệt so với ghép kênh theo tần số và ghép kênh theo thời gian. Trong phương pháp này, tất cả các kênh đều sử dụng cùng một phổ tần số vào cùng một thời điểm, nhưng mỗi kênh sẽ có một mã riêng biệt.

CDM dựa trên nguyên lý mở rộng phổ (Spread Spectrum). Ý tưởng chính của mở rộng phổ là chuyển đổi tín hiệu thông tin với băng thông hẹp thành tín hiệu có băng thông rộng. Điều này đạt được bằng cách điều chế tín hiệu thông tin với mã mở rộng, mã này hoàn toàn độc lập với tín hiệu thông tin và có băng thông lớn hơn. Kết quả của quá trình điều chế là công suất của tín hiệu gốc không thay đổi mà được phân bố trên một dải băng tần rộng hơn. Nói cách khác, băng tần của tín hiệu truyền đi được mở rộng đáng kể (mở rộng phổ tín hiệu).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_20_Spread_Spectrum_Method.png" alt="Hình 3.20 Phương pháp mở rộng phổ" width="800">
</p>
<p align="center"><b>Hình 3.20 Phương pháp mở rộng phổ</b></p>



Các mã mở rộng được chọn sao cho tín hiệu trở nên giống như nhiễu. Nhờ vậy, nhiều người dùng có thể đồng thời sử dụng cùng một dải tần số với mức nhiễu tương tác thấp.

Trong CDM, có một yêu cầu bổ sung đối với các mã mở rộng: chúng phải độc lập với nhau. Mã mở rộng là duy nhất cho mỗi bộ phát và được sử dụng để xác định kết nối. Nó là một chuỗi các bit dài 11, 16, 32, 64, v.v. (được gọi là chuỗi chip hoặc chip). Để tạo ra tín hiệu có phổ mở rộng, bộ phát thay thế mỗi bit trong dòng dữ liệu gốc bằng mã mở rộng thông qua phép toán XOR (hoặc loại trừ). Sau đó, tín hiệu giống như nhiễu này được truyền bởi bộ phát vào kênh chung, nơi đồng thời truyền các tín hiệu từ nhiều bộ phát khác.

Mỗi tín hiệu truyền đi có một mã mở rộng riêng biệt. Bộ thu biết mã mở rộng của bộ phát mà nó cần nhận tín hiệu. Điều này cho phép bộ thu tách tín hiệu dành cho nó ra khỏi nhiều tín hiệu nhận được. Trong quá trình này, tín hiệu của các bộ phát khác với các mã mở rộng khác nhau được bộ thu xem như nhiễu cộng.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_21_Code_Division_Multiplexing.png" alt="Hình 3.21 Ghép kênh phân chia theo mã" width="800">
</p>
<p align="center"><b>Hình 3.21 Ghép kênh phân chia theo mã</b></p>


Ưu điểm chính của phương pháp ghép kênh này là tính bảo mật và độ ẩn danh cao trong truyền dữ liệu: nếu không biết mã, không thể nhận tín hiệu, và trong một số trường hợp cũng không thể phát hiện sự hiện diện của nó. Ban đầu, phương pháp này được sử dụng trong các ứng dụng quân sự (bài báo đầu tiên về chủ đề này được công bố vào năm 1935 bởi nhà khoa học Liên Xô D.V. Ageev), sau đó được áp dụng trong các ứng dụng dân sự. Ngoài ra, không gian mã rộng hơn nhiều so với phương pháp ghép kênh theo tần số, cho phép dễ dàng gán mã riêng cho mỗi bộ phát mà không gặp vấn đề đáng kể. Tuy nhiên, vấn đề chính của ghép kênh theo mã trong thời gian dài là khó khăn trong việc thực hiện kỹ thuật cho các bộ thu và yêu cầu phải đảm bảo đồng bộ chính xác giữa bộ phát và bộ thu để đảm bảo nhận đúng khối dữ liệu.

CDM được sử dụng chủ yếu trong các mạng di động. Cơ chế này là nền tảng cho phương pháp truy cập đa mã (Code Division Multiple Access, CDMA), tên của nó được sử dụng để đặt tên cho tiêu chuẩn truyền thông di động IS-95a, cũng như một số tiêu chuẩn của hệ thống di động thế hệ thứ ba (CDMA2000, WCDMA, v.v.).

---

### 3.4.5 Ghép kênh và các phương pháp truy cập đa người dùng

Ghép kênh và truy cập đa người dùng (multiple access) có điểm chung là đều nhằm chia sẻ tài nguyên chung giữa các người dùng. Ghép kênh cho phép nhiều người dùng sử dụng chung một kênh vật lý để truyền nhiều thông điệp cùng lúc. Các phương pháp truy cập đa người dùng dựa trên các phương pháp ghép kênh theo thời gian, tần số và mã, giúp xác định cách các kênh logic được phân phối giữa nhiều người dùng, đồng thời quản lý tình huống khi nhiều người dùng cùng lúc muốn sử dụng một kênh (trong trường hợp số kênh logic ít hơn số người dùng).

Ghép kênh được thực hiện ở tầng vật lý của mô hình OSI, trong khi các phương pháp truy cập đa người dùng được thực hiện ở cả tầng vật lý và tầng liên kết của mô hình OSI.

Các phương pháp truy cập dựa trên ghép kênh phân chia theo thời gian (TDM) bao gồm:

- Truy cập đa người dùng phân chia theo thời gian (TDMA, Time Division Multiple Access);
- Truy cập đa người dùng có kiểm soát sóng mang và phát hiện va chạm (CSMA/CD, Carrier Sense Multiple Access With Collision Detection);
- Truy cập đa người dùng có kiểm soát sóng mang và tránh va chạm (CSMA/CA, Carrier Sense Multiple Access with Collision Avoidance);
- Truyền bằng mã thông (Token passing).

Các phương pháp truy cập dựa trên ghép kênh phân chia theo tần số (FDM) bao gồm:

- Truy cập đa người dùng phân chia theo tần số (FDMA, Frequency Division Multiple Access);
- Truy cập đa người dùng phân chia theo tần số trực giao (OFDMA, Orthogonal Frequency Division Multiple Access);
- Truy cập đa người dùng phân chia theo bước sóng (WDMA, Wavelength Division Multiple Access).

Phương pháp truy cập đa người dùng phân chia theo mã (CDMA, Code Division Multiple Access) được dựa trên ghép kênh phân chia theo mã (CDM).

---
## 3.5 Điều chế và mã hóa tín hiệu

Thông thường, các tín hiệu thông tin có tần số thấp và giới hạn về độ rộng phổ (băng tần cơ bản). Việc truyền các tín hiệu băng tần cơ bản trực tiếp (trong dải tần số cơ bản) được thực hiện bởi các kênh truyền cơ bản (baseband channel). Các kênh này có băng thông hẹp, do đó toàn bộ băng thông được sử dụng để truyền tín hiệu.

Tuy nhiên, trong nhiều trường hợp, không thể truyền tín hiệu gốc trực tiếp qua kênh truyền. Ví dụ, kênh truyền là kênh tần số cao, băng rộng và được thiết kế để truyền tín hiệu từ nhiều nguồn đồng thời bằng cách phân chia tần số các kênh.

Để dịch phổ của tín hiệu từ vùng tần số thấp sang vùng tần số cao dành cho truyền dẫn, cần sử dụng điều chế.

Giả sử tín hiệu tần số thấp cần truyền qua kênh truyền được xác định bởi hàm $$s(t)$$. Trong kênh truyền, một dải tần số cao được dành để truyền tín hiệu này. Ở đầu vào của kênh truyền, một thiết bị truyền đặc biệt tạo ra tín hiệu tần số cao phụ trợ, thường là tín hiệu liên tục theo thời gian $$u(t)$$. Nếu thay đổi các tham số của tín hiệu $$u(t)$$ theo dạng của tín hiệu $$s(t)$$, thì dạng của tín hiệu $$u(t)$$ sẽ có thuộc tính mới, mang thông tin giống như trong tín hiệu $$s(t)$$.

Do đó, tín hiệu $$u(t)$$ được gọi là tín hiệu sóng mang, dao động mang hoặc chỉ đơn giản là sóng mang (carrier), và quá trình chuyển tải thông tin vào các tham số của tín hiệu sóng mang được gọi là điều chế của nó (modulation).

**Điều chế** là quá trình thay đổi một tín hiệu theo dạng của một tín hiệu khác.  
Tín hiệu thông tin $$s(t)$$ được gọi là tín hiệu điều chế (modulating signal), và kết quả của điều chế là tín hiệu đã được điều chế (modulated signal). Quá trình ngược lại là tách tín hiệu điều chế ra khỏi dao động đã được điều chế, gọi là giải điều chế (demodulation).

Các thao tác điều chế và giải điều chế được thực hiện bằng modem (modem: modulator - demodulator), là một thiết bị riêng hoặc tích hợp trong các thiết bị khác.

Mục đích chính của điều chế là dịch phổ của tín hiệu sang một dải tần khác, đảm bảo cơ chế biểu diễn thông tin ít nhạy cảm với nhiễu và giao thoa, và khả năng sử dụng các phương pháp ghép kênh và truy cập đa người dùng.

Khi truyền dẫn băng rộng, việc sử dụng nhiều sóng mang có tần số khác nhau cho phép truyền nhiều kênh logic trong một kênh vật lý duy nhất.

Để phân biệt điều chế Tín hiệu tương tự (Analog signal) và tín hiệu số, điều chế Tín hiệu tương tự (Analog signal) trên cơ sở sóng mang được gọi là **điều chế tương tự** (analog modulation), còn điều chế tín hiệu số trên cơ sở sóng mang được gọi là **điều chế số** (digital modulation) hay thao tác điều chế.

Sóng mang thường cần thiết khi truyền dữ liệu qua dây điện thoại, môi trường không khí hoặc cáp quang. Tuy nhiên, trong một số trường hợp, điều chế có thể được thực hiện trên cơ sở các tín hiệu rời rạc dưới dạng các xung. Đối với truyền dẫn tín hiệu dựa trên các chuỗi xung tuần hoàn, sử dụng **điều chế xung** (pulse modulation).

Khi truyền tín hiệu số qua các kênh truyền băng cơ bản, các phương pháp mã hóa tuyến tính hoặc mã hóa số tín hiệu (line coding) được áp dụng.

---

### 3.5.1 Các phương pháp điều chế tương tự

Việc sử dụng điều chế tương tự cho dữ liệu tương tự có thể không rõ ràng ngay. Tín hiệu âm thanh thường được truyền qua đường dây điện thoại với phổ gốc được giữ nguyên, tức là không cần điều chế. Tuy nhiên, trong các môi trường phi định hướng, việc truyền Tín hiệu tương tự (Analog signal) mà không điều chế là gần như không khả thi — sẽ cần đến các ăng-ten dài hàng km. Để đạt hiệu quả trong truyền dẫn, có thể cần sử dụng tần số cao hơn cũng như khả năng ghép kênh theo tần số.

Điều chế tương tự dựa trên việc truyền tín hiệu tần số thấp bằng sóng mang tần số cao. Dạng chính của sóng mang là dao động điều hòa, có ba tham số tự do: biên độ, pha và tần số.

Dựa trên việc thông tin được mang trên tham số nào trong ba tham số này, có các loại điều chế biên độ (AM), điều chế tần số (FM) hoặc điều chế pha (PM) của sóng mang. Điều chế tần số và điều chế pha có liên quan với nhau, vì cả hai đều thay đổi tham số của hàm cosin, và chúng thường được gộp chung dưới tên gọi điều chế góc (angle modulation). 

- **Điều chế biên độ** (Amplitude Modulation, AM) là thay đổi biên độ của sóng mang theo biên độ tức thời của tín hiệu điều chế.
- **Điều chế tần số** (Frequency Modulation, FM) là thay đổi tần số của sóng mang theo biên độ tức thời của tín hiệu điều chế.
- **Điều chế pha** (Phase Modulation, PM) là thay đổi pha của sóng mang theo biên độ tức thời của tín hiệu điều chế.

Điều chế tương tự được sử dụng trong phát thanh, khi nhiều đài phát cùng hoạt động trong một môi trường truyền dẫn chung: điều chế biên độ (AM) cho các đài phát trong dải sóng AM và điều chế tần số (FM) cho các đài trong dải sóng FM.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_22_Amplitude_and_frequency_modulation_of_an_analog_signal.png" alt=" Hình 3.22: Điều chế biên độ và điều chế tần số của Tín hiệu tương tự (Analog signal)" width="500">
</p>
<p align="center"><b> Hình 3.22: Điều chế biên độ và điều chế tần số của Tín hiệu tương tự (Analog signal)</b></p>

---

### 3.5.2 Phương pháp điều chế số

Quá trình truyền dữ liệu số thông qua sóng mang được gọi là điều chế số hoặc điều biến số.

Để có thể truyền dữ liệu số qua kênh tương tự, dữ liệu cần được chuyển đổi thành Tín hiệu tương tự (Analog signal) cơ sở trước, sau đó tín hiệu này sẽ được đặt ở tần số sóng mang để truyền tối ưu qua môi trường vật lý. Ví dụ về các mạng mà dữ liệu số được truyền qua Tín hiệu tương tự (Analog signal) bao gồm mạng điện thoại công cộng và mạng không dây.

Như đã đề cập trước đó, trong quá trình điều chế, một trong ba đặc điểm của tín hiệu sóng mang sẽ được sử dụng: biên độ, pha và tần số. Do đó, có ba công nghệ điều chế chính thực hiện chuyển đổi dữ liệu số thành Tín hiệu tương tự (Analog signal):

- Điều biến biên độ (Amplitude-Shift Keying, ASK);
- Điều biến tần số (Frequency-Shift Keying, FSK);
- Điều biến pha (Phase-Shift Keying, PSK).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_23_Modulation_of_digital_data_by_analog_signals.png" alt="  Hình 3.23 Điều chế dữ liệu số với tín hiệu analog" width="900">
</p>
<p align="center"><b> Hình 3.23 Điều chế dữ liệu số với tín hiệu analog</b></p>


#### Điều biến biên độ (Amplitude-Shift Keying, ASK)

Trong điều biến biên độ, các giá trị "0" và "1" được biểu diễn bằng các tín hiệu sóng mang với hai biên độ khác nhau. Một trong các biên độ thường được chọn bằng không; tức là, một giá trị nhị phân được biểu diễn bằng sự hiện diện của sóng mang với biên độ cố định, và giá trị khác là sự vắng mặt của nó.

Công thức tín hiệu:

$$
y(t) = 
\begin{cases}
A \cos(2\pi f_c t) & \text{— nhị phân 1} \\
0 & \text{— nhị phân 0}
\end{cases}
$$

trong đó:
- $$A \cos(2\pi f_c t)$$: tín hiệu sóng mang,
- $$y(t)$$: tín hiệu đầu ra.

Điều biến biên độ là một trường hợp đặc biệt của điều chế biên độ vuông góc.



#### Điều biến tần số (Frequency-Shift Keying, FSK)

Trong điều biến tần số, thông tin số được biểu diễn bằng cách thay đổi tần số của sóng mang. Dạng đơn giản nhất của điều biến tần số là **điều biến tần số nhị phân** (Binary FSK, BFSK), trong đó các giá trị "0" và "1" được biểu diễn bằng các tín hiệu có hai tần số khác nhau, nằm gần tần số sóng mang.

Công thức tín hiệu:

$$
y(t) = 
\begin{cases}
A \cos(2\pi f_1 t) & \text{— nhị phân 1} \\
A \cos(2\pi f_2 t) & \text{— nhị phân 0}
\end{cases}
$$

trong đó:
- $$f_1$$ và $$f_2$$: các tần số được dịch từ tần số sóng mang $$f_c$$ với các giá trị bằng nhau về độ lớn, nhưng ngược dấu.

Điều biến tần số được sử dụng trong các modem đầu tiên và cho phép thực hiện truyền dữ liệu song công trên các đường dây điện thoại.



#### Điều biến pha (Phase-Shift Keying, PSK)

Trong điều biến pha, dữ liệu được biểu diễn bằng cách thay đổi pha của sóng mang. Hiện nay có nhiều biến thể của điều biến pha được phát triển để truyền dữ liệu ở các mạng không dây theo tiêu chuẩn IEEE 802.11.

Hình thức đơn giản nhất của điều biến pha là **điều biến pha nhị phân** hay **điều biến pha hai mức** (Binary PSK, BPSK), trong đó hai pha của sóng mang 0° và 180° được sử dụng để biểu diễn hai chữ số nhị phân.

Công thức tín hiệu:

$$
y(t) = 
\begin{cases}
A \cos(2\pi f_c t) & \text{— nhị phân 1} \\
A \cos(2\pi f_c t + \pi) & \text{— nhị phân 0}
\end{cases}
$$



#### Điều biến pha nhị phân (Binary PSK, BPSK)

BPSK là loại điều biến pha có khả năng chống nhiễu cao nhất, nhưng với mỗi lần thay đổi tín hiệu, nó chỉ có thể truyền 1 bit thông tin. Điều này khiến BPSK không phù hợp cho các ứng dụng yêu cầu tốc độ cao.

Một dạng khác của PSK hai mức là **Điều biến pha nhị phân vi sai** (Differential BPSK, DBPSK). Trong DBPSK, dữ liệu không được mã hóa trực tiếp theo bit thông tin mà dựa trên sự thay đổi của bit. Khi truyền giá trị nhị phân 0, pha của sóng mang không thay đổi, còn khi truyền giá trị nhị phân 1, pha của sóng mang sẽ thay đổi ngược lại. Nói cách khác, sự thay đổi pha phụ thuộc vào pha của tín hiệu trước đó.


#### Điều biến pha bốn mức hoặc điều biến pha vuông góc (Quadrature PSK, QPSK)

**Điều biến pha vuông góc** (Quadrature PSK, QPSK) sử dụng bốn giá trị pha khác nhau của sóng mang, với mỗi giá trị pha đại diện cho hai bit dữ liệu. So với BPSK, QPSK có thể tăng gấp đôi tốc độ truyền và sử dụng hiệu quả hơn băng thông. 

Trong QPSK, thay vì sử dụng dịch pha 180°, các pha dịch được chọn là bội số của π/2 (90°). Các giá trị bit được chọn sao cho khi thay đổi giữa các trạng thái pha lân cận của sóng mang, lỗi trong quá trình truyền chỉ gây ra lỗi một bit.

Công thức tín hiệu cho QPSK:

$$
y(t) = 
\begin{cases}
A \cos\left(2\pi f_c t + \frac{\pi}{4}\right) & \text{— 11} \\
A \cos\left(2\pi f_c t + \frac{3\pi}{4}\right) & \text{— 10} \\
A \cos\left(2\pi f_c t + \frac{5\pi}{4}\right) & \text{— 00} \\
A \cos\left(2\pi f_c t + \frac{7\pi}{4}\right) & \text{— 01}
\end{cases}
$$


#### Điều biến pha vi sai bốn mức (Differential QPSK, DQPSK)

Trong **Điều biến pha vi sai bốn mức** (Differential QPSK, DQPSK), tương tự như DBPSK, sự thay đổi pha xảy ra khi có sự thay đổi bit thông tin.



#### Điều biến biên độ vuông góc (Quadrature Amplitude Modulation, QAM)

**Điều biến biên độ vuông góc** (Quadrature Amplitude Modulation, QAM) được sử dụng rộng rãi trong các tiêu chuẩn mạng không dây và có dây, là một phương pháp truyền Tín hiệu tương tự (Analog signal).

Kỹ thuật điều chế này kết hợp giữa điều chế biên độ và điều chế pha. Phương pháp QAM cho phép truyền đồng thời hai tín hiệu khác nhau trên cùng một tần số sóng mang, sử dụng hai bản sao của sóng mang dịch pha nhau 90°. Trong QAM, hai tín hiệu độc lập được điều chế theo cả biên độ và pha, sau đó truyền qua môi trường. Tín hiệu được giải điều chế ở phía thu và được kết hợp để tái tạo lại tín hiệu nhị phân ban đầu.


Khi sử dụng điều biến biên độ hai mức (2QAM), mỗi luồng dữ liệu có thể có hai trạng thái, tạo ra một kết hợp hai trạng thái — tổng cộng có $$2 \times 2 = 4$$ trạng thái. Khi sử dụng điều biến biên độ bốn mức (4QAM), với bốn mức biên độ khác nhau, luồng dữ liệu kết hợp sẽ có tổng cộng $$4 \times 4 = 16$$ trạng thái. Hiện nay, có những hệ thống sử dụng 64 trạng thái (64QAM) hoặc thậm chí 256 trạng thái (256QAM). 

Số trạng thái càng lớn, tốc độ truyền càng cao, nhưng cũng tăng khả năng xảy ra lỗi do nhiễu hoặc suy hao tín hiệu.

---

### 3.5.3 Các phương pháp điều chế xung

Trong các phần trước, chúng ta đã xem xét các phương pháp điều chế sử dụng tín hiệu hài làm sóng mang. Trong hệ thống truyền thông, sóng mang dưới dạng chuỗi xung được sử dụng rộng rãi. Phương pháp điều chế sử dụng sóng mang như vậy được gọi là **điều chế xung** (Impulse Modulation). Nó được sử dụng để truyền dữ liệu đã được số hóa qua các kênh truyền thông. Ngoài ra, điều chế xung còn cho phép truyền đồng thời nhiều tín hiệu qua một kênh bằng cách **ghép kênh phân chia theo thời gian** (Time Division Multiplexing).

Thao tác thay thế hàm liên tục bằng chuỗi các giá trị tức thời của nó được gọi là **lấy mẫu** (discretization).

Trong điều chế xung, sóng mang có dạng chuỗi xung tuần hoàn. Xung được mô tả bằng các tham số như biên độ, độ dài, tần số lặp lại và pha ban đầu. Tùy thuộc vào tham số của xung thay đổi, người ta phân loại các loại điều chế xung như sau:

- Điều chế xung biên độ (Amplitude Impulse Modulation - AIM),
- Điều chế xung tần số (Frequency Impulse Modulation - FIM),
- Điều chế xung độ rộng (Pulse Width Modulation - PWM),
- Điều chế xung vị trí (Pulse Position Modulation - PPM),
- Điều chế xung mã (Pulse Code Modulation - PCM).

Cơ sở lý thuyết của tất cả các phương pháp điều chế xung là **định lý Nyquist-Kotelnikov**. Theo định lý này, bất kỳ tín hiệu liên tục nào với phổ tần giới hạn (từ 0 đến $$F_{max}$$) đều có thể được mô tả hoàn toàn bằng chuỗi các giá trị của nó tại các thời điểm cách nhau một khoảng thời gian $$T = 1/(2F_{max})$$, trong đó $$F_{max}$$ là tần số tối đa trong phổ của tín hiệu thông tin. Tần suất lấy mẫu càng cao thì tín hiệu điều chế sẽ được biểu diễn càng chính xác. Tần số tối thiểu của xung phụ thuộc vào định lý Nyquist-Kotelnikov.

Trong **điều chế xung biên độ** (Amplitude Impulse Modulation - AIM, hay Pulse Amplitude Modulation - PAM), biên độ của xung được thay đổi để truyền dữ liệu. Các tham số khác của xung không thay đổi. Trong trường hợp điều chế dữ liệu analog, biên độ của xung thay đổi theo biên độ của tín hiệu điều chế, và số mức biên độ của xung về lý thuyết có thể không giới hạn. Trong truyền dữ liệu số, số lượng mức biên độ khả thi bị giới hạn ở một số cấp độ cụ thể.

Điều chế xung biên độ (PAM) được sử dụng trong chuẩn IEEE 802.3. Ví dụ, trong đặc tả tầng vật lý của **Ethernet 1000Base-T** (Gigabit Ethernet qua cáp xoắn đôi), phương pháp PAM với 5 mức biên độ (PAM-5) được sử dụng. Bốn mức dùng để mã hóa hai bit thông tin, và mức thứ năm là dư thừa, được dùng để sửa lỗi. Đặc tả **10GBASE-T** (Ethernet 10 Gigabit) sử dụng phiên bản THP của mã hóa Tomlinson-Harashima (THP-coding) với 16 mức biên độ trong điều chế PAM.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_24_Pulse_amplitude_modulation_of_an_analog_signal.png" alt="  Hình 3.24 Điều chế biên độ xung của tín hiệu analog" width="900">
</p>
<p align="center"><b> Hình 3.24 Điều chế biên độ xung của tín hiệu analog</b></p>



#### Điều chế xung độ rộng (PWM - Pulse Width Modulation)

**Điều chế xung độ rộng** (PWM, Pulse Width Modulation), đôi khi còn được gọi là điều chế theo độ dài xung, là phương pháp điều chế trong đó độ dài của xung được điều chỉnh tỷ lệ với hàm của tín hiệu điều chế, trong khi biên độ của xung và khoảng cách giữa các xung được giữ cố định. 

#### Điều chế xung vị trí (PPM - Pulse Position Modulation)

Trong **điều chế xung vị trí** (PPM, Pulse Position Modulation), các xung có biên độ và độ dài như nhau nhưng vị trí của chúng lệch khỏi điểm bắt đầu chu kỳ theo khoảng thời gian tỷ lệ với tín hiệu thông tin. Phương pháp điều chế này thường được sử dụng trong truyền dẫn dữ liệu qua các kênh quang học.

#### Điều chế xung mã (PCM - Pulse Code Modulation)

**Điều chế xung mã** (PCM, Pulse Code Modulation) là phương pháp chuyển đổi dữ liệu tương tự thành tín hiệu số. Sau đó, tín hiệu số này có thể được truyền qua kênh số bằng một trong các phương pháp mã hóa vật lý, hoặc chuyển đổi ngược lại thành Tín hiệu tương tự (Analog signal) bằng phương pháp giải mã thích hợp.

Điều chế xung mã được sử dụng rộng rãi trong điện thoại IP. Nó bao gồm quá trình lấy mẫu theo thời gian, lượng tử hóa theo mức (biên độ) và mã hóa. Quá trình lấy mẫu biên độ tương tự xảy ra trong các khoảng thời gian cố định, và mỗi giá trị mẫu sẽ được làm tròn đến mức gần nhất trong tập hợp các mức xác định trước. Quá trình này gọi là **lượng tử hóa**. Số lượng mức được chọn theo bội số của 2, chẳng hạn 2⁸ = 256, 2⁴ = 16, 2⁵ = 32, v.v. Số bit dùng để biểu diễn các mức lượng tử hóa này được gọi là **độ sâu bit**. Như vậy, sau khi lượng tử hóa, mỗi mẫu có thể được biểu diễn dưới dạng mã nhị phân n-bit.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_25_Pulse code_modulation.png" alt="  Hình 3.25 Điều chế mã xung" width="900">
</p>
<p align="center"><b> Hình 3.25 Điều chế mã xung</b></p>

---

### 3.5.4 Phương pháp mã hóa số (Digital Coding Methods)

Mã hóa số (điều chế băng gốc số) – *Digital Coding (Digital Baseband Modulation)* – được sử dụng để truyền dữ liệu số qua các kênh băng gốc (*baseband channels*). Các mã số thường phản ánh yêu cầu kỹ thuật của môi trường truyền dẫn, chẳng hạn như cáp quang (*optical cable*) hoặc cáp xoắn đôi (*twisted pair cable*). Những yêu cầu này là duy nhất cho mỗi môi trường truyền dẫn, vì mỗi loại có khả năng chống nhiễu (*noise immunity*), băng thông (*bandwidth*), và tổn thất suy hao (*attenuation losses*) khác nhau.

Khi mã hóa thông tin số, người ta sử dụng các mã tiềm năng (*potential codes*) và mã xung (*pulse codes*).

Trong các mã tiềm năng (*potential coding*), giá trị tiềm năng của tín hiệu (*signal potential*, hoặc mức điện áp – *voltage level*) được sử dụng để biểu diễn các giá trị logic 1 và 0, và không quan tâm đến các biến thiên tạo thành các xung hoàn chỉnh (*complete pulses*).

**Mã hóa tiềm năng (Potential Coding)**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_26_Potential_Coding.png" alt="Hình 3.26 Mã hóa tiềm năng" width="900">
</p>
<p align="center"><b> Hình 3.26 Mã hóa tiềm năng</b></p>



Các mã xung (*pulse codes*) cho phép biểu diễn dữ liệu nhị phân bằng cách thay đổi phân cực của xung (*pulse polarity*) (Hình 3.27, a) hoặc bằng biến thiên điện áp (*voltage transition*) (Hình 3.27, b).

**Mã hóa xung (Pulse Coding)**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_27_Pulse_Coding.png" alt="Hình 3.27 Mã hóa xung" width="900">
</p>
<p align="center"><b>Hình 3.27 Mã hóa xung</b></p>



Thời gian dành để truyền một bit (0 hoặc 1) thông tin được gọi là **khoảng thời gian bit**. Độ dài của khoảng thời gian bit $$t_b$$ được liên kết với khả năng truyền tải của kênh theo công thức: $$t_b = 1/C$$.

Như đã biết, khi truyền tín hiệu qua kênh liên lạc, tín hiệu sẽ suy giảm, và cường độ tín hiệu tại điểm nhận sẽ thấp hơn nhiều so với cường độ tín hiệu gốc. Ngoài ra, bất kỳ kênh liên lạc thực tế nào cũng có nhiễu, chồng lên tín hiệu thông tin và có thể ảnh hưởng đến việc nhận diện tín hiệu chính xác. Hiểu rõ rằng ở phía nhận, để nhận diện tín hiệu một cách chính xác, cần đọc giá trị tín hiệu ở trung tâm của khoảng thời gian bit, vì đây là nơi cường độ tín hiệu thường mạnh nhất.

Để đảm bảo truyền nhận tín hiệu chất lượng cao, cần có đồng bộ giữa các bộ đếm thời gian của máy phát và máy thu. Điều này có nghĩa là các bộ đếm thời gian ở phía phát cần xác định đúng thời điểm phát tín hiệu, trong khi ở phía thu, chúng xác định thời điểm đọc giá trị tín hiệu. Đồng bộ này giúp các bộ đếm thời gian hoạt động cùng pha, tuy nhiên trong thực tế sẽ có một số sai lệch nhỏ theo thời gian. Sai lệch này có thể gây ra lỗi đồng bộ sau một chuỗi bit dài. Để tránh các vấn đề như vậy, cần có phương pháp mã hóa tự đồng bộ hóa (*self-synchronizing codes*), cho phép các bộ đếm thời gian của máy thu và máy phát tự động đồng bộ.

Với mã hóa tiềm năng, nếu có một chuỗi dài các bit 0 hoặc 1, sẽ tạo ra tín hiệu có thành phần cố định, khiến tần số tín hiệu gần như bằng không. Trong các kênh có băng thông lớn, giới hạn tần số thấp khác biệt nhiều với 0, điều này gây khó khăn trong việc duy trì đồng bộ giữa bộ phát và bộ thu. Khi truyền các chuỗi bit xen kẽ giữa 0 và 1, thành phần cố định sẽ biến mất.

Các phương pháp mã hóa số ảnh hưởng lớn đến chất lượng truyền tải dữ liệu rời rạc và xác định khả năng băng thông yêu cầu của môi trường truyền tải.

Do đó, mã hóa số cần đáp ứng các yêu cầu sau:
- Giảm thiểu phổ của tín hiệu đầu ra ở cùng tốc độ bit;
- Cho phép nhận diện và sửa lỗi;
- Hỗ trợ đồng bộ giữa máy thu và máy phát;
- Chi phí thực hiện thấp.

Ở phía nhận, thực hiện giải mã đối xứng.

Thông thường, mã hóa có thể chia thành hai dạng chính:
- **Mã hóa logic**;
- **Mã hóa vật lý**. 

--- 

#### 3.5.4.1 Mã hóa vật lý (Physical Encoding)

**Mã hóa vật lý** (Physical Encoding) là phương pháp biểu diễn thông tin rời rạc dưới dạng các tín hiệu điện hoặc quang học được đưa vào đường truyền.

Dưới đây là những phương pháp mã hóa vật lý thường được sử dụng:

- **Mã tiềm năng không quay về 0 (NRZ, Non-Return to Zero)**
- **Mã tiềm năng không quay về 0 với đảo chiều ở bit 1 (NRZI, Non-Return to Zero with One Inverted)**
- **Mã Manchester (Manchester Code)**
- **Mã truyền tải ba mức MLТ-3 (Multi-Level Transmission-3)**

Trong phương pháp **mã hóa tiềm năng không quay về 0 (NRZ)**, mức điện áp thấp biểu diễn 0 và mức điện áp cao biểu diễn 1. Sự chuyển đổi tín hiệu diễn ra tại ranh giới của mỗi chu kỳ xung nhịp. Khi truyền một chuỗi các bit 1 liên tiếp, tín hiệu sẽ không quay về mức 0 trong suốt chu kỳ xung nhịp.

**Mã tiềm năng NRZ**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_28_NRZ.png" alt="Hình 3.28 Mã tiềm năng NRZ" width="900">
</p>
<p align="center"><b>Hình 3.28 Mã tiềm năng NRZ</b></p>


Phổ của tín hiệu thực tế luôn thay đổi tùy thuộc vào cấu trúc của dữ liệu được truyền qua kênh. Tuy nhiên, khi truyền chuỗi dài các bit 0 hoặc bit 1, phổ tín hiệu dịch chuyển về tần số thấp, tiến dần đến tín hiệu không thay đổi, và không đảm bảo khả năng đồng bộ hóa giữa máy phát và máy thu. Mã NRZ có ưu điểm là dễ thực hiện và có khả năng chống nhiễu tốt nhờ vào hai mức tín hiệu khác biệt rõ rệt.

Mã NRZ được sử dụng ở lớp vật lý trong các chuẩn **1000BASE-SX, 1000BASE-LX**.

**Mã tiềm năng không quay về 0 với đảo chiều ở bit 1 (NRZI, Non-Return to Zero with Inverted at One)** là một biến thể của mã NRZ.

NRZI sẽ duy trì mức điện áp hiện tại khi truyền bit 0 (không thay đổi tín hiệu), còn khi truyền bit 1, tín hiệu sẽ đảo chiều sang mức đối diện.

**Mã tiềm năng NRZI**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_29_NRZI.png" alt="Hình 3.29 Mã tiềm năng NRZI" width="900">
</p>
<p align="center"><b>Hình 3.29 Mã tiềm năng NRZI</b></p>


Mã NRZI có khả năng tự đồng bộ hóa tốt hơn so với NRZ khi số lượng các bit 1 trong thông tin được mã hóa nhiều hơn các bit 0. Tuy nhiên, mã này không đảm bảo đồng bộ hóa khi có chuỗi dài các bit 0.

Phương pháp này được sử dụng ở lớp vật lý của chuẩn **100BASE-FX Fast Ethernet**.

Trong **mã Manchester (Manchester Code)**, việc mã hóa các bit 1 và 0 được thực hiện bằng cách thay đổi mức điện áp, tức là biên độ xung. Mỗi chu kỳ xung nhịp được chia thành hai phần. Thông tin được mã hóa bằng các sự thay đổi điện áp xảy ra ở giữa mỗi chu kỳ: bit 1 được mã hóa bằng sự thay đổi từ mức tín hiệu thấp lên mức cao, còn bit 0 thì ngược lại (theo chuẩn IEEE 802.3). Sự thay đổi này được sử dụng để đồng bộ hóa giữa máy phát và máy thu.

Ở đầu mỗi chu kỳ có thể xảy ra sự thay đổi tín hiệu phụ trợ để biểu diễn một chuỗi các bit 1 hoặc bit 0 liên tiếp.

**Mã Manchester**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_30_Manchester.png" alt="Hình 3.30 Mã Manchester" width="900">
</p>
<p align="center"><b>Hình 3.30 Mã Manchester</b></p>


Băng thông phổ khi sử dụng mã hóa Manchester rộng gấp đôi so với mã hóa NRZ. Phương pháp này được sử dụng ở lớp vật lý trong các chuẩn Ethernet tốc độ 10 Mbps (**10BASE5, 10BASE2, 10BASE-T, 10BASE-F**).

**Mã truyền tải ba mức MLТ-3 (Multi-Level Transmission-3)** sử dụng ba mức tín hiệu: +1, 0 và -1.

Bit 1 được mã hóa bằng cách chuyển từ mức tín hiệu này sang mức tín hiệu khác. Khi truyền bit 0, tín hiệu sẽ không thay đổi.

**Mã MLТ-3**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_31_MLT_3.png" alt="Hình 3.31 Mã MLТ-3" width="900">
</p>
<p align="center"><b>Hình 3.31 Mã MLТ-3</b></p>


Nhược điểm của phương pháp này là thiếu khả năng đồng bộ hóa khi xuất hiện chuỗi dài các bit 0. Mã MLT-3 được sử dụng ở lớp vật lý của chuẩn **100BASE-TX Fast Ethernet** kết hợp với phương pháp mã hóa logic **4B/5B**.

--- 

#### 3.5.4.2 Mã hóa logic (Logical Encoding)

**Mã hóa logic** (Logical Encoding), thực hiện trước mã hóa vật lý, nhằm khắc phục các hạn chế của các mã tiềm năng như **NRZ**, **NRZI** hoặc **MLT-3**. Mã hóa logic bao gồm việc thay thế các bit của thông tin gốc bằng một chuỗi bit mới, mang cùng nội dung thông tin nhưng có thêm các tính chất bổ sung, đặc biệt là khả năng giúp bên nhận phát hiện lỗi trong dữ liệu nhận được.

Ngoài ra, mã hóa logic cho phép loại bỏ các chuỗi dài các bit 0 và bit 1 có thể gây mất đồng bộ, đảm bảo nhận diện biên của khung và các trạng thái đặc biệt trong dòng bit liên tục, và cải thiện đặc điểm phổ của tín hiệu.

Mã hóa logic chuyển đổi dòng bit của khung MAC tại tầng con của tầng liên kết (Data Link Layer) thành chuỗi ký hiệu chuẩn bị cho mã hóa vật lý để truyền qua đường truyền.

Hai phương pháp chính cho mã hóa logic bao gồm:

- **Mã thừa (Redundant Codes)**
- **Xáo trộn (Scrambling)**

**Mã thừa** (Redundant Coding) dựa trên việc chia chuỗi bit gốc thành các đoạn có độ dài bằng nhau – được gọi là **ký hiệu (symbols)**. Sau đó, mỗi ký hiệu được thay thế (thường bằng cách tra bảng) bằng một ký hiệu mới có số bit lớn hơn.

**Mã logic 4B/5B** thay thế mỗi 4 bit của dòng dữ liệu gốc (ký hiệu gốc) bằng một ký hiệu đầu ra 5 bit (bảng 3.1). Trong chuỗi 4 bit gốc có 16 tổ hợp khác nhau của các bit 0 và 1, trong khi trong nhóm 5 bit có đến 32 tổ hợp. Do đó, trong mã kết quả, có thể chọn ra 16 tổ hợp không chứa nhiều bit 0 liên tiếp. Các tổ hợp còn lại có thể được xem là các chuỗi bị cấm. Nhờ vậy, ngoài việc cải thiện khả năng tự đồng bộ hóa của mã gốc, mã thừa còn cho phép máy thu nhận diện lỗi, vì sự xuất hiện của chuỗi bị cấm báo hiệu có lỗi xảy ra.

*bảng 3.1*

| Mã nhị phân 4B | Mã kết quả 5B |
|----------------|---------------|
| 0000           | 11110         |
| 0001           | 01001         |
| 0010           | 10100         |
| 0011           | 10101         |
| 0100           | 01010         |
| 0101           | 01011         |
| 0110           | 01110         |
| 0111           | 01111         |
| 1000           | 10010         |
| 1001           | 10011         |
| 1010           | 10110         |
| 1011           | 10111         |
| 1100           | 11010         |
| 1101           | 11011         |
| 1110           | 11100         |
| 1111           | 11101         |

Mã 4B/5B được sử dụng trong các chuẩn **100BASE-FX và 100BASE-TX**.

**Mã logic 8B/10B** thay thế mỗi ký hiệu 8 bit gốc bằng ký hiệu đầu ra 10 bit. Trong chuỗi gốc có 256 tổ hợp khác nhau của các bit 0 và 1, trong khi trong mã kết quả có đến 1024 tổ hợp. Nhờ đó, có thể mã hóa 256 tổ hợp của các ký hiệu 8 bit theo hai cách khác nhau. Mã 8B/10B được sử dụng trong các chuẩn Gigabit Ethernet: **1000BASE-SX, 1000BASE-LX**.

**Mã logic 64B/66B** thay thế mỗi ký hiệu 64 bit gốc bằng ký hiệu đầu ra 66 bit. Phương pháp này được sử dụng trong các chuẩn Ethernet 10 Gigabit: **10GBASE-SR, 10GBASE-LR, 10GBASE-ER, 10GBASE-LRM, 10GBASE-KR**.

**Xáo trộn (Scrambling)** bao gồm việc chuyển đổi từng bit của chuỗi bit gốc bằng cách sử dụng một chuỗi bit giả ngẫu nhiên để cải thiện đặc điểm phổ và khả năng tự đồng bộ của chuỗi bit kết quả. Quá trình xáo trộn thực hiện bằng phép toán XOR từng bit của chuỗi gốc với chuỗi giả ngẫu nhiên. Ở phía nhận, dòng bit gốc được khôi phục thông qua bộ giải xáo trộn (descrambler).

Về mặt phần cứng, bộ xáo trộn gồm một số cổng logic XOR và thanh ghi dịch với các kết nối hồi tiếp để tạo ra chuỗi bit giả ngẫu nhiên.

Các thuật toán xáo trộn khác nhau ở số lượng thành phần và độ dịch giữa các thành phần.

Ưu điểm của xáo trộn là không sử dụng mã thừa, nhưng nhược điểm là cần có thuật toán xáo trộn/giải xáo trộn tại các nút mạng, gây thêm chi phí thực hiện.

---

## 3.6 Tiêu chuẩn cáp (Cable Standards)

Trong các mạng máy tính, cáp phải đáp ứng các tiêu chuẩn nhất định, cho phép xây dựng hệ thống cáp mạng từ các loại cáp và thiết bị kết nối của các nhà sản xuất khác nhau.

Hiện nay, các tiêu chuẩn phổ biến nhất trong thực tế toàn cầu bao gồm:

- **Tiêu chuẩn Mỹ EIA/TIA-568**
- **Tiêu chuẩn quốc tế ISO/IEC 11801**
- **Tiêu chuẩn châu Âu EN50173**

Trong tiêu chuẩn hóa cáp, có một cách tiếp cận độc lập với các giao thức. Điều này có nghĩa là tiêu chuẩn không quy định loại cáp nào dành cho giao thức cụ thể nào. Thay vào đó, tiêu chuẩn mô tả các đặc tính điện, quang học và cơ học mà cáp hoặc đầu nối phải đáp ứng. Vì vậy, cần biết loại cáp tiêu chuẩn nào hỗ trợ các giao thức như Ethernet hoặc FDDI.

Cáp có thể chia thành hai nhóm: **cáp điện** và **cáp quang**. Cáp điện bao gồm cáp xoắn đôi (twisted pair), cáp đồng trục (coaxial cable) và cáp twinaxial. Cáp quang bao gồm cáp quang đơn mode và đa mode. 

**Phân loại:**

- **Cáp xoắn đôi (Twisted Pair)**: Loại cáp này thường được sử dụng trong các mạng LAN Ethernet.
- **Cáp đồng trục (Coaxial Cable)**: Chủ yếu dùng trong truyền hình cáp và một số mạng cũ.
- **Cáp twinaxial**: Loại cáp này được sử dụng trong một số ứng dụng chuyên dụng, như kết nối trong trung tâm dữ liệu.
- **Cáp quang đơn mode (Single-mode Fiber)**: Thường dùng trong các kết nối đường dài, cho phép truyền dữ liệu ở khoảng cách xa.
- **Cáp quang đa mode (Multi-mode Fiber)**: Dùng cho các kết nối ngắn hơn, thường thấy trong các mạng nội bộ hoặc trung tâm dữ liệu. 

Mỗi loại cáp và tiêu chuẩn sẽ phù hợp với các ứng dụng và nhu cầu truyền dẫn khác nhau, giúp tối ưu hóa hiệu quả hoạt động của mạng máy tính.

---

### 3.6.1 Đặc điểm chính của cáp điện (Main Characteristics of Electrical Cables)

Các đặc tính chính của cáp điện, có ý nghĩa thực tiễn và được quy định bởi các tiêu chuẩn hiện hành, bao gồm:

- **Suy hao (Attenuation)**: Giảm biên độ hoặc công suất tín hiệu khi truyền giữa hai điểm. Đây là một thông số quan trọng trong thiết kế kênh truyền và xác định chiều dài tối đa của cáp. Suy hao được đo bằng decibel trên mét (dB/m) và phụ thuộc vào tần số tín hiệu. 

- **Nhiễu xuyên âm cận kề (NEXT) và nhiễu xuyên âm xa (FEXT) - Near-End Crosstalk (NEXT) and Far-End Crosstalk (FEXT)**: Kết quả của nhiễu tín hiệu truyền trên các cặp dây dẫn lân cận. NEXT đo tại đầu phát, trong khi FEXT đo ở đầu xa của cáp. Giá trị NEXT và FEXT đều phụ thuộc vào tần số tín hiệu.

  - **NEXT**: Được tính ở đầu cáp có máy phát, là tỷ lệ giữa công suất tín hiệu vào và công suất tín hiệu nhiễu, đo bằng decibel (dB) cho một tần số nhất định. Giá trị tuyệt đối NEXT càng lớn thì mức độ nhiễu từ các cặp dây lân cận càng thấp, do đó chất lượng tín hiệu càng tốt.
  
  - **FEXT**: Khi truyền ở khoảng cách xa, tín hiệu sẽ suy yếu, do đó FEXT tạo ra mức nhiễu nhỏ hơn NEXT. NEXT thường quan trọng hơn FEXT trong việc đảm bảo chất lượng truyền tín hiệu.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_32_Crosstalk.png" alt="Hình 3.32 Nhiễu xuyên âm" width="900">
</p>
<p align="center"><b>Hình 3.32 Nhiễu xuyên âm</b></p>

- **Trở kháng (Impedance)**: Là tổng trở (bao gồm cả thành phần trở kháng và điện kháng) của mạch điện, đo bằng Ohm. Trở kháng thường ổn định trong hệ thống cáp nhưng có thể thay đổi ở tần số cao (trên 100 MHz). Các biến động đột ngột về trở kháng dọc theo chiều dài cáp có thể gây ra phản xạ bên trong, dẫn đến sóng đứng, làm gián đoạn việc truyền dữ liệu.

- **Điện trở kháng hoạt động (Active Resistance)**: Là điện trở đối với dòng điện một chiều trong mạch điện. Không phụ thuộc vào tần số và tăng lên khi chiều dài cáp tăng. Đơn vị đo là Ohm.

- **Điện dung (Capacitance)**: Khả năng của dây dẫn kim loại trong cáp tích trữ năng lượng điện. Điện dung là thông số không mong muốn vì giá trị cao có thể gây méo tín hiệu và giảm băng thông của kênh truyền. Do đó, điện dung càng thấp thì chất lượng cáp càng tốt.

- **Đường kính hoặc tiết diện dây dẫn**: Trong các tiêu chuẩn quốc tế và châu Âu, đường kính dây dẫn thường đo bằng milimet. Trong các mạng máy tính hiện đại, hệ thống chuẩn AWG (American Wire Gauge) thường được sử dụng để phân loại cáp đồng, ví dụ: 22AWG, 24AWG, và 26AWG. Số AWG càng nhỏ, đường kính dây dẫn càng lớn và điện trở càng thấp.

Các thông số này ảnh hưởng lớn đến hiệu suất và độ tin cậy của hệ thống cáp, đảm bảo các kênh truyền đạt yêu cầu về chất lượng và độ bền trong môi trường mạng máy tính.

---

### 3.6.2 Cáp đồng trục (Coaxial cable)

Cáp đồng trục (Coaxial cable) là loại cáp điện bao gồm dây dẫn trung tâm và lớp vỏ bọc được sắp xếp đồng trục, dùng để truyền tải tín hiệu tần số cao. Đặc điểm của loại cáp này là khả năng chống nhiễu cao và độ suy giảm tín hiệu thấp.

Cáp đồng trục bao gồm dây dẫn bên trong, có thể là dây đồng nguyên khối hoặc dây đồng xoắn.

Xung quanh dây dẫn bên trong là lớp vỏ nhựa cách điện (dielectric), bên ngoài lớp cách điện này là dây dẫn ngoài. Dây dẫn ngoài được làm từ lớp màng kim loại có chức năng như một màn chắn nhiễu điện từ, bao quanh bởi lớp bện đồng. Bên ngoài cùng của cáp là lớp ống nhựa cứng, đóng vai trò làm lớp vỏ bảo vệ bên ngoài của cáp (hình 3.33).

**Cáp đồng trục**


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_33_Coaxial_cable.png" alt="Hình 3.33 Cáp đồng trục" width="900">
</p>
<p align="center"><b>Hình 3.33 Cáp đồng trục</b></p>



Trong các mạng cục bộ (LAN), có hai loại cáp đồng trục từng được sử dụng là "cáp mỏng" và "cáp dày".

- **Cáp dày** (thick coaxial cable): RG-8 và RG-11 có trở kháng sóng 50 Ohm, được thiết kế cho mạng Ethernet 10BASE5. Loại cáp này có khả năng chống nhiễu tốt và suy giảm thấp, vì vậy có thể truyền dữ liệu ở khoảng cách xa. Đường kính của cáp vào khoảng 12 mm, với khoảng cách truyền tối đa lên đến 500 m. Tuy nhiên, so với cáp mỏng, cáp dày có giá thành cao hơn, khó uốn và yêu cầu lắp đặt phức tạp hơn.

- **Cáp mỏng** (thin coaxial cable): RG-58 được thiết kế cho mạng Ethernet 10BASE2. Loại cáp này có khả năng chống nhiễu thấp hơn cáp dày, nhưng lại linh hoạt và có giá thành rẻ hơn. Đường kính cáp vào khoảng 6 mm, trở kháng sóng là 50 Ohm, và khoảng cách truyền tối đa lên đến 185 m.

Hiện nay, cáp đồng trục RG-59 chủ yếu được sử dụng để truyền tín hiệu truyền hình.

Một loại biến thể của cáp đồng trục là **cáp twinaxial** (Twinaxial cable).

**Cáp twinaxial - Cáp trục đôi (Twinaxial cable)**

Cáp twinaxial là loại cáp điện chất lượng cao, có cấu tạo tương tự cáp đồng trục nhưng bao gồm hai dây dẫn bên trong. Đường kính của dây dẫn thường nằm trong khoảng từ 30 AWG đến 24 AWG, với trở kháng sóng là 100 Ohm.

**Cáp twinaxial - Cáp trục đôi**


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_34_Twinaxial_cable.png" alt="Hình 3.34 Cáp twinaxial" width="900">
</p>
<p align="center"><b>Hình 3.34 Cáp twinaxial</b></p>



Ban đầu, cáp twinaxial được thiết kế để sử dụng trong mạng Gigabit Ethernet theo chuẩn 1000BASE-CX cho truyền tải dữ liệu ở khoảng cách ngắn (tối đa 25 m). Hiện tại, cáp này được sử dụng rộng rãi trong mạng Ethernet tốc độ cao ở các chuẩn như 10GBASE-CX4, 40GBASE-CR4 và 100GBASE-CR10 cho các khoảng cách ngắn.

Để đạt hiệu suất tối ưu, cáp twinaxial trong các mạng theo chuẩn 10GBASE-CX4, 40GBASE-CR4 và 100GBASE-CR10 nên được kết thúc tại nhà máy sản xuất. Để phục vụ mục đích này, các nhà sản xuất thiết bị mạng cung cấp các bộ cáp thụ động hoặc chủ động, bao gồm cáp twinaxial (hoặc nhiều cáp twinaxial), và các bộ thu phát SFP+ và/hoặc QSFP+ hoặc các đầu nối InfiniBand được kết nối trực tiếp ở hai đầu.

**Cáp twinaxial thụ động** để kết nối trực tiếp với các bộ thu phát QSFP+ có chiều dài 3 mét

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_35.jpg" alt="Hình 3.35 Cáp twinaxial thụ động để kết nối trực tiếp với các bộ thu phát QSFP+ có chiều dài 3 mét" width="900">
</p>
<p align="center"><b>Hình 3.35 Cáp twinaxial thụ động để kết nối trực tiếp với các bộ thu phát QSFP+ có chiều dài 3 mét</b></p>


--- 

### 3.6.3 Cáp xoắn đôi (Twisted pair cable)

**Cáp xoắn đôi** (*Twisted pair*) là một loại dây dẫn cách điện, trong đó các dây dẫn được xoắn lại với nhau theo từng cặp, với một số vòng xoắn nhất định trên một đơn vị chiều dài, và được bao bọc trong một lớp vỏ nhựa (*plastic sheath*).

Như đã đề cập trước đó, việc xoắn các dây dẫn theo từng cặp giúp giảm nhiễu chéo (*crosstalk*), vì các sóng điện từ do từng dây phát ra sẽ triệt tiêu lẫn nhau. Bước xoắn khác nhau cho từng cặp dây và được xác định trong các tiêu chuẩn.

Cáp xoắn đôi là loại cáp phổ biến nhất trong điện thoại và mạng máy tính cục bộ (*LAN*) do giá thành rẻ và dễ dàng lắp đặt.

Cáp thường chứa nhiều cặp dây xoắn: thường có 2, 4, 6, 8, 25, 50 hoặc 100 cặp trong một bó. Trong các mạng cục bộ, cáp 4 cặp là loại được sử dụng phổ biến nhất.

Các lõi dẫn điện (*conductors*) trong các cặp dây được làm bằng đồng. Chúng có thể là loại dây đơn (nguyên một sợi) hoặc dây xoắn (gồm nhiều sợi nhỏ kết hợp chặt chẽ với nhau). Độ dày của lõi dẫn điện nằm trong khoảng 0,4 đến 0,6 mm theo hệ mét và từ 26 đến 22 AWG theo hệ AWG. Trong các cáp 4 cặp tiêu chuẩn, đường kính lõi chủ yếu là 0,51 mm (24 AWG).

Phía trên lõi dẫn điện là lớp cách điện (*insulation*), có thể là lớp đặc, lớp xốp, hoặc lớp cách điện dạng phim. Cáp được bọc bởi lớp vỏ nhựa PVC (*Polyvinyl chloride*), PP (*Polypropylene*) hoặc PE (*Polyethylene*).

Có hai loại cáp xoắn đôi chính:

1. **Cáp xoắn đôi không được che chắn** (*UTP, Unshielded Twisted Pair*)
2. **Cáp xoắn đôi được che chắn** (*STP, Shielded Twisted Pair*)

Như tên gọi, cáp không che chắn (*UTP*) không có thêm lớp màn chắn bảo vệ khỏi nhiễu điện từ (*EMI*) hoặc nghe lén trái phép.

**Cáp UTP**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_36_UTP_cable.png" alt="Hình 3.36 Cáp UTP" width="900">
</p>
<p align="center"><b>Hình 3.36 Cáp UTP</b></p>


Các cáp có che chắn có thêm lớp bảo vệ. Dựa vào công nghệ sử dụng, có một số loại cáp xoắn đôi có che chắn:

- **Cáp xoắn đôi có che chắn** (*STP, Shielded Twisted Pair*)
- **Cáp xoắn đôi có màn chắn bảo vệ** (*ScTP, Screened Twisted Pair*)
- **Cáp xoắn đôi có che chắn bảo vệ kép** (*SSTP, Screened Shielded Twisted Pair*)

Trong cáp **STP** (U/FTP - *Unshielded/Foiled Twisted Pair* theo tiêu chuẩn ISO/IEC 11801), mỗi cặp dây đồng xoắn để giảm nhiễu và nhiễu chéo được bọc thêm một lớp màn chắn bằng nhôm.

**Cáp STP**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_37_STP_cable.png" alt="Hình 3.37 Cáp STP" width="900">
</p>
<p align="center"><b>Hình 3.37 Cáp STP</b></p>

Trong **cáp ScTP** có một lớp màn chắn bảo vệ chung xung quanh tất cả các cặp không có che chắn. Các loại phổ biến là F/UTP (*Foiled/Unshielded Twisted Pair*) với màn chắn làm từ lá nhôm, S/UTP (*Shielded/Unshielded Twisted Pair*) với màn chắn dạng lưới dây đồng, và SF/UTP (*Shielded Foiled/Unshielded Twisted Pair*) có hai lớp che chắn ngoài từ lá nhôm và dây đồng bện.

**Cáp F/UTP**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_38_F_UTP_cable.png" alt="Hình 3.38 Cáp F/UTP" width="900">
</p>
<p align="center"><b>Hình 3.38 Cáp F/UTP</b></p>


**Cáp xoắn đôi có che chắn bảo vệ kép** bảo vệ tối ưu khỏi nhiễu điện từ và nhiễu chéo, vì mỗi cặp dây đều có màn chắn riêng và một lớp màn chắn chung cho tất cả các cặp. Có hai loại cáp này: F/FTP và S/FTP theo tiêu chuẩn ISO/IEC 11801. Trong cáp F/FTP (*Foiled/Foiled Twisted Pair*), các lớp màn chắn xung quanh các cặp và màn chắn chung được làm từ lá nhôm. Trong cáp S/FTP (*Shielded/Foiled Twisted Pair*), màn chắn quanh các cặp là lá nhôm, và màn chắn chung là lưới đồng.

**Cáp S/FTP**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_39_S_FTP_cable.png" alt="Hình 3.39 Cáp S/FTP" width="900">
</p>
<p align="center"><b>Hình 3.39 Cáp S/FTP</b></p>



Dù lớp che chắn giúp tăng khả năng chống nhiễu, nhưng đồng thời làm cho các loại cáp có che chắn đắt và nặng hơn so với cáp không có che chắn, và yêu cầu nối đất đúng cách. Do đó, trong các mạng cục bộ chạy ở tốc độ 100 hoặc 1000 Mb/s, thường sử dụng cáp không có che chắn. Tuy nhiên, với các mạng tốc độ cao như 10 Gb/s, 40 Gb/s, và 100 Gb/s, tiêu chuẩn chỉ định phải dùng cáp có che chắn.

Cáp xoắn đôi được phân thành các **loại (categories)** theo băng thông của chúng. Loại cáp càng cao thì băng thông càng lớn và hiệu suất càng tốt.

Các loại này được quy định trong tiêu chuẩn EIA/TIA-568 của Mỹ và tiêu chuẩn ISO/IEC 11801 quốc tế. Hiện tại có 8 loại cáp được xác định. Mô tả các loại cáp được đưa ra trong bảng 3.2.

Đối với cáp không che chắn theo tiêu chuẩn EIA/TIA-568, các loại cáp được xác định là 3, 4, 5, 5e, và 6; còn trong tiêu chuẩn ISO/IEC 11801, các loại được quy định là A, B, C, D, và E. Đối với cáp có che chắn, các loại cáp trong tiêu chuẩn EIA/TIA-568 bao gồm 6A, 7, 7A, 8.1 và 8.2, trong khi tiêu chuẩn ISO/IEC 11801 bao gồm các loại Ea, F, Fa, I, và II.

Khoảng cách truyền tối đa của cáp xoắn đôi là 100 m nếu không có các hạn chế theo tiêu chuẩn tương ứng. Trở kháng của tất cả các loại và loại cáp xoắn đôi là 100 Ohm. Các tham số khác, như suy giảm tín hiệu (*attenuation*), nhiễu chéo gần (*NEXT*), tốc độ lan truyền tín hiệu và các đặc điểm khác, thay đổi tùy theo loại cáp.

**Bảng 3.2: Các loại cáp xoắn đôi (twisted pair)**

| **Tên gọi (EIA/TIA-568)** | **Tên gọi (ISO/IEC 11801)** | **Băng tần (MHz)** | **Ứng dụng** | **Ghi chú và nhận xét** |
|----------------------------|----------------------------|--------------------|--------------|-------------------------|
| -                          | Class A                    | Đến 100 KHz       | xDSL         | Cáp điện thoại. Chỉ dùng cho truyền thoại hoặc dữ liệu qua modem analog hoặc ADSL. |
| -                          | Class B                    | Đến 1 MHz         | ISDN, 1BASE5 | Hiện không còn sử dụng. |
| Category 3 (Cat. 3)        | Class C                    | Đến 16 MHz        | Token Ring, 10BASE-T | Cáp UTP 2 cặp. Chủ yếu dùng để truyền thoại. |
| Category 4 (Cat. 4)        | -                          | Đến 20 MHz        | Token Ring, 10BASE-T, 100BASE-T | Cáp UTP 4 cặp. Không còn được sử dụng. |
| Category 5 (Cat. 5)        | Class D                    | Đến 100 MHz       | 10BASE-T, 100BASE-TX (2 cặp), 1000BASE-T (4 cặp) | Cáp UTP 4 cặp. Không còn được sử dụng. |
| Category 5e (Cat. 5e)      | -                          | Đến 125 MHz       | 10BASE-T, 100BASE-TX (2 cặp), 1000BASE-T (4 cặp), 2.5GBASE-T, 5GBASE-T | Cáp UTP 4 cặp. Loại phổ biến trong các mạng hiện nay. |
| Category 6 (Cat. 6)        | Class E                    | Đến 250 MHz       | 1000BASE-T, 10GBASE-T, 2.5GBASE-T, 5GBASE-T | Cáp UTP 4 cặp. Giới hạn khoảng cách tối đa 10GBASE-T là 55 m. |
| Category 6A (Cat. 6A)      | Class Ea                   | Đến 500 MHz       | 1000BASE-T, 10GBASE-T | Cáp U/FTP, F/UTP với 4 cặp dây. |
| Category 7 (Cat. 7)        | Class F                    | Đến 600 MHz       | 1000BASE-T, 10GBASE-T | Cáp F/FTP hoặc S/FTP với 4 cặp dây. |
| Category 7A (Cat. 7A)      | Class Fa                   | Đến 1 GHz         | 1000BASE-T, 10GBASE-T | Cáp F/FTP hoặc S/FTP với 4 cặp dây. |
| Category 8.1               | Class I                    | Đến 2 GHz         | 25GBASE-T, 40GBASE-T | Cáp U/FTP, F/UTP với 4 cặp dây. Khoảng cách truyền tối đa là 30 m. |
| Category 8.2               | Class II                   | Đến 2 GHz         | 25GBASE-T, 40GBASE-T | Cáp F/FTP hoặc S/FTP với 4 cặp dây. Khoảng cách truyền tối đa là 30 m. Dùng các đầu nối TERA, GG45. |

**Kết nối cáp xoắn đôi vào các thiết bị mạng**

Để kết nối cáp xoắn đôi (*twisted pair cable*) vào các thiết bị mạng, người ta sử dụng đầu nối loại 8P8C (*8 Position 8 Contact*), thường được gọi là **RJ-45**. Mặc dù tên gọi này có phần không chính xác (vì RJ-45 thực sự là đầu nối loại 8P2C), do có vẻ ngoài tương tự, đầu nối 8P8C đã thừa hưởng tên gọi RJ-45 và trở nên phổ biến với tên này. Trong phần tiếp theo, chúng ta sẽ tiếp tục sử dụng thuật ngữ RJ-45. Hiện tại, đầu nối này được sử dụng cho cả cáp xoắn đôi không che chắn (*UTP - Unshielded Twisted Pair*) và cáp xoắn đôi có che chắn (*STP - Shielded Twisted Pair*).

**Cáp UTP Cat. 5e với đầu nối 8P8C (RJ-45)**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_40.jpg" alt="Hình 3.40 Cáp UTP Cat. 5e với đầu nối 8P8C (RJ-45)" width="400">
</p>
<p align="center"><b>Hình 3.40 Cáp UTP Cat. 5e với đầu nối 8P8C (RJ-45)</b></p>


**Cáp U/FTP Cat. 6a với đầu nối 8P8C (RJ-45)**  


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_41.jpg" alt="Hình 3.41 Cáp U/FTP Cat. 6a với đầu nối 8P8C (RJ-45)" width="400">
</p>
<p align="center"><b>Hình 3.41 Cáp U/FTP Cat. 6a với đầu nối 8P8C (RJ-45)</b></p>

**Các phương pháp bấm đầu nối 8P8C trên cáp**

Số thứ tự các chân của đầu nối được xác định từ trái qua phải khi nhìn từ phía các chân tiếp xúc (hình 3.42).

**Số thứ tự các chân của RJ-45**  
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_42.jpg" alt="Hình 3.42 Số thứ tự các chân của RJ-45" width="400">
</p>
<p align="center"><b>Hình 3.42 Số thứ tự các chân của RJ-45</b></p>



Cách sắp xếp thứ tự các cặp dây dẫn trong đầu nối được quy định theo tiêu chuẩn **EIA/TIA-568A** và **EIA/TIA-568B** (hình 3.43). Mỗi cặp dây có màu sắc riêng, trong đó một dây được phủ hoàn toàn màu đó, còn dây còn lại có sọc.

- **Tiêu chuẩn EIA/TIA-568A** quy định thứ tự chân trên đầu nối:  
  1 - trắng-xanh lá, 2 - xanh lá, 3 - trắng-cam, 4 - xanh dương, 5 - trắng-xanh dương, 6 - cam, 7 - trắng-nâu, 8 - nâu.

- **Tiêu chuẩn EIA/TIA-568B** quy định thứ tự chân trên đầu nối:  
  1 - trắng-cam, 2 - cam, 3 - trắng-xanh lá, 4 - xanh dương, 5 - trắng-xanh dương, 6 - xanh lá, 7 - trắng-nâu, 8 - nâu.

Hai tiêu chuẩn khác nhau ở cách sắp xếp cặp màu cam và xanh lá, khi chúng đổi vị trí cho nhau.

**Thứ tự sắp xếp dây dẫn trong đầu nối**  


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_43.jpg" alt="Hình 3.43 Thứ tự sắp xếp dây dẫn trong đầu nối" width="500">
</p>
<p align="center"><b>Hình 3.43 Thứ tự sắp xếp dây dẫn trong đầu nối</b></p>

**Phân loại cáp xoắn đôi theo cách bấm đầu nối hai đầu**

Tùy thuộc vào cách bấm dây dẫn trong các đầu nối ở hai đầu cáp, cáp xoắn đôi được chia thành:

1. **Cáp thẳng** (*straight through cable*): Dây xoắn đôi được bấm giống nhau ở cả hai đầu, không có hoán đổi giữa các cặp dây bên trong.
   
   **Cáp xoắn đôi thẳng**
   
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_44.png" alt="Hình 3.44 Cáp xoắn đôi thẳng" width="900">
</p>
<p align="center"><b>Hình 3.44 Cáp xoắn đôi thẳng</b></p>

   
3. **Cáp chéo** (*crossover cable*): Dây dẫn được bố trí đảo ngược với sự hoán đổi giữa các cặp dây bên trong.
   
   **Cáp xoắn đôi chéo**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_45.jpg" alt="   Hình 3.45 Cáp xoắn đôi chéo" width="900">
</p>
<p align="center"><b>   Hình 3.45 Cáp xoắn đôi chéo</b></p>




**Các loại giao diện Ethernet với đầu nối 8P8C (RJ-45)**

Có ba loại giao diện (*port interfaces*) Ethernet với đầu nối 8P8C (RJ-45):

1. **MDI** (*Medium Dependent Interface*): Giao diện phụ thuộc vào môi trường vật lý.
2. **MDI-X** (*Medium Dependent Interface crossover*): Giao diện phụ thuộc vào môi trường vật lý, có hoán đổi.
3. **Auto MDI/MDI-X**: Giao diện tự động xác định cấu hình MDI hoặc MDI-X.

Các loại giao diện này khác nhau ở việc sử dụng các chân cho nhận (Rx) và truyền (Tx) tín hiệu:
- Ở cổng MDI, các chân 1 và 2 dùng cho truyền (Tx) và các chân 3 và 6 dùng cho nhận (Rx).
- Ở cổng MDI-X, các chân 1 và 2 dùng cho nhận (Rx) và các chân 3 và 6 dùng cho truyền (Tx).

Khi kết nối các cổng MDI–MDI-X, người ta sử dụng cáp thẳng, còn khi kết nối cổng MDI–MDI hoặc MDI-X–MDI-X, cần dùng cáp chéo.

Hiện nay, hầu hết các nhà sản xuất thiết bị mạng đều trang bị cổng Ethernet hỗ trợ tính năng tự động xác định cực tính **Auto MDI/MDI-X**, cho phép sử dụng bất kỳ loại cáp nào (cả cáp thẳng và cáp chéo) để kết nối thiết bị. Tính năng Auto MDI/MDI-X là một phần của tiêu chuẩn IEEE 802.3-2018.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_46_Ethernet_port.png" alt="Hình 3.46 Các cổng Ethernet MDI và MDI-X" width="900">
</p>
<p align="center"><b>Hình 3.46 Các cổng Ethernet MDI và MDI-X</b></p>

**Công nghệ Power over Ethernet (PoE)**


Lưu ý rằng cáp xoắn đôi không chỉ dùng cho truyền và nhận dữ liệu. Trong mạng Ethernet, nó cũng có thể được sử dụng để cung cấp điện năng cho thiết bị từ xa cùng với dữ liệu. Công nghệ này được gọi là **Power over Ethernet (PoE)**, được mô tả trong các tiêu chuẩn IEEE 802.3af, 802.3at và 802.3bt. Công nghệ PoE sẽ được trình bày trong chương 6.

---

### 3.6.4 Cáp quang (cáp sợi quang)

**Cáp quang** (*fiber-optic cable*) khác với cáp đồng trục (*coaxial cable*) hoặc cáp xoắn đôi (*twisted pair cable*) ở chỗ nó truyền tín hiệu ánh sáng thay vì tín hiệu điện. Các đặc tính của sợi quang khiến nó trở thành môi trường lý tưởng để truyền tải lượng lớn thông tin với tốc độ cao trên khoảng cách xa. Cáp quang có nhiều ưu điểm như băng thông cao, chống nhiễu tốt, bảo mật tốt, đường kính nhỏ, trọng lượng nhẹ, không cần nối đất và phạm vi truyền xa. Nhược điểm của cáp quang là lắp đặt phức tạp và chi phí cao của thiết bị mạng quang.

Cáp quang là một phương tiện truyền dẫn bao gồm các sợi quang được bọc trong một lớp vỏ bảo vệ bên ngoài.

Để đảm bảo độ bền cơ học cần thiết và ngăn ngừa áp lực cơ học lớn, cáp quang được gia cố bằng các thành phần chịu lực đặc biệt như dây thép, đồng, nhôm, sợi aramid và thanh sợi thủy tinh. Các thành phần chịu lực này được bố trí ở trung tâm (tăng độ linh hoạt) hoặc ngoại vi (tăng khả năng chịu lực va đập và căng kéo).

**Sợi quang** bao gồm một lõi dẫn ánh sáng (*core*) và lớp vỏ (*cladding*) bao quanh với các chỉ số khúc xạ khác nhau. Hiện tượng truyền dẫn ánh sáng của sợi quang dựa trên hiệu ứng phản xạ toàn phần khi ánh sáng đi từ môi trường có chỉ số khúc xạ cao sang môi trường có chỉ số khúc xạ thấp. Lõi dẫn, nơi ánh sáng lan truyền, được làm từ vật liệu quang học có mật độ cao hơn. Các sợi quang khác nhau ở đường kính lõi và vỏ, cũng như ở cấu trúc chỉ số khúc xạ của lõi. Các thông số quan trọng của sợi quang là suy hao (*attenuation*) và tán sắc (*dispersion*).

**Cáp quang**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_47_Fiber_optic_cable.png" alt="Hình 3.47 Cáp quang" width="900">
</p>
<p align="center"><b>Hình 3.47 Cáp quang</b></p>

#### Các loại sợi quang

Sợi quang được chia thành hai nhóm chính: **đa mode** (*Multi-Mode Fiber - MMF*) và **đơn mode** (*Single-Mode Fiber - SMF*).

Tiêu chuẩn quy định hai loại sợi đa mode phổ biến nhất: **62,5/125 µm** và **50/125 µm**, trong đó 62,5 µm hoặc 50 µm là đường kính lõi, và 125 µm là đường kính vỏ. Do đường kính lõi quang (50 và 62,5 µm) lớn hơn nhiều so với bước sóng ánh sáng, nên nhiều sóng điện từ (gọi là mode) có thể truyền đồng thời trong lõi. Các mode đi vào lõi dưới các góc khác nhau, phản xạ nhiều lần trong lõi và vỏ, và đi qua các khoảng cách khác nhau, dẫn đến sự khác biệt về thời gian đến điểm nhận. Hiện tượng này gọi là tán sắc mode (*modal dispersion*), gây mở rộng dần các xung ánh sáng, giới hạn băng thông. Băng thông của sợi quang được đo bằng megahertz trên mỗi kilomet (MHz·km).

Sợi đa mode có hai loại cấu trúc khúc xạ:

1. **Cấu trúc bậc**: Lõi có chỉ số khúc xạ không đổi, được bao bọc bởi lớp vỏ với chỉ số khúc xạ khác biệt. Ánh sáng phản xạ từ mặt tiếp xúc lõi/vỏ để truyền dọc theo lõi. Tuy nhiên, sợi với cấu trúc bậc có tán sắc cao, gây giới hạn băng thông đáng kể.

2. **Cấu trúc giảm dần**: Chỉ số khúc xạ của lõi giảm dần từ trung tâm lõi ra ngoài, làm cho các tia sáng bị uốn cong khi di chuyển qua lõi, tạo thành các sóng ánh sáng hình sin. Tán sắc ở sợi cấu trúc giảm dần thấp hơn so với sợi bậc, nhưng vẫn giới hạn băng thông.

**Sợi quang đa mode**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_48_Multimode_fiber_optic.png" alt="Hình 3.48 Sợi quang đa mode" width="900">
</p>
<p align="center"><b>Hình 3.48 Sợi quang đa mode</b></p>


Trong sợi MMF, các nguồn phát ánh sáng thường là laser có bước sóng 850 nm và 1310 nm. Khoảng cách truyền tối đa của sợi đa mode là 2 km, thường được sử dụng trong các mạng LAN có phạm vi ngắn.

**Sợi đơn mode** có cấu trúc chỉ số khúc xạ bậc, nhưng đường kính lõi rất nhỏ (5-10 µm, với đường kính vỏ 125 µm), gần bằng bước sóng ánh sáng, cho phép chỉ một mode truyền qua. Điều này loại bỏ tán sắc mode, giúp tăng băng thông sợi đơn mode lên trên 10 Gbps.

**Sợi quang đơn mode**  

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_49_Single_mode_fiber.png" alt="Hình 3.49 Sợi quang đơn mode" width="900">
</p>
<p align="center"><b>Hình 3.49 Sợi quang đơn mode</b></p>

Khoảng cách truyền của sợi đơn mode có thể lên tới 100 km hoặc hơn, thường dùng cho các tuyến liên tỉnh, mạng đô thị và khu vực.

Các nguồn phát ánh sáng cho SMF thường là laser với bước sóng 1310 nm và 1550 nm. Bước sóng 1310 nm tối ưu về tán sắc, nhưng suy hao thấp nhất là ở 1550 nm.

#### Ghép kênh WDM - Wavelength Division Multiplexing

Để tối ưu kênh quang, người ta áp dụng kỹ thuật **ghép kênh phân chia bước sóng WDM** (*Wavelength Division Multiplexing*). Phần lớn hệ thống WDM sử dụng sợi đơn mode với đường kính lõi 9/125 µm. Sợi đơn mode với **tán sắc dịch chuyển không** (*NZDSF - Non-Zero Dispersion Shifted Fiber*) tối ưu cho truyền nhiều bước sóng, hỗ trợ ghép kênh WDM.

#### Phân loại cáp quang

Cáp quang có thể được phân loại theo các yếu tố sau:

- Mục đích sử dụng
- Điều kiện áp dụng
- Cách thức lắp đặt
- Đặc điểm cấu tạo và công nghệ
- Số lượng sợi quang và dây dẫn điện

Theo mục đích, cáp quang chia thành các loại:

- **Cáp trục**: quốc tế và liên tỉnh
- **Cáp vùng**: kết nối và liên tỉnh
- **Cáp địa phương**: kết nối, phân phối và cáp thuê bao
- **Cáp nội bộ**: trạm và thuê bao

Theo phân loại của Liên minh Viễn thông Quốc tế (*ITU-T*), cáp quang được chia thành cáp ngoài trời và cáp trong nhà:

- **Cáp ngoài trời**: kết nối liên tỉnh, liên trạm, phân phối (cáp treo, cáp chôn trong đất, cáp đặt trong cống, hầm hoặc dưới nước).
- **Cáp trong nhà**: cáp thuê bao và trạm (trong tòa nhà).

#### Yêu cầu môi trường cho cáp ngoài trời và trong nhà

Cáp quang không bị nhiễu điện từ nên có thể đi dọc đường dây điện hoặc đường sắt điện khí hóa.

Lựa chọn cáp ngoài trời phụ thuộc nhiều vào điều kiện sử dụng, tác động bên ngoài như nhiệt độ (co rút vỏ, tăng suy hao do thay đổi nhiệt độ, độ giòn của vỏ khi lạnh); nước mặn (ăn mòn dây treo và giáp); mưa, suối nóng (ăn mòn cáp và vỏ ngoài); dòng điện một chiều (ăn mòn điện ly); hỏa hoạn; gió, tuyết, và băng (hư hỏng do dao động, trọng lượng tuyết và băng); hydrogen (tăng suy hao); và nguy cơ phá hoại từ động vật gặm nhấm, chim và côn trùng.

Đối với cáp trong nhà, yếu tố quan trọng nhất khi lựa chọn là độ linh hoạt khi lắp đặt và tính an toàn cháy nổ.

**ISO/IEC 11801** phân loại các loại sợi đa mode và đơn mode dùng trong nhà. Tiêu chuẩn này quy định bốn lớp sợi đa mode (OM1 đến OM4) và hai lớp sợi đơn mode (OS1 và OS2), phân biệt theo suy hao và băng thông (bandwidth).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/table_3_3.png" alt="Bảng 3.3 Các loại sợi quang đa mode theo tiêu chuẩn ISO/IEC 11801" width="900">
</p>
<p align="center"><b>Bảng 3.3 Các loại sợi quang đa mode theo tiêu chuẩn ISO/IEC 11801</b></p>


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/table_3_4.png" alt="Bảng 3.4 Các loại sợi quang đơn mode theo tiêu chuẩn ISO/IEC 11801" width="900">
</p>
<p align="center"><b>Bảng 3.4 Các loại sợi quang đơn mode theo tiêu chuẩn ISO/IEC 11801</b></p>

Trong tiêu chuẩn này, các kênh quang học được phân loại theo các cấp (tương tự như các hạng cáp xoắn đôi). OF-300, OF-500 và OF-2000 hỗ trợ các ứng dụng của lớp quang học ở các khoảng cách lên tới 300, 500 và 2000 m tương ứng.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/table_3_5.png" alt="Bảng 3.5 Các loại kênh theo tiêu chuẩn ISO/IEC 11801" width="900">
</p>
<p align="center"><b>Bảng 3.5 Các loại kênh theo tiêu chuẩn ISO/IEC 11801</b></p>



Có rất nhiều loại đầu nối quang học (optical connectors) khác nhau, khác biệt về cấu trúc, phương pháp cố định, đường kính ferrule, loại đánh bóng, v.v. Các yêu cầu đối với chúng được quy định trong các phần khác nhau của tiêu chuẩn IEC 61754.

Các thành phần cấu trúc chính của đầu nối quang học bao gồm vỏ (housing), ferrule và khóa (latch). Ferrule hoặc đầu quang học (optical tip) giúp căn chỉnh chính xác sợi quang. Đầu này có thể được làm từ gốm, kim loại, thủy tinh hoặc nhựa. Có những đầu nối cho phép kết nối chỉ một sợi quang hoặc nhiều sợi cùng lúc.

Hãy cùng tìm hiểu ngắn gọn các loại đầu nối đang được sử dụng trong các mạng máy tính hiện đại.

**Đầu nối FC (Ferrule Connector)** được mô tả trong tiêu chuẩn IEC 61754-13. Nó có vỏ kim loại và cố định bằng cách kết nối ren (threaded connection). Đường kính của ferrule là 2,5 mm. Đầu nối này bền và chống rung tốt, chủ yếu được thiết kế cho sợi quang đơn mode (single-mode fiber), nhưng cũng có thể dùng cho sợi quang đa mode (multi-mode fiber). Đầu nối FC chủ yếu được sử dụng trong các tuyến truyền dẫn quang dài, trong công nghiệp và thiết bị đo lường.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_50_FC.jpg" alt="Hình 3.50 Đầu nối FC" width="600">
</p>
<p align="center"><b>Hình 3.50 Đầu nối FC</b></p>


**Đầu nối SC (Subscriber Connector, Square Connector, Standard Connector)** được sử dụng cho cả sợi quang đơn mode và đa mode. Yêu cầu của loại đầu nối này được mô tả trong tiêu chuẩn IEC 61754-4. Đầu nối SC bao gồm vỏ trong và vỏ ngoài, với ferrule gốm có đường kính 2,5 mm. Đầu nối sử dụng cơ chế “push-pull” (đẩy-kéo), cho phép nối tự động khóa, rất thuận tiện khi chuyển đổi. Đầu nối này không thích hợp với các tác động cơ học và rung động, nhưng cho phép đạt mật độ kết nối cao trên bảng viễn thông. Đầu nối SC có thể là loại simplex (đơn) hoặc duplex (kép). Đầu nối duplex là một mô-đun bao gồm hai đầu nối và được sử dụng cho kết nối duplex (một sợi quang dùng để truyền tín hiệu đi, còn sợi kia để truyền tín hiệu ngược lại).

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_51_SC.jpg" alt="Hình 3.51 Đầu nối SC" width="600">
</p>
<p align="center"><b>Hình 3.51 Đầu nối SC</b></p>



**Đầu nối LC (Lucent Connector, Local Connector)** được mô tả trong tiêu chuẩn IEC 61754-20. Nó được sử dụng cho cả sợi quang đơn mode và đa mode. Đường kính ferrule gốm là 1,25 mm, đòi hỏi phải thao tác cẩn thận. Đầu nối này nhỏ gọn hơn so với đầu nối SC, giúp tăng mật độ kết nối. Đầu nối này thuộc loại SFF (Small Form Factor - Hình thức nhỏ gọn), có kích thước bên ngoài phù hợp với khe cắm của đầu nối RJ-45. Đầu nối LC được đặt trong vỏ nhựa với cơ chế "push-pull" (có khóa, tương tự như khóa của đầu nối RJ-45). Nó có thể được sử dụng cho cả kết nối simplex và duplex.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_52_LC.jpg" alt="Hình 3.52 Đầu nối LC" width="600">
</p>
<p align="center"><b>Hình 3.52 Đầu nối LC</b></p>


Các đầu nối quang học được mô tả ở trên chỉ cho phép kết nối một sợi quang. **Đầu nối MPO (Multi-Fiber Push-On)** bao gồm nhiều sợi quang. Các sợi quang này có thể là đơn mode hoặc đa mode. Loại đầu nối này được mô tả trong các tiêu chuẩn IEC 61754-7 và EIA/TIA-604-5 (FOCSI 5).

Trong vỏ nhựa, có một ferrule bằng vật liệu composite (polyphenylene), các sợi được xếp thành một hàng hoặc nhiều hàng tùy theo mật độ cáp. Ở một phía của vỏ có khóa (key), giúp xác định phân cực của đầu nối. Trong các trung tâm dữ liệu và kết nối mạng nội bộ, các đầu nối MPO với 8, 12 hoặc 24 sợi thường được sử dụng.

Khác với các đầu nối quang đơn sợi, là loại đầu nối "papa" (male), đầu nối MPO được chia thành loại "papa" (male) và "mama" (female). Đầu nối "papa" có các chốt (pins), trong khi đầu nối "mama" có các lỗ (holes).


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_53_MPO.png" alt="Hình 3.53 Đầu nối MPO" width="600">
</p>
<p align="center"><b>Hình 3.53 Đầu nối MPO</b></p>



<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_54_MPO_Female.jpg" alt="Hình 3.54 Mô-đun giao diện thay thế 100 Gbit/s với đầu nối MPO (female)" width="400">
</p>
<p align="center"><b>Hình 3.54 Mô-đun giao diện thay thế 100 Gbit/s với đầu nối MPO (female)</b></p>

--- 


### 3.6.5 Hệ thống cáp

Hệ thống cáp bao gồm tập hợp các loại cáp khác nhau (cáp quang, cáp xoắn đôi), cáp nối (patch cords), đầu nối cho cáp, ổ cắm kết nối, các bảng kết nối hoặc bảng phân phối (patch panels), tủ và giá viễn thông, được sử dụng để kết nối các thiết bị mạng khác nhau vào mạng máy tính.

- **Bảng phân phối (Patch Panel)**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_55_Patch_panel.jpg" alt=" Hình 3.55 Bảng phân phối" width="600">
</p>
<p align="center"><b> Hình 3.55 Bảng phân phối</b></p>

 

- **Giá viễn thông (Telecommunications Rack)**  
 
<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_56_Telecommunication_rack.jpg" alt=" Hình 3.56 Giá viễn thông" width="450">
</p>
<p align="center"><b>  Hình 3.56 Giá viễn thông</b></p>

Thiết bị được sử dụng để tổ chức mạng máy tính có thể chia thành hai loại: thiết bị thụ động và thiết bị chủ động.

Các thành phần của hệ thống cáp là thiết bị mạng thụ động, trong khi các thiết bị mạng mà chúng kết nối là thiết bị mạng chủ động.

Thiết bị thụ động là các thiết bị mạng không tiêu thụ điện và không gây thay đổi tín hiệu ở cấp độ thông tin. Thiết bị mạng chủ động bao gồm các thiết bị điện tử và điện tử-quang học, có chức năng xử lý, hình thành, biến đổi và chuyển mạch tín hiệu điện, radio và/hoặc quang học. Để truyền và nhận tín hiệu, thiết bị mạng chủ động sử dụng các nguồn năng lượng bổ sung, tức là cần điện để hoạt động.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_57_Types_of_network_equipment.png" alt="Hình 3.57 Các loại thiết bị mạng" width="900">
</p>
<p align="center"><b>Hình 3.57 Các loại thiết bị mạng</b></p>

---

### 3.6.6 Hệ thống cáp có cấu trúc

Hệ thống cáp có cấu trúc (Structured Cabling System - SCS) là hệ thống cáp của một tòa nhà hoặc nhóm tòa nhà đáp ứng các yêu cầu của các tiêu chuẩn. SCS được quy định bởi các tiêu chuẩn quốc tế, châu Âu và quốc gia.

Hiện tại, có ba tiêu chuẩn chính:

- **TIA/EIA-568 C Commercial Building Telecommunications Wiring Standard** (Tiêu chuẩn Mỹ);
- **ISO/IEC 11801-2002 Information Technology. Generic cabling for customer premises** (Tiêu chuẩn quốc tế);
- **CENELEC EN 50173 Information Technology. Generic cabling systems** (Tiêu chuẩn châu Âu).

Tại Liên bang Nga, các tiêu chuẩn GOST R 53246-2008 và GOST R 53245-2008 đã được đưa vào thực tiễn, dựa trên tiêu chuẩn quốc tế ISO/IEC 11801.

Tất cả các tiêu chuẩn này xác định cấu trúc của SCS, các thông số hoạt động của các thành phần chức năng, nguyên tắc thiết kế, quy tắc lắp đặt, phương pháp đo lường, quy tắc quản lý, và các yêu cầu về tiếp đất viễn thông. Cần lưu ý rằng các tiêu chuẩn này có sự khác biệt về thuật ngữ, danh sách các thành phần chức năng của SCS và số lượng các phân hệ của SCS.

Hệ thống cáp có cấu trúc là một cơ sở hạ tầng cáp toàn diện, cung cấp khả năng truyền tín hiệu của tất cả các loại: dữ liệu, thoại và video. Các lợi ích của nó bao gồm khả năng kết nối với bất kỳ thiết bị mạng nào và sử dụng các giao thức mạng khác nhau. Ngoài ra, SCS sử dụng các thành phần và vật liệu tiêu chuẩn, cho phép kết hợp nhiều loại cáp trong cùng một mạng, có tính mô-đun, khả năng điều chỉnh và mở rộng hệ thống cáp, cũng như đảm bảo tuổi thọ lâu dài. Đơn giản trong quản lý được đạt được nhờ tất cả các thành phần của SCS (cổng, cáp, bảng, tủ, v.v.) đều được đánh dấu và ghi chép.

**Ví dụ về lắp đặt và đánh dấu ổ cắm**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_58.jpg" alt="Hình 3.58 Ví dụ về lắp đặt và đánh dấu ổ cắm" width="700">
</p>
<p align="center"><b>Hình 3.58 Ví dụ về lắp đặt và đánh dấu ổ cắm</b></p>


Nhược điểm của SCS là các tiêu chuẩn khuyến nghị việc lắp đặt thiết bị dự phòng, dẫn đến chi phí ban đầu đáng kể, nhưng những chi phí này sẽ nhanh chóng được hoàn vốn.

Một trong những thủ tục quan trọng giúp tránh các vấn đề với hoạt động của các ứng dụng mạng máy tính là thử nghiệm và chứng nhận SCS. SCS có thể đáp ứng các tiêu chuẩn nhưng không đảm bảo hoạt động của một số ứng dụng trong mạng cục bộ theo thông số tỷ lệ lỗi bit (BER, Bit Error Rate). Việc thử nghiệm cho phép phát hiện các lỗi tiềm ẩn gây ra các sự cố và lỗi hệ thống.

Để chẩn đoán SCS, người ta sử dụng các thiết bị chuyên dụng:

- **Bộ phân tích mạng (network analyzers)**: là các thiết bị đo tiêu chuẩn dùng để chẩn đoán và chứng nhận cáp và hệ thống cáp trong điều kiện phòng thí nghiệm bởi các nhân viên đã qua đào tạo (không nên nhầm lẫn với bộ phân tích giao thức).
- **Máy quét cáp (cable scanners)**: là các thiết bị di động dùng để chứng nhận hệ thống cáp, cho phép xác định chiều dài cáp, các đặc tính điện từ (NEXT, suy hao, trở kháng), sơ đồ đi dây cáp, mức độ của trường điện từ, tỷ lệ tín hiệu/nhiễu.
- **Máy kiểm tra cáp (cable testers)**: là các thiết bị di động cho phép chẩn đoán hệ thống cáp để đảm bảo tính chính xác của việc lắp đặt và phát hiện các lỗi trong cáp.

---

### 3.6.7 Bộ chuyển đổi phương tiện (Media Converters)

Khi mở rộng hoặc nâng cấp mạng hiện có, cũng như khi tổ chức truy cập Internet cho người dùng, có thể xảy ra các vấn đề liên quan đến sự không tương thích giữa các loại phương tiện truyền tải và tín hiệu. Ví dụ, khi kết nối thiết bị với giao diện "dây đồng" (copper interface) vào các kênh truyền dẫn quang hoặc ngược lại. Để tránh chi phí tài chính đáng kể cho việc thiết lập các kết nối mới hoặc mua sắm thiết bị đắt tiền, những vấn đề này trong mạng có thể được giải quyết bằng cách sử dụng bộ chuyển đổi phương tiện (media converters).

**Bộ chuyển đổi phương tiện (Media Converter)** là thiết bị chuyển đổi loại phương tiện truyền dẫn tín hiệu từ một dạng này sang dạng khác.

Trong mạng máy tính, "phương tiện truyền dẫn tín hiệu" mà bộ chuyển đổi phương tiện xử lý thường là cáp đồng và cáp quang. Nói cách khác, nó là cầu nối giữa hai môi trường vật lý - cáp đồng và cáp quang.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_59_Using_a_media_converter_on_the_network.png" alt="Hình 3.59 Sử dụng bộ chuyển đổi phương tiện trong mạng" width="1000">
</p>
<p align="center"><b>Hình 3.59 Sử dụng bộ chuyển đổi phương tiện trong mạng</b></p>


Để kết nối với cáp đồng, bộ chuyển đổi phương tiện được trang bị giao diện RJ-45. Để kết nối với cáp quang, thường sử dụng giao diện SC.

**Bộ chuyển đổi phương tiện DMC-F02SC với giao diện quang SC**


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_60.jpg" alt="Hình 3.60 Bộ chuyển đổi phương tiện DMC-F02SC với giao diện quang SC" width="400">
</p>
<p align="center"><b>Hình 3.60 Bộ chuyển đổi phương tiện DMC-F02SC với giao diện quang SC</b></p>

Để linh hoạt hơn trong việc lựa chọn loại kết nối quang, thay vì giao diện quang cố định, bộ chuyển đổi phương tiện có thể được trang bị khe cắm để lắp các mô-đun giao diện có thể thay thế, thông thường là SFP.

**Bộ chuyển đổi phương tiện DMC-G01L với khe cắm SFP**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_61.jpg" alt="Hình 3.61 Bộ chuyển đổi phương tiện DMC-G01L với khe cắm SFP" width="400">
</p>
<p align="center"><b>Hình 3.61 Bộ chuyển đổi phương tiện DMC-G01L với khe cắm SFP</b></p>


Các bộ chuyển đổi phương tiện do D-Link sản xuất có thể hoạt động như các thiết bị độc lập (được đặt trong vỏ riêng và được trang bị bộ cấp nguồn), hoặc là một phần của hệ thống khung (chassis). Khung chứa bộ chuyển đổi phương tiện rất tiện lợi khi sử dụng trong mạng của các nhà cung cấp dịch vụ viễn thông, khi cần tổ chức truy cập Internet cho người dùng. Khung có thể chứa đến 16 bộ chuyển đổi phương tiện, có thể thiết lập dự phòng nguồn điện cho chúng, cũng như giám sát chúng trong thời gian thực. Khung có thể được đặt trong giá viễn thông.

**Khung cho bộ chuyển đổi phương tiện DMC-1000**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_62.jpg" alt="Hình 3.62 Khung cho bộ chuyển đổi phương tiện DMC-1000" width="400">
</p>
<p align="center"><b>Hình 3.62 Khung cho bộ chuyển đổi phương tiện DMC-1000</b></p>


Truyền thống, bộ chuyển đổi phương tiện được xem là thiết bị hoạt động ở lớp vật lý của mô hình OSI. Tuy nhiên, sự phát triển công nghệ đã dẫn đến sự ra đời của các bộ chuyển đổi phương tiện có chức năng thông minh, hoạt động ở lớp liên kết dữ liệu.

Các bộ chuyển đổi phương tiện hiện đại có thể không chỉ chuyển đổi phương tiện truyền dẫn mà còn có khả năng điều chỉnh tốc độ và chế độ truyền dữ liệu. Việc điều chỉnh tốc độ và chế độ hoạt động (song công/ bán song công) được thực hiện qua cổng kết nối cáp xoắn đôi, thường là giao diện Ethernet. Ngoài ra, bộ chuyển đổi phương tiện còn có các chức năng dịch vụ khác. Ví dụ, chúng có thể kiểm soát lưu lượng dữ liệu (flow control), giám sát các cổng quang và cổng đồng để phát hiện sự mất tín hiệu (chức năng Link Pass Through), thực hiện chuyển mạch khung ở chế độ Store-and-forward.


---

## 3.7 Hệ thống dây điện

Mạng cục bộ (local network) có thể được xây dựng bằng cách sử dụng dây điện 220 V thông thường, tức là sử dụng hệ thống dây điện gia đình để truyền tải giọng nói hoặc dữ liệu. Để làm điều này, tín hiệu analog (analog signal) được chồng lên dòng điện xoay chiều (alternating current) chuẩn có tần số 50 Hz. Lý do sử dụng hệ thống dây điện làm phương tiện truyền dẫn là do sự phổ biến của các mạng gia đình.

Hầu như mỗi gia đình đều có ít nhất một hoặc hai máy tính. Công nghệ Smart TV (TV thông minh) đang phát triển mạnh mẽ - tích hợp Internet và các dịch vụ tương tác số vào các thiết bị như TV hiện đại, đầu thu kỹ thuật số, đầu phát Blu-ray, máy chơi game và các thiết bị tương tự. Bạn có thể kéo hàng chục mét cáp xung quanh nhà để kết nối tất cả máy tính, máy in, TV và các thiết bị mạng khác với nhau. Nhưng trong trường hợp đó, mỗi thiết bị sẽ được bố trí cố định trong phòng. Việc di chuyển máy tính hoặc TV đồng nghĩa với việc phải di dời cáp mạng. Bạn có thể cài đặt mạng Wi-Fi không dây (wireless network Wi-Fi) tại nhà, nhưng có thể gặp vấn đề khi tín hiệu xuyên qua tường và trần nhà.

Có một phương pháp khác - sử dụng hệ thống dây điện và ổ cắm điện có sẵn được lắp trong tường. Ổ cắm điện có trong mỗi phòng của mỗi căn hộ và ngôi nhà. Điều duy nhất bạn cần là các bộ chuyển đổi PowerLine (PowerLine adapters) phù hợp, chúng được cắm trực tiếp vào ổ cắm điện.

Bộ chuyển đổi PowerLine có loại có dây và không dây, với hỗ trợ giao diện Wi-Fi.

Ngoài ra, hệ thống dây điện còn có thể được sử dụng để thực hiện ý tưởng "nhà thông minh" (smart home), nơi tất cả các thiết bị điện tử gia dụng được kết nối vào một mạng duy nhất với khả năng điều khiển tập trung.

Ứng dụng của công nghệ PowerLine không chỉ giới hạn ở gia đình mà còn có thể được áp dụng trong các văn phòng nhỏ (tối đa 15 máy tính), nơi yêu cầu chính là tính đơn giản và khả năng mở rộng, tính di động của các thiết bị. Cả mạng văn phòng và từng phân đoạn của nó đều có thể được xây dựng bằng cách sử dụng các bộ chuyển đổi PowerLine. Một tình huống phổ biến là khi cần kết nối máy tính hoặc máy in mạng ở phòng khác hoặc ở đầu kia của tòa nhà vào mạng đã tồn tại. Vấn đề này cũng dễ dàng được giải quyết với các bộ chuyển đổi PowerLine.

Công nghệ PowerLine có thể được sử dụng trong tự động hóa quy trình công nghệ, kết nối các khối tự động hóa thông qua dây điện hoặc các loại dây khác.

**Bộ chuyển đổi PowerLine AV DHP-P309AV**


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_63.jpg" alt="Hình 3.63 Bộ chuyển đổi PowerLine AV DHP-P309AV" width="500">
</p>
<p align="center"><b>Hình 3.63 Bộ chuyển đổi PowerLine AV DHP-P309AV</b></p>

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_64.png" alt="Hình 3.64 Mở rộng mạng gia đình bằng công nghệ PowerLine" width="500">
</p>
<p align="center"><b>Hình 3.64 Mở rộng mạng gia đình bằng công nghệ PowerLine</b></p>


Hiện nay, phần lớn kết nối cuối cùng được thực hiện bằng cách kéo cáp từ đường truyền tốc độ cao đến căn hộ hoặc văn phòng của người dùng. Đây là giải pháp rẻ nhất và đáng tin cậy nhất, nhưng nếu không thể kéo cáp, bạn có thể sử dụng hệ thống dây điện hiện có trong tòa nhà. Bất kỳ ổ cắm điện nào trong tòa nhà có thể trở thành điểm truy cập Internet. Người dùng chỉ cần có modem PowerLine (PowerLine modem) hoặc bộ định tuyến (router) PowerLine để kết nối với thiết bị tương tự, thường được lắp đặt trong tủ điện của tòa nhà và kết nối với kênh tốc độ cao.

Truyền dữ liệu qua mạng điện (PowerLine Communication - PLC) cũng là giải pháp lý tưởng cho "last mile" trong các khu nhà biệt thự và khu xây dựng thấp tầng, vì việc tổ chức các kênh truyền thông thay thế sẽ tốn kém hơn so với hệ thống dây điện sẵn có.

Để tạo ra một tiêu chuẩn duy nhất cho truyền dữ liệu qua mạng điện, liên minh HomePlug Power Line Alliance đã được thành lập. Tiêu chuẩn IEEE 1901-2010, dựa trên đặc tả HomePlug AV, xác định truyền dữ liệu băng rộng tốc độ cao (lên đến 500 Mbps) qua dây điện. Tiêu chuẩn này quy định băng thông từ 1,8 đến 30 MHz cho truyền dữ liệu.

Mọi công nghệ truyền dữ liệu đều cần thích ứng với môi trường vật lý, do đó cần có các phương tiện phát hiện và khắc phục lỗi cũng như xung đột khi sử dụng chung. Khi truyền tín hiệu qua mạng điện, người ta phải đối mặt với nhiều vấn đề, bao gồm méo tín hiệu do truyền đa đường (multipath propagation), suy giảm tín hiệu (signal attenuation), nhiễu xung (impulse noise) và nhiễu liên ký tự (inter-symbol interference).

Cấu trúc mạng điện, đặc biệt là hệ thống dây điện gia đình, ban đầu không được thiết kế cho truyền dữ liệu tốc độ cao. Nó chứa nhiều ổ cắm, công tắc, máy biến áp phân phối và thiết bị bảo vệ quá tải (cầu chì). Đường truyền tín hiệu tần số cao từ thiết bị phát đến thiết bị nhận phụ thuộc vào nhiều yếu tố, chủ yếu là vào cấu trúc mạng điện (topology). Thứ nhất, vì tính phân nhánh của mạng, luôn có nhiều đường truyền từ nguồn tới nơi nhận. Thứ hai, do có nhiều điểm không đồng nhất, tín hiệu đến nơi nhận không chỉ là tín hiệu trực tiếp mà còn là các tín hiệu phản xạ (hiện tượng phản xạ đa đường). Trong khi tín hiệu truyền qua mạng điện, mức độ suy giảm xảy ra. Một nguyên nhân khác làm suy giảm tín hiệu là sự hiện diện của các phần tử chuyển mạch trong mạng. Thông thường, mạch điện chứa các công tắc và biến áp tần số thấp (50 Hz), là trở ngại chính cho tín hiệu tần số cao. Các nguồn gây nhiễu trong căn hộ và văn phòng bao gồm các bộ sạc điện thoại di động, điều chỉnh độ sáng đèn halogen, và các thiết bị gia dụng khác.

Công nghệ PowerLine ở cấp độ vật lý chủ yếu sử dụng **multiplexing với tần số phân chia trực giao (OFDM - Orthogonal Frequency Division Multiplexing)**, trong đó dòng dữ liệu tốc độ cao được chia thành nhiều dòng tốc độ thấp hơn, mỗi dòng truyền trên một tần số sóng mang phụ và sau đó được gộp lại thành một tín hiệu.

Sử dụng OFDM giúp tăng khả năng chống nhiễu bằng cách thích ứng với các thông số của môi trường truyền vật lý. Tuy nhiên, do tín hiệu suy giảm và méo trên đường truyền do phản xạ đa đường, mức độ nhiễu cao, và nhiễu xung ngắn nhưng mạnh trong mạng điện gây lỗi dữ liệu, chỉ riêng OFDM là chưa đủ để đảm bảo truyền thông tin đáng tin cậy. Để đảm bảo độ chính xác chấp nhận được, cần áp dụng các biện pháp bổ sung.

Một phương pháp để giải quyết vấn đề này là sử dụng mã hóa chống nhiễu (noise-resistant coding) cho luồng bit trước khi điều chế và truyền qua mạng. Mã hóa chống nhiễu giúp phát hiện và sửa lỗi tại đầu nhận bằng cách thêm các bit dư vào luồng dữ liệu.

Mạng điện là một mạng với phương tiện truyền chia sẻ. Để giải quyết các vấn đề truy cập đa điểm, các phương pháp **CSMA/CA (Carrier Sense Multiple Access with Collision Avoidance)** và **TDMA (Time Division Multiple Access)** được sử dụng. CSMA/CA tương tự như phương pháp trong MAC của tiêu chuẩn IEEE 802.11. TDMA được sử dụng để đảm bảo chất lượng dịch vụ (QoS).

Bảo vệ dữ liệu truyền được thực hiện bằng mã hóa AES 128-bit.

Tốc độ truyền dữ liệu qua mạng PowerLine về mặt lý thuyết có thể đạt tới 500 Mbps. Tuy nhiên, băng thông thực tế bị ảnh hưởng nhiều bởi chất lượng dây (vật liệu, tiết diện, số lượng kết nối), hoạt động của các thiết bị điện khác, số lượng adapter PowerLine trong mạng (băng thông được chia giữa các thiết bị, vì vậy khuyến nghị không nên kết nối quá 15 thiết bị), loại và khối lượng lưu lượng. Khoảng cách tối đa giữa các thiết bị PowerLine không nên quá 100 m trong mạng LAN và 1500 m khi kết nối Internet.

Năm 2012, đặc tả HomePlug AV2 ra đời. Thiết bị theo đặc tả này tương thích ngược với HomePlug AV và tiêu chuẩn IEEE 1901-2010. So với HomePlug AV, HomePlug AV2 mở rộng băng thông từ 30 MHz lên 86 MHz và thêm hỗ trợ công nghệ **MIMO (Multiple Input Multiple Output)**, giúp tăng băng thông đáng kể. Cũng có hỗ trợ chế độ tiết kiệm năng lượng.

---

## 3.8 Môi trường truyền không dây

Khác với các mạng có dây, nơi tín hiệu được truyền qua các chất dẫn cố định như dây xoắn đồng (twisted copper pair) hoặc cáp quang (optical fiber), trong các mạng không dây, môi trường truyền vật lý là bầu khí quyển và không gian mở. Trong môi trường cáp, tín hiệu luôn được truyền theo hướng nhất định, còn môi trường vật lý của truyền không dây thì không thể định hướng tín hiệu theo một hướng nhất định. Để thiết lập một đường truyền không dây, mỗi nút mạng đều được trang bị một ăng-ten (antenna). Ăng-ten có thể được định nghĩa là một chất dẫn (hoặc hệ thống chất dẫn) dùng để phát ra và thu nhận sóng điện từ (electromagnetic waves) từ không gian. Để truyền tín hiệu, các xung điện tần số vô tuyến (radio frequency electrical impulses) từ bộ phát (transmitter) được chuyển đổi thành năng lượng điện từ thông qua ăng-ten và phát ra không gian xung quanh (khí quyển, không gian, hoặc nước). Khi nhận tín hiệu, năng lượng của sóng điện từ đến ăng-ten sẽ được chuyển đổi thành các xung điện tần số vô tuyến và đưa vào bộ thu (receiver). Thông thường, trong truyền thông hai chiều, cùng một ăng-ten có thể được sử dụng cho cả việc thu và phát tín hiệu. Điều này là do đặc tính của ăng-ten không thay đổi trong quá trình thu và phát năng lượng điện từ.

Sóng điện từ (electromagnetic waves) là sự dao động (biến đổi) của trường điện từ truyền đi trong không gian.

**Đường truyền không dây**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_65.png" alt="Hình 3.65 Đường truyền không dây" width="500">
</p>
<p align="center"><b>Hình 3.65 Đường truyền không dây</b></p>


Hướng lan truyền của sóng phụ thuộc vào loại ăng-ten được sử dụng. Về tổng thể, ăng-ten có thể được phân loại thành **ăng-ten đa hướng (omni-directional)** và **ăng-ten định hướng (directional)**. Trong truyền dẫn định hướng, ăng-ten phát sẽ phát ra một chùm sóng điện từ hội tụ, do đó ăng-ten phát và ăng-ten thu cần phải được căn chỉnh cẩn thận. Trong truyền dẫn không định hướng (sử dụng ăng-ten đa hướng), tín hiệu truyền đi theo mọi hướng và có thể được thu nhận bởi nhiều ăng-ten khác nhau.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_66.png" alt="Hình 3.66 Phát sóng của ăng-ten đa hướng và ăng-ten định hướng" width="500">
</p>
<p align="center"><b>Hình 3.66 Phát sóng của ăng-ten đa hướng và ăng-ten định hướng</b></p>



**Hệ số khuếch đại (antenna gain) $$ G $$** là thước đo **độ định hướng (directionality)** của ăng-ten. Nó được xác định bằng tỷ lệ công suất của tín hiệu $$ P_1 $$, phát ra theo một hướng cụ thể, với công suất của tín hiệu $$ P_2 $$ phát ra bởi ăng-ten lý tưởng (đẳng hướng - isotropic) theo mọi hướng.

$$
G = \frac{P_1}{P_2}
$$

Từ công thức này, ta thấy rằng hệ số khuếch đại của ăng-ten là một đại lượng không có đơn vị. Trong thực tế, nó thường được biểu diễn dưới dạng tỷ lệ công suất theo thang đo logarit, tính theo **decibel (dB)**:

$$
G = 10 \cdot \log \left( \frac{P_1}{P_2} \right)
$$

Trong các mô tả kỹ thuật của ăng-ten, đơn vị đo lường của hệ số khuếch đại ăng-ten thường được biểu diễn dưới dạng decibel đẳng hướng (**dBi**), nghĩa là đo bằng decibel với ký tự "i" (isotropic - đẳng hướng) chỉ rằng bức xạ của ăng-ten trong một hướng cụ thể được so sánh với bức xạ của ăng-ten đẳng hướng.

**Ăng-ten đẳng hướng (Isotropic antenna)** là một loại ăng-ten lý tưởng (mang tính lý thuyết), phát ra năng lượng điện từ có cường độ bằng nhau theo mọi hướng. Ăng-ten đẳng hướng có thể được so sánh với Mặt Trời. 


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_67.png" alt="Hình 3.67 Ăng-ten đẳng hướng" width="500">
</p>
<p align="center"><b>Hình 3.67 Ăng-ten đẳng hướng</b></p>


Thuật ngữ **"hệ số khuếch đại (antenna gain)"** thường gây hiểu lầm, dẫn đến giả định sai rằng ăng-ten có khả năng khuếch đại tín hiệu. Trên thực tế, điều này không đúng. Ăng-ten là thiết bị thụ động (passive devices) và không có nguồn năng lượng nào để tăng cường tín hiệu truyền. Hệ số khuếch đại của ăng-ten chỉ ra sự tập trung công suất vào một hướng nhất định, chứ không phải là khuếch đại nó. Việc tăng cường công suất tín hiệu theo một hướng nhất định xảy ra là nhờ giảm công suất trong các hướng phát sóng khác. Nói cách khác, việc tăng công suất ở một hướng sẽ dẫn đến giảm công suất ở các hướng khác.

Để hiểu rõ hơn về nguyên tắc tập trung năng lượng theo các hướng khác nhau, hãy tưởng tượng một ăng-ten đẳng hướng (isotropic antenna) được minh họa trong Hình 3.67 giống như một quả bóng cao su. Hãy tưởng tượng bạn ấn mạnh lên quả bóng từ phía trên (theo hướng thẳng đứng). Quả bóng hơi dẹt lại, nhưng vẫn giữ hình dạng tròn trong mặt phẳng ngang, còn trong mặt phẳng thẳng đứng thì bị ép lại dưới tác động của lực. Ví dụ này có thể được sử dụng để mô tả nguyên lý hoạt động của **ăng-ten đa hướng (omni-directional antenna)**, nơi mà năng lượng được tập trung nhiều hơn trong mặt phẳng ngang bằng cách giảm năng lượng ở mặt phẳng thẳng đứng.

Nếu bạn ép mạnh quả bóng từ một trong các đầu, hình dạng của nó sẽ trở thành hình nón. Ví dụ này mô tả nguyên lý phát xạ của **ăng-ten định hướng (directional antenna)**.

Biểu đồ phụ thuộc của hệ số khuếch đại vào hướng của ăng-ten trong một mặt phẳng nhất định được gọi là **sơ đồ định hướng (radiation pattern)**.

Thông thường, sơ đồ định hướng của ăng-ten được biểu diễn bằng hai mặt cắt ngang hai chiều của sơ đồ ba chiều: mặt cắt ngang nằm ngang và mặt cắt ngang thẳng đứng. Trong trường hợp này, sơ đồ định hướng là một đường khép kín trong hệ tọa độ cực (polar coordinate system), được xây dựng sao cho khoảng cách từ ăng-ten (tâm của sơ đồ) đến bất kỳ điểm nào trên sơ đồ định hướng tỷ lệ thuận với năng lượng được ăng-ten phát ra theo hướng đó.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_68.png" alt="Hình 3.68 Sơ đồ định hướng của ăng-ten định hướng trong mặt phẳng ngang và mặt phẳng thẳng đứng" width="800">
</p>
<p align="center"><b>Hình 3.68 Sơ đồ định hướng của ăng-ten định hướng trong mặt phẳng ngang và mặt phẳng thẳng đứng</b></p>


Hướng bức xạ tối đa được gọi là **thùy chính (main lobe)** của ăng-ten. Các thùy còn lại trên sơ đồ định hướng của ăng-ten là **thùy phụ (side lobes)**, và thùy bức xạ theo hướng ngược lại với hướng chính được gọi là **thùy sau (back lobe)** của sơ đồ định hướng ăng-ten.

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_69.png" alt="Hình 3.69 Các tham số của ăng-ten" width="800">
</p>
<p align="center"><b>Hình 3.69 Các tham số của ăng-ten</b></p>



Một tham số quan trọng của ăng-ten là **độ rộng sơ đồ định hướng (beamwidth)**, hay **độ rộng của thùy chính (main lobe)**, được hiểu là góc giữa hai hướng, dọc theo đó cường độ trường (hoặc mật độ dòng công suất) giảm xuống một giá trị nhất định. Độ rộng sơ đồ định hướng được đo bằng độ (degrees). Trong thực tế, độ rộng sơ đồ định hướng thường được đánh giá trong mặt phẳng ngang và mặt phẳng đứng theo mức giảm công suất xuống còn 3 dB (giảm một nửa) hoặc 2 lần. Các tham số này thường được nhà sản xuất chỉ ra trong các đặc tính của ăng-ten.

Một đặc tính quan trọng khác của ăng-ten là **phân cực (polarization)**. Trong sóng điện từ (electromagnetic wave), các vector điện (electric field vector $$\vec{E}$$) và từ trường (magnetic field vector $$\vec{H}$$) tại mỗi thời điểm được định hướng trong không gian theo một cách nhất định. Phân cực của sóng điện từ là một đặc tính không gian - thời gian và được xác định bởi loại đường di chuyển của vector cường độ trường điện $$\vec{E}$$ trong mặt phẳng vuông góc với hướng lan truyền của sóng điện từ. Nói cách khác, nó mô tả sự thay đổi của vector điện $$\vec{E}$$ theo thời gian.

Phân cực của sóng được xác định thông qua hình chiếu của vector $$\vec{E}$$ lên mặt phẳng yz. Nếu hình chiếu là một đường thẳng, thì đó là **phân cực tuyến tính (linear polarization)**, nếu là một đường tròn hoặc hình elip thì đó là **phân cực tròn hoặc phân cực elip (circular or elliptical polarization)**. Phân cực tuyến tính có thể là **phân cực thẳng đứng (vertical)** hoặc **phân cực ngang (horizontal)** (song song với mặt phẳng của Trái Đất). Phân cực tròn (circular polarization) hoặc phân cực elip (elliptical polarization) có thể là phân cực theo chiều **xoay phải hoặc xoay trái (right-hand or left-hand rotation)** (Hình 3.70). Nhà sản xuất thường chỉ định kiểu phân cực của ăng-ten trong các đặc tính của nó. Ăng-ten cũng có thể được trang bị một chỉ báo đặc biệt để xác định phân cực.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_70.png" alt="Hình 3.70 Các loại phân cực của sóng" width="800">
</p>
<p align="center"><b>Hình 3.70 Các loại phân cực của sóng</b></p>



Phân cực của sóng trong một số trường hợp có thể có ảnh hưởng đáng kể đến chất lượng kết nối. Việc tính toán phân cực cho phép đạt được lợi thế năng lượng bổ sung khi thiết lập các đường truyền không dây khoảng cách xa. Nếu khi thiết lập một đường truyền hai điểm (cầu không dây - wireless bridge) với khoảng cách giữa các ăng-ten hàng trăm mét hoặc xa hơn, một ăng-ten hoạt động với phân cực tuyến tính ngang (horizontal linear polarization) và ăng-ten kia với phân cực thẳng đứng (vertical polarization), thì kết nối sẽ không ổn định hoặc có thể không kết nối được. Điều này xảy ra vì trường sóng với phân cực tuyến tính ngang không ảnh hưởng đến trường sóng với phân cực thẳng đứng. Điều này có thể hữu ích cho các hệ thống sử dụng MIMO (Multiple Input Multiple Output) với nhiều ăng-ten, mỗi ăng-ten truyền các tín hiệu khác nhau với các phân cực khác nhau. Khi sử dụng hai ăng-ten với các phân cực tuyến tính khác nhau, có thể tạo ra một hệ thống với hai kênh độc lập (không gây nhiễu sóng vô tuyến cho nhau), từ đó tăng gấp đôi tốc độ truyền tải.

Khi thiết lập các đường truyền không dây hai điểm khoảng cách xa mà không sử dụng hệ thống MIMO, cần sử dụng các ăng-ten có cùng phân cực và định hướng chúng theo cùng một phân cực. Nói cách khác, cần phải điều chỉnh ăng-ten theo phân cực.

Tuy nhiên, khi hoạt động trong nhà, do có nhiều phản xạ từ các vật thể xung quanh, đặc biệt là các vật bằng kim loại (nội thất, tường nhà), phân cực của sóng có thể thay đổi (phân cực tuyến tính ngang có thể quay và trở thành phân cực thẳng đứng). Vì vậy, trong môi trường trong nhà, không cần thiết phải điều chỉnh ăng-ten theo phân cực.



### 3.8.1 Sự lan truyền tín hiệu trong môi trường truyền không dây

Khi lan truyền, tín hiệu phát ra từ ăng-ten có thể bao quanh bề mặt Trái Đất, phản xạ từ các lớp trên của khí quyển hoặc truyền dọc theo đường nhìn trực tiếp. Phương thức lan truyền tín hiệu, khoảng cách truyền của nó, v.v., phụ thuộc nhiều vào dải tần số của phổ điện từ được sử dụng.

Toàn bộ phổ bức xạ điện từ được chia thành các dải tần số tùy theo loại sóng điện từ:

- Sóng vô tuyến;
- Bức xạ hồng ngoại;
- Ánh sáng nhìn thấy;
- Bức xạ tia cực tím;
- Bức xạ tia X;
- Bức xạ gamma.

Chúng ta quan tâm đến dải vi sóng của tần số vô tuyến, nơi có thể truyền dẫn không dây (xem Hình 3.71).

Trong dải tần từ 30 MHz đến 300 GHz là sóng siêu ngắn, với bước sóng từ 10 m đến 0,1 m (tần số càng cao thì bước sóng càng ngắn). Sóng siêu ngắn được sử dụng rộng rãi để tổ chức các đường truyền vô tuyến, kênh vệ tinh, mạng cục bộ không dây Wi-Fi và hệ thống truy cập không dây cố định. Hạn chế chính của liên lạc bằng sóng siêu ngắn là máy thu và máy phát phải ở trong vùng có thể nhìn thấy nhau trực tiếp. Điều này là do sóng siêu ngắn lan truyền chủ yếu theo đường thẳng và hầu như không thể đi qua các chướng ngại vật tự nhiên hoặc nhân tạo trên đường đi của chúng. Địa hình, các chướng ngại vật và điều kiện thời tiết có ảnh hưởng đáng kể đến sự lan truyền của chúng. Đặc biệt, sóng trong dải SHF (Super High Frequency - tần số siêu cao, từ 3 đến 30 GHz), được sử dụng rộng rãi trong các mạng Wi-Fi, bị hấp thụ mạnh bởi mưa, tuyết, sương mù và các khí trong khí quyển, dẫn đến suy giảm nhanh chóng cường độ trường điện từ.

**Phổ sóng điện từ**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_71.png" alt="Hình 3.71 Phổ sóng điện từ" width="1000">
</p>
<p align="center"><b>Hình 3.71 Phổ sóng điện từ</b></p>



Nếu vị trí của các ăng-ten trong hệ thống truyền thông là tương đối ngẫu nhiên, có thể xảy ra trường hợp kênh không dây trùng với đường nhìn trực tiếp giữa máy phát và máy thu (khi không có chướng ngại vật nào gây nhiễu). Thường thì vị trí này được chọn cho các kênh truyền thông hai điểm tần số cao. Tuy nhiên, trong hầu hết các trường hợp, giữa máy phát và máy thu có nhiều chướng ngại vật. Trong nhà, các chướng ngại vật bao gồm tường, trần và đồ nội thất. Trong không gian mở, chúng bao gồm nhà cửa, cây cối và phương tiện giao thông. Khi gặp chướng ngại vật trên đường truyền, sóng điện từ có thể bị phản xạ, khúc xạ, tán xạ hoặc nhiễu xạ.

**Phản xạ** xảy ra khi sóng điện từ gặp một chướng ngại vật lớn hơn rất nhiều so với bước sóng của nó. Trong trường hợp này, một phần năng lượng của sóng điện từ bị phản xạ khỏi chướng ngại vật đó.

**Phản xạ sóng điện từ**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_72.png" alt="Hình 3.72 Phản xạ sóng điện từ" width="800">
</p>
<p align="center"><b>Hình 3.72 Phản xạ sóng điện từ</b></p>



Khi sóng gặp ranh giới giữa hai môi trường trong suốt cho sóng điện từ nhưng có mật độ khác nhau, một phần sóng bị phản xạ và một phần truyền qua môi trường khác, bị khúc xạ.

**Khúc xạ sóng điện từ**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_73.png" alt="Hình 3.73 Khúc xạ sóng điện từ" width="800">
</p>
<p align="center"><b>Hình 3.73 Khúc xạ sóng điện từ</b></p>


Nếu sóng điện từ gặp một chướng ngại vật không thể xuyên qua được, có kích thước tương đương với bước sóng (như nhà cửa, núi), xảy ra nhiễu xạ – tín hiệu dường như bao quanh chướng ngại vật. Vì vậy, tín hiệu có thể được nhận ngay cả khi không nằm trong vùng nhìn trực tiếp.

**Nhiễu xạ sóng điện từ**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_74.png" alt="Hình 3.74 Nhiễu xạ sóng điện từ" width="800">
</p>
<p align="center"><b>Hình 3.74 Nhiễu xạ sóng điện từ</b></p>




Khi gặp chướng ngại vật có kích thước nhỏ hơn nhiều so với bước sóng (như sương mù, lá cây, bụi), xảy ra hiện tượng tán xạ – sóng bị phản xạ theo các góc khác nhau.

**Tán xạ sóng điện từ**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_75.png" alt="Hình 3.75 Tán xạ sóng điện từ" width="800">
</p>
<p align="center"><b>Hình 3.75 Tán xạ sóng điện từ</b></p>


Kết quả của phản xạ, nhiễu xạ và tán xạ là máy thu có thể nhận được tín hiệu gốc và một số bản sao phản xạ của nó, đến từ các đường truyền khác nhau và vào các khoảng thời gian khác nhau. Đây được gọi là sự **truyền đa đường (multipath propagation)**. Tình huống này thường xảy ra trong các mạng không dây trong nhà.

**Truyền đa đường**

<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_76.png" alt="Hình 3.76 Truyền đa đường" width="800">
</p>
<p align="center"><b>Hình 3.76 Truyền đa đường</b></p>


**Tại điểm thu**, tín hiệu ban đầu và các tín hiệu phản xạ chồng lên nhau (gây ra hiện tượng giao thoa), do đó tín hiệu kết quả là tổng hợp của nhiều tín hiệu với các biên độ khác nhau. Một trong những hiệu ứng không mong muốn của sự truyền sóng đa đường là sự lệch pha giữa biên độ của tín hiệu ban đầu và tín hiệu phản xạ theo thời gian (sự khác biệt về pha). Kết quả của sự cộng pha khác nhau có thể làm giảm hoặc thậm chí đưa mức công suất của tín hiệu kết quả về 0, gây khó khăn cho bộ thu trong việc nhận diện tín hiệu.

**Hiện tượng truyền sóng đa đường** ảnh hưởng đến hiệu suất của hệ thống khác nhau tùy theo đặc điểm của địa hình và sự di chuyển của thiết bị không dây (ví dụ như điện thoại thông minh hoặc máy tính bảng). Trong môi trường có đường truyền thẳng giữa nguồn và bộ thu, ảnh hưởng của hiện tượng truyền sóng đa đường thường yếu và dễ khắc phục. Biên độ của tín hiệu phản xạ yếu hơn nhiều so với tín hiệu gốc. Trong trường hợp không có đường truyền thẳng, tín hiệu phản xạ có thể có mức công suất cao hơn, vì đường truyền của tín hiệu gốc có thể bị chắn một phần hoặc toàn bộ bởi các vật cản. Kết quả là công suất tín hiệu gốc, khi cộng với tín hiệu phản xạ, có thể giảm so với nhiễu, khiến bộ thu khó nhận diện tín hiệu hơn. Nhìn chung, hiệu ứng của hiện tượng truyền sóng đa đường nổi bật hơn trong các trường hợp này. Tuy nhiên, cần lưu ý rằng trong trường hợp không có đường truyền thẳng giữa bộ phát và bộ thu (như trong công viên hoặc trên phương tiện có dịch vụ Wi-Fi), tín hiệu chủ yếu được thu nhận nhờ vào sự nhiễu xạ và tán xạ.

Một hiệu ứng không mong muốn khác của truyền sóng đa đường là hiện tượng **nhiễu liên ký tự (InterSymbol Interference, ISI)**. Điều này xảy ra khi độ trễ của tín hiệu phản xạ so với tín hiệu gốc tương đương hoặc lớn hơn thời lượng của một ký tự (bit). Tín hiệu phản xạ của ký tự trước có thể được thu cùng lúc với tín hiệu cơ bản của ký tự sau. Kết quả là các tín hiệu đại diện cho các bit khác nhau cộng vào nhau, dẫn đến hỏng dữ liệu. Khi dữ liệu bị hỏng, bộ phát phải truyền lại dữ liệu. Số lượng lớn các lần truyền lại do nhiễu liên ký tự có thể làm giảm đáng kể băng thông của mạng không dây.

Việc **sử dụng điều chế OFDM** giúp giảm hoặc loại bỏ ảnh hưởng tiêu cực của nhiễu liên ký tự trong các hệ thống không dây. Nhiễu liên ký tự ảnh hưởng đáng kể khi tốc độ truyền dữ liệu cao, do khoảng cách giữa các ký tự (hoặc bit) là nhỏ. Với điều chế OFDM, tốc độ truyền dữ liệu giảm n lần (n là số kênh con mà luồng chính được chia thành), cho phép tăng thời gian truyền ký tự lên n lần, từ đó giảm thiểu ảnh hưởng của nhiễu liên ký tự.

Ngoài truyền sóng đa đường, các yếu tố khác như **suy hao tín hiệu, mất mát trong không gian tự do, nhiễu và hấp thụ bởi môi trường** cũng gây ra sự biến dạng tín hiệu trong kênh không dây.

Khi truyền tín hiệu qua bất kỳ môi trường nào, **cường độ tín hiệu** sẽ giảm theo khoảng cách, tức là xảy ra hiện tượng suy hao tín hiệu. Nếu khoảng cách giữa bộ thu và bộ phát vượt quá một giá trị nhất định, vượt quá mức suy hao có thể chấp nhận được, các bộ khuếch đại hoặc bộ lặp tín hiệu được đặt tại các điểm cụ thể trong không gian để tăng cường tín hiệu. Việc tăng cường tín hiệu trở nên phức tạp nếu có nhiều bộ thu, đặc biệt khi khoảng cách giữa chúng và trạm phát thay đổi.

**Mất mát trong không gian tự do (Free Space Path Loss, FSPL)** xảy ra khi tín hiệu được phân tán khi truyền trong không gian (tương tự như ánh sáng của đèn pha xe hơi giảm dần theo khoảng cách). Loại suy hao này làm giảm công suất tín hiệu từ bộ phát đến bộ thu, ngay cả khi không có nguyên nhân suy hao nào khác.

Nguyên nhân chính gây mất công suất tín hiệu bổ sung là **hấp thụ bởi môi trường**, trong đó hơi nước và oxy đóng vai trò quan trọng trong việc làm suy giảm tín hiệu. Mưa và sương mù (các giọt nước lơ lửng trong không khí) làm tán xạ sóng vô tuyến và dẫn đến suy yếu tín hiệu.

**Nguồn gây nhiễu trong các kênh không dây** bao gồm lò vi sóng, điện thoại không dây, máy phát vô tuyến, cảm biến chuyển động, mạng không dây lân cận, camera giám sát không dây, sét và nhiều nguồn khác. Tỷ lệ lỗi bit trong mạng không dây (BER) là 10⁻³.

**Giải pháp khắc phục vấn đề nhiễu cao trong các kênh không dây** được thực hiện theo nhiều cách khác nhau. Trong môi trường đô thị, các bộ phát tín hiệu (và bộ thu nếu có thể) thường được đặt trên các tòa nhà cao hoặc tháp để tránh hiện tượng phản xạ nhiều lần. Trong mạng không dây gia đình, một trong các giải pháp là thay đổi kênh tần số của điểm truy cập nếu có một thiết bị phát tín hiệu khác đang sử dụng cùng kênh tần số, đồng thời tắt tất cả các thiết bị gây nhiễu như lò vi sóng trước khi kết nối với mạng không dây.

Để xử lý lỗi do truyền sóng đa đường, **các phương pháp phân tán (diversity)** được sử dụng rộng rãi. Phân tán dựa trên thực tế rằng hiện tượng giảm công suất tín hiệu trong mỗi kênh xảy ra độc lập. Các lỗi có thể được khắc phục bằng cách tạo nhiều kênh logic giữa bộ thu và bộ phát, truyền các bản sao của tín hiệu qua từng kênh. Bộ thu sẽ chọn tín hiệu gốc tin cậy nhất từ các bản sao đã nhận.

Các loại phân tán trong mạng không dây bao gồm:

- **Phân tán theo tần số (Frequency diversity)** — tín hiệu được truyền qua nhiều sóng mang khác nhau, có thể thông qua các kênh tần số khác nhau hoặc bằng cách sử dụng các công nghệ mở rộng phổ và OFDM.
- **Phân tán theo thời gian (Time diversity)** — tín hiệu được truyền nhiều lần trong các khoảng thời gian khác nhau, sử dụng các khe thời gian và mã hóa kênh.
- **Phân tán theo không gian (Space diversity)** — sử dụng nhiều ăng-ten đặt gần nhau để thu nhận nhiều bản sao của tín hiệu. Đây là cơ sở cho công nghệ MIMO.

**MIMO (Multiple Input Multiple Output)** là công nghệ ăng-ten trong đó bộ thu và bộ phát sử dụng nhiều ăng-ten để cung cấp nhiều kênh truyền dữ liệu. MIMO được ứng dụng trong các mạng Wi-Fi hiện đại như chuẩn IEEE 802.11n, 802.11ac và 802.11ax, cũng như trong mạng di động LTE thế hệ thứ tư. Công nghệ này không chỉ giúp giảm thiểu ảnh hưởng tiêu cực của hiện tượng truyền sóng đa đường mà còn tận dụng hiệu ứng này để tăng băng thông của kênh truyền. Công nghệ MIMO sẽ được đề cập chi tiết hơn trong phần hai của khóa học.


<p align="center">
  <img src="https://github.com/CHu292/SOC/blob/main/Networking/Dlink_Fundamentals_of_Network_Technology/Data_Transmission_and_Switching_in_Computer_Networks/3_Physical_layer_of_the_OSI_model/image/3_77.png" alt="Hình 3.77 Truyền dữ liệu với hai luồng không gian (spatial streams) trong công nghệ MIMO" width="800">
</p>
<p align="center"><b>Hình 3.77 Truyền dữ liệu với hai luồng không gian (spatial streams) trong công nghệ MIMO</b></p>
