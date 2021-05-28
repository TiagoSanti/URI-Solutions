#include <stdio.h>
#include <string.h>

int main(){
	char data[13], data2[10], data3[11];

	scanf("%s", data);

	if(strcmp(data, "vertebrado") == 0)
	{
		scanf("%s", data2);

		if(strcmp(data2, "ave") == 0)
		{
			scanf("%s", data3);

			if(strcmp(data3, "carnivoro") == 0)
				printf("aguia\n");

			else if(strcmp(data3, "onivoro") == 0)
				printf("pomba\n");
		}
		else if(strcmp(data2, "mamifero") == 0)
		{
			scanf("%s", data3);

			if(strcmp(data3, "onivoro") == 0)
				printf("homem\n");

			else if(strcmp(data3, "herbivoro") == 0)
				printf("vaca\n");
		}
	}

	else if(strcmp(data, "invertebrado") == 0)
	{
		scanf("%s", data2);

		if(strcmp(data2, "inseto") == 0)
		{
			scanf("%s", data3);

			if(strcmp(data3, "hematofago") == 0)
				printf("pulga\n");

			else if(strcmp(data3, "herbivoro") == 0)
				printf("lagarta\n");
		}
		else if(strcmp(data2, "anelideo") == 0)
		{
			scanf("%s", data3);
			
			if(strcmp(data3, "hematofago") == 0)
				printf("sanguessuga\n");

			else if(strcmp(data3, "onivoro") == 0)
				printf("minhoca\n");
		}
	}
}