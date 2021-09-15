#include <stdio.h>

int main(){
	int i, j, k = 1, l = 10;
	float soma = 0.0, M[12][12], media;
	char O;

	scanf(" %c", &O);
	
	for(i = 0; i <= 11; i++){
		for(j = 0; j <= 11; j++)
			scanf("%f", &M[i][j]);
	}
	
	for(i = 0; i <= 4; i++){
		for(j = k; j <= l; j++)
			soma += M[i][j];

		k++;
		l--;
	}
	
	if(O == 'S')
		printf("%.1f\n", soma);
	
	else if(O == 'M'){
        media = soma/30.0;
		printf("%.1f\n", media);
	}

	return 0;
}
