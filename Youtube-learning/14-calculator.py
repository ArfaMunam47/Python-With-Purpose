
# SIMPLE CALCULATOR
print('Supported only +,-,*,/')
num1=int(input('Enter num1:- '))
num2=int(input('Enter num2:- '))
oper=input('Enter operation u wanna perform:- ')
if oper=='+':
    print(num1+num2)
elif oper=='-':
    print(num1-num2)
elif oper=='*':
    print(num1*num2)
elif oper=='/':
    print(num1/num2)
else:
    print('Operation not supported')

# Another example
print('Supported only +,-')
n1=int(input('Enter num1:- '))
n2=int(input('Enter num2:- '))
opr=input('operation:- ')
if opr=='+':
    print(n1+n2)
if opr=='-':
    print(n1-n2)
if oper!='+' and opr!='-':
    print('Invalid Operation... ')