# 1. Mã hóa kỹ thuật số

Mã hóa kỹ thuật số của dữ liệu rời rạc được thực hiện bằng cách sử dụng mã xung hoặc mã điện thế. Để biểu diễn các số 0 và số 1 nhị phân, các mã thế sử dụng các giá trị tiềm năng tín hiệu khác nhau và mã xung sử dụng các xung có cực tính hoặc mức giảm tiềm năng khác nhau.

Chất lượng truyền dữ liệu, cụ thể là: độ tin cậy và độ chính xác của việc phân phối, khả năng phát hiện và sửa lỗi xảy ra cũng như chi phí thực hiện, phụ thuộc đáng kể vào phương pháp mã hóa kỹ thuật số đã chọn, do đó, quyết định phần lớn thông lượng của dữ liệu phương tiện truyền dẫn.

Về vấn đề này, để đảm bảo chất lượng truyền dữ liệu, một số yêu cầu được đặt ra đối với các phương thức mã hóa kỹ thuật số:

- Giảm phổ tín hiệu ở cùng tốc độ bit;
- Hỗ trợ đồng bộ hóa giữa máy phát và máy thu tín hiệu do sự hiện diện của các tín hiệu được truyền đi trên cơ sở thực hiện tự đồng bộ hóa;
- Sự vắng mặt của thành phần không đổi trong tín hiệu, làm dịch chuyển phổ tín hiệu sang vùng tần số thấp;
- Khả năng phát hiện lỗi và sửa chúng;
- Chi phí thực hiện phương pháp mã hóa thấp, tùy thuộc vào số lượng mức tín hiệu.

Việc giảm thiểu phổ của tín hiệu thu được sẽ đảm bảo rằng, đối với băng thông kênh liên lạc nhất định, lượng dữ liệu lớn hơn có thể được truyền đi trên một đơn vị thời gian. Điều này có thể được thực hiện, ví dụ, thông qua việc sử dụng ghép kênh tần số bằng cách tổ chức một số kênh logic trong cùng một đường truyền, cho phép tăng tốc độ truyền dữ liệu.

Ngoài ra, trong phổ tín hiệu không được có thành phần trực tiếp, tức là không được có dòng điện một chiều giữa máy phát và máy thu. Điều này là do việc sử dụng các mạch biến áp trong đường dây truyền thông điện để cách ly điện, ngăn cản dòng điện một chiều đi qua. Phổ của tín hiệu thu được phụ thuộc vào:

- Phương pháp mã hóa và điều chế;
- Tốc độ điều chế, ảnh hưởng đến tốc độ truyền dữ liệu;
- Thành phần của dữ liệu được truyền đi.

Để đồng bộ hóa máy phát và máy thu tín hiệu nhằm xác định thời điểm máy thu đọc giá trị của khoảng bit tiếp theo, các phương pháp mã hóa tự đồng bộ đặc biệt được sử dụng. Trong các phương pháp này, việc đồng bộ hóa máy thu với máy phát được thực hiện trên cơ sở dấu hiệu, tức là bất kỳ sự thay đổi đột ngột nào trong tín hiệu, được gọi là biên tín hiệu.

Yêu cầu không có thành phần không đổi trong tín hiệu là do nhu cầu duy trì sự đồng bộ giữa máy thu và máy phát. Ngoài ra, điều mong muốn là tần số thấp hơn của tín hiệu truyền đi khác với 0. Điều này giúp giảm phổ tín hiệu và cũng không cản trở dòng điện một chiều đi qua đường dây truyền thông điện khi có mạch cách ly điện máy biến áp.

Một yêu cầu mong muốn nhưng không bắt buộc đối với các phương pháp mã hóa kỹ thuật số là khả năng phát hiện lỗi và lý tưởng nhất là sửa chúng. Điều này giúp tiết kiệm thời gian vì lỗi được phát hiện ở lớp vật lý. Trong trường hợp này, khung bị lỗi sẽ bị loại bỏ trước khi hoàn tất quá trình nhận vào bộ đệm.

Chi phí thực hiện phương pháp mã hóa kỹ thuật số liên quan đến số lượng mức tín hiệu và càng nhiều mức tín hiệu thì thiết bị thu và phát càng mạnh và do đó, đắt hơn.

Các yêu cầu đối với các phương pháp mã hóa kỹ thuật số là trái ngược nhau. Hơn nữa, mỗi phương pháp mã hóa kỹ thuật số, so với các phương pháp khác, đều có những ưu điểm và nhược điểm riêng, sẽ được thảo luận dưới đây.
