#include <stdio.h>

int main()
{
	int hi, mi, hf, mf;

	scanf("%d %d %d %d", &hi, &mi, &hf, &mf);

	if(hi == mi && mi == hf && hf == mf)
		printf("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)");
	else {
		if(mf - mi > 0)
        	printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)", hf - hi, mf - mi);
    	else
        	printf("O JOGO DUROU %d HORA(S) E %d MINUTO(S)", (hf - hi) - 1, (mf - mi) + 60);
	}
}