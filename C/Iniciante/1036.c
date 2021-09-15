#include <stdio.h>
#include <math.h>

int main (){
	double a, b, c, d, x1, x2;
	
	printf("A = "); scanf("%lf", &a);
	printf("B = "); scanf("%lf", &b);
	printf("C = "); scanf("%lf", &c);
	
	d = pow(b,2) - (4*a*c);
	
	if(d < 0){
		printf("Impossivel calcular\n");
	}
	
	else if(d == 0){
		x1 = -b/(2*a);
		x2 = x1;
		printf("X1 = %lf\nX2 = %lf\n", x1, x2);
	}

	else if(d > 0 && a != 0){
		x1 = (-b + sqrt(d))/(2*a);
		x2 = (-b - sqrt(d))/(2*a);
		printf("X1 = %lf\nX2 = %lf\n", x1, x2);
	}

	else if(d > 0 && a == 0){
		printf("Impossivel calcular\n");
	}

	return 0;
}
