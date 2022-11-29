def check_num(lis):
  if len(lis) == len(set(lis)):
    print("All are different")
  else:
    print("All are not different");

n = int(input())
lis = []
for i in range(n):
    num = int(input())
    lis.append(num)

chk = check_num(lis)