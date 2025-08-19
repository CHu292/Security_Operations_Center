# JavaScript Essentials

## Mục lục

1. [Task 1: Introduction](#task-1-introduction)
2. [Task 2: Essential Concepts](#task-2-essential-concepts)
3. [Task 3: JavaScript Overview](#task-3-javascript-overview)


## Nội dung


# Task 1: Introduction
>Giới thiệu

JavaScript (JS) là một ngôn ngữ kịch bản phổ biến cho phép các nhà phát triển web thêm các tính năng tương tác vào các trang web chứa HTML và CSS (trình bày). Khi các phần tử HTML được tạo, bạn có thể thêm các tính năng tương tác như xác thực, hành động onClick, hoạt ảnh, v.v. thông qua JS. Việc học ngôn ngữ này cũng quan trọng không kém so với HTML và CSS. Các tập lệnh JS chủ yếu được sử dụng với HTML.

Phòng học này được thiết kế như một cái nhìn tổng quan giới thiệu về JS, đặc biệt phù hợp cho người mới bắt đầu với ít kinh nghiệm về JS. Trọng tâm chính là dạy các kiến thức cơ bản của JS từ góc độ an ninh mạng và cách tin tặc lợi dụng các chức năng hợp pháp để đạt được mục đích độc hại.

Mục tiêu học tập

* Hiểu những kiến thức cơ bản về JS
* Tích hợp JS trong HTML
* Lạm dụng hàm đối thoại
* Vượt qua các câu lệnh điều khiển luồng
* Khám phá các tệp đã được thu nhỏ

---

# Task 2: Essential Concepts
>Các khái niệm cơ bản

JavaScript (JS) là một công nghệ cốt lõi của phát triển web, chạy ở phía client để thêm tính tương tác, xử lý đầu vào của người dùng và thao tác với DOM (Document Object Model). JS rất linh hoạt và có thể được sử dụng như một ngôn ngữ thủ tục cũng như hướng đối tượng. Một số khái niệm cơ bản bao gồm:

* **Biến (Variables):** Lưu trữ giá trị dữ liệu và có thể được khai báo bằng `var`, `let`, hoặc `const`.

* **Kiểu dữ liệu (Data Types):** Bao gồm chuỗi (string), số (number), boolean, đối tượng (object) và mảng (array). JavaScript là ngôn ngữ kiểu động, nghĩa là kiểu dữ liệu được xác định khi chạy chương trình.

* **Hàm (Functions):** Khối mã được định nghĩa để thực hiện các tác vụ cụ thể và có thể tái sử dụng với nhiều đầu vào khác nhau.

Ví dụ mã:

```javascript
let age = 25;
let name = "Alice";
function greet(person) {
    console.log("Hello, " + person + "!");
}
greet(name); // Outputs: "Hello, Alice!"
```

---

## Functions


Một hàm đại diện cho một khối mã được thiết kế để thực hiện một tác vụ cụ thể. Bên trong một hàm, bạn nhóm lại những đoạn mã cần thực hiện một tác vụ tương tự.

Ví dụ, bạn đang phát triển một ứng dụng web trong đó cần in kết quả của học sinh trên trang web. Trường hợp lý tưởng là tạo ra một hàm `PrintResult(rollNum)` sẽ nhận số báo danh của học sinh làm tham số.

```html
<script>
        function PrintResult(rollNum) {
            alert("Username with roll number " + rollNum + " has passed the exam");
            // any other logic to display the result
        }

for (let i = 0; i < 100; i++) {
            PrintResult(rollNumbers[i]);
        }
    </script>
```

Vậy nên, thay vì viết cùng một đoạn mã in cho tất cả học sinh, chúng ta sẽ sử dụng một hàm đơn giản để in kết quả.


## Loops - Vòng lặp

Vòng lặp cho phép bạn chạy một khối mã nhiều lần miễn là điều kiện còn `true`. Các vòng lặp phổ biến trong JS là `for`, `while` và `do...while`, được sử dụng để lặp lại các tác vụ, giống như duyệt qua một danh sách các mục.

Ví dụ, nếu chúng ta muốn in kết quả của 100 học sinh, ta có thể gọi hàm `PrintResult(rollNum)` 100 lần bằng cách viết nó 100 lần, hoặc có thể tạo một vòng lặp lặp từ 1 đến 100 và sẽ gọi hàm `PrintResult(rollNum)` như minh họa bên dưới.

```html
<script>
        function PrintResult(rollNum) {
            alert("Username with roll number " + rollNum + " has passed the exam");
            // any other logic to display the result
        }

for (let i = 0; i < 100; i++) {
            PrintResult(rollNumbers[i]);
        }
    </script>
```

## Chu trình Yêu cầu – Phản hồi

Trong phát triển web, chu trình yêu cầu – phản hồi diễn ra khi trình duyệt của người dùng (client) gửi một yêu cầu đến máy chủ web, và máy chủ phản hồi lại với thông tin được yêu cầu. Thông tin này có thể là một trang web, dữ liệu hoặc các tài nguyên khác. Bạn có thể tìm hiểu thêm về nó tại đây.

## Câu hỏi

**Thuật ngữ nào cho phép bạn chạy một khối mã nhiều lần miễn là nó còn là một điều kiện?**
> Loop

---

# Task 3: JavaScript Overview
>Tổng quan về JavaScript

JavaScript thường được thực thi trực tiếp trong trình duyệt web, cho phép các nhà phát triển kiểm tra và thao tác mã theo thời gian thực. Sử dụng **Console** của Google Chrome là một cách nhanh chóng để kiểm thử và gỡ lỗi mã JavaScript:

1. Mở Developer Tools của Chrome (**Ctrl + Shift + I** trên Windows hoặc **Cmd + Option + I** trên Mac).
2. Điều hướng đến tab **Console** để nhập lệnh JavaScript trực tiếp.

**Ví dụ lệnh:**

```javascript
console.log("Hello, World!"); // In ra "Hello, World!" trên console
```

JavaScript chủ yếu được thực thi phía client (trình duyệt), giúp dễ dàng kiểm tra và tương tác với HTML trực tiếp trong trình duyệt. Chúng ta sẽ sử dụng tính năng **Chrome Console** để chạy chương trình JS đầu tiên, cho phép viết và thực thi mã JS một cách dễ dàng mà không cần công cụ bổ sung.

**Các bước bắt đầu:**

* Mở **Google Chrome** bằng cách nhấp vào biểu tượng **Google Chrome** trên màn hình Desktop của máy ảo (VM).

![](./img/2_JavaScript_Essentials/3.1webp)

* Khi Chrome đã mở, nhấn **Ctrl + Shift + I** để mở **Console** hoặc nhấp chuột phải vào bất kỳ đâu trên trang và chọn **Inspect**.

![](./img/2_JavaScript_Essentials/3.2.webp)

* Sau đó, nhấp vào tab **Console**. Bảng điều khiển này cho phép bạn chạy mã JS trực tiếp trong trình duyệt mà không cần cài đặt thêm phần mềm.

![](./img/2_JavaScript_Essentials/3.3.webp)

* Hãy tạo một chương trình JS đơn giản cộng hai số và hiển thị kết quả. Dưới đây là đoạn mã:

```javascript
let x = 5;
let y = 10;
let result = x + y;
console.log("The result is: " + result);
```

* Trong đoạn mã trên, `x` và `y` là các biến lưu giữ số. `x + y` là một biểu thức cộng hai số lại với nhau, trong khi `console.log` là một hàm dùng để in kết quả ra bảng điều khiển.

* Sao chép đoạn mã trên và dán vào bảng điều khiển bằng cách nhấn phím `Ctrl + V`. Sau khi dán, nhấn `Enter`. Bạn sẽ thấy kết quả hiển thị như sau:

![](./img/2_JavaScript_Essentials/3.4.webp)

## Câu hỏi

Trả lời các câu hỏi dưới đây

**Câu hỏi:** Kết quả của đoạn mã sẽ là gì nếu giá trị của `x` được thay đổi thành 10?

**Trả lời:** Kết quả là: 20

![](./img/2_JavaScript_Essentials/3.5.png)

---

**Câu hỏi:** JavaScript là ngôn ngữ biên dịch hay thông dịch?

**Trả lời:** Thông dịch
