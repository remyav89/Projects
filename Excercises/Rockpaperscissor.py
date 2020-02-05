P1=input("The first player is")
p2=input("Second player is")


if(P1=='rock' and p2=='scissor'):
    print("p1 wins")
elif(P1=='scissor' and p2=='paper'):
    print("pi wins")
elif(P1=='paper' and p2=='rock'):
    print("p1 wins")
else:print("p2 wins")