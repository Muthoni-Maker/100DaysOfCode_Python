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