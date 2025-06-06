#include <stdio.h>
 
int main()
{
    int N;
    scanf("%d", &N);
    for(int i = 0; i < N; i++)
    {
        for(int j = -N + 1; j <= N; j++)
        {
            if(j >= -i && j <= i) printf("*");
            else if(j <= i) printf(" ");
        }
        printf("\n");
    }
    return 0;
}