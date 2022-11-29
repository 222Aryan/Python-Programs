print('For String Method Press 1')
print('For 0 to 9 Press 2')
inp=int(input('Enter Your Choice: '))
if(inp==1):
    num=input('Enter Number: ')
    print(num,num*2,num*3,'Sum of Numbers is',int(num)+int(num*2)+int(num*3))
elif(inp==2):
    num=int(input('Enter Number '))
    print(num,num*10+num,num*100+num*10+num,' Sum of Numbers is ',num+num*10+num+num*100+num*10+num)
print('Passed')