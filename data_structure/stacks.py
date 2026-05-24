from collections import deque

#STACKS 
#WORKS ON LIFO (LAST IN FIRST OUT ) PRINCIPLE 

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

#IMPLEMENTATION OF STACK USING LIST 
'''class Stack:
    def __init__(self):
        self.values=[]
    def push(self,x):
        self.values.append(x)
    def pop(self):
        if len(self.values) ==0:
            return -1
        x=self.values[-1]
        self.values.pop()
        return x 
    def top(self):
        if len(self.values) ==0:
            return -1
        return self.st[-1]
    def size(self):
        return len(self.values)'''
    

#IMPLEMENTATION OF STACKS USING LINKED LIST 
class Stack:
    def __init__(self):
        self.top=None
        self.size=0
    def push(self,x):
        if self.top==None:
            self.top=node(x)
        else:
            newNode=node(x)
            newNode.next=self.top 
            self.top=newNode
        self.size+=1
    def pop(self):
        if self.top==None:
            return -1
        x=self.top.data
        self.top=self.top.next 
        self.size-=1
        return x 
    def peek(self):
        return self.top.data
    def len(self):
        return self.size
        



#IMPLEMENTATION OF STACKS USING LISTS 
'''s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)'''
#print(s.values)
#print(s.pop())
#DISPLAY A STACK 

#IMPLEMENTATION OF STACKS USING LINKED LIST 
'''st=Stack()
st.push(5)
st.push(10)
st.push(14)
st.push(3)

print(st.len())
print(st.peek())'''





