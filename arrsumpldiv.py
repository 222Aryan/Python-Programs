lst = []
num = int(input('Enter number: '))
for i in range(0,num):
    ele=int(input())
    lst.append(ele)
print(lst)
sum=0
for i in lst[:num]:
    div = lst[i]
    i+=1
print(div)