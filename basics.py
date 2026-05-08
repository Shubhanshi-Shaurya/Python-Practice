from datetime import date


#BASICS 
'''print("hello coder")
print("this is your \nconsole")  #\n for next line 
name="rimjhim"
x=5


#PRINT DATA TYPE OF ANY VARIABLE 
print(type(name))
print(type(x))


#TAKING INPUT 
#by default input in python is of string data type 
y=int(input("enter the valus of y : "))
print(x+y)


#OPERATIONS 
a=int(input("enter number 1 : "))
b=int(input("enter number 2 : "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)       #floor division 
print(a**b)       #exponentiation '''


#CONDITIONALS 

#POSITIVE OR NEGATIVE NUMBER 
'''x=int(input("enter x : "))
if x>=0:
    print("the number is positive ")
else :
    print("the number is negative ")'''


#EVEN OR ODD NUMBER 
'''x=int(input("enter the number : "))
if x%2==0:
    print("the number is even ")
else:
    print("the number is odd ")'''


#DETERMINE PROFIT OR LOSS 
'''sell=int(input("enter the selling price : "))
cost=int(input("enter the cost price : "))
x=sell-cost
if x>0:
    print("the seller made o profit of : ",x)
elif x<0:
    print("the seller incurred loss of : ",x)
else:
    print("the seller neither made a profit nor incurred a loss")'''


#MATCH CASE 
#CALCULATOR 
'''a=int(input("enter number 1 : "))
b=int(input("enter number 2 : "))
oprt=input("enter the operator : ")
match oprt:
    case"+":
        print("the sum is : ",a+b)
    case"-":
        print("the difference is : ",a-b)
    case"*":
        print("the product is : ",a*b)
    case"/":
        print("the quotient is : ",a/b)
    case _ :
        print("invalid operator ")'''


#TERNARY OPERATOR 
'''n=int(input("enter the number : "))
x="even number" if n%2==0 else "odd number"
print(x)'''


#wap to compute n+nn+nnn for input n
# n=int(input("enter the no. : "))
# print(n+n*n+n*n*n)

#wap to count a no. in list
# numbers=[1,4,6,4,8,4,9]
# y=numbers.count(4)
# print(y)

#wap to calculate no. of days between two dates
# first=date(2025,12,14)
# last=date(2026,1,11)
# print(last-first)







