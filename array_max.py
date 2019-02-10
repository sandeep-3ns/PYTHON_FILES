from numpy import *
arr=array([12,45,67,77])
print(arr)
max=arr[0]
for e in arr:
    if e>max:
     max=e
print(max)