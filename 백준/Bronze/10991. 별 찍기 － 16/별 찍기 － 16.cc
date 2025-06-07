#include<stdio.h>
int main()
{
    int i,j,k = 0;
    int check = 0;
   
    scanf("%d",&check);
   
    for(i=0;i<check;i++)
    {
    	for(j=0;j<check-i-1;j++)
            printf(" ");
  
        if(i==0){
            printf("*\n");
            continue;
        }
        else{
        for(k=0;k<=(i*2)+1;k++){
            if(k%2==0)
                printf("*");
            else
                printf(" ");
  
            }
        printf("\n");
        }
    }
    return 0;
      
  }   