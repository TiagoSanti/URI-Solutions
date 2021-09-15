#include <stdio.h>

int main(){
    int n, q;
    float media, x, y;

    n = 0;
    q = 0;

    while (n < 6)
    {
        scanf("%f", &x);

        if (x > 0){
            q = q + 1;
            y += x;
        }
        
        n = n + 1;
    }

    media = y/q;

    printf("%d valores positivos\n", q);
    printf("%.1f\n", media);

    return 0;
}

