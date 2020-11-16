"""DAY 10-20 OF 100 DAYS OF CODE"""
"""This file contains python challenges that consists of questions that will help me understand python basics"""
"""QUIZ1:Write a Python program to display the current date and time."""
import datetime
currentDate=datetime.datetime..now()
currentTime=datetime.time()
print(currentDate)
print(currentTime)

"""QUIZ2: Write a Python program which accepts the radius of a circle from the user and compute the area."""
import math
from math import pi
radius=eval(input("Enter measurements:"))
area_of_a_circle=pi*(radius*radius)
print(area_of_a_circle)

"""QUIZ3:Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them. """
FirstName=input("Enter First Name:")
SecondName=input("Enter SecondName:")
BothNames=FirstName+"\t"+SecondName
print(BothNames)
reverse=BothNames[ : :-1]
print(reverse)

"""QUIZ4: Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers"""
Numbers=list(eval(input("Enter numbers:")))
print(Numbers)
print(tuple(Numbers))

"""QUIZ5:Write a Python program to accept a filename from the user and print the extension of that"""
fileName=input("Enter a file name:")
New_list=list(fileName.split("."))
print(New_list)
a=New_list[1]
print(a)
print(fileName)


"""QUIZ6:Write a Python program to display the first and last colors from the following list,color_list = ["Red","Green","White" ,"Black"]"""
Color_list=["RED","GREEN","WHITE","BLACK"]
first_color=Color_list[0]
last_color=Color_list[-1]
print(first_color+","+last_color)

"""QUIZ7: Write a Python program to display the examination schedule. (extract the date from exam_st_date),exam_st_date = (11, 12, 2014)"""
exam_st_date=(11,12,2014)
transform_to_list=list(exam_st_date)
print(transform_to_list)
print(transform_to_list[0])

"""QUIZ8: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. """

"""QUIZ9:Write a Python program to print the calendar of a given month and year."""
import calendar

yy=2020
month=11
print(calendar.month(yy,month))



