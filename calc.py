def add(a,b):
	r=a+b
	return r,r
def sub(a,b):
	r=a-b
	return r,r
def div(a,b):
	r=a/b
	return r,r
def mul(a,b):
	r=a*b
	return r,r
def cont():
	c=input('Enter q to quit or Enter to continue ? \n')
	return c

def main():
	print('\a')
	a=int(input('Enter the first num ? \n'))
	c=' '
	while(c!='q'):
		op=input('Choose Operator: + for addition ; - for substraction ; * for multiply ; / for divide  \n')
		if(op.strip()=='+'):
			b=int(input('Enter other number ? \n'))
			r,a=add(a,b)
			print(f'Your result : {r}')
			c=cont()
		elif(op.strip()=='-'):
			b=int(input('Enter other number ?'))
			r,a=sub(a,b)
			print(f'Your result : {r}')
			c=cont()
		elif(op.strip()=='*'):
			b=int(input('Enter other number ?'))
			r,a=mul(a,b)
			print(f'Your result : {r}')
			c=cont()
		elif(op.strip()=='/'):
			b=int(input('Enter other number ?'))
			r,a=div(a,b)
			print(f'Your result : {r}')
			c=cont()
		else:
			print('Wrong input MORON !')
			c=cont()

main()
