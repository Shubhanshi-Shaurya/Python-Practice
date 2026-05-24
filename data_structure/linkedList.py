#LINKED LIST 
#NODE CLASS MAKING 

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printI(head):
    temp=head
    while temp is not None:
        print(temp.data)
        temp=temp.next

def printR(head):
    temp=head
    if temp is None:
        return 
    print(temp.data)
    printR(temp.next)

def nthnode(head,n):
    fast=head
    slow = head
    for i in range (1,n+1,1):
        fast=fast.next
    while fast is not None:
        fast=fast.next
        slow=slow.next
    return slow

def deleteNth(head,n):
    fast=head
    slow=head
    for i in range (1,n+1,1):
        fast=fast.next
    while fast.next is not None:
        slow=slow.next
        fast=fast.next
    slow.next=slow.next.next

def cycleDetect(head):
    fast=head
    slow= head 
    while fast is not None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            return True
    return False

def cycleNode(head):
    fast=head 
    slow=head
    while fast is not None:
        fast=fast.next.next
        slow=slow.next
        if fast==slow:
            break
        else:
            return
    temp=head
    while temp is not slow:
        temp=temp.next
        slow=slow.next
    return temp

def size(head):
    temp=head
    count=0
    while temp is not None:
        temp=temp.next
        count+=1
    return count

def intersectionLL(head1,head2):
    temp1=head1
    temp2=head2
    s1=size(temp1)
    s2=size(temp2)
    if s1>s2:
        for i in range (1,s1-s2+1,1):
            temp1=temp1.next
    else:
        for i in range (1,s2-s1+1,1):
            temp2=temp2.next
    while temp1 is not None:
        if temp1.data==temp2.data:
            return True
        temp1=temp1.next
        temp2=temp2.next
    return False

def middleElement(head):
    fast=head
    slow = head 
    while fast is not None and fast.next is not None:
        fast=fast.next.next
        slow=slow.next
    return slow 

def deleteMiddle(head):
    fast=head.next 
    slow = head 
    while fast.next is not None and fast.next.next:
        fast=fast.next.next
        slow=slow.next
    slow.next=slow.next.next

def removeDuplicates(head):
    if head is None:
        return
    temp=head
    while temp is not None and temp.next is not None:
        if temp.next.data==temp.data:
            temp.next=temp.next.next
        if temp.next is None:
            return
        if temp.next.data!=temp.data:
            temp=temp.next





#IMPLEMENTATION OF LINKED LIST 
#CREATING NODES 
a=node(10)
b=node(20)
c=node(30)
d=node(40)
e=node(50)
f=node(60)

#CONNECTING NODES 
a.next=b
b.next=c
c.next=d
d.next=e
e.next=f

#ACCESSING NODE DATA 
'''print(b.data)
print(e.next.data)'''

#PRINTING LINKED LIST 
#USING ITERATION 
#printI(a)
#USING RECURSION 
#printR(a)


#SIZE OF LINKED LIST 
#print(size(a))

#FINDING NTH NODE FROM THE END OF THE LIST IN ONE TRAVERSAL 
#ans=nthnode(a,3)
#print(ans.data)

#REMOVING NTH NODE FROM END IN ONE TRAVERSAL 
#deleteNth(a,3)
#printI(a)
#CYCLE IN A LINKED LIST 
#print(cycleDetect(a))

#NODE AT WHICH CYCLE STARTS IN THE LINKED LIST 
#ans=cycleNode(a)

#INTERSECTION OF TWO LINKED LIST 
'''x=node(103)
y=node(50)
x.next=y
y.next=b 
print(intersectionLL(a,x))'''

#FINDING MIDDLE ELEMENT IN A LINKED LIST 
#ans=middleElement(a)
#print(ans.data)

#DELETING MIDDLE ELEMENT IN A LINKED LIST 
#deleteMiddle(a)
#printI(a)

#REMOVING DUPLICATES FROM A LINKED LIST 
#removeDuplicates(a)





    
    