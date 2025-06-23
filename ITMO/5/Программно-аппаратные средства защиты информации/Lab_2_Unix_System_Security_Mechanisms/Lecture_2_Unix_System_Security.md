# Bài giảng 2: Bảo mật hệ thống Unix

## Các nhóm hệ thống Linux

Hiện tại có 7 nhóm hệ thống Unix:

- Debian
- Red Hat (RHEL)
- Arch Linux
- Gentoo
- Slackware
- SUSE
- Independent


# 1. Bảo mật trong các phân phối Debian-based, Arch Linux-based, Slackware-based

Các phân phối dựa trên Debian như Debian, Ubuntu, Linux Mint và các hệ điều hành khác được biết đến với độ tin cậy và ổn định cao, điều này cũng làm cho chúng trở thành lựa chọn tốt về mặt bảo mật. Tuy nhiên, bảo mật hệ thống phụ thuộc vào nhiều yếu tố, bao gồm cập nhật thường xuyên, cấu hình chính xác và sử dụng các công cụ tích hợp sẵn. Dưới đây là các khía cạnh chính của bảo mật trong các phân phối Debian-based:

## 1.1 Cập nhật thường xuyên

Debian và các bản phân phối khác thường cung cấp các bản cập nhật bảo mật cho tất cả các gói hỗ trợ. Các bản cập nhật này bao gồm các bản vá cho các lỗ hổng bảo mật được phát hiện trong hệ điều hành hoặc phần mềm của bên thứ ba.

Người dùng được khuyến nghị cập nhật hệ thống thường xuyên bằng APT để đảm bảo rằng tất cả các gói được cập nhật lên phiên bản ổn định và bảo mật nhất. Nhóm bảo mật của Debian theo dõi các lỗ hổng mới và nhanh chóng phát hành các bản cập nhật.

[Hướng dẫn đầy đủ về APT](https://manpages.ubuntu.com/manpages/bionic/man8/apt.8.html)

[Hướng dẫn cách sử dụng ATP](https://github.com/CHu292/SOC/blob/main/Software_and_hardware_for_information_security/Lab_2_Unix_System_Security_Mechanisms/Further_reading/ATP.md)


Các lệnh cập nhật hệ thống:

```bash
sudo apt update
sudo apt upgrade
```

## 1.2 Các gói hỗ trợ dài hạn (LTS)

Debian Stable và Ubuntu LTS tập trung vào hỗ trợ dài hạn (Ubuntu LTS hỗ trợ 5 năm), điều này giúp chúng ổn định và an toàn khi sử dụng trên các máy chủ và hệ thống quan trọng. Các phiên bản này chỉ bao gồm các phiên bản phần mềm đã được kiểm tra kỹ lưỡng và ổn định, giảm thiểu nguy cơ từ các lỗ hổng bảo mật.

## 1.3 AppArmor và SELinux

Trong các phân phối dựa trên Debian, AppArmor thường được sử dụng (Ubuntu bật sẵn AppArmor). AppArmor là một cơ chế kiểm soát truy cập dựa trên hồ sơ, hạn chế hành động của các chương trình trong hệ thống, ngăn chặn truy cập trái phép vào các tài nguyên hệ thống.

[Thông tin thêm về AppArmor](https://gitlab.com/apparmor/apparmor/-/wikis/Documentation)

Quản lý AppArmor:

```bash
sudo systemctl status apparmor
sudo aa-status
```

SELinux (Security-Enhanced Linux) cũng có thể được cài đặt và cấu hình, cung cấp chính sách bảo mật phức tạp hơn nhưng cần thiết lập kỹ lưỡng.

[Thông tin thêm về SELinux](https://losst.pro/nastrojka-selinux)

## 1.4 Mã hóa dữ liệu

Các phân phối Debian-based hỗ trợ mã hóa toàn bộ ổ đĩa với LUKS (Linux Unified Key Setup) và dm-crypt. Điều này đặc biệt quan trọng để bảo vệ dữ liệu nhạy cảm khi có truy cập vật lý vào thiết bị.

Trong quá trình cài đặt, bạn có thể chọn mã hóa thư mục cá nhân hoặc toàn bộ ổ đĩa, thêm một lớp bảo mật bổ sung.

[Thông tin thêm về LUKS](https://gitlab.com/cryptsetup/cryptsetup/)

[Thông tin thêm về dn-crypt](https://en.wikipedia.org/wiki/Dm-crypt)

## 1.5 Firewall - Tường lửa

Hầu hết các hệ thống Debian-based tích hợp và dễ cấu hình tường lửa dựa trên iptables hoặc phiên bản đơn giản hơn ufw (Uncomplicated Firewall), có thể dùng để lọc lưu lượng mạng và ngăn chặn truy cập trái phép.

UFW được cài đặt mặc định trong Ubuntu và các bản phân phối liên quan, nhưng có thể thêm vào các phân phối khác.

Các lệnh cấu hình UFW:

```bash
sudo ufw enable
sudo ufw allow ssh
sudo ufw deny 80
```

[Tìm hiểu thêm về iptables](https://wiki.archlinux.org/title/Iptables)

[Tìm hiểu thêm về UFW](https://help.ubuntu.com/community/UFW)

## 1.6 Cập nhật thường xuyên kernel và gói

Debian và Ubuntu sử dụng phiên bản ổn định của nhân Linux, nhưng người dùng có thể cập nhật nhân thủ công nếu cần. Điều này cho phép các lỗ hổng ở cấp kernel được giải quyết kịp thời.

Ngoài ra còn có backport - kho lưu trữ với các phiên bản gói mới hơn dành cho các bản phát hành ổn định, có thể được sử dụng để cài đặt các bản cập nhật quan trọng mà không cần phải cập nhật toàn bộ bản phân phối.

[Tìm hiểu thêm về backports](https://wiki.debian.org/ru/Backports)

## 1.7 Cách ly ứng dụng trong các container

Các phân phối Debian-based hiện đại hỗ trợ sử dụng container như Docker, tạo môi trường cách ly cho ứng dụng với các phụ thuộc và cấu hình riêng, cải thiện bảo mật bằng cách giảm thiểu tác động của các lỗ hổng có thể có.

[Tìm hiểu thêm về Docker](https://docs.docker.com/)

LXC (Linux Container) là một tùy chọn chứa khác được Debian hỗ trợ, có thể được sử dụng để cách ly và cải thiện bảo mật ứng dụng.

[Tìm hiểu thêm về LXC](https://ubuntu.com/server/docs/lxc-containers)

## 1.8 Kiểm tra chữ ký gói

Tất cả các gói trong kho của Debian và các bản phân phối liên quan đều được ký bằng khóa mật mã, ngăn chặn cài đặt các gói không có thẩm quyền hoặc bị thay đổi.

Người dùng cũng có thể thêm kho lưu trữ và khóa ký theo cách thủ công thông qua APT, nhưng cần cẩn thận với các nguồn không chính thức.

## 1.9 Fail2Ban

Để bảo vệ khỏi các cuộc tấn công brute-force nhắm vào các dịch vụ như SSH, bạn có thể sử dụng Fail2Ban, công cụ này theo dõi nhật ký và tự động chặn các địa chỉ IP sau một số lần đăng nhập thất bại.

[Tìm hiểu thêm về Fail2Ban](https://help.ubuntu.com/community/Fail2ban)

Cài đặt và cấu hình Fail2Ban:

```bash
sudo apt install fail2ban
sudo systemctl enable fail2ban
sudo systemctl start fail2ban
```

## 1.10 Kiểm soát tài khoản và quyền hạn

Trong các hệ thống Debian-based, phân quyền truy cập của người dùng và nhóm được thực hiện nghiêm ngặt với quyền POSIX và hệ thống kiểm soát quyền (ví dụ: dùng sudo).

Bạn cũng có thể sử dụng các cơ chế như PAM (Pluggable Authentication Modules-Các Mô-đun Xác Thực Cắm Được) để quản lý các chính sách xác thực và truy cập.

[Tìm hiểu về Posix](https://ru.wikipedia.org/wiki/POSIX)

[Tìm hiểu về PAM](https://wiki.archlinux.org/title/PAM)

## 1.11 Thiết lập an toàn cho SSH

Để tăng cường bảo mật truy cập từ xa qua SSH, nên sử dụng khóa SSH thay vì mật khẩu, vô hiệu hóa truy cập root, và áp dụng xác thực hai yếu tố (ví dụ, qua Google Authenticator).

Ví dụ về cấu hình SSH:

```bash
sudo nano /etc/ssh/sshd_config
#Vô hiệu hóa đăng nhập mật khẩu
PasswordAuthentication no
# Vô hiệu hóa quyền truy cập root
PermitRootLogin no
```

## 1.12 Tự động áp dụng cập nhật bảo mật

Trong các hệ thống Debian-based, bạn có thể cấu hình áp dụng tự động các bản cập nhật bảo mật thông qua công cụ unattended-upgrades, điều này đặc biệt hữu ích cho các máy chủ.

Cài đặt và cấu hình:

```bash
udo apt install unattended-upgrades
sudo dpkg-reconfigure unattended-upgrades
```

[Tìm hiểu thêm về unattended-upgrades](https://wiki.debian.org/UnattendedUpgrades)

# 2. Bảo mật cho các hệ thống dựa trên Red hat-based

Các cơ chế bảo mật cơ bản của hệ thống Red Hat tương tự với các hệ thống dựa trên Debian, nhưng có một số khác biệt cụ thể:

## 2.1 Hỗ trợ các tiêu chuẩn và chứng nhận bảo mật cho doanh nghiệp

Red Hat Enterprise Linux (RHEL) được chứng nhận theo các tiêu chuẩn bảo mật quốc tế khác nhau, bao gồm Common Criteria và FIPS (Federal Information Processing Standards). Điều này giúp RHEL phù hợp với các tổ chức chính phủ, tài chính và các ngành khác có yêu cầu bảo mật cao.

[Tìm hiểu thêm về Common Criteria](https://access.redhat.com/articles/1403233)

[Tìm hiểu thêm về FIPS](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards)

Đối với các môi trường yêu cầu tiêu chuẩn mã hóa cao, RHEL có thể được cấu hình theo chế độ FIPS, đảm bảo tuân thủ các tiêu chuẩn mã hóa.

## 2.2 Xác thực và quản lý truy cập

Red Hat hỗ trợ nhiều phương thức xác thực khác nhau, bao gồm Kerberos, LDAP, và SSSD (System Security Services Daemon), cho phép tích hợp với các hệ thống quản lý truy cập tập trung.

[Tìm hiểu thêm về Kerberos](https://www.kerberos.org/software/tutorial.html)

[Tìm hiểu thêm về LDAP](https://ldapwiki.com/wiki/Wiki.jsp?page=LDAP)

[Tìm hiểu thêm về SSSD](https://sssd.io/docs/introduction.html)

PAM (Pluggable Authentication Modules) cũng được sử dụng để cấu hình linh hoạt về xác thực và kiểm soát truy cập, cho phép cài đặt các tính năng như xác thực hai yếu tố (ví dụ: sử dụng Google Authenticator).

## 2.3 Bảo mật container

Trong hệ sinh thái Red Hat, container là thành phần quan trọng của cơ sở hạ tầng, và các biện pháp kiểm soát truy cập nghiêm ngặt được áp dụng để bảo mật container. Red Hat cung cấp Podman như một giải pháp thay thế cho Docker, hoạt động với các image container tương tự nhưng cải thiện tính cô lập do Podman không yêu cầu quá trình demon để chạy.

[Tìm hiểu thêm về podman](https://podman.io/)

Các container cũng hoạt động dưới sự quản lý của SELinux, mang lại một lớp bảo mật bổ sung và ngăn chặn container vượt quá quyền hạn của chúng.

## 2.4 SCAP (Security Content Automation Protocol)

Red Hat cung cấp OpenSCAP, một bộ công cụ cho việc kiểm tra bảo mật và tuân thủ tiêu chuẩn. Công cụ này được sử dụng để kiểm tra hệ thống theo các tiêu chuẩn bảo mật khác nhau, như PCI-DSS hoặc HIPAA, và cung cấp các khuyến nghị để nâng cao bảo mật hệ thống.

OpenSCAP có thể tự động kiểm tra cấu hình hệ thống và cung cấp báo cáo về sự tuân thủ chính sách bảo mật.

[Tìm hiểu thêm về OpenSCAP](https://www.open-scap.org/)

## 2.5 Tích hợp với Red Hat Satellite

Red Hat Satellite là một công cụ quản lý vòng đời hệ thống, cho phép quản lý cập nhật, vá lỗi và cấu hình bảo mật của số lượng lớn hệ thống một cách tập trung. Điều này rất quan trọng đối với các môi trường doanh nghiệp lớn với hàng ngàn node (máy chủ hoặc thiết bị mạng).

# 3. Gentoo-based

Gentoo Linux là một bản phân phối có khả năng cấu hình cao, nổi tiếng với tính linh hoạt và hệ thống quản lý gói mạnh mẽ. Gentoo cho phép người dùng kiểm soát hoàn toàn hệ thống, tạo điều kiện cho việc cấu hình nhằm đảm bảo mức độ bảo mật tối đa. Cũng giống như Arch Linux, bảo mật của Gentoo phụ thuộc vào cách người dùng cấu hình và duy trì hệ thống của mình. Các khía cạnh bảo mật chính của Gentoo Linux bao gồm:

## 3.1 Linh hoạt và cấu hình bảo mật ở cấp độ biên dịch

Điểm khác biệt chính của Gentoo so với các bản phân phối khác là các gói được biên dịch từ mã nguồn bằng hệ thống Portage. Người dùng có thể sử dụng cờ USE để bật hoặc tắt các tính năng khác nhau, giúp tránh cài đặt những tính năng không cần thiết hoặc có khả năng gây lỗ hổng.

Người dùng cũng có thể tùy chỉnh cài đặt của trình biên dịch với CFLAGS và LDFLAGS để thêm các tham số bảo mật bổ sung, như bảo vệ khỏi tràn bộ đệm và bảo vệ bộ nhớ.

Ví dụ về cài đặt cờ bảo mật:

```bash
CFLAGS="-O2 -pipe -fstack-protector-strong"
LDFLAGS="-Wl,-z,relro,-z,now"
```

##  3.2 Hardened Gentoo

Hardened Gentoo là phiên bản Gentoo đặc biệt, tập trung vào các biện pháp bảo mật nâng cao. Nó bao gồm nhiều bản vá và cấu hình để tăng cường bảo mật, như PaX, grsecurity (trước khi ngừng hỗ trợ công khai), và hỗ trợ PIE (Position Independent Executables), làm cho nó trở thành một lựa chọn tuyệt vời cho các hệ thống yêu cầu bảo mật cao.

Bật profile hardened sẽ tự động cấu hình hệ thống để tăng cường bảo mật, bao gồm hỗ trợ bảo vệ bộ nhớ và các biện pháp quan trọng khác.

## 3.3 Kiểm tra tính toàn vẹn của gói

Tất cả các gói trong Gentoo đều được kiểm tra tính toàn vẹn bằng chữ ký GPG, bảo vệ người dùng khỏi việc cài đặt các gói giả mạo hoặc bị thay đổi. Hệ thống Portage sử dụng các chữ ký để xác minh rằng các gói không bị thay đổi.

Người dùng có thể cấu hình kiểm tra tính toàn vẹn bổ sung cho các gói và sử dụng `eix` để kiểm tra tính bảo mật của các gói đã cài đặt.

## 3.4 Cập nhật và bản vá bảo mật

Gentoo không có chu kỳ phát hành phiên bản cố định và sử dụng mô hình rolling release. Điều này có nghĩa là các bản cập nhật bảo mật có thể được nhận ngay khi chúng được phát hành.

Người dùng có thể cấu hình hệ thống để tự động kiểm tra cập nhật và chỉ cài đặt các bản vá bảo mật quan trọng.

Các lệnh cập nhật hệ thống:

```bash
emerge --sync
emerge -avuDN @world
```




