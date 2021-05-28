#include <stdio.h>

int main()
{
	float x;

	scanf("%f", &x);

	if(x >= 0.0 && x <= 2000.0)
		printf("Isento\n");

	else if(x >= 2000.01 && x <= 3000.0)
		printf("R$ %.2f\n", (x - 2000)*0.08);

	else if(x >= 3000.01 && x <= 4500.0)
		printf("R$ %.2f\n", 1000*0.08 + (x - 3000)*0.18);

	else if(x >= 4500.0)
		printf("R$ %.2f\n", 1000*0.08 + (x - 3000)*0.18 + (x - 4500)*0.28);
}