#STRINGS 
#SEQUENCE OF CHARACTERS
#IMMUTABLE 


'''name="rimjhim"
subject="physics"
#PRINTING A STRING
print(name,subject)


#PRINTING DATA TYPE 
print(type(name))
print(type(subject))'''


#MULTI LINE STRING
#name2='''hello
#world'''
#print(name2)


#ARRAY LIKE INDEXING IN STRINGS (HAVE NEGATIVE INDEXING)
name="rimjhim"
subject="physics"
print(name[2])
print(name[-3])


#TRAVERSING A STRING 
name="rimjhim" 
for i in name:
    print(i)


#USING LIST COMPREHENSION 
list=[char for char in name]
for i in list:
    print(i)


#LENGTH OF STRING 
print(len(name))


#CHARACTER/SUBSTRING IN A STRING 
print(name.find('i'))
print(name.find('jhim'))


#SLICING A STRING 
name="rimjhim"
print(name[1:5])


#creation of non empty string
s1=''
s2=""
s3=str()







