Num=int(input("Enter one number"))
listnum=list(range(1,Num+1))
listdiv=[]
for number in listnum:
    if(Num%number==0):
        listdiv.append(number)
print(listdiv)


