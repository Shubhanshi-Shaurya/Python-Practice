#OOPS 
#it is a programming paradigm where the software design revolves around objects/data rather than functions 
#it helps to mimic real world entities and their interactions 
#code reusibility 
#organisation and maintainibility of code 


class student:
    def set_name(self,name):
        self.name=name

    def get_name(self):
        return self.name
    
student1=student()
student1.set_name("rimjhim")
print(student1.name)


#make a python class rectangle 
class rectangle:
    def set_dimensions(self,height,width):
        self.height=height
        self.width=width
    
    def area(self):
        return self.height*self.height
    
    def perimeter(self):
        return 2*(self.height+self.width)
    
#creating objects 
rectangle1=rectangle()
rectangle1.set_dimensions(10,5)
print(rectangle1.area())
print(rectangle1.perimeter())


#CLASS CONSTRUCTOR 
#special function that gets invoked every time an object is created for that class 
#used when we want to pass values at the time of initialisation 
class rectangle:

    def __init__(self,height,width):      #constructor
        self.height=height
        self.width=width

    def set_dimensions(self,height,width):
        self.height=height
        self.width=width
    
    def area(self):
        return self.height*self.height
    
    def perimeter(self):
        return 2*(self.height+self.width)
    
rectangle1=rectangle(10,5)





