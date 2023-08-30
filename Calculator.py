def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
        return x/y
    else:
        return "Ans cannot be determined!"

print("Select operation to be performed \n 1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division")
choice = input("Enter choice = ")

a = float(input("Enter no. = "))
b = float(input("Enter no. = "))

if choice == "1":
    print("Addition is ",add(a,b))
elif choice == "2":
    print("Subtraction is ",subtract(a,b))
elif choice == "3":
    print("Multiplication is ",multiply(a,b))
elif choice == "4":
    print("Division is ",divide(a,b))
else:
    print("Incorrect Input")
