l1=[1,2,4,5,20,31,55,56]
'''l2=[]
for i in l1:
    if(i%2==0):
        l2.append(i)
print(l2)'''

l2=[i for i in l1 if(i%2==0)]
print(l2)
