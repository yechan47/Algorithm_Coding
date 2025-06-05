#include <stdio.h>

main() 
{
	int N;
	int temp;
	scanf("%d", &N);

	if (N < 10) 
        N *= 10;

	int cnt = 0;
	temp = N;

	while (1) 
    {
		cnt++;
		temp = temp % 10 * 10 + (temp / 10 + temp % 10) % 10;

		if (temp == N) 
			break;
	}
	printf("%d", cnt);
}