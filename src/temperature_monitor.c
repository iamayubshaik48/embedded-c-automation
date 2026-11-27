#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <math.h>
int main(int argc, char *argv[])
{
    if (argc != 2) {
        fprintf(stderr, "ERROR: Provide temperature value\n");
        return 2;
    }
    errno = 0;
    char *end;
    float temperature = strtof(argv[1], &end);
    if (end == argv[1] || *end != '\0' ||
        errno == ERANGE || !isfinite(temperature) ||
        temperature < -50 || temperature > 100) {
        fprintf(stderr, "ERROR: Invalid temperature\n");
        return 2;
    }
    printf("Temperature: %.2f C\n", temperature);
    if (temperature > 45) {
        printf("STATUS: CRITICAL\n");
    }
    else if (temperature > 35) {
        printf("STATUS: WARNING\n");
    }
    else {
        printf("STATUS: NORMAL\n");
    }
    return 0;
}