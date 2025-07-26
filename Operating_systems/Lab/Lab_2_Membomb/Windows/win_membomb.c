#include <windows.h>
#include <stdio.h>

int main() {
    SYSTEM_INFO sysInfo;
    GetSystemInfo(&sysInfo);
    SIZE_T page_size = sysInfo.dwPageSize;
    SIZE_T block_size = page_size * 1000;  // mỗi block khoảng 4MB

    FILE* f = fopen("win_membomb.txt", "w");
    if (!f) {
        printf("Cannot open file\n");
        return 1;
    }

    fprintf(f, "Time\tAvailable_MB\n");

    int count = 0;
    while (1) {
        char* addr = (char*)VirtualAlloc(NULL, block_size, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
        if (addr == NULL) {
            printf("Allocation failed at block %d\n", count);
            break;
        }

        for (SIZE_T i = 0; i < block_size; i += page_size)
            addr[i] = 0;

        // Ghi bộ nhớ khả dụng hiện tại
        MEMORYSTATUSEX memInfo;
        memInfo.dwLength = sizeof(memInfo);
        GlobalMemoryStatusEx(&memInfo);
        DWORDLONG avail_phys = memInfo.ullAvailPhys;
        fprintf(f, "%d\t%lld\n", count, avail_phys / (1024 * 1024));  // đơn vị MB

        printf("Block %d, Available: %lld MB\n", count, avail_phys / (1024 * 1024));
        Sleep(200);  // delay để quan sát
        count++;
    }

    fclose(f);
    printf("Done. Press Enter to exit.\n");
    getchar();
    return 0;
}
