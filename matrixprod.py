r1 = int(input('Enter No. of Row in Matrix 1st '))
c1 = int(input('Enter No. of Col in Matrix 1st '))
r2 = int(input('Enter No. of Row in Matrix 2nd '))
c2 = int(input('Enter No. of Col in Matrix 2nd '))

matrix_1 = []
matrix_2 =  []
result = []

if c1==r2:
    for i in range(r1):
        temp = []
        for j in range(c1):
            temp.append(int(input('ENter Elements for Matrix 1st: ')))
        matrix_1.append(temp)
    print(matrix_1)

    for i in range(r2):
        temp = []
        for j in range(c2):
            temp.append(int(input('Enter the Elements of Matrix 2nd: ')))
        matrix_2.append(temp)
    print(matrix_2)
    for i in range(r1):
        temp = []
        for j in range(c2):
            temp.append(int(0))
        result.append(temp)
    for i in range(r1):
        for j in range(c2):
            for k in range(r2):
                result[i][j]+=matrix_1[i][k]+matrix_2[k][j]
    print(result)

else:
    print('Matrix is not possible')