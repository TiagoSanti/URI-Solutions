#include <stdio.h>

int main (void){
	
	char nome;
	double salario, vendas, total;
	
	scanf("%s\n%lf\n%lf", &nome, &salario, &vendas);
	
	total = salario + vendas*0.15;
	
	printf("TOTAL = R$ %.2lf\n", total);
	
	return 0;
}	
