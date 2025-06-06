#include <stdio.h>

main()
{
	int a, b, c;
	
	while(1)
	{
		scanf("%d %d %d", &a, &b, &c);
		
		if(a==0 && b==0 && c==0)
			break;
			
		int A = a * a;
		int B = b * b;
		int C = c * c;
		
		if(A+B==C || A+C==B || B+C==A)
			printf("right\n");
			
		else
			printf("wrong\n");
	}
}