"""
Quiz User Defined Function
November 4, 2020
Tyler Decaro
24140389
"""
import math
import random


def circleArea():
    print("-- Exercise 1 --")
    r = int(input("Enter a radius: " ))
    while r <= 0:
        r = int(input("Error: Enter a radius that is greater than 0: " ))
    a = math.pi * (math.pow(r, 2))
    a = round(a, 2)

    print("Circle with radius %s has an area of %s"%(r, a))


circleArea()

def rand():
    print("-- Exercise 2 --")
    num = int(input("Enter a number of rolls: "))
    while num <=0 or num >=21:
        num = int(input("Error: Enter a number of rolls between 1 and 20 inclusive: "))

    for i in range(num):
        ra = random.randint(1,6)
        i+=1
        print("Round %s = %s" %(i, ra))

rand()