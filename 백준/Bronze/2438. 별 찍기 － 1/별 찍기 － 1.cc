#include<stdio.h>
main()
{
	int n,i,p;
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(p=1;p<=i;p++)
		{
			printf("*");
		}
		printf("\n");
	}
	
}