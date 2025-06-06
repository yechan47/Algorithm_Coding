#include <stdio.h>
int main()
{
	int n, x, y, i;
	scanf("%d", &n);
	for(i = 0; i < n; i++)
	{
		scanf("%d %d", &x, &y);
		printf("Case %d: %d\n", i + 1, x + y);
	}
}