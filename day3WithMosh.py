import os
#if else statement
# is_hot = False
# is_cold = True
#
#
# if is_hot:
#     print("hot day drink more water")
# elif is_cold:
#     print("Cold day be warm using warm clothes")
# else:
#     print("Nice day not cold not so hot" )

#students gpa grade calculation using if else
# def grade(marks):
#     if(marks>=80):
#         return  "A+"
#     elif marks>=75 and marks<80:
#         return "A"
#     elif(marks>=70 and marks <75):
#         return "A-"
#     elif marks<70 and marks>=65:
#         return "B+"
#     elif marks<65 and marks>=60:
#         return "B"
#     elif(marks<60 and marks>=55):
#         return "B-"
#     elif (marks<55 and marks>=50):
#         return "C+"
#     elif(marks<50 and marks>=45):
#         return "C"
#     elif(marks<45 and marks>=40):
#         return "D"
#     else:
#         return "F"
#
# grd=grade(59)
# print(grd)

#logical operators

# is_pocket_full_of_money=False
#
# if(is_pocket_full_of_money):
#     print("money money money")
#
# else:
#     print("dewan er singara gayeb")

#excersice

#
# name='junayed Ahamed'
# if(len(name)<=3):
#     print("it's too short to take the name")
# elif (len(name)>=50):
#     print("name is too long")
# else:
#     print("name looks good")


# weight converter
# w=int(input("enter weight: "))
# convert_to=(input("enter conversion form pund(p) kg(k):"))
# if(convert_to=='k'):
#     print("pound to kg ",.453592*w)
# elif(convert_to=='p'):
#     print("kg to pound= ",2.20462*w)
# else:
#     print("your given notation (",convert_to,") is not a conversion form")
#     print("your given weight: ",w)

#guessing game
#using python


# import time
# import random as r
# import subprocess
#
# lis=[1,2,3,4,5,6,7,8,9,10]
#
# val=r.choice(lis)
#
# chance=1
# while chance<=3:
#     chance=chance+1
#     guss=int(input("guss the number btwn 1 to 10: "))
#     time.sleep(2)
#     if(guss==val):
#         print("Congratulation!!! you win")
#         break
#
#     print("Wrong!!")
#
# if chance>3:
#
#     print("opps!! you failled")

#taking input in list

value=0
arr=[0]
arr.clear()
for i in range(5):
     value=int(input("num: "))
     arr.append(value)

for i in range(len(arr)):
    print(arr[i],end=" ")
