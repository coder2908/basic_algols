#include<iostream>
#include<stdlib.h>
using namespace std;
int main()
{
	int nos[8]={4,8,9,2,8,19,5,6};
	int max=nos[0];
	int * flag=(int*)calloc((max+1),sizeof(int));
	for(int i=0;i<8;i++)
	{
		if(max<nos[i])
		{
			max=nos[i];
			flag=(int*)realloc(flag,max+1);
		}
		if(flag[nos[i]]==123)
		{
			cout<<"Duplicate element found "<<endl<<nos[i]<<endl;
			break;
		}
		else
		{
			flag[nos[i]]=123;
		}
	}
  cout<<"Duplicate element not found";
}
