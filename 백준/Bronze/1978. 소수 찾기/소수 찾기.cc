#include <stdio.h>
 
main()
{
    int N;
    scanf("%d", &N);
 
    int numbers[N];
    for(int n=0; n<N; n++)
        scanf("%d", &numbers[n]);
 
    int count = 0;
    for(int i=0; i<N; i++)
	{
        int number = numbers[i];

        for(int j=2; j<number; j++)
		{
            if(number%j==0)
                break;
            
            if(j==number-1)
                count++;
            
        }
        if(number==2)
            count++;
    }
    
    printf("%d\n", count);
}