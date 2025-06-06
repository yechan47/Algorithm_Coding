#include <stdio.h>
int main()
{
	int a,b,c,d,e,f,g,h,S,T;
	scanf("%d%d%d%d",&a,&b,&c,&d);
	scanf("%d%d%d%d",&e,&f,&g,&h);
	S=a+b+c+d;
	T=e+f+g+h;
	if(S>T)
	{
		printf("%d",S);
	}
	else if(S<T)
	{
		printf("%d",T);
	}
	else
	{
		printf("%d",S);
	}
}