#include <stdio.h>

int main()
{
	char c[1001];
	int n;
	
	scanf("%s", c);
	scanf("%d", &n);
	
	printf("%c", c[n-1]);
	
	return 0;
}