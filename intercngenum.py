c=int(input('Enter 1st Number: '))
d=int(input('Enter 2nd Number: '))
print('Before interchange')
print('Value of 1st Number: ',c)
print('Value of 2nd Number: ',d)
d+=c
c=d-c
d=d-c
print('After interchange')
print('Value of 1st Number: ',c)
print('Value of 2nd Number: ',d)
print('Passed')