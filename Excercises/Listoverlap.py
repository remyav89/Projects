a=[1,1,2,3,5,8,13,21]
b=[1,1,2,3,5,8,13,13,21,34,45]
c=[]
for i in a:
    for j in b:
        if i==j:
            c.append(i)
            c=list(set(c))#remove duplicates using set
print(c)


