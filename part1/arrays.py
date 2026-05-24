import array
import numpy as np

#PYTHON ARRAYS 
arr=array.array('i',[1,2,3,4,5,6])

#ACCESSING ARRAY ELEMENTS 
print(arr[0],arr[1])
print(arr)


#ADDING ELEMENTS IN ARRAY 
arr.insert(7,100)
print(arr)


#REMOVING ELEMENTS FROM ARRAY 
#pop function in array removes the element from array and return its value
print(arr.pop(2))
print(arr)


#SLICING OF AN ARRAY 
slicedArray=arr[3:5]
print(slicedArray)
slicedArray=arr[2:]
print(slicedArray)
slicedArray=arr[-1:]       #using negative indexing 
print(slicedArray)
print(arr[:])      #to print complete list


#SEARCHING ELEMENT IN ARRAY 
print(arr.index(5))


#COUNTING NUMBER OF OCCURENCES OF AN ELEMENT IN ARRAY 
print(arr.count(10))


#REVERSE AN ARRAY 
arr.reverse()
print(arr)


#EXTEND ELEMENT ARRAY (ADD ANOTHER ARRAY AT THE END)
arr.extend([7,8,9,10])
print(arr)






