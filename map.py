def even_odd(num):
    if (num % 2 == 0):
        return "even"
    else:
        return "Odd"


numbers = [1, 2, 3, 4, 5, 6]
numbers1 = [1, 4, 7, 8, 9]

result = map(even_odd, numbers)
print(list(result))

sum = map(lambda x, y: x+y, numbers, numbers1)
print(list(sum))
