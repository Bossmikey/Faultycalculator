
#faulty digits are "45*3" "56+9" "56/6"

n1=int(input("Enter your first number:\n"))
n2=int(input("Enter your second number:\n"))
ans= "Answer is:"
chuzz= int(input("Select an operation:\n"
        "1. Add\n"
        "2. Sub\n"
        "3. Multiply\n"
        "4. Divide\n"))
if(n1==45 and chuzz==3 and n2==3):
    print("55")
elif(n1==56 and chuzz==1 and n2==9):
    print("59")
elif (n1 == 56 and chuzz == 4 and n2 == 6):
        print("45")
elif(chuzz==1):
    print(ans ,n1+n2)
elif(chuzz==2):
    print(ans,n1-n2)
elif(chuzz==3):
    print(ans, n1*n2)
elif(chuzz==4):
    print(ans,n1/n2)
elif(chuzz>4):
    print("\n Wrong selection of choice")


