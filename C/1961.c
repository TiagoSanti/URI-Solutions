#include <stdio.h>

#define min 1
#define max 5
#define MIN 2	
#define MAX 100

int main(){
	int P, N, C1, C2, i;

	scanf("%d %d", &P, &N);

	if(P >= min && P <= max && N >= MIN && N <= MAX)
	{
		for(i = 0; i <= N; i++)
		{
			scanf("%d %d", &C1, &C2);
			
			if(C2 > C1 + P || C2 < C1 - P || C1 > C2 + P || C1 < C2 - P)
				printf("GAME OVER\n");
		}
	}
	
	return 0;
}
