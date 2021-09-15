#include <stdio.h>

int main (){
	int N[10], i, V;
	
	scanf("%d", &V);
	
	N[0] = V;
	printf("N[0] = %d\n", V);
	
	for(i = 1; i <= 10; i++){
		V = V * 2;
		printf("N[%d] = %d\n", i, V);
	}
	
	return 0;
}
