#guessing game
#using python


import time
import random as r
import subprocess

lis=[1,2,3,4,5,6,7,8,9,10]

val=r.choice(lis)

chance=1
while chance<=3:
    chance=chance+1
    guss=int(input("guss the number btwn 1 to 10: "))
    time.sleep(1)
    if(guss==val):
        chance-=1
        print("Congratulation!!! you win")
        break

    print("Wrong!!")

if chance>3:

    print("opps!! you failled")