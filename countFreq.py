from collections import OrderedDict

st = "bcdaccbbda"
l = list(st)

dic = {}
for i in l:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

dict = OrderedDict(sorted(dic.items()))


for k,v in dict.items():
    print(v,k,end =" ")
