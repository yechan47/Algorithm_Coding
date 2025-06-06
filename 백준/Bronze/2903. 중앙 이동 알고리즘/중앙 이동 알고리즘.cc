#include <stdio.h>

main()
{
	int n; // 반복 횟수 
	int s = 1; // s = 루트 사각형 개수
	int result;
	scanf("%d", &n);
	
	for(int i=1; i<=n; i++)
	{
		if(n==1)
			s = 2;
			
		else
			s = s * 2;
	}
	
	printf("%d", (s+1) * (s+1)); 
	
}