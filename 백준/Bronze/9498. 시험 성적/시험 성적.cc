#include <stdio.h>
int main()
{
	int t;
	scanf("%d",&t);
	if(t>89)
	{
		printf("A");
	}
	else if(t>79)
	{
		printf("B");
	}
	else if(t>69)
	{
		printf("C");
	}
	else if(t>59)
	{
		printf("D");
	}
	else
	{
		printf("F");
	}
}