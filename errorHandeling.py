
try:
    age =int(input("Age: "))
    income =20145
    risk=income/age

    print(risk)

    print(age)
except ValueError:
    print("invalid valu")
except ZeroDivisionError:
    print("cann't divide value by 0")