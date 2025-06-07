#include <stdio.h>

int main()
{
    int X, N;
    int i;
    int a, b;
    int result = 0;
    
    scanf("%d", &X);	
    scanf("%d", &N);
    
    for(i=0; i<N; i++)
    {
    	scanf("%d %d", &a, &b);
    	result = result + a * b;
	}
	
	if(X == result)
		printf("Yes");
		
	else
		printf("No");
}