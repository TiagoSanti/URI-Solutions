#include <stdio.h>

int main(){
	int x, y, i, j, s = 0;
	
	scanf("%d %d", &x, &y);
	
	if(x > y)
	{
		i = x;
		x = y;
		y = i;
	}
	
	for(x++; x < y; x++)
	{
		if(x%2 == -1 || x%2 == 1)
		{
			s += x;
		}
	}
	
	printf("%d\n", s);
	
	return 0;
}
