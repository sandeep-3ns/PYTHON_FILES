from array import *
arr=array('i',[10,20,30,40,50,60])
print(arr)
for i in range(len(arr)//2):
    temp=arr[i]
    arr[i]=arr[len(arr)-i-1]
    arr[len(arr)-i-1]=temp
print(arr)