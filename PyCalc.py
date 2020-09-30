def calcHelp():
    print("Calculator Help :")
    print("Only accepted values :")
    print("1 - Addition of two numbers")
    print("2 - Subtraction of two numbers")
    print("3 - Multiplication of two numbers")
    print("4 - Division of two numbers")

def boolHelp():
    print("Boolean Help :")
    print("Only accepted values :")
    print("1 - Greater than.")
    print("2 - Less than.")
    print("3 - Equal to.")
    print("4 - Not equal to.")
    print("5 - Greater than or Equal to.")
    print("6 - Less than or Equal to.")

def globalHelp():
    calcHelp()
    boolHelp()

a = input("Which one would you Like to open: ")
x = input("Type The First Number : ")
y = input("Type The Second Number : ")
z = input("Type The Operation : ")
x1 = int(x)    # Makes the x an integer.
y1 = int(y)    # Makes the y an integer.

if z == "1": #Addition and Greater than.
    if a == "Calc":
        b = x1 + y1
    elif a == "Bool":
        b = x1 > y1
    else:
        b = int(0)
elif z == "2": #Minus and Less than.
    if a == "Calc":
        b = x1 - y1
    elif a == "Bool":
        b = x1 < y1
    else:
        b = int(0)
elif z == "3": #Multiply and equal to.
    if a == "Calc":
        b = x1 * y1
    elif a == "Bool":
        b = x1 == y1
    else:
        b = (0)
elif z == "4": #Division and not equal to .
    if a == "Calc":
        b = x1 / y1
    elif a == "Bool":
        b = x1 != y1
    else:
        b = int(0)
elif z == "5": # Null and Greater than or equal to.
    if a == "Calc":
        pass
    elif a == "Bool":
        b = x1 >= y1
    else:
        b = int(0)
elif z == "6" : #Null and Less than or equal to.
    if a == "Calc":
        pass
    elif a == "Bool":
        b = x1 >= y1
    else:
        b = int(0)
elif z == "?": #Help
    b = int(0)

if b == 0:
    globalHelp()
else :
    print(b)
