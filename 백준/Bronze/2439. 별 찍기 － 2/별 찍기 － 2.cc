#include<stdio.h>
main()
{
	int n,i,p,k;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(k=1;k<=n-i;k++)
		{
			printf(" ");
		}
		for(p=1;p<=i;p++)
		{
			printf("*");
		}
		printf("\n");
	}
	
}