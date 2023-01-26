def addition(a,b):
    result = a + b
    print(str(a) + " + " + str(b) + " = " + str(result))

def substraction(a,b):
    result = a - b
    print(str(a) + " - " + str(b) + " = " + str(result))

def multiplication(a,b):
    result =  a * b
    print(str(a) + " * " + str(b) + " = " + str(result))

def division(a,b):
    result =  a / b
    print(str(a) + " / " + str(b) + " = " + str(result))

print("A. Addition")
print("B. Substraction")
print("C. Multiplication")
print("D. Division")

while True:
    ask = input("What you want to calculate: ")
    if ask == "a" or ask == "A":
        print("Addition")
        a = int(input("Enter your first integer: "))
        b = int(input("Enter your second integer: "))
        addition(a,b)
    elif ask == "b" or ask == "B":
        print("Substraction")
        a = int(input("Enter your first integer: "))
        b = int(input("Enter your second integer: "))
        substraction(a,b)
    elif ask == "c" or ask == "C":
        print("Multiplication")
        a = int(input("Enter your first integer: "))
        b = int(input("Enter your second integer: "))
        multiplication(a,b)
    elif ask == "d" or ask == "D":
        print("Division")
        a = int(input("Enter your first integer: "))
        b = int(input("Enter your second integer: "))
        division(a,b)
    elif ask == 'e' or ask == 'E':
        print("Program ended")
        quit()

