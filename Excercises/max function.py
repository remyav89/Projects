import sys
def Calacmaxmin(intlist):
    max = list[0]
    min=list[0]
    for index in range(1, len(list)):
        #print(index)
        if not(index >= len(list)):
            if (max <= list[index]):
                max = list[index]

            if(min>=list[index]):
                min=list[index]

    return max,min
list=[35,22,11,808,56,103,202,1,7,8]
print(Calacmaxmin(list))








