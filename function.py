def fact(x):
    if (x == 1):
        return 1
    return x*fact(x-1)


y = 4
z = fact(y)
print(z)
