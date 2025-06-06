#include<stdio.h>
main()
{
	int n,i,p;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(p=1;p<=n-i+1;p++)
		{
			printf("*");
		}
		printf("\n");
	}
	
}