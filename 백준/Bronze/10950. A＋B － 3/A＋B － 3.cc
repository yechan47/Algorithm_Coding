#include <stdio.h>
int main()
{	
	int N, i, x, y;
	
	scanf("%d", &N);
	
	for(i = 0; i < N; i++){
		
		scanf("%d %d", &x, &y);
		printf("%d\n", x + y);
	}
}