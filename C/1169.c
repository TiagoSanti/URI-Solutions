#include <stdio.h>
#include <math.h>

int main()
{
	int c, n;
	int i, j;
	unsigned long long int soma, massa;

	scanf("%d", &n);

	for(i = 0; i < n; i++)
	{
		soma = 0;

		scanf("%d", &c);
		
		for(j = 0; j < c; j++)
			soma += pow(2, j);

		massa = soma/12000;
		
		printf("%llu kg\n", massa);
	}

	return 0;
}