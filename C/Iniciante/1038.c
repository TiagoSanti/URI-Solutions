#include <stdio.h>

int main (){
	int i, q;
	float t;
	
	scanf("%d %d", &i, &q);
	
	if(i == 1){
		t = q * 4.;
	}
		
	else if(i == 2){
		t = q * 4.5;
	}
		
	else if(i == 3){
		t = q * 5.;
	}
		
	else if(i == 4){
		t = q * 2.;
	}
		
	else if(i == 5){
		t = q * 1.5;
	}
	
	printf("Total: R$ %.2f\n", t);
	
	return 0;
}
