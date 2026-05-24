#QUEUE 
#WORKS ON FIFO PRINCIPLE ( FIRST IN FIRST OUT )


class queue:
    def __init__(self):
        self.values=[]
        self.front=-1
    def push(self,x):
        if self.front==-1:
            self.front=0
        self.values.append(x)
    def pop(self):
        if len(self.values)==0:
            return -1
        x=self.values[self.front]
        self.front+=1
        if self.front==len(self.values):
            self.front=-1
            self.values=[]
        return x 
    def getFront(self):
        if len(self.values)==0:
            return -1
        return self.values(self.front)
    def size(self):
        if self.front==-1:
            return 0
        return len(self.values) - self.front
    
    

#IMPLEMENTATION OF QUEUE USING LIST  
q=queue()
q.push(10)
q.push(20)
q.push(30)
q.push(40)
print(q.getFront())



