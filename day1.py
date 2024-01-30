# name=input("enter name ")
#
#
# age=int(input('enter age'))
#
# fav_color=input("enter favourite color name: ")
# print("hi i am "+name)
# print("i like "+fav_color+" color")
# print("my age ",age)

#age calculation

# birth_year=int (input("enter birth year: "))
# age=2023-birth_year
# print(age)

#kilo to pound

# weight=int(input("enter weight in kilo : "))
#
# in_pound=weight*2.20462
# print(in_pound)


#string

# description=("'junayed ahamed ,i am 20 yr's old'"
#
#              ' i am the student of diu in BSc in comp.') # if you want an apstop(') in string then use double cote("") in string
# print(description)



#for an multiple separate line we gonna  use triple coute('''dhhdhh ''')
#example

# email='''
# hi junayed,
#
# welcome to the  python programming,
# thenk you juna
#
#
# '''
#
# print(email)


#getting character from string

#
# course='hello everyone wellcome here'
#
# print(course[0]) #getting first char
#
# print(course[-1]) #getting chracter from last
#
# #getting string's from  index (x to y)
#
# print(course[6:14]) #we will get the char as string from index 6 to 13 (space are aslo count as part of string
#
# print(course[2:]) #for this case we get all the string except first 2 character
# print(course[:10]) #for this case we get all the string before char index 10
#
# #string copying
# hello=course [:] #by using this squere bracket  here in two gap first take 0 index and last take the length of string [0:course.length]
# print(hello)

#practice
# name='junayed'
# last='ahamed'
# print(name[1:-1])#we will get the value from  index 1 to brefore index -1 ---- [start index: end index]
#
#
# message= name+' ['+last+'] is a coder' #not ideal
# print(message)
#
# msg=f'{name} [{last}] is a coder' #this to {} is called placeholder
# print(msg)

#string method


# course="Hello evEryone Welcome "
# name="junayed"
# #
# # print(len(course))#this show's the length of string
# # print(course.upper()) #this will make all char of string in upper case but it cann't mske modify string
# # print(course.lower()) #this will make all char of string in lower case  but it cann't mske modify string
# #
# # print(course.find('e'))#it will find the first occurance index of 'e'
# # print(course.find("Welcome"))#it will show the starting index of welcome
# print(course.replace("Welcome","bye"))#this will replace welcome as bye
#
# print(course.replace('H','G'))#this will replace 'H' as 'G'
#
# print('Hello'in course)#this will return a boolean is there has the specific string or not
# print("junayed" in course)#it will return false
#
# hi=f'{course}[{name}]'
# print(hi)
#
# print(name.find("yed"))

