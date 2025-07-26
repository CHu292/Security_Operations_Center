#include <stdlib.h>
#include <sys/mman.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>

int main(){
    unsigned int size = 50*1024*1024;
    long page_size = sysconf(_SC_PAGESIZE);
    int count = 0;

    while(1){
        unsigned char *p = mmap(NULL, size, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
        if (p == MAP_FAILED) {
            perror("mmap failed");
            break;
        }

        for(int i = 0; i < size; i += page_size)
            p[i] = 0;

        count++;
        if (count % 10 == 0)  // log sau mỗi 10 lần
            system("free -m >> membomb.txt");

        // usleep(50000); // không bắt buộc
    }

    return 0;
}

