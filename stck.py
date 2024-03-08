
values = [1, 3, 4, 5]


class Stack:

    def push(item):
        values.append(item)
        for i in range(len(values)):
            if (i == 0):
                temp = values[i]
                values[i] = values[-1]
                values[-1] = temp
            else:
                temp = values[i]
                values[i] = values[-1]
                values[-1] = temp

    def pop():
        values.sort()
        values.pop()

    def peek():
        return values[0]

    def is_empty():
        if (len(values) == 0):
            return True
        else:
            return False

    def size():
        return len(values)


Stack.push(77)


print(Stack.peek())

print(Stack.is_empty())
print(Stack.size())
