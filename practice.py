# print(25//5)
from ast import While
from math import radians
from pickle import DICT
import readline
from traceback import print_tb
from typing import Dict


tuple_1 = (1,(3,5,6.7),78,0,(23,56),2)
# print(tuple_1[1][1])
# print(tuple_1[0])
A = [1,3,4,5,7]
A.append(["a", "b"])
# print(A[5][1])
# help(A)
# B = A[:]
B = A
B[2] = "Muhammad Sayem Ijaz"
# print(A[2])
Sp = B[2].split("1")
# print(Sp)
set_A = {"Muhammad", "Sayem", "Ijaz", 190, 1890 , 22}
set_B = {"Muhammad", "Sayem", "Ijaz"}
# print(set_B.issubset(set_A))
DICT = {"Name" : 'Muhammad Sayem Ijaz', "Roll_No" : "bsf1901890" , "Class" : "BSIT", "Semester" : 6}
# print(DICT.keys(),DICT.values())
ABC = {"Name" : "Muhammad Sayem Ijaz" , "Roll" : 12345 , "D": (4,4,4)}
# print(ABC["D"])
# i= 10000000
# print(i!=0)
# print(A)
# for element in enumerate(A):
#     print(element)
# b = [3,4,5]
# for a in b:
#         print(a)
# x= 3
# y =1 
# while(x!=y):
#     print(y)
#     y=y+1

# a = [1,5,7,3,6,8,2]
# print("a =" , a)
# # b = sorted(a)
# a.sort()
# print("a after =" , a)

# def Mul(name):
#     print(name)
#     return name
# c =  Mul("Muhammad Sayem ijaz")
# print(c)

# class Circle():
#     def __init__(self , radius , color):
#         self.radius = radius
#         self.color = color

# RedCircle = Circle(10,"red")
# YellowCircle = Circle(12,"Yellow")
# BlueCircle = Circle(67,"Blue")
# print(RedCircle.color , RedCircle.radius)
# print(YellowCircle.color , YellowCircle.radius)
# print(BlueCircle.color , BlueCircle.radius)

# class Person():
#     def __init__(self, name, gender, cnic, contact):
#         self.name = name
#         self.gender = gender
#         self.cnic = cnic 
#         self.contact = contact
#     def walk(self):
#         print(f"{self.name} is walking")

# Person1 = Person(name = "Muhammad Sayem Ijaz",gender ="Male",cnic = 12345 ,contact = 452341)
# print(Person1.name)
# print(Person1.gender)
# print(Person1.cnic)
# print(Person1.contact)

# A12 = ['1','2','3']
# for a in A12:
#     print(2*a)

# def Delta(x):
#     if x==0:
#         y=1
#     else:  
#         y=0
    
#     return(y)

# print(Delta(1))

# class Person:
#     "This is a person class which is used for Person Information"
#     age = 10

#     def greet(self):
#         print('Hello')


# # Output: 10
# print(Person.age)

# # Output: <function Person.greet>
# print(Person.greet)

# # Output: "This is a person class"
# print(Person.__doc__)

# ABC = [1,3,4,5,6,7]

# for i in ABC:
#     print(ABC[i])

# Read files 

# with open("Example01.txt", "r") as File1:
#     # fileTitle = File1.readlines(16);
#     # print(fileTitle)
#     fileTitle = File1.readlines();
#     print(fileTitle)
