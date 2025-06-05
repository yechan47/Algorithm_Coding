#include <stdio.h>

int main()
{
    int n, cnt = 0;

    scanf("%d", &n);

    for(long long i = 666;;i++)
    {

        if(i % 1000 == 666)
            cnt++;

        else
        {
            long long temp = i;
            while(temp > 0)
            {
                temp /= 10;
                if(temp % 1000 == 666)
                {
                    cnt++;
                    break;
                }
            }
        }
        
        if(cnt == n)
        {
            printf("%lld\n", i);
            return 0;
        }
    }
}