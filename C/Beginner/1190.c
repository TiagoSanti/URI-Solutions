#include <stdio.h>

int main(){
	int i, j, k = 11, l = 7;
	double soma = 0.0, M[12][12], media;
	char O;

	scanf(" %c", &O);
	
	for(i = 0; i <= 11; i++){
		for(j = 0; j <= 11; j++)
			scanf("%lf", &M[i][j]);
	}
	
	for(i = 1; i <= 10; i++){
        if(i <= 5){
            for(j = k; j <= 11; j++)
                soma += M[i][j];
            k--;
        }
        else if(i >= 6){
            for(j = l; j <= 11; j++)
                soma += M[i][j];
        	l++;
        }
	}
	
	if(O == 'S')
		printf("%.1lf\n", soma);
	
	else if(O == 'M'){
        media = soma/30.0;
		printf("%.1lf\n", media);
	}

	return 0;
}
