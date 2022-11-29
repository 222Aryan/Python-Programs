print('Press 1 for Product by 2')
print('Press 2 for Product B\W any 2 number')
choi=int(input('Enter the Choice '))
if choi==1:
    num1=2
    num2=int(input('Enter Number '))
    prod=0
    while num2>0:
        prod += num1
        num2 -=1
    print('Product of Numbers is: ',prod)
elif choi==2:
    num1=int(input('Enter 1st Number '))
    num2=int(input('Enter 2nd Number '))
    prod=0
    while num2>0:
        prod += num1
        num2 -=1
    print('Product of Numbers is: ',prod)
print('Passed')