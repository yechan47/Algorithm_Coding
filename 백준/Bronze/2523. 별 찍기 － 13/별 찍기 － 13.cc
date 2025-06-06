#include <stdio.h>



int main(){

	

	int n, i, j;

	

	scanf("%d", &n);

	

	for(i = 1; i <= n; i++){

		

		for(j = 1; j <= i; j++)

			printf("*");

		

		puts("");

	}

	

	for(i = n - 1; i >= 1; i--){

		

		for(j = i + 1; j > 1; j--)

			printf("*");

		

		puts("");

	}



}


