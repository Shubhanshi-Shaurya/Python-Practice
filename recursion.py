#RECURSION 
#SOLVES A PROBLEM BY DIVIDED A PROBLEM INTO SMALLER SUB PROBLEMS 


#CALCULATE FACTORIAL  OF GIVEN NUMBER 
def factorial(n):
    if n==0:
        return 1
    fac=1
    return n*factorial(n-1)

print(factorial(5))


#WAP TO PRINT NUMBERS FROM N TO 1
def printing(n):
    if n==0:
        return
    print(n)
    printing(n-1)
printing(5)


#WAP TO PRINT NUMBERS FROM 1 TO N
def printing(n):
    if n==0:
        return
    printing(n-1)
    print(n)
printing(5)


#WAP TO PRINT SUM FROM 1 TO N 
def add(n):
    if n==1:
        return 1
    return n+add(n-1)
    
print(add(5))


#WAP TO CALCULATE A RAISED TO THE POWER B 
def power(a,b):
    if b==0:
        return 1
    return a*power(a,b-1)

print(power(2,3))


#WAP WHICH CALCULATES FIBONACCI SEQUENCE 
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
for i in range(1,8,1):
    print(fibonacci(i))




