import string
result = ''
st = ('punjab delhi Bihar')
city = st.split(' ')
print(city)
for i in city:
    for j in i:
        j.upper()
        result+=j
print(result)