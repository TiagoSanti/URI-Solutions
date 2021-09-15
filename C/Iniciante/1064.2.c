#include <stdio.h>

int main(){
	int n, q = 0;
	float x, y, media;
	
	y = 0;
	for(n = 0; n < 6; n++)
	{
		scanf("%f", &x);
		
		if(x > 0){
			q = q + 1;
			y += x;
		}
	}
	
	media = y / q;

	printf("%d valores positivos\n%.1f\n", q, media);
	
	return 0;
}
