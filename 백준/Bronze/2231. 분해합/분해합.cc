#include <stdio.h>

main()
{
    int n;
    scanf("%d", &n);
    
    for(int i=1; i<n; i++)
    {
        int temp = i;
        int num = i;
        
        while(temp > 0)
        {
            num += temp % 10;
            temp /= 10;
        }
        
        if(num == n)
        {
            printf("%d", i);
            n = 0;
            break;
        }
    }
    
    if(n != 0)
        printf("0");
}