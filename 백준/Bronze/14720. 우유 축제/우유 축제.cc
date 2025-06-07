#include <stdio.h>

main()
{
	int n;
	scanf("%d", &n);
	
	int milk[n];
	for(int i=0; i<n; i++)
	{
		scanf("%d", &milk[i]);
	} 
	
	int count = 0;
	int nextmilk = 0;
	
	for(int i=0; i<n; i++)
	{
		if(milk[i] == nextmilk)
		{
			count++;
			nextmilk = (nextmilk + 1) % 3;
		}
	}
	
	printf("%d", count);
}