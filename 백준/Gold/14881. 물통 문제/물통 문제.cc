#include<stdio.h>

int gcd(long long x, long long y)
{
    if(y==0) 
		return x;
		
    return gcd(y, x%y);
}

main(){
    int t;
    long long a, b, c;
    
    scanf("%d", &t);
    
    for(int i=0; i<t; i++)
	{
        scanf("%lld %lld %lld", &a, &b, &c);
        
        if(a<c&&b<c) 
			printf("NO\n");
        else if(c%gcd(a, b)==0) 
			printf("YES\n");
        else 
			printf("NO\n");
    }
}