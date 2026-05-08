#SETS
#CONTAINER FOR STORING MULTIPLE VALUES 
#ENCLOSED IN CURLY BRACKETS 
#UNORDERED
#IMMUTABLE
#UNINDEXED
#DUPLICATES NOT ALLOWED
#ANY DATA TYPE CAN BE STORED
#MIX OF DIFFERENT DATA TYPES CAN BE STORED


#PRINTING ITEMS IN SET
names={"sia","john","dave"}
print(names)

#LENGTH OF SET 
print(len(names))


#CHECK DATA TYPE OF SET 
print(type(names))


#ACCESSING ITEMS IN A SET 
for x in names:
    print(x)


#CHECK IF AN ITEM EXISTS IN A SET 
if "sia" in names:
    print("sia is in the set ")


#ADD ELEMENTS IN SET
names.add("mia")
print(names)


#ADD ANOTHER SEQUENCE IN A SET 
new_names={"ted","max"}
names.update(new_names)
print(names)


#REMOVING ELEMENTS FROM SET 
names.remove("john")
print(names)


#JOIN TWO SETS 
s1={'a','b','c'}
s2={'w','r','h'}
ans=s1.union(s2)
print(ans)

s1.update(s2)
print(s1)


#KEEP ONLY DUPLICATES WHILE JOINING
s1={'a','b','c'}
s2={'w','r','h','a'}
s1.intersection_update(s2)
print(s1)


#KEEP ALL VALUES EXCEPT DUPLICATES 
s1.symmetric_difference(s2)
print(s1)


#GIVEN THREE ARRAYS WE HAVE TO FIND COMMON ELEMENTS IN THREE SORTED LISTS USING SETS 
l1=[1,5,5]
l2=[3,5,4,5,10]
l3=[5,5,10,20]
s1=set(l1)
s2=set(l2)
s3=set(l3)
s=s1.intersection(s2)
final=s.intersection(s3)
final_list=list(final)
print(final_list)







