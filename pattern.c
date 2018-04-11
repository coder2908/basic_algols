#include<stdio.h>
int main(void)
{
    int i,j,k;
    for(i = 1;i <= 10; i++)
        {

            for(j = 1;j <= 10-i; j++)
            printf(" ");
            for(j = i;j <= 2*i-1; j++)
            printf("%d",j%10);
            for(k = j-2;k >= i;k --)
            printf("%d",k%10);
            printf("\n");
        }
}
