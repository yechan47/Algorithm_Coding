#include <stdio.h>

main()
{
	int n;
	int sq[1001] = {0, };
	sq[1] = 1;
	sq[2] = 2;
	for(int i=3; i<1001; i++)
	{
		sq[i] = (sq[i-2] + sq[i-1])%10007;
	}
	scanf("%d", &n);
	printf("%d", sq[n]);
}