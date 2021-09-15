#include <stdio.h>

int main(){
	int h, m, s, s2, m2;
	
	scanf("%d", &s);
	
	s2 = s % 60;
	
	m = s / 60;

	if(m > 60){
		m2 = m % 60;
	
		h = m / 60;
	
		printf("%d:%d:%d\n", h, m2, s2);
	}
	
	else if(m < 60){
		h = m / 60;
		
		printf("%d:%d:%d\n", h, m, s2);
	}
	
	return 0;
}
