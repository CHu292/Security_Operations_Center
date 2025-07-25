# **Lab 2**

## **Membomb**

1. Viết một chương trình cấp phát bộ nhớ và điền nó bằng số 0
   với bước nhảy bằng kích thước của một trang bộ nhớ (sử dụng `mmap`, `VirtualAlloc`)
2. Vẽ biểu đồ bộ nhớ trống
3. Tìm hiểu cách hoạt động của daemon OOM Killer trong Linux
4. Nhận được thông báo không thể cấp phát thêm bộ nhớ trong Windows

```bash
swapon -a
```

---

## **Tài liệu tham khảo**

* [https://www.informit.com/articles/article.aspx?p=101760\&seqNum=2](https://www.informit.com/articles/article.aspx?p=101760&seqNum=2) - Bộ lập lịch cũ
* [Bộ lập lịch mới- Inside the Linux 2.6 Completely Fair Scheduler](../Lab_2_Membomb/Documents/Inside_the_Linux_2_6_Completely_Fair_Scheduler.md)
* [https://csc.sibsutis.ru/sites/csc.sibsutis.ru/files/courses/os/Lecture\_06.pdf](https://csc.sibsutis.ru/sites/csc.sibsutis.ru/files/courses/os/Lecture_06.pdf)

---

## **Thông tin thêm về bộ lập lịch và phân tích hiệu năng**

* [https://www.ibm.com/developerworks/ru/library/l-scheduler/index.html](https://www.ibm.com/developerworks/ru/library/l-scheduler/index.html)
* [https://www.tux.in.ua/articles/527](https://www.tux.in.ua/articles/527)
* [https://www.kernel.org/doc/html/latest/scheduler/sched-design-CFS.html](https://www.kernel.org/doc/html/latest/scheduler/sched-design-CFS.html)
* [https://serverfault.com/questions/948401/debugging-and-fine-tuning-the-linux-process-scheduler](https://serverfault.com/questions/948401/debugging-and-fine-tuning-the-linux-process-scheduler)
* [https://developer.ibm.com/tutorials/l-completely-fair-scheduler/](https://developer.ibm.com/tutorials/l-completely-fair-scheduler/)
* [https://www.brendangregg.com/perf.html#SchedulerAnalysis](https://www.brendangregg.com/perf.html#SchedulerAnalysis)
* [https://doc.opensuse.org/documentation/leap/archive/42.1/html/book.slx.tuning/cha.tuning.taskscheduler.html](https://doc.opensuse.org/documentation/leap/archive/42.1/html/book.slx.tuning/cha.tuning.taskscheduler.html)
* [https://man7.org/linux/man-pages/man7/sched.7.html](https://man7.org/linux/man-pages/man7/sched.7.html)

---
