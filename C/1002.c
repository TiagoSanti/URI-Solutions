#include <stdio.h>
#include <math.h>
 
int main() {
 
    double area, p, raio;
    
	p = 3.14159;

    scanf("%lf", &raio);
	
    area = p * pow(raio,2);
    
    printf("A=%.4f\n", area);
 
    return 0;
}
