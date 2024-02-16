
lst = [4.0,3.75,3.75,3.5]
lst2 = [2,2,3,3]

for n in enumerate(zip(lst,lst2)):
    print(n)
    print(n[0],n[1][0],n[1][1])



