#consecutive sum

numbers=[1,2,3,4]
val=0

conNum=[]
for each in numbers:
    val+=each
    conNum.append(val)


print(conNum)