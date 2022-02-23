#include "stdio.h"
#include "string.h"
#include "libdemo.h"

int main() {
    GoSlice hello;
    unsigned char h[] = "{\"code\": 1, \"msg\": \"success\", \"data\": \"success\"";
    hello.data = &h;
    hello.len = sizeof(h);

    GoString result;
    result = parseJSON(hello);
    printf("%s", result.p);
    return 0;
}