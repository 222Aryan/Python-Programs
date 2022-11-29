tic=[[5,3,2],[7,2,9],[1,3,4],[2,4,3]]
l={}
for r,c1,c2 in tic:
    l[r]=[c1,c2]
for r in l:
    print(l[r][0],l[r][1])