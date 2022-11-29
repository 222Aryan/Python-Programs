num1 = int(input('Enter Total Populaton: '))
num4 = int(input('Enter Total Litracy Rate: '))
num2 = int(input('Enter Percentage of Men:  '))
num3 = int(input('Enter Percentage of Lit Men: '))

menpop = num1*num2//100
print('Population of Men is:     ',menpop)

litmen = menpop*num3//100
print('Nmuber of Literate Men:   ',litmen)
print('Number of illiterate Men: ',menpop-litmen)

wmen = num1-menpop
print('Population of Women is:   ',wmen)

litwmen = wmen*(num4-num3)//100
print('Number of Literate Women: ',litwmen)
print('Numb of illiterate Women: ',wmen-litwmen)