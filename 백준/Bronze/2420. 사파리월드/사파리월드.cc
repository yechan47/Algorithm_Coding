#include <stdio.h>
#include <stdlib.h>

main() 
{
    long long n, m;
    scanf("%lld %lld", &n, &m);
    printf("%lld", llabs(n - m));
}