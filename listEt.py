values = [1, 2, 3, 4, 5, 6, 7, 8, 9]


values.append(10)
values.insert(0, 12)
print(values)
values.append([99, 100])
values.extend([100])  # extend one value

values.insert(0, 10)
print(values.count(100))
print(values.index(100))
values.reverse()
print(f'reverse: {values}')

values.remove(2)
x = values.pop(2)
print(f'pooped :{x}')
