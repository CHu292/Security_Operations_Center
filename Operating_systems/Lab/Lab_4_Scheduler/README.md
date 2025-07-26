# LAB 4 - Scheduler (Bộ lập lịch)

**Nhiệm vụ:**
Thực hiện kiểm thử và tìm ra **bộ lập lịch I/O (nhập/xuất) tốt nhất** trong số các lựa chọn.

---

### Lựa chọn nâng cao:

**Chỉnh sửa bộ lập lịch hiện có ở cấp độ nhân hệ điều hành**

---

**Lập lịch I/O**
[https://habr.com/ru/post/81504/](https://habr.com/ru/post/81504/)

```bash
DISC="sda"; \
cat /sys/block/$DISC/queue/scheduler; \
for T in kyber bfq none; do \
    echo $T > /sys/block/$DISC/queue/scheduler; \
    cat /sys/block/$DISC/queue/scheduler; \
    sync && /sbin/hdparm -tT /dev/$DISC && echo "---"; \
    sleep 15; \
done
```

Liên kết bài viết liên quan:
[https://xakep.ru/2014/05/11/input-out-linux-planning/](https://xakep.ru/2014/05/11/input-out-linux-planning/)

---

### Tài liệu tham khảo thêm:

* [https://habr.com/ru/company/selectel/blog/346844/](https://habr.com/ru/company/selectel/blog/346844/)
* [https://habrahabr.ru/post/337102/](https://habrahabr.ru/post/337102/)
* [https://www.opennet.ru/base/sys/linux\_shedulers.txt.html](https://www.opennet.ru/base/sys/linux_shedulers.txt.html)
* [https://books.gigatux.nl/mirror/kerneldevelopment/0672327201/ch13lev1sec5.html](https://books.gigatux.nl/mirror/kerneldevelopment/0672327201/ch13lev1sec5.html)
* [https://www.kernel.org/doc/Documentation/block/cfq-iosched.txt](https://www.kernel.org/doc/Documentation/block/cfq-iosched.txt)
* [https://web.archive.org/web/20080606005055/http://www.dcs.ed.ac.uk/home/stg/pub/D/disk.htm](https://web.archive.org/web/20080606005055/http://www.dcs.ed.ac.uk/home/stg/pub/D/disk.htm)
* [https://www.kernel.org/doc/html/latest/block/bfq-iosched.html](https://www.kernel.org/doc/html/latest/block/bfq-iosched.html)

---
