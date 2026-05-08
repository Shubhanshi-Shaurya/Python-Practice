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

#wap that asks the user to enter the number and breaks the loop if the number entered is negative 
'''while True:
    num=int(input("enter the number : "))
    if num<0:
        print("loop termination")
        break

print(num)'''

#wap that asks the user to enter a password and only allows them 3 attempts .if the password is correct , break the loop 
'''correctpass="py123"
cnt=0
while cnt<3:
    passwd=input("enter the password : ")
    if passwd==correctpass:
        print("correct password")
        break 
    else:
        print("try again")
    cnt+=1
if cnt==3:
    print("too many attempts")'''

#wap that keeps asking the user for numbers and adds them together and loops breaks if number entered is negative 
'''sum=0
while True:
    num=int(input("enter the number : "))
    if num<0:
        break
    sum=sum+num 
print(sum)'''

#wap that uses a while loop to print only odd numbers between 1 and 10 .if the number is even , skip the iteration using continue 
'''num=0
while num<10:
    num+=1
    if num%2==0:
        continue
    print(num)'''

#wap that continuously asks the user to input a number . if the user enters 0,skip the rest of the loop and ask for input again and break the loop if user enters negative number 
'''while True:
    num=int(input("enter the number : "))
    if num<0:
        break
    elif num==0:
        continue
print(num)'''

#wap that asks the user for a string and prints each character except vowels 
'''text=input("enter the string : ")
i=0
while i<len(text):
    if text[i].lower() in 'aeiou':
        i+=1
        continue
    print(text[i])
    i+=1'''

#wap that prints all numbers between 1 and 50 but skips numbers that are divisible by 5 using continue 
'''i=1
while i<51:
    if i%5==0:
        i+=1
        continue
    print(i)
    i+=1'''


    


