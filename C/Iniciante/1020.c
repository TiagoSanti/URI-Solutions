#include <stdio.h>

int main(){
	int x, a, m, d;
	
	scanf("%d", &x);
	
	if(x >= 365){
		a = x / 365;
		if(x % 365 >= 30){
			m = (x % 365)/30;
			d = (x % 365)%30;
		}
		else if(x % 365 < 30){
			m = 0;
			d = x % 365;
		}
	}
	else if(x <= 365){
		a = 0;
		if(x >= 30){
			m = x / 30;
			d = x % 30;
		}
		else if(x < 30){
			m = 0;
			d = x;
		}
	}
	
	printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n", a, m, d);
		
	return 0;	
}
