#include <stdio.h>
#include <string.h>

int main()
{
	int n, i, j, point, count;
	char k[80];
    
	scanf("%d", &n);
	for(i=0; i<n; i++)
	{
		scanf("%s", k);
        point = 0;
        count = 1;
		for(j=0; j<strlen(k); j++)
		{
			if(k[j]=='O')
			{
				point += count;
				count++;
			}
			else
				count = 1;
		}
		printf("%d\n", point);
	}
}