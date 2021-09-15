#include <stdio.h>

int main(){
	float A, B, C, aux;
	
	scanf("%f%f%f", &A, &B, &C);
	
	if (C > A && C > B){
		aux = C;
		C = A;
		A = aux;
	}
	else if (B > A && B > C){
		aux = B;
		B = A;
		A = aux;
	}
	
	if(A >= B + C){
		printf("NAO FORMA TRIANGULO\n");
	}
	if(A*A == B*B + C*C){
		printf("TRIANGULO RETANGULO\n");
	}
	if(A*A > B*B + C*C && A < B + C){
		printf("TRIANGULO OBTUSANGULO\n");
	}
	if(A*A < B*B + C*C){
		printf("TRIANGULO ACUTANGULO\n");
	}
	if(A == B && B == C && C == A){
		printf("TRIANGULO EQUILATERO\n");
	}
	if(A == B && A != C){
		printf("TRIANGULO ISOSCELES\n");
	}
	if(B == C && B != A){
		printf("TRIANGULO ISOSCELES\n");
	}
	if(C == A && C != B){
		printf("TRIANGULO ISOSCELES\n");
	}
	
	return 0;
}
