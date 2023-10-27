#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#define BUFSIZE         BUFSIZE_32K
#define BUFSIZE_32K     32768
#define STR(x)          STR_(x)
#define STR_(x)         #x
/**
 * Convert hex string from stdin to binary stdout
 * Written by davidhcefx, 2023.4.6
 */

uint8_t octet_to_uint(const char* hex) {
    char octet[3] = {0};
    octet[0] = hex[0];
    octet[1] = hex[1];
    return (uint8_t)strtoul(octet, NULL, 16);
}

int main() {
    char input[BUFSIZE + 1];
    uint8_t output[BUFSIZE / 2] = {0};
    uint32_t i;

    fprintf(stderr, "Hex string input:\n");
    if (scanf("%" STR(BUFSIZE) "s", input) <= 0) {
        perror("Error: scanf failed");
        return -1;
    }
    for (i = 0; i < strlen(input); i += 2) {
        output[i / 2] = octet_to_uint(&input[i]);
    }
    write(1, output, strlen(input) / 2);

    return 0;
}
