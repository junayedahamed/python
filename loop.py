#
# for each in range(110,120,2): #(initialization ,endIndex,increment)
#     print(each)

# name=["juna","susa","ajoy","hasn't","murad"]
#
#
# for each in name:
#     print(each)

numbers=[10,12,36,15,199]
val=0
for each in numbers:
    val=val+each

print(val)

# nested loop coordinate(x,y)

for i in range(3):
    for j in range(3):
        print(f'({i},{j})')

# F shape using loop

num=[8,2,8,2,2]
for each in num:
    for i in range(each):
        print("X",end="")
    print()