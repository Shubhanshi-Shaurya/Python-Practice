#TUPLES
#USED TO STORE MULTIPLE ITEMS IN A VARIABLE 
#USE ROUND BRACKETS 
#ORDERED 
#IMMUTABLE 
#DUPLICATES ALLOWED 
#INDEXING OF ELEMENS (ZERO BASED INDEXING)
#ANY DATA TYPE CAN BE STORED 
#MIX OF DIFFERENT DATA TYPES CAN BE STORED 


#CREATING A TUPLE
colors=("blue","green","pink","red","yellow")


#CREATING A TUPLE WITH 1 ITEM
fruit=("apple",)
fruit=tuple(("apple"))


#CHECK TYPE OF TUPLE 
print(type(colors))
print(type(fruit))


#LENGTH OF TUPLE 
print(len(colors))


#ACCESSING ITEMS IN TUPLE 
print(colors[0])
print(colors[-2])      #using negative indexing 
print(colors[1:4])     #range indexing 
print(colors[-3:-1])


#CHECK FOR AN ITEM IN A TUPLE
if "green" in colors:
    print("green is present in tuple ")
if "black" not in colors:
    print("black not in colours")


#TRAVERSE THE TUPLE 
for i in colors:
    print(i)


#CONCATENATE TWO STRINGS
new_colors=("pink","black")
colors=colors+new_colors
print(colors)


#UNPACKING A TUPLE 
color1,color2,color3,color4,color5=colors
print(color1,color2,color3,color4,color5)


#REVERSE A TUPLE 
number=(1,2,3,4,5,6)
list=[]
for x in reversed(number):
    list.append(x)
answer=tuple(list)     #typecast into tuple
print(answer)


