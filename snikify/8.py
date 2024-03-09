def factorial(val):
    if (val == 1):
        return 1
    return (val)*factorial(val-1)


n = int(input())
sum = 0
for i in range(1, n+1):
    v = factorial(i)
    sum += v
    v = 0
print(sum)
