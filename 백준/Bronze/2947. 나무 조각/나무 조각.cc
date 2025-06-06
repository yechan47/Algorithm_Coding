#include <stdio.h>
void bubbleSort(int arr[]);

int main() {
	int i;
	int arr[5];
	for (i = 0; i < 5; i++) {
		scanf("%d",&arr[i]);	
	}
	bubbleSort(arr);
}

void bubbleSort(int arr[]) {
	int i, j,k,tmp;
	for (i = 0; i < 5; i++) {
		for (j = 0; j < 4; j++) {
			if (arr[j] > arr[j + 1]) {
				tmp = arr[j];
				arr[j] = arr[j + 1];
				arr[j + 1] = tmp;
				for (k = 0; k < 5; k++) {
					printf("%d ", arr[k]);
				}
				printf("\n");
			}
		}
	}
}