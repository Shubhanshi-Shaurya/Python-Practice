#DICTIONARY 
#STORES KEY VALUE PAIR 
#ORDERED
#CHANGEABLE
#UNINDEXED
#DUPLICATES NOT ALLOWED
#ANY DATATYPE 


phone={
    "ria":56478,
    "john":79831,
    "max":12875
}


#PRINTING A DICTIONARY 
print(phone)


#LENGTH OF A DICTIONARY 
print(len(phone))


#PRINTING DATA TYPE 
print(type(phone))


#ACCESSING ELEMENTS OF A DICTIONARY 
print(phone["john"])
print(phone.get("john"))
print(phone.keys())


#UPDATING VALUE IN A DICTIONARY 
phone["john"]=234587
print(phone)


#ADD ELEMENTS IN A DICTIONARY 
phone["sam"]=287591
print(phone)


#ADD ANOTHER SEQUENCE 
more_phone={
    "tia":540978
}
phone.update(more_phone)
print(phone)


#REMOVE ELEMENTS FROM A DICTIONARY 
phone.pop("ria")
print(phone)
phone.popitem()      #remove last item 
print(phone)
phone.clear()
print(phone)


#PRINTING VALUES OF A DICTIONARY 
for x in phone:
    print(x)

for x in phone:
    print(phone[x])

for x in phone.items():
    print(x)


#NESTED DICTIONARY 
phone={
    "area1":{
        "x":0,
        "y":1,
        "z":2
    },
    "area2":{
        "a":3,
        "b":4,
        "c":5
    }
}
print(phone["area1"]["y"])
print(phone["area2"]["c"])


#WAP TO FIND THE SUM OF ALL ITEMS IN THE DICTIONARY
numbers={
    'a':100,
    'b':200,
    'c':300
}
print(sum(numbers.values()))

#GIVEN A STRING AND A NUMBER N , WE NEED TO MIRROR THE CHARACTERS FROM THE NTH POSITION UP TO THE LENGTH OF THE STRING IN ALPHABETICAL ORDER . IN MIRROR OPERATION , WE CHANGE 'A' TO 'Z','B' TO 'Y' AND SO ON 








