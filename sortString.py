

st = "babbbacdde"
l = list(st)

d = {}

for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

dict(sorted(d.items(), key=lambda item: item[1]))

print(d)