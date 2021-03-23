name=str(input("Enter your name in capital letters= "))

for i in range(len(name)):

#print A
    if name[i]=="A":
        for i in range(7):
            for j in range(5):
                if ((j==0 or j==4) and (i!=0)) or (i==0 or i==3) and (j>0 and j<4):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print B
    elif name[i]=="B": 
        for i in range(7):
            for j in range(5):
                if ((j==4) and (i!=0 and i!=6 and i!=3)) or (j==0) or ((i==0 or i==3 or i==6) and (j==1 or j==2 or j==3)):
                   print("*",end="")
                else:
                    print(" ",end="")
            print()
#print C
    elif name[i]=="C":
        for i in range(7):
            for j in range(5):
                if (j==0) or ((i==0 or i==6) and (j!=0)):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print D
    elif name[i]=="D": 
        for i in range(7):
            for j in range(5):
                if (i==0 or i==6) and (j!=4) or (j==0 or j==4) and (i!=0 and i!=6):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print E
    elif name[i]=="E": 
        for i in range(7):
            for j in range(5):
                if (j==0) or ((i==0 or i==3 or i==6) and (j!=0)):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print F
    elif name[i]=="F": 
        for i in range(7):
            for j in range(5):
                if (j==0) or ((i==0 or i==3) and (j!=0)):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print G
    elif name[i]=="G": 
        for i in range(7):
            for j in range(5):
                if ((j==0) and i!=0 and i!=6) or ((i==0 or i==6) and (j!=0 and j!=4)) or ((j==4) and (i!=0 and i!=2 and i!=3)) or (j==3 and i==4) :
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print H
    elif name[i]=="H": 
        for i in range(7):
            for j in range(5):
                if ((j==0 or j==4) and (i!=0)) or (i==3) and (j>0 and j<4):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print I
    elif name[i]=="I": 
        for i in range(7):
            for j in range(5):
                if (i==0 or i==6) or (j==2) : 
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print J
    elif name[i]=="J": 
        for i in range(7):
            for j in range(5):
                if (i==0) or (i==6) and (j!=3 and j!=4)  or ((j==2) and (i==5 and i==4)) or (j==2) or (j==0) and (i==5): 
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print K
    elif name[i]=="K": 
        for i in range(7):
            for j in range(5):
                if (j==0) or (j==4-i or i==2+j):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print L
    elif name[i]=="L": 
        for i in range(7):
            for j in range(5):
                if(j==0) or (i==6):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print M
    elif name[i]=="M": 
        for i in range(7):
            for j in range(5):
                if (j==0 and (i!=6) or j==4 and (i!=6)) or (j==0+i or j==4-i) and (i!=3):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print N
    elif name[i]=="N": 
        for i in range(7):
            for j in range(5):
                if (j==0 or j==4) or (i==j):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print O
    elif name[i]=="O": 
        for i in range(7):
            for j in range(5):
                if ((j==0 or j==4) and i!=0 and i!=6) or ((i==0 or i==6) and j!=0 and j!=4):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print P
    elif name[i]=="P": 
        for i in range(7):
            for j in range(5):
                if (j==0) or ((i==0 or i==3) and j!=4) or ((j==4) and i!=0 and i<3): 
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print Q
    elif name[i]=="Q": 
        for i in range(7):
            for j in range(5):
                if ((j==0 or j==3) and i!=0 and i!=5 and i!=6) or ((i==0 or i==5) and j!=0 and j!=3 and j!=4) or ( j==2 and i==4 or j==3 and i==5 or j==4 and i==6):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print R
    elif name[i]=="R": 
        for i in range(7):
            for j in range(5):
                if (j==0) or ((i==0 or i==3) and j!=4) or ((j==4) and i!=0 and i<3 ) or ((j==4) and i!=0 and i>3 )  :
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print S
    elif name[i]=="S": 
        for i in range(7):
            for j in range(5):
                if (i==0 or i==3 or i==6) or (j==0 and i<4) or (j==4 and i>3) :
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print T
    elif name[i]=="T": 
        for i in range(7):
            for j in range(5):
                if (i==0) or (j==2):
                    print("*",end="")
                else:   
                    print(" ",end="")
            print()
#print U
    elif name[i]=="U": 
        for i in range(7):
            for j in range (5):
                if (j==0 or j==4) or (i==6):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print V
    elif name[i]=="V": 
        for i in range(7):
            for j in range(5):
                if (j==0 or j==4) and (i<4)or ((i==4) and j==1 and j==3) or (i==5) and (j==2 and j==2):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
#print W
    elif name[i]=="W": 
        for i in range(7):
            for j in range(6):
                if (j==0 or j==5) or ((i==6 and j==0)  or (i==5 and j==1) or (i==4 and j>1 and j<4) or j==4 and i==5) or (j==5 and i==6):
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
# print X
    elif name[i]=="X": 
        for i in range(7):
            for j in range(6):
                if (j==i) or (j==7-2-i):
                    print("*",end="")
                else:       
                    print(" ",end="")
            print()
#print Y
    elif name[i]=="Y": 
        for i in range(7):
            for j in range(6):
                if (((j == 1 or j == 5) and i < 2) or i == j and j > 0 and j < 4 or (j == 4 and i == 2) or (( j== 3) and i > 3)):
                    print("*",end="")
                else:   
                    print(" ",end="")
            print()
#print Z
    elif name[i]=="Z": 
        for i in range(7):
            for j in range(6):
                if ((i==0 or i==6) and j>=0 and j<=5) or (i+j==5):
                    print("*",end="")
                else:   
                    print(" ",end="")
            print()
    else:
        print("Wrong Input")
    print(end="\n")
input()
