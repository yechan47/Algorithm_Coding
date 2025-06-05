#include <stdio.h>

main()
{
	int a;
	int count = 2;
	int i = 1;
	int sum = 0;
	int b;
	
	scanf("%d", &a);
	
	while(1)
	{
		sum += i;
		
		if(sum >= a)
			break;
			
		else
		{
			count++;
			i++;
		}
	}
	
	b = sum - a;
	
	if(count % 2 == 0)
		printf("%d/%d", 1 + b, count - 1 - b);
		
	else
		printf("%d/%d", count - 1 - b, 1 + b);
}