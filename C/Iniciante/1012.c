#include <stdio.h>
#include <math.h>

int main(){
	double A, B, C, triangulo, circulo, trapezio, quadrado, retangulo;
	
	scanf("%lf\n%lf\n%lf", &A, &B, &C);
	
	triangulo = A*C/2;
	circulo = 3.14159*pow(C,2);
	trapezio = (A+B)*C/2;
	quadrado = pow(B,2);
	retangulo = A*B;
	
	printf("TRIANGULO: %.3lf\nCIRCULO: %.3lf\nTRAPEZIO: %.3lf\nQUADRADO: %.3lf\nRETANGULO: %.3lf\n", triangulo, circulo, trapezio, quadrado, retangulo); 
	
	return 0;
}
