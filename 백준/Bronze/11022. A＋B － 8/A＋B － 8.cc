#include <stdio.h>
int main(){
    int t ;
    int a, b;
    scanf("%d",&t);
    int i = 1;
    while(t--){
        scanf("%d %d", &a, &b);
        printf("Case #%d: %d + %d = %d\n",i++,a,b, a + b);
    }
}