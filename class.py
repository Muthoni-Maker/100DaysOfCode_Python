"""Class in Python
Python is an object oriented programming language
Almost Everything in python is an object
Objects have properties and values
A class in any object oriented language is like a blue printor 
or a constractor for creating objects.print.
Class in python is defined by the keyword class
A class identifier is written in capital letters
"""
class HumanBeing:
  age=10
  height='1 meter'
  print('the height of this girl is '+','+height +','+'her age is {}'.format(age))

HumanBeing()

class Person:
  def __init__(self,name,age,height):
    self.age=age
    self.name=name
    self.height=height
  
  def sing(self):
    print("The person named "+self.name+","+"is of age{}".format(self.age))

Person1=Person("Ann",10,10.5)
Person2=Person("Kamau",34,100.8)
print(Person1.name)
print(Person1.age)
print(Person1.height)
print(Person2.name)
print(Person2.age)
print(Person2.height)
print(Person2.sing())

"""Class Inheritance
   To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class
"""

class Car:
  def __init__(self,model,size,color,price):
    self.model=model
    self.size=size
    self.color=color
    self.price=price

  def speed(self):

    print("The car of color red covered a distance of one kilometer at a speed of wind")

class Subaru(Car):
  pass

class Subaru2(Car):
  def __init__(self,model,size,color,price,distance,wheels):
    Car.__init__(self,model,size,color,price)
    self.distance=1800
    self.wheels=wheels

     



  
car1=Car("BMW","SMALL","BLACK",100000)
print(car1.speed())
print(car1.model)
car2=Subaru("Toyota","Big","Red",200000000)
print(car2.speed())
print(car2.model)
car3=Subaru2("Toyota","Small","Yellow",450000,180,9)
print(car3.distance)
print(car3.speed())
print(car3.wheels)

  
                      