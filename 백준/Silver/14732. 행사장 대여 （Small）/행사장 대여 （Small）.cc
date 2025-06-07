#include <stdio.h>

int n, i, j, a, b, c, d, ans;
bool chk[501][501];

int main() 
{
	for (scanf("%d", &n); n--;) 
    {
		scanf("%d %d %d %d", &a, &b, &c, &d);
		for (i = a; i < c; i++) for (j = b; j < d; j++)
			if (!chk[i][j]) ans++, chk[i][j] = 1;
	}
	printf("%d", ans);
	return 0;
}