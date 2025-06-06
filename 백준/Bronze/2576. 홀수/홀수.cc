#include <stdio.h>

main()
{
	int number[7];
	int i;
	int sum = 0;
	int min = 100;
	
	for(i=0; i<7; i++)
	{
		scanf("%d", &number[i]);
	} // 7개의 숫자를 number 배열에 저장 
	
	for(i=0; i<7; i++)
	{
		if(number[i]%2 == 1)
		{
			sum += number[i]; // sum = sum + number[i]
			if(number[i] < min)
				min = number[i];   // 최솟값 찾기 
		}
	}
	
	if(sum == 0)
		printf("-1");
		
	else
		printf("%d\n%d", sum, min);
}