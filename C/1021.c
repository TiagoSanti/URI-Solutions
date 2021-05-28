#include <stdio.h>
#include <math.h>

int main()
{
	float money;
	int a, b, c, d, e, f;
	int g, h, i, j, k, l;

	a = 0; b = 0; c = 0; d = 0; e = 0; f = 0;
	g = 0; h = 0; i = 0; j = 0; k = 0; l = 0;

	scanf("%f", &money);

	if(money <= 1000000.0 && money >= 0.0)
	{
		if(money >= 100.0){
			a = money / 100;
			money = money - a*100;
		}   

		if(money >= 50.0){
			b = money / 50;
			money = money - b*50;
		}

		if(money >= 20.0){
			c = money / 20;
			money = money - c*20;
		}

		if(money >= 10.0){
			d = money / 10;
			money = money - d*10;
		}

		if(money >= 5.0){
			e = money / 5;
			money = money - e*5;
		}

		if(money >= 2.0){
			f = money / 2;
			money = money - f*2;
		}

		if(money >= 1.0){
			g = money / 1;
			money = money - g;
		}

		if(money >= 0.5){
			h = money / 0.5;
			money = money - h*0.5;
		}

		if(money >= 0.25){
			i = money / 0.25;
			money = money - i*0.25;
		}

		if(money >= 0.10){
			j = money / 0.10;
			money = money - j*0.10;
		}

		if(money >= 0.05){
			k = money / 0.05;
			money = money - k*0.05;
		}

		if(money >= 0.01){
			l = (money+0.009) / 0.01;
			money = money - l*0.01;
		}

		printf("NOTAS:\n"
			   "%d nota(s) de R$ 100.00\n"
			   "%d nota(s) de R$ 50.00\n"
			   "%d nota(s) de R$ 20.00\n"
			   "%d nota(s) de R$ 10.00\n"
			   "%d nota(s) de R$ 5.00\n"
			   "%d nota(s) de R$ 2.00\n"
			   "MOEDAS:\n"
			   "%d moeda(s) de R$ 1.00\n"
			   "%d moeda(s) de R$ 0.50\n"
			   "%d moeda(s) de R$ 0.25\n"
			   "%d moeda(s) de R$ 0.10\n"
			   "%d moeda(s) de R$ 0.05\n"
			   "%d moeda(s) de R$ 0.01\n",
			   a, b, c, d, e, f, g, h, i, j, k, l);
	}
}