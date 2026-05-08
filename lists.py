#LISTS 
#ENCLOSED IN SQUARE BRACKETS 
#ALLOWS US TO STORE MULTIPLE ITEM IN A SINGLE VARIABLE 
#ITEMS ARE INDEXED (ZERO BASED INDEXING)
#ITEMS ARE ORDERED 
#MUTABLE 
#DUPLICATES ALLOWED 
#ANY DATA TYPE CAN BE STORED 
#MIX OF DIFFERENT DATA TYPES CAN BE STORED 


fruits=["apple","banana","cherry","orange","guava"]


#PRINTING LISTS 
print(fruits)

#TYPE OF LIST
print(type(fruits))

#LENGTH OF LIST 
print(len(fruits))


#CHECKING FOR A ITEM IS PRESENT IN THE LIST 
if "banana" in fruits:
    print("banana is present in list ")
if "kiwi" not in fruits:
    print("kiwi is not part of fruits")

    
#ACCESSING ELEMENTS OF A LIST 
print(fruits[1])
print(fruits[-2])
print(fruits[-3:-1])

#ADDING ELEMNETS TO A LIST 
fruits.append("kiwi")
print(fruits)
fruits.insert(2,"lime")
print(fruits)
veggie=["chilli","potato"]
fruits.extend(veggie)
print(fruits)


#REMOVING ELEMENTS FROM LIST 
fruits.remove("banana")
print(fruits)
fruits.pop(4)
print(fruits)


#CHANGING ITEMS IN LIST 
fruits[1]="pineapple"
print(fruits)
fruits[1:3]=["papaya"]
print(fruits)


#SORTING A LIST 
fruits.sort()        #ascending by default
print(fruits)
fruits.sort(reverse=True)       #sort in descending order 
print(fruits)
fruits.reverse()
print(fruits)


#LIST COMPREHENSION 
#WHEN WE WANT TO MAKE A NEW LIST FROM AN EXISTING LIST 
new_fruits=[fruit for fruit in fruits if "a" in fruit]
print(new_fruits)


#COPY A LIST 
copy_fruits=fruits.copy()
print(copy_fruits)


#CONCATENATE TWO LISTS 
new_fruits=fruits+new_fruits
print(new_fruits)


#NESTED LIST 
#LIST INSIDE LIST 
fruits.insert(2,["chilli","onion"])
print(fruits)
print(fruits[2][0])


#SWAP TWO ELEMENTS WITH THE GIVEN INDICES 
n=int(input("enter the size of list :"))
list=[]
for i in range(n):
    num=int(input())
    list.append(num)

print(list)
idx1=int(input("enter the index 1 : "))
idx2=int(input("enter the index 2 : "))
temp=list[idx1]
list[idx1]=list[idx2]
list[idx2]=temp

print(list)



