matrix=[
    [1,2,3],
    [7,8,9],
    [4,5,6]
]

print(matrix)

#sum of all value of matrix
total=0
for each in matrix:

    for i in range(len(each)):
        # print(each[i],end=" ")
        total+=each[i]

    print()

print(total)



