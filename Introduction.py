#Python Introduction
#Python is a high level programming language
#Python is a case sensitive programming language
#Python is an object-Oriented programming language
#Can be used in web development,automation etc
#Python uses indentation to show blocks of code
"""Different flavours of python-CPython,Canopy,Jython,IronPython,PyPy,Anaconda,IPython"""

#Day1

#Variables
#Variables are  named values/memory location for 
#storing data.
#Variables naming-Allows letters,numbers and underscores,uses camel case,does not allow use of reserved words
#types of variables-metasyntactic
                """-local variables
                   -global variables"""

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

#Tuples
#Tuples are python data structures that allows datasets to be stored inside paranthesis.Data in tuples is  organised.Tuples are mutable.


names=("Ivy","Aaron","Mike","Nancy")
print(names)
print(names[0])
for b in names:
	print(b)


###Day 7
#Set
#Sets in python are created inside curley brackets
#Sets are not ordered thus cannot be indexed.
#Sets do not allow duplicates
food={"Sushi","Ugali","Mayai"}
print(food)
for l in food:
	print(l)
	
#Dictionaries
#Dictionaries in python allows data to be stored in key value pairs.
"""A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
   You can access the items of a dictionary by referring to its key name, inside square brackets:
   There is also a method called get() that will give you the same result

"""
student={"Name":"Maker","Age":20,"school":"JKUAT"}
name=student.get("Name")
print(name)
print(student.get("Age"))

"""When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
   You can use the values() method to return values of a dictionary
   Loop through both keys and values, by using the items() method
"""
dict={"name":"Ivy","age":24,"schools":"Kabete"}
print(dict)
print(dict.get("age"))

for i in dict:
  print(i)

x=dict["name"]
print(x)

dict["age"]=20
print(dict)

for x in dict.keys():
  print(x)
for y in dict.values():
  print(y)

for x,y in dict.items():
  print(x,y)

	
