food_ite=['Non-Veg','Veg']
food_pric=[150,120]
food_qty=[]

food_com=dict(zip(food_ite,food_pric))

print(food_com)
user_order={}
flag=True

while flag==True:
    choice=input('Enter your choice: ')
    qnty= int(input('Enter Quantity: '))
    user_order[choice]=qnty
    req=input('Press Y for continue and N for exit: ')
    if req=='N':
        flag=False
    else:
        flag = True
print(user_order)

dist = int(input('Enter Distace: '))
bill_amnt=0

for k in user_order:
    if k in food_com:
        bill_amnt += food_com[k]*user_order[k]
    else:
        print('Enter only Veg or Non Veg')

if dist <3:
    print(bill_amnt)
elif 3<=dist<7:
    bill_amnt=bill_amnt+(dist-3)*3
    print(bill_amnt)
else:
    bill_amnt=bill_amnt+(dist-6)*6
