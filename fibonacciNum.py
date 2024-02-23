x=0
y=1
val=int (input("enter num: "))
print(x," " ,y,end=" ")
for i in range(val):
    sum=x+y
    print(sum,end=" ")
    x=y
    y=sum
    sum=0
