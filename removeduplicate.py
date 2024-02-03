numbers=[1,3,3,2,1,4,8,2]
# remove duplicate from a list
val=0
count=0
for each in numbers:
    if(numbers.count(each)>1):
        for e in numbers:
            if(e==each and count>0):

                numbers.remove(each)
            elif e==each:
                count+=1
        count=0

print(numbers)