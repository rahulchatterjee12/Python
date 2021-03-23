n1= int (input("Enter 1st number= \n"))
n2= int (input("Enter 2nd number= \n"))
op1=input("+,-,/,* \n")
while True:
    
    if op1=='+':
        print("Anwer is= ",n1+n2)
    elif op1== '-':
        print("Answer is= ",n1-n2)
    elif op1== '*':
        print("Anwer is= ", n1*n2)
    elif op1== '/':
        print("Answer is= ", n1/n2)
    else:
        print("Error! Try agane")
exit1 = input("Do you want to run it again press \" y \" or \" n\" ")

