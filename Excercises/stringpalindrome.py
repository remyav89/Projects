s=input("enter one stirng")
s1=""
l=len(s)
while(l>0):
    s1=s1+s[l-1]
    l=l-1
print(s1)
if s!=s1:
    print("palindrome")
else:
    print("not a palindrome")









