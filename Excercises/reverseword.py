

'''def reverse_v1(x):
  y = x.split()
  result = []
  for word in y:
    result.insert(0,word)
  return " ".join(result)
test=("enter one sentance")
print(reverse_v1(test))'''

O_string = ("Me name is Mr_T")
split_result = O_string.split()
print(split_result)

x=0
list=[]

while x <= len(split_result):

  list.append(split_result[ : : -1])
  x = x-1
print(list)
result=" ".join(list)
print (result)
