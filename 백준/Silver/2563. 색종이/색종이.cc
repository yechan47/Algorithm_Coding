#include <stdio.h>
int main()
{
	int paper[100][100]={}, T, a, b, ans=0;
	scanf("%d", &T);
	for(int i=0; i<T; i++){
		scanf("%d %d",&a,&b);
		for(int j=a; j<a+10; j++)
			for(int k=b; k<b+10; k++)
				paper[j][k] = 1;
	}
	for(int q=0; q<100; q++)
		for(int w=0; w<100; w++)
			if(paper[q][w]==1)
				ans++;
	printf("%d", ans);
}