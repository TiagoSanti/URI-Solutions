#include <stdio.h>

int main()
{
	int n, x, y, menor, mdc, aux, i;

	scanf("%d", &n);

	for(i = 0; i < n; i++)
	{
		mdc = 1;
		aux = 1;
		scanf("%d %d", &x, &y);

		if(x > y)
			menor = y;
		else
			menor = x;
	
		while(aux <= menor)
		{
			if(x % aux == 0 && y % aux == 0)
				mdc = aux;

			aux++;
		}

		printf("%d\n", mdc);
	}

	return 0;
}