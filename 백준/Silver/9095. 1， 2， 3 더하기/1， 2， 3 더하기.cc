#include <stdio.h>

int dp(int k)
{
	if(k==1)
		return 1;
	else if(k==2)
		return 2;
	else if(k==3)
		return 4;
	else
		return dp(k-1) + dp(k-2) + dp(k-3);
}
main()
{
	int n;
	scanf("%d", &n);
	int t;
	
	for(int i=0; i<n; i++)
	{
		scanf("%d", &t);
		printf("%d\n", dp(t));
	}
}