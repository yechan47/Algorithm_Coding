#include <stdio.h>



int main(){

	

	int n = 0, x = 0, y = 0, i = 0;

	

	scanf("%d", &n);

	

	for(i = 1; i < n + 1; i++){

		

		scanf("%d %d", &x, &y);

		

		printf("Case #%d: %d\n", i , x + y);

	}

	

	

}