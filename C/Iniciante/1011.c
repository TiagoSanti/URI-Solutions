#include <stdio.h>
#include <math.h>

int main (void){
	
	double raio, p, volume;
	p = 3.14159;
	
	scanf("%lf", &raio);
	
	volume = (4.0/3)*p*pow(raio,3);
	
	printf("VOLUME = %.3lf\n", volume);
	
	return 0;
}
