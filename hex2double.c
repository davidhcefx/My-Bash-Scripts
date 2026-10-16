/**
 * SPDX-AI-Disclosure: ai-assisted
 */
#include <stdio.h>
#include <string.h>
#include <math.h>
// Convert hex string to double and vice versa. Written by davidhcefx, 2026.10.16

double hexstr_to_double(const char *hexstring)
{
    unsigned long long int ull;
    if (sscanf(hexstring, "%llx", &ull) != 1) {
        return NAN;
    }
    double value_d;
    memcpy(&value_d, &ull, sizeof(double));
    return value_d;
}

const char *double_to_hexstr(const char *double_s)
{
    static char hexstring[32];
    double value_d;
    if (sscanf(double_s, "%lf", &value_d) != 1) {
        return "";
    }
    unsigned long long int ull;
    memcpy(&ull, &value_d, sizeof(double));
    snprintf(hexstring, sizeof(hexstring), "%llx", ull);
    return hexstring;
}

int main(int argc, char *argv[])
{
    if (argc < 2) {
        fprintf(stderr, "Usage: %s {<hexstring> | <double>}\n", argv[0]);
        return 1;
    }
    double value_d = hexstr_to_double(argv[1]);
    const char *hexstring = double_to_hexstr(argv[1]);

    printf("Hex str -> Double: %.16lf\n", value_d);
    printf("Double -> Hex str: %s\n", hexstring);

    return 0;
}
