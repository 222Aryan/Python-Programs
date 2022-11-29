air=input('Enter Airline name: ')
src=input('Enter Source: ')
dest=input('Enter Destination: ')
num= int(input('Enter No. of passengers: '))
lis=[]
if num<5:
    for i in range(num):
        lis.append(air+':'+src[0:3]+':'+dest + ':' + str(101+i))
else:
    for i in range(num-4,num+1):
        lis.append(air+':'+src[0:3]+':'+dest[0:3] + ':' + str(101+i))
print(lis)