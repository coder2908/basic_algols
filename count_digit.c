/* Given a number N and a digit d, find the total number of occurrence of digit d in number N*/
#include<stdio.h>

void main(void)
{
  int n, d, counter = 0;
  scanf("%d %d",&n,&d);
  while (n > 0)
  {
    int temp;
    temp = n % 10;
    n = n / 10;
    if (temp == d)
      counter ++;
  }
  printf("%d",counter);
}

