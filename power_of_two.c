/* C program to check whether a number N is power of 2 or not*/
#include<stdio.h>

int main(void)
{
  int n, flag = 0;
  scanf("%d",&n);
  while (n > 1)
  {
    if (n % 2 == 0)
      n = n / 2;
    else
    {
      flag = 1;
      break;
    }
  }
  if (flag == 0)
    printf("YES");
  else
    printf("NO");
}
