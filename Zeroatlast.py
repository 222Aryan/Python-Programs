lst = []
num = int(input('Enter number of Elements'))
for i in range(0,num):
    ele = int(input())
    lst.append(ele)

print(lst)

for i in lst:
    if i==0:
        z=i
        s=lst.index(i)
        print('m',s)
        if i!=0:
            nz=i
            p=lst.index(i)
            print('k',p)
    i=i+1