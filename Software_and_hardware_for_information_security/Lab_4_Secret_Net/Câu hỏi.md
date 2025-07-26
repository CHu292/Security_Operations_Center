### Цели лабораторной работы

Познакомиться с системой Secret Net 5.1 для защиты информации от несанкционированного доступа (НСД).  (Làm quen với hệ thống Secret Net 5.1 để bảo vệ thông tin khỏi truy cập trái phép (НСД).)
Изучить механизмы управления доступом в системе:
- Избирательное (дискреционное) управление доступом.  - Quản lý truy cập có chọn lọc (Discretionary Access Control).

- Полномочное (мандатное) управление доступом.  - Quản lý truy cập toàn quyền (Mandatory Access Control).
  
- Замкнутая программная среда (ЗПС).  - Môi trường phần mềm khép kín (ЗПС).


---
### **Câu hỏi và trả lời**

---

#### 1. Какие механизмы управления доступом пользователей к ресурсам компьютера используются в системе Secret Net 5.1?
Những cơ chế quản lý truy cập nào được sử dụng trong hệ thống Secret Net 5.1?

- В системе Secret Net 5.1 используются следующие механизмы управления доступом:
  1. Избирательное (дискреционное) управление доступом.
  2. Полномочное (мандатное) управление доступом.
  3. Замкнутая программная среда (ЗПС).
- Trong hệ thống Secret Net 5.1, các cơ chế quản lý truy cập được sử dụng gồm:
  1. Quản lý truy cập có chọn lọc (Discretionary Access Control).
  2. Quản lý truy cập toàn quyền (Mandatory Access Control).
  3. Môi trường phần mềm khép kín (ЗПС).

---

#### 2. Каковы особенности функционирования механизма разграничения доступа к устройствам в «мягком» режиме?

Đặc điểm của cơ chế phân quyền thiết bị trong chế độ "мягкий" là gì?
- В «мягком» режиме доступ пользователей к устройствам контролируется, но не ограничивается. Все попытки доступа записываются в журнал событий.
- Trong chế độ **"мягкий" (mềm)**, quyền truy cập của người dùng vào thiết bị được giám sát nhưng không bị hạn chế. Tất cả các lần truy cập được ghi lại vào nhật ký sự kiện.

---

#### 3. Каковы особенности функционирования механизма разграничения доступа к устройствам в «жестком» режиме?
Đặc điểm của cơ chế phân quyền thiết bị trong chế độ "жесткий" là gì?

- В «жестком» режиме доступ блокируется при превышении пользователем установленных прав. Попытки доступа также регистрируются в журнале событий.
- Trong chế độ **"жесткий" (cứng)**, quyền truy cập bị chặn nếu người dùng vượt quá quyền được cấp. Các lần truy cập cũng được ghi lại trong nhật ký sự kiện.

---

#### 4. Можно ли поменять права доступа на системный диск (C:)?
Có thể thay đổi quyền truy cập trên ổ đĩa hệ thống (C:) không?

- Изменение прав доступа к системному диску (C:) возможно только с правами администратора. В некоторых случаях система может запретить такие изменения для защиты данных.
- Quyền truy cập trên ổ đĩa hệ thống (C:) chỉ có thể thay đổi với quyền quản trị viên. Trong một số trường hợp, hệ thống có thể chặn các thay đổi này để bảo vệ dữ liệu.

---

#### 5. Для чего предназначен механизм замкнутой программной среды?
Môi trường phần mềm khép kín được thiết kế để làm gì?

- Механизм ЗПС ограничивает запуск только тех программ, которые входят в список разрешённых. Это предотвращает несанкционированное выполнение приложений.
- Cơ chế môi trường phần mềm khép kín (ЗПС) hạn chế việc chỉ khởi chạy các chương trình nằm trong danh sách được phép, ngăn chặn việc thực thi trái phép các ứng dụng.

---

#### 6. Что представляет собой модель данных в системе Secret Net 5.1?
Mô hình dữ liệu trong hệ thống Secret Net 5.1 là gì?

- Модель данных в системе Secret Net 5.1 представляет собой иерархическую структуру объектов, описывающую связи между ресурсами, группами ресурсов, задачами, заданиями и субъектами управления.
- Mô hình dữ liệu trong hệ thống Secret Net 5.1 là một cấu trúc phân cấp các đối tượng, mô tả mối quan hệ giữa tài nguyên, nhóm tài nguyên, tác vụ, nhiệm vụ và đối tượng quản lý.

---

#### 7. Какие пользователи имеют право изменять категорию конфиденциальности ресурсов в системе Secret Net 5.1?
Người dùng nào có quyền thay đổi mức độ bảo mật tài nguyên trong hệ thống Secret Net 5.1?
- Только пользователи с привилегией «Управление категориями конфиденциальности» могут изменять категории конфиденциальности ресурсов.
- Chỉ những người dùng có đặc quyền "Quản lý mức độ bảo mật" mới có quyền thay đổi mức độ bảo mật của tài nguyên.

---

#### 8. На дисках с какой файловой системой должны быть расположены ресурсы в системе Secret Net 5.1, чтобы им можно было присвоить категорию конфиденциальности?
Tài nguyên phải nằm trên hệ thống file nào để có thể gán mức độ bảo mật?

- Ресурсы должны находиться на дисках с файловой системой NTFS, чтобы им можно было присвоить категорию конфиденциальности.
- Các tài nguyên phải nằm trên ổ đĩa sử dụng hệ thống file NTFS để có thể áp dụng mức độ bảo mật.

---

#### 9.  Назовите привилегии, доступные для пользователей с уровнем допуска к конфиденциальной информации «конфиденциально» или «строго конфиденциально».
Những đặc quyền nào được cấp cho người dùng có quyền truy cập "Confidential" hoặc "Strictly Confidential"?
- Привилегии для таких пользователей:
  - Управление категориями конфиденциальности.
  - Печать конфиденциальных документов.
  - Вывод конфиденциальной информации на внешние носители.
- Các đặc quyền cho những người dùng này gồm:
  - Quản lý mức độ bảo mật.
  - In tài liệu bảo mật.
  - Xuất thông tin bảo mật ra các thiết bị ngoài.

---

#### 10. Назовите особенности работы механизма замкнутой программной среды в «мягком» режиме.
Đặc điểm của cơ chế môi trường phần mềm khép kín trong chế độ "мягкий" là gì?

- В «мягком» режиме пользователям разрешается запуск любых программ, но все попытки запуска незарегистрированных программ фиксируются в журнале событий.
- Trong chế độ **"мягкий" (mềm)**, người dùng được phép khởi chạy bất kỳ chương trình nào, nhưng tất cả các lần khởi chạy chương trình không được phép đều được ghi lại trong nhật ký sự kiện.

---

#### 11. Назовите особенности работы механизма замкнутой программной среды в «жестком» режиме. 
Đặc điểm của cơ chế môi trường phần mềm khép kín trong chế độ "жесткий" là gì?

- В «жестком» режиме разрешается запуск только тех программ, которые входят в список разрешённых. Запуск других программ блокируется, а события фиксируются в журнале.
- Trong chế độ **"жесткий" (cứng)**, chỉ các chương trình trong danh sách được phép mới có thể khởi chạy. Việc khởi chạy các chương trình khác sẽ bị chặn, và sự kiện sẽ được ghi lại trong nhật ký.

--- 

