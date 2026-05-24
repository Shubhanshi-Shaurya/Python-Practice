#FUNCTIONS
#BLOCKS OF REUSABLE CODE THAT PERFORMS A SPECIFIC TASKS 
#TYPES - BUILT - IN , USER DEFINED 
#CREATING A FUNCTION 

#FUNCTION TO PRINT 
def printH():
    print("hello")

printH()


#FUNCTION TO FIND SUM AND RETURNS SUM 
def sum(a,b):
    ans=a+b
    return ans
print(sum(5,6))


#ARGUMENTS  - POSITIONAL ARGUMENTS,KEYWORD ARGUMENTS,DEFAULT ARGUMENTS,ARBITRARY ARGUMENTS(VARIABLE LENGTH ARGUMENTS *args AND **kwargs)
#ARBITRARY ARGUMENTS IS USED TO PASS MULTIPLE ARGUMENTS TO A FUNCTION , THEY ARE *args and **kwargs
#args ARE TUPLES 
def addAllNumbers(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print("sum of all numbers is ",addAllNumbers(2,3,4,5,8,6))


# **kwargs IS USED FOR KEYWORDED ARGUMENTS OR FOR KEY - VALUE PAIRS ARGUMENTS 
def studentInfo(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
studentInfo(name="rimjhim",age=19,city="noida")


#FUNCTION TO CALCULATE SUM FROM 1 TO N
def add(n):
    sum=0
    for i in range(1,n+1,1):
        sum+=i
    return sum
print("sum of numbers till n is ",add(11))


#NESTED FUNCTIONS - FUNCTION INSIDE FUNCTION 
def outer():
    x=1
    def inner():
        y=2
        result=x+y
        return result
    
    return inner()
output=outer()
print(output)


#CALCULATE THE FACTORIAL OF N NUMBER 
def factorial(n):
    fac=1
    for i in range(1,n+1,1):
        fac*=i
    return fac

print("factorial of the number n is ",factorial(5))





