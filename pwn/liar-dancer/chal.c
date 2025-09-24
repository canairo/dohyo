// gcc chal.c -no-pie -o chal
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_DANCES 16
#define DANCE_SIZE 256

char *dances[MAX_DANCES];

void win() {
    printf("PEARTO IS PLEASED\n");
    system("cat flag.txt");
    exit(0);
}

void create_dance() {
    int index;
    printf("WHERE IS TETO DANCING? (0 to %d) > ", MAX_DANCES - 1);
    scanf("%d", &index);
    getchar(); // Consume the newline character

    if (index < 0 || index >= MAX_DANCES) {
        printf("WE CAN'T DANCE HERE.\n");
        return;
    }

    dances[index] = (char *)malloc(DANCE_SIZE * sizeof(char));

    printf("DESCRIBE TETO'S DANCE (max %d characters) > ", DANCE_SIZE - 1);
    fgets(dances[index], DANCE_SIZE, stdin);
    dances[index][strcspn(dances[index], "\n")] = 0;

    printf("TETO IS NOW DANCING AT POSITION %d AT %p.\n", index, dances[index]);
}

void delete_dance() {
    int index;
    printf("WHICH DANCE MUST GO? (0 to %d) > ", MAX_DANCES - 1);
    scanf("%d", &index);

    if (index < 0 || index >= MAX_DANCES || dances[index] == NULL) {
        printf("THERE IS NO DANCE HERE.\n");
        return;
    }

    free(dances[index]);
    printf("NOW THE DANCE AT %d IS GONE.\n", index);
}

void edit_dance() {
    int index;
    printf("ENTER THE DANCE YOU WOULD LIKE MODIFIED > ", MAX_DANCES - 1);
    scanf("%d", &index);
    getchar(); // Consume the newline character

    if (index < 0 || index >= MAX_DANCES || dances[index] == NULL) {
        printf("THERE IS NO DANCE HERE.\n");
        return;
    }

    printf("DESCRIBE YOUR NEW DANCE. (max %d characters) > ", DANCE_SIZE - 1);
    fgets(dances[index], DANCE_SIZE, stdin);
    dances[index][strcspn(dances[index], "\n")] = 0; // Remove newline character

    printf("TETO IS NOW DANCING A NEW DANCE AT %d.\n", index);
}

int main() {
    int choice;
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    while (1) {
        printf("-------\nLIAR DANCER\n-------\n");
        printf("1. CREATE DANCE\n");
        printf("2. DELETE DANCE\n");
        printf("3. EDIT DANCE\n");
        printf("4. QUIT\n\n");
        printf("TETOTETOTETO > ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                create_dance();
                break;
            case 2:
                delete_dance();
                break;
            case 3:
                edit_dance();
                break;
            case 4:
                return 0;
            default:
                printf("LIAR!!!\n");
                exit(0);
        }
    }

    return 0;
}
