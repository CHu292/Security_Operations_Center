# Chương Trình Đăng Ký Người Dùng Đơn Giản

Dự án này triển khai một hệ thống đăng ký người dùng đơn giản yêu cầu nhập họ và tên của người dùng và lưu trữ thông tin này vào tệp văn bản. Chương trình có hai giới hạn sử dụng: dựa trên thời gian và số lượt sử dụng. Khi đạt đến các giới hạn này, chương trình sẽ ngừng hoạt động và đề xuất người dùng mua phiên bản đầy đủ hoặc gỡ cài đặt chương trình.

## Tổng Quan Chương Trình

**Yêu cầu đề bài**:
- Phát triển một chương trình đơn giản yêu cầu người dùng nhập họ và tên (ФИО) và lưu thông tin này vào một tệp văn bản.
- Nếu họ và tên đã tồn tại trong tệp, chương trình sẽ thông báo cho người dùng.
- Sau khi nhận được thông tin, chương trình sẽ kết thúc và thông báo cho người dùng về giới hạn sử dụng (giới hạn thời gian hoặc số lượt sử dụng).
- Khi đạt đến giới hạn, chương trình sẽ đề xuất người dùng mua phiên bản đầy đủ hoặc gỡ cài đặt chương trình.
- Khi cài đặt lại, chương trình sẽ phát hiện lần cài đặt trước và tuân thủ các giới hạn trước đó (tức là không cho phép vượt qua giới hạn bằng cách cài đặt lại).

Dự án bao gồm:
- Tập lệnh cài đặt (`install.sh`),
- Chương trình chính (`simple_program.py`), và
- Tập lệnh gỡ cài đặt (`uninstall.sh`).

Hai loại giới hạn sử dụng:
1. **Giới hạn thời gian** (Giới hạn thời gian sử dụng là 30 giây trong phiên bản này).
2. **Giới hạn số lượt khởi động** (Giới hạn 5 lần khởi động chương trình).

## Các Tính Năng

- Chương trình lưu trữ họ và tên người dùng vào tệp (`user_data.txt`).
- Nếu họ và tên của người dùng đã tồn tại, chương trình sẽ thông báo.
- Chương trình áp dụng hai giới hạn: thời gian sử dụng và số lượt khởi động.
- Khi vượt quá các giới hạn, chương trình sẽ dừng hoạt động và yêu cầu người dùng mua phiên bản đầy đủ hoặc gỡ cài đặt chương trình.
- Giới hạn được lưu lại giữa các lần cài đặt, không thể vượt qua giới hạn bằng cách cài đặt lại.

## Hướng Dẫn Sử Dụng

### Cài Đặt

1. Tải về các tệp của dự án hoặc sao chép từ repository.
2. Mở terminal và điều hướng đến thư mục chứa các tệp.
3. Chạy tập lệnh cài đặt để cài đặt chương trình:
   ```bash
   ./install.sh
   ```
   Tập lệnh sẽ tạo ra các tệp cần thiết (`user_data.txt`, `limit_data.txt`) trong thư mục hiện tại. Nếu chương trình đã được cài đặt trước đó, nó sẽ thông báo cho bạn.

### Chạy Chương Trình

Sau khi cài đặt, bạn có thể chạy chương trình bằng lệnh sau:

```bash
./simple_program.py
```

- Chương trình sẽ yêu cầu bạn nhập họ và tên (ФИО).
- Nếu tên của bạn đã tồn tại trong hệ thống, chương trình sẽ thông báo.
- Bạn có thể sử dụng lệnh `show` trong quá trình chạy để xem số lượt còn lại và thời gian trước khi hết hạn.

**Lưu ý**: 
- Nếu vượt quá giới hạn số lượt khởi động hoặc thời gian, chương trình sẽ thông báo và không cho phép sử dụng tiếp.

### Gỡ Cài Đặt

Để gỡ cài đặt chương trình, hãy sử dụng tập lệnh gỡ cài đặt:

```bash
./uninstall.sh
```

Tập lệnh này sẽ xóa các tệp của chương trình (`user_data.txt`, `limit_data.txt`, và cờ cài đặt) khỏi thư mục hiện tại.

## Quy Trình Chi Tiết

1. **Nhập Thông Tin Người Dùng**: 
   - Chương trình yêu cầu người dùng nhập họ và tên.
   - Tên này được mã hóa và kiểm tra với dữ liệu đã lưu trong `user_data.txt`.
   - Nếu tên đã tồn tại, chương trình sẽ thông báo; nếu chưa, tên sẽ được lưu vào tệp.

2. **Kiểm Tra Giới Hạn**:
   - Chương trình kiểm tra xem người dùng có vượt quá giới hạn thời gian (30 giây) hoặc số lượt khởi động (5 lần) không.
   - Nếu giới hạn đã đạt, chương trình sẽ kết thúc và đề xuất người dùng mua phiên bản đầy đủ hoặc gỡ cài đặt chương trình.

3. **Cài Đặt Lại**:
   - Nếu chương trình bị gỡ cài đặt và cài lại, dữ liệu về giới hạn sử dụng vẫn được giữ nguyên, người dùng không thể vượt qua giới hạn bằng cách cài đặt lại.

### Ví Dụ Sử Dụng

1. **Lần Chạy Đầu Tiên**:
   ```bash
   ./simple_program.py
   ```
   Output:
   ```
   Vui lòng nhập họ và tên của bạn: Nguyễn Văn A
   Thông tin của bạn đã được lưu thành công.
   ```

2. **Lần Chạy Sau Khi Đạt Giới Hạn**:
   Nếu người dùng đã đạt giới hạn:
   ```bash
   ./simple_program.py
   ```
   Output:
   ```
   Hết lượt sử dụng. Vui lòng mua phiên bản đầy đủ hoặc gỡ cài đặt chương trình.
   ```

## Yêu Cầu Hệ Thống

- Python 3.x
- Hệ điều hành Unix-like (Linux hoặc macOS) có hỗ trợ bash để cài đặt/gỡ cài đặt.

## Ghi Chú

- Giới hạn thời gian sử dụng được đặt thành 30 giây để dễ dàng kiểm tra.
- Giới hạn số lần khởi động là 5 lần để kiểm tra nhanh.

Chương trình này thể hiện các chức năng yêu cầu của đề bài, bao gồm lưu thông tin người dùng, kiểm tra giới hạn sử dụng và xử lý trường hợp cài đặt lại nhưng vẫn giữ nguyên dữ liệu giới hạn.

## Giấy Phép

Dự án này được cấp phép theo MIT License.
