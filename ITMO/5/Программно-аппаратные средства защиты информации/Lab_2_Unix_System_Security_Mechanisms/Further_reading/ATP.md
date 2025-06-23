# Hướng dẫn sử dụng lệnh apt trên Linux


## 1. Giới thiệu
APT sử dụng trên các hệ điều hành phân phối dựa trên Debian hoặc Debian-based như Ubuntu hoặc Linux Mint

**APT**, là từ viết tắt củaAdvanced Package Tool là một công cụ quản lý gói dành cho hệ thống Debian. Công cụ APT giúp người dùng thực hiện nhiều tác vụ khác nhau bao gồm cài đặt, cập nhật, nâng cấp và gỡ bỏ các gói phần mềm trên hệ điều hành.

Khi sử dụng công cụ APT, đôi khi sẽ yêu cầu người dùng nhập ‘Y‘(viết tắt của Yes) để tiến hành thao tác như cài đặt hoặc gỡ bỏ một gói.

Trên các bản phân phối dựa trên Debian/Ubuntu cũ hơn, apt-get đã được sử dụng. Trong các phiên bản mới hơn như Ubuntu 18.04/20.04 trở lên và Debian 10/Mint 20 lệnh apt sẽ thay thế cho lệnh apt-get cũ kỹ trên các phiên bản trước đó và nó hoàn toàn tương thích ngược với apt-get.

## 2. Cách sử dụng

### 2.1 Cập nhật chỉ mục cho APT

Trong hệ thống sử dụng Debian/Ubuntu, kho lưu trữ được chỉ định trong tệp tin `/etc/apt/sources.list`. Chỉ mục gói APT là cơ sở dữ liệu của tất cả các gói được xác định trong tệp này. Bạn nên cập nhật chỉ mục gói APT trên hệ thống để đồng bộ hóa các thay đổi được thực hiện trong kho lưu trữ. Điều này đặc biệt quan trọng sau khi cài đặt hệ thống mới và trước khi cài đặt các gói tin mới.

Để cập nhật cơ sở dữ liệu APT các bạn hãy chạy lệnh sau:

```bash
sudo apt update -y
```
### 2.2 Nâng cấp gói bằng lệnh APT

Lệnh `apt update -y` được đề cập ở trên sẽ không cài đặt hoặc nâng cấp bất kỳ gói nào. Vì vậy, sau khi chạy lệnh trên, bạn sẽ biết được các gói nào cần cập nhật.

Nếu bạn muốn cập nhật toàn bộ các gói đã cài đặt lên phiên bản mới nhất thì các bạn cần chạy lệnh sau:

```bash
sudo apt upgrade
```

Để nâng cấp một gói riêng lẻ, hãy sử dụng lệnh sau, trong đó `package-name` chính là tên gói bạn cần nâng cấp:

```bash
sudo apt upgrade package-name
```

### 2.3 Nâng cấp đầy đủ và nâng cấp phiên bản

Trường hợp bản muốn có một nâng cấp đầy đủ và loại bỏ một số gói không còn cần cần thiết để hoàn toàn nâng cấp hệ thống thì các bạn sử dụng lệnh sau:

```bash
sudo apt full-upgrade
```

Ngoài lệnh trên thì chúng ta vẫn có lệnh sau để nâng cấp toàn bộ các gói ít quan trọng hơn:

```bash
sudo apt dist-upgrade
```

**Cách nâng cấp phiên bản của hệ điều hành**

 Ví dụ từ phiên bản Ubuntu 19.04 lên Ubuntu 20.04.

 Tuy nhiên để an toàn, trước khi chạy lệnh này, bạn phải đảm bảo chạy hai lệnh trên trước nhé:

 ```bash
do-release-upgrade
```

Như vậy quy trình sẽ là `sudo apt upgrade` sau đó `sudo apt dist-upgrade` và cuối cùng chạy `sudo apt do-release-upgrade`.


### 2.4 Cài đặt một gói phần mềm

Để cài đặt một gói trên hệ thống của bạn, hãy sử dụng lệnh apt như sau:

```bash
sudo apt install package-name
```

Ví dụ ở đây mình sẽ cài gói nload thì mình sử sử dụng lệnh sudo apt install nload.

```bash
$ sudo apt install nload
```

Ngoài ra, bạn có thể cài đặt nhiều gói trên một lệnh bằng cách điền tên các gói giữa khoảng trắng như lệnh sau:

```bash
sudo apt install package-name1 package-name2 package-name3
```
Nếu chúng ta cài đặt một gói đã cài đặt thì nó sẽ được nâng cấp lên phiên bản mới nhất nếu có

### 2.5 Liệt kê các gói đã cài đặt

Để xem tất cả các gói đã cài đặt trên hệ thống của bạn, hãy chạy lệnh sau:

```bash
sudo apt list --installed
```

Để tìm kiếm một gói cụ thể, các bạn hãy thêm grep phía sau như lệnh sau:

```bash
sudo apt list --installed | grep package-name
```

Ví dụ sau mình cần tìm tập hợp các gói có từ khóa ssh.

```bash
$ sudo apt list --installed | grep ssh

WARNING: apt does not have a stable CLI interface. Use with caution in scripts.

libssh-4/jammy-updates,jammy-security,now 0.9.6-2ubuntu0.22.04.3 amd64 [installed,automatic]
libssh-4/jammy-updates,jammy-security,now 0.9.6-2ubuntu0.22.04.3 i386 [installed,automatic]
libssh-gcrypt-4/jammy-updates,jammy-security,now 0.9.6-2ubuntu0.22.04.3 amd64 [installed,automatic]
libssh2-1/jammy,now 1.10.0-3 amd64 [installed,automatic]
openssh-client/jammy-updates,jammy-security,now 1:8.9p1-3ubuntu0.10 amd64 [installed,automatic]
```

### 2.6 Tìm kiếm một gói bằng APT

```bash
sudo apt search package-name
```

Lệnh này sẽ cho phép bạn tìm kiếm và kiểm tra sự sẵn có của một gói trong kho Ubuntu/Debian. Trong ví dụ dưới đây, mình đang tìm kiếm tính khả dụng của gói `net-tools` trong kho lưu trữ Ubuntu:

```bash
sudo apt search net-tools
Sorting... Done
Full Text Search... Done
atm-tools/jammy 1:2.5.1-4build2 amd64
  Base programs for ATM in Linux, the net-tools for ATM

ddnet-tools/jammy 15.9.1-1 amd64
  Tools for DDNet

hobbit-plugins/jammy,jammy 20201127 all
  plugins for the Xymon network monitor

iproute2/jammy,now 5.15.0-1ubuntu2 amd64 [installed]
  networking and traffic control tools

net-tools/jammy,now 1.60+git20181103.0eebece-1ubuntu5 amd64 [installed]
  NET-3 networking toolkit
```

### 2.7 Hiển thị thông tin về một gói bằng lệnh APT

Trước khi cài đặt hoặc gỡ bỏ một gói, bạn có thể tìm kiếm thông tin bổ sung về một gói bằng lệnh `apt show`. Ví dụ: để hiển thị thêm thông tin về gói nload thì chúng ta sử dụng lệnh sau:

```bash
chu@chu-Latitude-5510:~$ sudo apt show nload
[sudo] password for chu: 
Package: nload
Version: 0.7.4-2build3
Priority: extra
Section: universe/net
Origin: Ubuntu
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Original-Maintainer: Marcio de Souza Oliveira <m.desouza20@gmail.com>
Bugs: https://bugs.launchpad.net/ubuntu/+filebug
Installed-Size: 173 kB
Depends: libc6 (>= 2.14), libgcc-s1 (>= 3.0), libncurses6 (>= 6), libstdc++6 (>= 5.2), libtinfo6 (>= 6)
Homepage: http://www.roland-riegel.de/nload/
Download-Size: 55,1 kB
APT-Manual-Installed: yes
APT-Sources: http://ru.archive.ubuntu.com/ubuntu jammy/universe amd64 Packages
Description: realtime console network usage monitor
 Nload is a console application which monitors network traffic and bandwidth
 usage in real time. It displays the total amount of data that has been
 transferred over a network device since the last reboot, the current bandwidth
 usage, and the minimum, maximum, and average bandwidth usage measured
 since it started.
 .
 If the user wants, it is also able to display two bars, similar to progress
 bars, presenting the current load graphically. Support for displaying several
 devices simultaneously is included.
```

Thông tin đầu ra sẽ bao gồm thông tin chi tiết như tên gói, phiên bản, nhà phát hành, kích thước cài đặt, …vv…

### 2.8 Loại bỏ các gói không sử dụng sau khi cài đặt

Đôi khi chúng ta cài đặt một gói, các thư viện và các gói cần phụ thuộc khác cũng sẽ được yêu cầu cài đặt. Tuy nhiên sau khi cài đặt, các thư viện và phụ thuộc này không cần thiết nữa và nó chiếm một phần dung lượng của các bạn.

Và để loại bỏ các tệp và các gói phụ thuộc này nhằm giải phóng một số dung lượng đĩa, các bạn hãy thực hiện lệnh APT sau:

```bash
sudo apt autoremove
```

### 2.9 Loại bỏ các gói đã cài đặt

Bạn có thể gỡ một gói đã được cài đặt bằng cách sử dụng lệnh APT sau:

```bash
sudo apt remove package-name
```

Ngoài ra, bạn cũng có thể gỡ nhiều gói đồng thời với lệnh sau:

```bash
sudo apt remove package-name1 package-name2 package-name3
```

Việc loại bỏ một gói bằng lệnh ```apt remove``` sẽ để lại các tệp cấu hình của gói đó, nhằm việc sau này bạn cài đặt lại gói đó thì mọi cấu hình sẽ được giữ nguyên như trước đây. Để xóa hoàn toàn gói cùng với các tệp cấu hình của nó, các bạn hãy sử dụng ```purge``` ở vị trí ```remove``` như lệnh sau là được:

```bash
sudo apt purge package-name
```





[Bài viết tham khảo tại đây](https://azdigi.com/blog/linux-server/linux-can-ban/lenh-apt-tren-linux-ubuntu-debian/)
