from array import *
arr=array('i',[10,20,30,40,50,60])
#deleet elemenr at index2
new_arr = array('i',[])

for i in range(len(arr)):
    if i==2:
        continue;
    else:
        new_arr.append(arr[i])

print(new_arr)
