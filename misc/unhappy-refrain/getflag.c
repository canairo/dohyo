#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *f = fopen("/flag.txt", "r");
    if (!f) {
        perror("fopen");
        return 1;
    }

    char buf[256];
    if (fgets(buf, sizeof(buf), f)) {
        puts(buf);
    }

    fclose(f);
    return 0;
}
