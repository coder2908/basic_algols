#include<stdio.h>
/* To check an year is leap year no or not
A leap year is divisible by 4. A century leap year is divisible by 400.*/
int main(void)
{
  int y;
  printf("Enter the year");
  scanf("%d",&y);
  if (y % 400==0) //For century leap year rules
    printf("YES");
  else if(y%100!=0&&y%4==0) //for non-century years
    printf("YES");
  else
    printf("NO");
}
