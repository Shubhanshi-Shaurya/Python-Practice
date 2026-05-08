from functools import reduce
import time
import argparse

#MISCELLANEOUS FUNCTION IN PYTHON 
#LAMBDA FUNCTION 
#LAMBDA FUNCTIONS ARE SMALL,ANONYMOUS FUNCTIONS DEFINED USING lambda KEYWORD 

double =lambda x:x*2
print(double(5))
cube= lambda x:x*x*x 
print(cube(3))
#CAN TAKE MULTIPLE VALUES
avg=lambda x,y:(x+y)/2
print(avg(4,2))


#MAP , FILTER AND REDUCE FUNCTIONS 

def cube(x):
    return x*x*x

#MAP FUNCTION RETURNS A CLASS AND IT IS USED TO SIMPLIFY AN ITERATION PROCESS
l=[1,2,4,6,4,3]
newl=list(map(lambda x:x*x*x,l))      #passing lambda function as argument
print(newl)


#FILTER FUNCTION FILTERS ELEMENTS FROM LIST WHICH QUALIFY THE CRITERIA PASSED IN FILTER FUNCTION AND IT ALSO RETURNS A CLASS 

def filter_func(a):
    return a>4

lis=list(filter(lambda a:a>4,l))
print(lis)


#REDUCE FUNCTION DO THE OPERATION PASSED AS AN ARGUMENT ON THE LIST 
numbers=[1,2,3,4,5]
sum=reduce(lambda x,y:x+y,numbers)
print(sum)


#EXCEPTION HANDLING 
a=input("enter the number : ")
try:
    for i in range(1,11):
        print(int(a)*i)
except Exception as e:
    print(e)
print("some important lines of code")
print("new code") 


#CUSTOM ERRORS 
a=int(input("enter any value between 5 and 9 :"))
if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")


#TIME MODULE 
#time.time() FUNCTION CALCULATES THE TIME TAKEN BY A PROGRAM TO RUN 
def usingWhile():
    i=0
    while(i<5000):
        i=i+1
        print(i)

def usinfFor():
    for i in range(5000):
        print(i)

init=time.time()
usinfFor()
print(time.time()-init)
init=time.time()
usingWhile()
print(time.time()-init)


#TIME SLEEP 
print(4)
time.sleep(3)
print("this is printed after 3 sec")


#TIME LOCAL TIME 
#IT SHOWS LOCAL TIME 
t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H-%M-%S",t)

print(formatted_time)


#COMMAND LINE UTILITY 









