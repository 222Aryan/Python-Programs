yr=int(input("enter the year"))
n=int(input("enter the number of years"))
leap_year=[]
for i in range (yr,yr+n*4):
    if (( i%400==0 or i%4==0) and i%100!=0) :
            leap_year.append(yr)
            print (i)
            