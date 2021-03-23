def add(x,y):
    return x +y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Select operation=")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    
    choice = input("Enter choice(1/2/3/4)\n")


    if choice in('1', '2', '3', '4'):
        n1 = int(input("Enter 1st number= "))
        n2 = int(input("Enerr 2nd number= "))

        if choice == '1':
            print(n1, "+",n2, "=", add(n1,n2))

        elif choice == '2':
            print(n1, "-", n2,"=", subtract(n1,n2))

        elif choice == '3':
            print(n1, "*", n2, "=", multiply(n1,n2))

        elif choice == '4':
            print(n1, "/", n2, "=", divide(n1,n2))
    else:
        print("Wrong input")

    try:
        if input("Press Y or N: ") == "Y":
            continue
        else:
            break
    except InputError:
        break


