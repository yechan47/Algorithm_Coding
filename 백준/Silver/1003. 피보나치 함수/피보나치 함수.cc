#include<stdio.h>
 
int fib[41][2];
 
int main() {
    int T, n;
    int t, i;
    fib[0][0] = 1;
    fib[0][1] = 0;
    fib[1][0] = 0;
    fib[1][1] = 1;
 
    scanf("%d", &T);
    for (t = 0; t < T; t++) {
        scanf("%d", &n);
        for (i = 2; i <= n; i++) {
            fib[i][0] = fib[i - 1][0] + fib[i - 2][0];
            fib[i][1] = fib[i - 1][1] + fib[i - 2][1];
        }
        printf("%d %d\n", fib[n][0], fib[n][1]);
    }
	return 0;
}