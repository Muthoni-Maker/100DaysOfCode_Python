#Python Introduction
#Python is a high level programming language
#Python is a case sensitive programming language
#Python is an object-Oriented programming language
#Can be used in web development,automation etc
#Python uses indentation to show blocks of code

#Day1

#Variables
#Variables are  named values/memory location for 
#storing data.
#Variables naming-Allows letters,numbers and underscores,uses camel case,does not allow use of reserved words
#types of variables-metasyntactic

a=12
b=24
c=a+b
print(c)
d="Kenya"
print(d)

#Functions
#A function is a block of code written to perform a certain task
#In python,function is declared using the def keyword

def name():
	school="Kenya High"
	print(school)
	
name()

def name(n):  #Arguments
	print(n)
	
g=name("Akinyi")  #keyword Arguments
print(g)

def name(n="Atieno"):
	print(n)
	
name()

#Arguments in python
#Five types of python arguments
#1:Default Arguments/non-default arguments
#2:Positional arguments
#3:Keyword arguments
#4:Arbitrary positional arguments
#5:Arbitrary keyword arguments

#Day 2
#If else statement
car="BMW"
car2="Benz"
if car =="BMW" and car2=="Toyota":
	print("Good stuff")
else:
	print("Above average")
	
student_one="Anne"
student_marks=20
student_class="Emerald"
if student_one =="Aoko":
	print("Present")
elif student_one =="Anne":
	print("Not present")
	
else:
	print("Not a member")
