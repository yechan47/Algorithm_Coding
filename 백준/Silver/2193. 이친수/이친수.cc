#include <stdio.h>

main()
{
	int n;
	long long sq[91] = {0, };
	sq[1] = 1;
	sq[2] = 1;
	for(int i=3; i<91; i++)
	{
		sq[i] = sq[i-2] + sq[i-1];
	}
	scanf("%d", &n);
	printf("%lld", sq[n]);
}