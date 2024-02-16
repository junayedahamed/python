t=(1,2,3,4)
t+= (5,6,7,8) # that how we can add more values in tuple

for i in t:
    print(i)
    if(i==3):
        break

while(i<len(t)):
    print(i)
    break


num=[1,2,3,4,5]
num.insert(2,5)
print(num)