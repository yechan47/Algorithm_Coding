#include <stdio.h>

main()
{
    int n;
    int a = 1;
    
    scanf("%d", &n);
    
    for (int i=2; i*i<n+1; i++) 
		a += 1;

    printf("%d", a);
}