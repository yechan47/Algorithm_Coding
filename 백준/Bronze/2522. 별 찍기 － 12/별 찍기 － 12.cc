#include <stdio.h>

int main()
{	
	int n, i, j, k;
	
	scanf("%d", &n);
	
	for(i = 1; i <= n; i++){
		
		for(k = n - i; k >= 1; k--)
			printf(" ");
			
		for(j = 1; j <= i; j++)
			printf("*");
		
		puts("");
	}
	
	for(i = n - 1; i >= 1; i--){
		
		for(k = n - i; k >= 1; k--)
			printf(" ");
		
		for(j = i + 1; j > 1; j--)
			printf("*");
		
		puts("");
	}

}