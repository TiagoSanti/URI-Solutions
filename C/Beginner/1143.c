#include <stdio.h>

#define MAX 1000
#define MIN 1

int main (void)
{
	int n, x, x1, x2;
	
	
	scanf("%d", &n);
	
	if(n < MAX && n > MIN)
	{
		for(x = n - n + 1; x <= n; x++)
		{
			x1 = x*x;
			x2 = x*x*x;
			printf("%d %d %d\n", x, x1, x2);
		}
	}
	return 0;
}
