#include<stdio.h>
#include<iostream>
using namespace std;

class test
{
	int var;
	public:
	test()//default constructor.
	{
		var=10;
	}
	test(int var)//parametrised constructor.
	{
		this->var=var;
	}
	void output()
	{
		cout<<"\nValue is:\n"<<var<<endl;
	}
};

int main()
{
	test t1;//default constructor will be called.
	test t2(5);//parametrised constructor will be called.
	t1.output();
	t2.output();
}
