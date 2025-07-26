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

* [Bộ lập lịch cũ](https://www.informit.com/articles/article.aspx?p=101760&seqNum=2)

* [Bộ lập lịch mới- Inside the Linux 2.6 Completely Fair Scheduler](../Lab_2_Membomb/Documents/Inside_the_Linux_2_6_Completely_Fair_Scheduler.md)

* [Process Scheduling](../Lab_2_Membomb/Documents/Process_Scheduling.md)

* [CFS Scheduling](./Documents/CFS_Scheduler.md)

* [EEVDF Scheduler](./Documents/EEVDF_Scheduler.md)

* [Debugging and fine-tuning the linux process scheduler](https://serverfault.com/questions/948401/debugging-and-fine-tuning-the-linux-process-scheduler)

* [perf Examples](https://www.brendangregg.com/perf.html#SchedulerAnalysis)

* [Tuning the Task Scheduler](./Documents/Tuning_the_Task_Scheduler.md)

* [sched(7) — Linux manual page](https://man7.org/linux/man-pages/man7/sched.7.html)

---

### [Control Group Version 1](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v1/index.html#cgroup-v1)

1. [Control Groups](./Documents/Control_Groups.md)

2. [Block IO Controller]()

3. [CPU Accounting Controller]()

4. [CPUSETS](./Documents/CPUSETS.md)

5. [Device Whitelist Controller]()

6. [HugeTLB Controller]()

7. [Memory Resource Controller(Memcg) Implementation Memo]()

8. [Memory Resource Controller]()

9. [Misc controller]()

10. [Network classifier cgroup]()

11. [Network priority cgroup]()

12. [Process Number Controller]()

13. [RDMA Controller]()

---

### [Control Group Version 2](./Documents/Control_Group_V2.md)
