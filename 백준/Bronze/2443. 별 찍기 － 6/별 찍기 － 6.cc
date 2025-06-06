#include <stdio.h>
 
int main()
{
    int N;
    scanf("%d", &N);
    for(int i = 0; i < N; i++)
    {
        int cnt = i;
        for(int j = N - 1 ; j > -N + i; j--)
        {
            if(cnt-- > 0) printf(" ");
            else printf("*");
        }
        printf("\n");
    }
    return 0;
}
