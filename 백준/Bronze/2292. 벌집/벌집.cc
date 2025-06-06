#include <stdio.h>

main()
{
	int n;
	int cnt = 2;
	int dept = 1;
	
	scanf("%d", &n);
	
	while(n>dept)
	{
		if(n==1)
		{
			cnt = 1;
			break;
		}
		else
		{
			dept = dept + 6*(cnt-1);
			cnt++;
		}
	}
	printf("%d", cnt-1);
}