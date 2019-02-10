from array import array
arr=array('i',[10,-5,56,1,78,9])
arr.append(23)
print(arr)
for i in range(6):
    print(arr[i]," ",end='')
arr.reverse()
print(arr)
arr.pop(3)
print(arr)