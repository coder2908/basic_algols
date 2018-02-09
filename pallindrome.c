#include<stdio.h>
/*pallindrome program.*/
void main(void)
{
	int n, rn=0 ,backup;
	printf("Input: ");
	scanf("%d",&n);
	backup = n;
	while (n > 0)
	{
		rn = (rn * 10) + (n % 10);
		n = n / 10;
	}
	if (rn == backup)
	printf("Output: YES");
	else
	printf("Output: NO");
}
