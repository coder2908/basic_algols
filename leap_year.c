#include<stdio.h>
/* To check a num is leap year no or not
A leap year is divided by 4.*/
int main(void)
{
  int y;
  scanf("%d",&y);
  if (y % 4 == 0)
    printf("YES");
  else
    printf("NO");
}
