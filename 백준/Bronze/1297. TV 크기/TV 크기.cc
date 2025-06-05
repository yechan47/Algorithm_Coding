#include <stdio.h>
#include <math.h>

main()
{
    int d, h, w;
    double d2;
    scanf("%d %d %d", &d, &h, &w);
    d2 = sqrt((h*h) + (w*w));
    double h1 = d*h/d2;
    double w1 = d*w/d2;
    printf("%d %d", (int)h1, (int)w1);
}