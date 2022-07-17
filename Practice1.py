# Input Number
num1 = int(input("Enter First Number = "))
num2 = int(input("Enter Second Number = "))
sum = num1 + num2 
if(sum < 20):
    if(sum == 10):
        print("Sum = ", sum)
    else:
        print("Sum is not equal to 10")
else:
    print("Sum is less than 20 \nsum = " , sum) 
# print("Sum = " , sum)



# Write a program in which user input numbers.Find Maximum number

# firstNumber = int(float(input("Enter First Number : ")))
# secondNumber = int(float(input("Enter Second Number :")))
# thirdNumber = int(float(input("Enter Third Number : ")))
# fourhtNumber = int(float(input("Enter Fourth Number : ")))
# fifthNumber = int(float(input("Enter Fifth Number : ")))

# if firstNumber == secondNumber:
#     if secondNumber == thirdNumber:
#         if thirdNumber == fourhtNumber:
#             if fourhtNumber == fifthNumber:
#                 print("All is well !")
#             else: 
#                 print("Fourth Number not equals to Fifth Number")
#         else:
#             print("Third Number is not equals to Fourth Number")
#     else:
#         print("Second Number is not equals to Third Number")
# else:
#     print("First Number is not equals to Second Number")

# Lists


# students_list = []
# print(type(students_list))

# NumberType =34;
# print(type(NumberType))

# studentName = ["Usama" , "Sayem" ,"Tanzeel"]
# print(type(studentName))
# print(studentName[-2])

# stdmarks = [90, 56, 87, 89, 65, 89, 74]
# print(stdmarks)
# print(type(stdmarks))

# allDataTypeList = ["Python", 100, 29.6, True, stdmarks]
# print(allDataTypeList)
# print(allDataTypeList[0][2])

# allDataTypeList[0]="JAVA"
# print(len(allDataTypeList))
# newlist = [34, 45,76,89,34,23,12]
# print(newlist)

# newlist.append(input("Enter any value which you want to store in List : "))

# print(newlist)
# del newlist[2]
# print(newlist)
# country_Name = "Pakistan"
# print(country_Name[3])

# newlist.clear()
# print(newlist)

# copy_of_newlist = newlist.copy()
# print(copy_of_newlist)
# copy_of_newlist.append(100)
# copy_of_newlist.append(100)
# copy_of_newlist.append(100)
# copy_of_newlist.append(200)
# copy_of_newlist.append(200)
# copy_of_newlist.append(200)
# print(copy_of_newlist)

# print(copy_of_newlist.count(100))
# newlist.append(copy_of_newlist)
# print(newlist)
# print(len(newlist))

# newlist.extend(copy_of_newlist)

# print(newlist)
# print(len(newlist))

from ast import For, Num
from audioop import reverse
from copy import copy
import numbers
from re import A


# alist = [1,2,3]
# blist = [4,5,6]
# print("Before Extend Function")
# print(alist)
# print(blist)
# alist.extend(blist)
# print("After Using Extend Function \n",alist)
# print(alist.index(5))

# alist.clear()
# print(alist)
# alist.extend(blist)
# print(alist)
# alist.insert(0,1)
# print(alist)
# alist.insert(1,2)
# print(alist)
# alist.insert(2,3)
# print(alist)

# alist.pop()
# print(alist)
# alist.pop()
# print(alist)
# alist.pop()
# print(alist)
# alist.pop()
# print(alist)
# print(alist)
# alist.pop()
# print(alist)
# alist.pop()
# print(alist)

# names = ["Usama" , "Faraz" , "Ali", "Raza"]
# print(names)
# names.remove('Faraz')
# print(names)
# names.reverse()
# print()

# print(alist)

# Num = [1,2,3,5,2,3,6,4]
# print(Num)
# Num.reverse()
# print(Num)
# Num.sort()
# print(Num)
# Num.sort(reverse=True)
# print(Num)

# print(type(alist1))

# alist1.sort(reverse=True)

# Num = [1,2,3,5,2,3,6,4]
# print(Num)
# Num.sort()
# print("Sorted List" ,Num)
# part1 = Num[0:5]
# part2 = Num[5:]
# print(part1)
# # print(part2)

# aarr = ["Muhammad Sayem Ijaz"]
# b = aarr[8:]
# print("#"+ str(b))

# arr = ["Asad", "Usama", "Faisal","Sayem","Tanzeel"]
# print("Array = ",arr)
# print("id = ",id(arr))

# sndArr = arr
# print(sndArr)
# print(id(sndArr))
# sndArr.pop()
# print(arr)
# print(sndArr)
# newArr = arr.copy()
# print(id(newArr))
# newArr.pop()
# print(arr)
# print(newArr)

# numbers = [11,22,33,44,55,66,77,88,99,100]
# silce_Arr = numbers[3:7]
# print("Orignal Numbers = ", numbers)
# print(silce_Arr)
# print("Orignal Numbers id = ",id(numbers))
# print(id(silce_Arr))

# number_copy = numbers.copy()
# print("Copy array Numbers using .copy() function = ", number_copy)
# print("Copy array id using .copy() function = ",id(number_copy))

# number_assignment = numbers
# print("Copy of array using reference =",number_assignment)
# print("Copy of array using reference id = " , id(number_assignment))

# number_assignment[5] = 3333
# print(numbers)
# print(number_assignment)

# numbers = [11,22,33,44,55,66,77,88,99,100]
# even_Num = []
# odd_Num = []
# for i in numbers:
#     if i%2 == 0 :
#         print(f"{i} is an even Number")
#         even_Num.append(i)
#     else:
#         print(f"{i} is an odd Number")
#         odd_Num.append(i)

# print(f"Even Numbers are = {even_Num}")
# print(f"Odd Numbers are= {odd_Num}")

# even_Num = []
# odd_Num = []
# for i in range(20):
#     if i%2 == 0 :
#         print(f"{i} is an even Number")
#         even_Num.append(i)
#     else:
#         print(f"{i} is an odd Number")
#         odd_Num.append(i)

# print(f"Even Numbers are = {even_Num}")
# print(f"Odd Numbers are= {odd_Num}")

# names = "Muhammad Sayem Ijaz"
# names_list = "Muhammad Sayem Ijaz".split(' ')
# print(type(names_list))

# store values of integers from string to List

# numbers = "123435456765768231223423"
# numbers_list = numbers.split(',')
# print(numbers_list)

# a_tuple = ()
# print(type(a_tuple))

# a_set ={1,2,3,5,6,7}
# print(type(a_set))






arr = ["Sayem" , "Usama", "Tanzeel"]
#         0         1          2
# print(id(arr))
# newarr = arr.copy()
# print(newarr)
# print(id(newarr))

# sndarr =copy(arr) 
# print(sndarr)
# print(id(sndarr))



# print(arr[:])

numArr = [1,2,3,4,5,6,7,8,9,0]


# Slicing
# arr[start:end:step] by default step == 1

# print(numArr[3::2])