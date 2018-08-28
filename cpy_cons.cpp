#include<iostream>
using namespace std;

class test
{
	int x;
	public:
	test(int a)
	{
		x=a;
	}
	test(const test * o)//copy constructor.
	{
		this->x=o->x;
	}
	void output()
	{
		cout<<"Data is :"<<x<<endl;
	}
};

int main(void)
{
	test t1(20);
	test t2(&t1);
	t1.output();
	t2.output();
}
