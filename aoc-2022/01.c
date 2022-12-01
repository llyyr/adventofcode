#include <stdio.h>
#include <stdlib.h>

int compr(const void *a, const void *b) {
    return *(int *)b > *(int *)a ? 1 : -1;
}

int main()
{
    FILE *fp = fopen("01.txt", "r");
    int block_sum[4096];
    int block_count = 0;

    int current_block_sum = 0;
    char line[4096];

    while (fgets(line, sizeof(line), fp)) {
        if (line[0] != '\n') {
            current_block_sum += atoi(line);
        } else {
            block_sum[block_count++] = current_block_sum;
            current_block_sum = 0;
        }
    }

    qsort(block_sum, block_count, sizeof(block_sum[0]), compr);

    printf("%d\n", block_sum[0]);
    printf("%d\n", block_sum[0] + block_sum[1] + block_sum[2]);
}
