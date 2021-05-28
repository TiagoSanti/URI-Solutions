#include <stdio.h>

int main()
{
	int x, y, i = 1, j;

	scanf("%d %d", &x, &y);
	while(i <= y)
	{
		j = 0;

		while(j < x)
		{
			if(j == x - 1)
				printf("%d\n", i);
			else
				printf("%d ", i);
			i++;
			j++;
		}
	}
}