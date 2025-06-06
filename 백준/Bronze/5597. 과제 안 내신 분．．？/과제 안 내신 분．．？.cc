#include <stdio.h>

main()
{
	int s[31] = {0};
	int a;
	int i;
	
	for(i=0; i<28; i++)
	{
		scanf("%d", &a);
		s[a] = 1;
	}
	
	for(i=1; i<=30; i++)
	{
		if(s[i] == 0)
			printf("%d\n", i);
	}
}