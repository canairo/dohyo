#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <string.h>
#include <time.h>

int main() {
    setuid(0);
    srand(time(NULL));
    char flag[256];
    memset(flag, 0, sizeof(flag));
    char hexbytes[256];

    for (int i = 0; i < 32; i++) {
    	sprintf(hexbytes + i, "%x", rand() % 16);
    }
 
    strcat(flag, "DOHYO{");
    strcat(flag, hexbytes);
    strcat(flag, "}");

    printf("%s", flag);
    return 0;
}
