from numpy import *
arr=array([1,2,3])
arr2=array([10,20,30])
for i in  range(len(arr)):
    arr[i]=arr[i]+arr2[i]
print(arr)