Num=int(input("Enter a number"))
check=int(input("Enter another number"))
if(Num%2==0):
    print("It is an Even number")
    if(Num%4==0):
        print("The number is a mulltiple of 4")
else:
    print("It is an Odd number")

if(Num%check==0):
    print("divides evenly")
else:
    print("does not divides evenly")