#include "stdio.h"
#include "string.h"
#include "libdemo.h"

int main() {
    char *h = "{\"code\": 1, \"msg\": \"success\", \"data\": \"success\"}";
    char *result;
    result = parseJSON(h);
    printf("%s", result);
    return 0;
}