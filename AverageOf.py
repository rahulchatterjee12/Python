hw =  int(input("Enter Your Average Of HomeWork= "))
q =  int(input("Enter Your Average Of Quiz= "))
e1 =  int(input("Enter Your Average Of 1st Exam= "))
e2 =  int(input("Enter Your Average Of 2nd Exam= "))
e3 =  int(input("Enter Your Average Of 3rd Exam= "))
total = hw+q+e1+e2+e3
av=total/5
if av>=90:
    print("You are Awesome in this course! Your average is= ",av,"You get A")
elif av>=80:
    print("You are Awesome in this course! Your average is= ",av,"You get B")
elif av>=70:
    print("You are Very good in this course! Your average is= ",av,"You get C")
elif av>=60:
    print("You are good in this course! Your average is= ",av,"You get D")
elif av>=50:
    print("You are not bad in this course! Your average is= ",av,"You get E")
elif av>=40:
    print("You are bad in this course! Your average is= ",av,"You get F")
else:
    print("You are Fale in this course! Your average is= ",av,"You get D")
