# Floating-Point Operations Per Second (FLOPS)

[Bài Viết Gốc](https://www.geeksforgeeks.org/computer-organization-architecture/what-is-floating-point-operations-per-second-flops/)

---

## 1. FLOPS là gì – Số lượng phép toán dấu phẩy động mỗi giây?


Khi nói đến máy tính hoặc hiệu suất tính toán, đặc biệt là trong các lĩnh vực yêu cầu hiệu suất cao như tính toán khoa học, mô phỏng, và học máy, thuật ngữ FLOPS (Floating-Point Operations Per Second – Số phép toán dấu phẩy động mỗi giây) thường được nhắc đến. Để hiểu rõ hơn, trước tiên ta cần định nghĩa FLOPS – nghĩa là số phép toán dấu phẩy động được thực hiện mỗi giây – đây là một yếu tố quan trọng khi so sánh sức mạnh tính toán của các hệ thống khác nhau, đặc biệt là trong những lĩnh vực mà phép tính số học là yếu tố then chốt. Bài viết này nhằm cung cấp kiến thức cơ bản về FLOPS, tầm quan trọng của nó, và ảnh hưởng của FLOPS đến hiệu năng của máy tính.

---

## 2. Phép toán dấu phẩy động là gì?

Phép toán dấu phẩy động là các phép tính toán học được thực hiện trên các số dấu phẩy động, bao gồm cộng, trừ, nhân hoặc chia. Các số dấu phẩy động là cách biểu diễn các số thực có phần thập phân, giúp duy trì độ chính xác cao trong các phép tính khoa học và ứng dụng khác đòi hỏi tính chính xác tuyệt đối. So với các phép toán trên số nguyên, các phép toán dấu phẩy động có khả năng xử lý phạm vi giá trị rộng hơn rất nhiều và có thể biểu diễn các số rất lớn hoặc rất nhỏ tùy theo yêu cầu của tác vụ cụ thể. Vì vậy, chúng phù hợp hơn cho các bài toán đòi hỏi khối lượng tính toán lớn hơn so với các phép toán số nguyên.

---

## 3. Tại sao lại sử dụng số dấu phẩy động?

Số dấu phẩy động rất quan trọng trong tính toán vì chúng đại diện cho các giá trị số thực gần đúng, dễ dàng được xử lý bởi máy tính. Chúng thường được lưu trữ theo định dạng tuân theo tiêu chuẩn IEEE 754. Định dạng này cung cấp một phương pháp chính xác để thao tác với các số trong môi trường chuẩn, có thể được triển khai trong nhiều hệ thống máy tính. Nó cũng đảm bảo độ chính xác của các phép tính nhờ tuân thủ bộ hướng dẫn nghiêm ngặt trong nghiên cứu, kỹ thuật và các hoạt động quản lý tài chính.

---

## 4. FLOPS – Số phép toán dấu phẩy động mỗi giây nghĩa là gì?

FLOPS là khả năng của máy tính trong việc thực hiện các phép tính, đặc biệt là các phép toán dấu phẩy động, và thường được sử dụng trong các phép tính thiên về khoa học. Nó đo lường số lượng các phép toán mà hệ thống có thể thực hiện trong một giây. FLOPS biểu thị hiệu suất tính toán theo thời gian thực – nơi mà FLOPS cao hơn đồng nghĩa với việc hệ thống có khả năng thực hiện số lượng lớn phép tính trong một khoảng thời gian nhất định.

---

## 5. Tầm quan trọng của FLOPS

Trong lĩnh vực siêu máy tính, FLOPS là viết tắt của Floating Point Operations Per Second (số phép toán dấu phẩy động mỗi giây) và là một chỉ số thiết yếu để đo lường sức mạnh tính toán. Trước hết, nó cung cấp một phương pháp để so sánh khả năng tính toán thô của các hệ thống hiện đại – từ máy tính cá nhân của người dùng thông thường cho đến các siêu máy tính được xếp hạng toàn cầu. Ví dụ, trong danh sách Top 500 – nơi liệt kê các siêu máy tính mạnh nhất thế giới – FLOPS được xem là thước đo quan trọng nhất để đánh giá và so sánh khả năng của các máy tính này.

---

## 6. FLOPS được tính như thế nào?

### 6.1 Đo lường FLOPS

FLOPS có thể được xác định dựa trên tốc độ thực hiện các phép toán dấu phẩy động trong một hệ thống mỗi giây. Điều này được thiết lập bằng cách so sánh các bài kiểm tra thực hiện một số lượng cố định các phép toán trong thanh ghi dấu phẩy động và thời gian thực hiện. Trong số đó có LINPACK, một bộ kiểm tra tiêu chuẩn cung cấp một ví dụ cụ thể để giải một hệ phương trình tuyến tính dày đặc, cũng như các bài kiểm tra khác được tối ưu hóa cho từng loại phép toán cụ thể.

---

### 6.2 Các yếu tố ảnh hưởng đến FLOPS

Nhiều yếu tố ảnh hưởng đến hiệu suất FLOPS của một hệ thống:

* **Kiến trúc vi xử lý (Processor Architecture):** Số lượng lõi hoặc kiến trúc tổng thể của CPU hoặc GPU quyết định mức độ hiệu quả trong việc tính toán các phép toán dấu phẩy động (floating points). Các phiên bản vi xử lý hiện đại có tích hợp đơn vị FPU chuyên biệt để thực hiện các phép toán này một cách hiệu quả hơn.

* **Tốc độ xung nhịp (Clock Speed):** Một yếu tố khác là tốc độ xung nhịp, đo lường số lượng lệnh (instructions) mà bộ xử lý có thể thực hiện trong một giây, thường được biểu diễn bằng gigahertz (GHz).

* **Tính song song (Parallelism):** Khả năng thực hiện đồng thời nhiều phép toán, hay còn gọi là tính đồng bộ của hệ thống. Điều này bao gồm số lõi trong một CPU, việc sử dụng GPU cũng như các cấu hình tính toán song song khác.

* **Băng thông bộ nhớ (Memory Bandwidth):** Khả năng xử lý thông tin, cụ thể là tốc độ đọc hoặc ghi dữ liệu vào bộ nhớ mỗi giây. Băng thông bộ nhớ cao là cần thiết để dữ liệu được truyền đến bộ xử lý với tốc độ đủ nhanh nhằm duy trì hiệu suất FLOPS.

* **Hiệu suất thuật toán (Algorithm Efficiency):** Bản chất của các thuật toán được sử dụng trong quá trình tính toán có thể ảnh hưởng mạnh đến FLOPS. Những thuật toán tối ưu hóa có thể giúp giảm số lượng phép toán cần thiết để hoàn thành một tác vụ, từ đó nâng cao hiệu quả tổng thể.

---

## 7. Ứng dụng của FLOPS

### 7.1 Nghiên cứu khoa học

FLOPS tạo ra tác động lớn đối với các nhiệm vụ nghiên cứu khoa học như mô phỏng, mô hình hóa và xử lý phân tích dữ liệu. Khả năng xử lý FLOP cao giúp các nhà nghiên cứu thực hiện các mô phỏng chi tiết, phân tích tập dữ liệu lớn và thu được kết quả nhanh hơn. Mô hình khí hậu – một lĩnh vực yêu cầu mô phỏng khí quyển chi tiết với độ chính xác cao và mô phỏng các mô hình thời tiết trong khoảng thời gian dài – là một nhiệm vụ tính toán phức tạp tiêu tốn FLOPS lớn. Ngoài ra, vật lý thiên văn (astrophysics), liên quan đến mô phỏng các tương tác phức tạp giữa các thiên thể (celestial bodies), cũng là một ví dụ điển hình về nhiệm vụ cần FLOPS cao.

---

### 7.2 Học máy và trí tuệ nhân tạo (Machine Learning and AI)

Tương tự, các ứng dụng học máy và trí tuệ nhân tạo (artificial intelligence) đòi hỏi hiệu suất FLOPS cực kỳ cao. Ví dụ, trong quá trình huấn luyện các mạng nơ-ron sâu (deep neural networks), cần một lượng FLOPS lớn để điều chỉnh tập hợp các tham số dấu phẩy động của mạng thông qua thuật toán lan truyền ngược (backpropagation). Tất cả điều này có nghĩa là nếu môi trường tính toán của bạn có hiệu suất FLOPS cao, bạn sẽ cảm thấy hoàn toàn phù hợp – giúp giảm thời gian huấn luyện và có thể cho phép sử dụng các mô hình phức tạp hơn trên tập dữ liệu lớn hơn.

---

### 7.3 Mô hình tài chính (Financial Modeling)

FLOPS đóng góp vào lĩnh vực tài chính thông qua đánh giá rủi ro, định giá quyền chọn và mô phỏng giao dịch thời gian thực. Các mô hình tài chính thường yêu cầu khối lượng tính toán lớn, trong nhiều trường hợp cần được xử lý nhanh chóng và chính xác. FLOPS đảm bảo dữ liệu được xử lý theo thời gian thực, từ đó hỗ trợ ra quyết định tốt hơn và đảm bảo dòng chảy giao dịch trên thị trường diễn ra suôn sẻ.

---

## 8. FLOPS trong sự phát triển điện toán

### 8.1 Thời kỳ đầu của FLOPS

Khái niệm này được đưa ra như một nỗ lực nhằm đo lường hiệu suất của các máy tính khoa học thời kỳ đầu, vốn chủ yếu được sử dụng để giải các phương trình vi phân và thực hiện phân tích thống kê. Những siêu máy tính đầu tiên như Cray-1 được đo bằng đơn vị megaflops (hàng triệu phép toán dấu phẩy động mỗi giây).

---

### 8.2 Siêu máy tính hiện đại

Hiện nay, những siêu máy tính mạnh mẽ nhất được đo bằng đơn vị petaflops (nghìn nghìn tỷ FLOPS) và exaflops (tỷ tỷ FLOPS). Những hệ thống này triển khai hàng ngàn bộ xử lý cùng lúc, thường sử dụng CPU kết hợp với GPU để đạt được hiệu suất cực cao. Một số ví dụ tiêu biểu bao gồm: Summit – được phát triển bởi IBM cho Phòng thí nghiệm Quốc gia Oak Ridge (Mỹ), và Fugaku – được phát triển bởi RIKEN và Fujitsu (Nhật Bản), hiện đang giữ vị trí số một trong danh sách Top500.

---

### 8.3 Triển vọng tương lai

Tương lai của FLOPS phụ thuộc vào các công nghệ điện toán mới – trong đó nổi bật là điện toán lượng tử và điện toán thần kinh (neuromorphic computing). Những công nghệ này hứa hẹn mang lại hiệu năng vượt trội bằng cách tận dụng các nguyên lý của cơ học lượng tử và mô phỏng kiến trúc não người. Khi những công nghệ này phát triển và hoàn thiện, chúng ta có thể kỳ vọng sẽ đạt được các chỉ số FLOPS cao hơn nữa, cũng như xuất hiện những ứng dụng mới mà trước đây không ai có thể hình dung được.

---

##  9. Kết luận

FLOPS (Floating-Point Operations Per Second) là một chỉ số có vai trò cực kỳ quan trọng trong lĩnh vực điện toán. Nó cung cấp một phương pháp phổ quát và nhất quán để đo lường và so sánh sức mạnh tính toán, dù là trong nghiên cứu khoa học, học máy (machine learning) hay mô hình tài chính. Trong tương lai, khi công nghệ ngày càng thay đổi, FLOPS sẽ trở thành một yếu tố then chốt thúc đẩy các phát minh và đột phá trong nhiều lĩnh vực khác nhau.

---

