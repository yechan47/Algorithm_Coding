#include <stdio.h>

typedef unsigned long long ull;
int mod;

int sol(int a, int b)
{
    if (b == 0) return 1;
    else if (b == 1) return a;
    else {
        ull ret = sol(a, b/2);
        if (b & 1) return (a * ((ret * ret) % mod)) % mod;
        else return (ret * ret) % mod;
    }
}

main()
{
    int a, b;
    scanf("%d %d %d", &a, &b, &mod);
    printf("%d", sol(a % mod, b));
}