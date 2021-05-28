#include <stdio.h>

int main(){
	int i, n, x;
	float d, y;
	
	scanf("%d", &n);
	
	for(i == 0; i < n; i++){
		scanf("%d %f", &x, &y);
		
		if(x != 0 && y != 0){
			d = x / y;
			printf("%.1f\n", d);
		}
		
		else if(x == 0 && y!= 0){
			printf("0.0\n");
		}
		
		else if(x == 0 && y == 0 || x != 0 && y == 0){
			printf("divisao impossivel\n");
		}
	}
	
	return 0;
}
