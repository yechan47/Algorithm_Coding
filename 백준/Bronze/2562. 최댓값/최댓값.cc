#include <stdio.h>

int main()
{
	int a;
	int max = 0;
	int r;
	
	for(int i=0; i<9; i++)
	{
		scanf("%d\n", &a);
		if(a > max)
		{
			max = a;
			r = i+1;
		}
	}
	
	printf("%d\n%d", max, r);
	return 0;
}