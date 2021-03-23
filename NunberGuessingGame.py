import random
n = random.randint(0,100)
number_of_guess = 1
print("Welcome In Number guessing game")
print("Developed By Rahul Chatterjee")
name1 = str(input("Enter Your name= "))
print("You have 10 live to win the game")

while number_of_guess<=10:
    num = int(input("Guess the number 1 to 100="))
    if num>n:
        print("You enter a big number. Try smaller one",end="")

    elif num<n:
        print("you enter a small number. Try bigger one",end="")
    else:
        print(name1,"You win!")
        print("Your score is= ", 10 - number_of_guess)
        break
    print("                 Guess left= ",10-number_of_guess )
    number_of_guess = number_of_guess  + 1
    
if number_of_guess>10:
    print(name1,"You lose! \n Game Over! \n Play Again \n The Number was:- ",n)
input()

