#include<stdio.h>
int main()
{
	int i,n,k;
	scanf("%d",&n);
	i=1;
	k=0;
	while(i<=n)
	{
		k=k+i;
		i++;
	};
	printf("%d",k);
}