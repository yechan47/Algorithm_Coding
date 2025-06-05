#include <stdio.h>
#include <math.h>
 
int arith_mean(int *arr, int N);
int median(int *counting, int N);
int mode(int *counting, int N);
int range(int *counting, int N);
 
int main(void)
{
    int N;
    scanf("%d", &N);
 
    int arr[N];
    for(int i=0; i<N; i++)
        scanf("%d", &arr[i]);

    int counting[8001];
    
    for(int i=0; i<8001; i++)
        counting[i]=0;
    
    for(int i=0; i<N; i++)
        counting[arr[i]+4000]++;
    
    printf("%d\n", arith_mean(arr, N));
    printf("%d\n", median(counting, N));
    printf("%d\n", mode(counting, N));
    printf("%d\n", range(counting, N));
}
 
int arith_mean(int *arr, int N)
{
    double sum=0;
    for(int i=0; i<N; i++)
        sum += arr[i];
    
    return (int) round(sum/N);
}
 
int median(int *counting, int N)
{
    int num=0;
    for(int i=0; i<8001; i++)
    {
        num+=counting[i];
        
        if(num>=(N+1)/2)
            return i-4000;
    }
    return 0;
}
 
int mode(int *counting, int N)
{
    int max=0;
    int num=0;
    int mode=0;
    for(int i=0; i<8001; i++)
    {
        if(counting[i]>max)
        {
            max=counting[i];
            num=1;
            mode=i-4000;
        }
        else if(counting[i]==max)
        {
            if(num==1)
            {
                num++;
                mode=i-4000;
            }
            else
                num++;
            
        }
    }
    return mode;
}
 
int range(int *counting, int N)
{
    int max=0;
    int min=0;
    for(int i=8000; i>=0; i--)
    {
        if(counting[i]!=0)
        {
            max=i;
            break;
        }
    }
    for(int i=0; i<8001; i++)
    {
        if(counting[i]!=0)
        {
            min=i;
            break;
        }
    }
    return max-min;
}