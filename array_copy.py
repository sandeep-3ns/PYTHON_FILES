from numpy import *
#from array import *
arr=array([1,2,3,4,5,6])
arr2=arr
print(id(arr))
print(id(arr2))
arr[1]=12
print(arr)
print(arr2)

arr3=arr.view()
#view() uses sghallow copy internally and any modification done on
#one array reflects the changes automatically in the other array
print(arr)
print(id(arr))
print(arr3)
print(id(arr3))
arr[4]=444
print(arr)
print(arr3)

arr4=arr.copy() #uses deep copy internally creates a new array
#independent of the existing arrays
print(arr)
print(arr4)
arr[0]=90
print(arr)
print(arr4)