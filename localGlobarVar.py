#
# name="Junayed"
#
# def sum(a,b):
#     global total
#     total=0
#     total+=a+b
#
#
# print(f'name ={name},age={sum(10,11)},total={total}')
#
#
# values=[1,5,8,6,7,26,1,25,6]
#
#
#
# values.insert(0,124)
# values.append(45)
# try:
#     for v in values:
#         print(v,end=" ")
#     print()
# except IndexError:
#     print(":))")
#
#
# values.sort(reverse=True)
# print(values)
# lst=sorted(values)
# print(lst)

quantity=[1,2,3,6]
price=[2,5,6,7]

print(price)
print("here")
total=0
for i in range(len(quantity)):
    sum=price[i]*quantity[i]
    print(sum)
    total=total+sum
    sum=0
print(total)


def do_sum(a,b=5):
    return a+b,a,b
print(do_sum(20))