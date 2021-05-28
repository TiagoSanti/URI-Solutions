#include <stdio.h>

int main (void){
	
	float A, B, C, MEDIA;
	
	scanf("%f\n%f\n%f", &A, &B, &C); 
	
	MEDIA = (A*2 + B*3 + C*5)/10;
	
	printf("MEDIA = %.1f\n", MEDIA);
	
	return 0;
}
