add= lambda x,y: x+y

subtract= lambda x,y: x-y 

multiply = lambda x, y: x*y

divide = lambda x,y: x/y
 

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

        break
    else:
        print("Wrong input")
z=input()
