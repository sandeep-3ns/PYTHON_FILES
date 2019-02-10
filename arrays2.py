from array import array
arr=array('i',[10,-5,56,1,78,9])
for i in arr:
    print(i)
#####someties we have to create a new array with existing array elements but not knowing the type of the elemnets
#then we use the syntax as below

new_arr=array(arr.typecode,(k for k in arr))
print(new_arr)