#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to- 
price_list=[1700,2000,1500,3900,3900]

gems_quan=[30,45,32,33,31]

d1=dict(zip(gems_list,price_list))
d2=dict(zip(gems_list,gems_quan))
print(d1)

user_order = {}
flag= True

while flag==True:
    name = input('Enter Name of gems: ')
    quan = int(input('Enter Quantity: '))
    user_order[name]=quan
    req = input('Press Y for continue and N to exit: ')
    if req=='N' or 'n':
        flag=False
    else:
        flag = True
print(user_order)

bill_amnt=0

for k in user_order:
    if k in d2:
        if d2[k]>= user_order[k]:
            bill_amnt += d1[k]*user_order[k]
            d2[k]=d2[k] - user_order[k]
    else:
        bill_amnt = -1
        break
if bill_amnt>30000:
    bill_amnt -= bill_amnt*0.05
    print(bill_amnt)
else:
    print(bill_amnt)