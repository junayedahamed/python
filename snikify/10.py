n = int(input())

numbers = []

for i in range(1, n):
    y = int(input())
    numbers.append(y)
numbers.sort()


for i in range(0, len(numbers)):

    if (numbers[i] != i+1):
        print(i+1)
        break
