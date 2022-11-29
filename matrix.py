r = int(input("Enter rows "))
c = int(input("Enter Cols "))

matrix = []

for i in range(r):
    temp = []
    for j in range(c):
        temp.append(int(input('Enter Elements')))
    matrix.append(temp)

print(matrix)