#include <stdio.h>

int main()
{
    int a, b, c;
    int result, k;
    
	scanf("%d %d %d", &a, &b, &c);
    
    if(a==b && b==c)
    {
    	result = 10000 + a * 1000;
	}
	
	else if(a==b && a!=c)
	{
		result = 1000 + a * 100;
	}
	
	else if(a==c && a!=b)
	{
		result = 1000 + a * 100;
	}
	
	else if(b==c && a!=b)
	{
		result = 1000 + b * 100;
	}
	
	else if(a != b && a != c && b != c)
	{
		if(a>b)
		{
			k = a;
			if(a>c)
				k = a;
			else
				k = c;
		}
		else if(a<b)
		{
			k = b;
			if(b>c)
				k = b;
			else 
				k = c;
		}
		result = k * 100;	
	}
	
    printf("%d", result);
}