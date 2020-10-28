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
	
#Day 3
#Python Data types
"""Numbers
     Floats
     Strings
     Booleans
     """
a=10
print(a)
b=10.789
print(b)
name="Ann"
print(name)
 
 #Day 4
 #For loop
d="Kenya"
for i in d:
  print(i)
 
 #While loop
f=10
while f<=1:
 	print(f)
 	
 #Day 5
 #Type casting
 #Changing of data types in python
number=10
print(str(number))

letter="200"
print(int(letter))
print(float(letter))

one=1
print(bool(one))

#Strings
#Strings in python are written in quotation marks

sentence="My name is Aoko"
print(sentence)

#String Methods
print(sentence.capitalize())
print(sentence.upper())
print(sentence.lower())
print(sentence.casefold())
print(sentence.islower())
print(sentence.isupper())

#String Concatination
sentence2="I love singing"
concatinate=sentence+sentence2
print(concatinate)

#String repetition
print(sentence*2)

#String Indexing
#String indices must be intergers
print(sentence[0])
print(sentence[-1])
print(sentence[6])

#String slicing
print(sentence[0:-1])
print(sentence[ : ])
print(sentence[1::1]) #Strides
print(sentence[::-1])

#String Formatting
school="Moi Forces Cademy"
year=2020
statement="My school is called"+school+"{}".format(year)
print (statement)

#Day6
#List In Python
schools=["Kenya","Moi","Karima"]
print(schools)
for n in schools:
	print(n)
print(schools[2])
print(schools[0:2])
schools[0]="Kabarak"
print(schools)

#List methods
schools.append("Naivasha")
print(schools)
schools.sort()
print(schools)
schools.reverse()
print(schools)

#List concatination
schools2=["Njabini Boys","Bishop Gatimu"]
add=schools+schools2
print(add)
print(schools*2)

#Tuples