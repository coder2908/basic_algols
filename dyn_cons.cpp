#include<iostream>
using namespace std;

class test
{
	int *x;
	public:
	test()//default dynamic constructors.
	{
		x=new int;
		*x=10;
	}
	void output()
	{
		cout<<"The value is: \n"<<*x<<endl;
	}
};

int main(void)
{
	test t1;
	t1.output();
}
