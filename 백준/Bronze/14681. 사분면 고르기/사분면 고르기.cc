#include <stdio.h>

main()
{
	int a, b;
	int result;
	
	scanf("%d %d", &a, &b);
	
	if(a>0 and b>0)
		result = 1;
		
	else if (a<0 and b>0)
		result = 2;
		
	else if (a<0 and b<0)
		result = 3;
		
	else if (a>0 and b<0)
		result = 4;
		
	printf("%d", result);
}