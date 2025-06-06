#include <stdio.h>
#include <math.h>

main()
{
	int a, b, v;
	int day = 0;
	
	scanf("%d %d %d", &a, &b, &v);
	day = (int)ceil((double)(v-b)/(a-b));
	
	printf("%d", day);
}