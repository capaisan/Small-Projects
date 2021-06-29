"""
Quiz: Build-in Function
November 2, 2020
Tyler Decaro
24140389

"""
import math

print("--- Exercise 1: Hypotenuse ---\n")
x = int(input("Enter the valiue of x: "))
y = int(input("Enter the value of y: "))

h1 = math.pow(x, 2) + math.pow(y, 2)
h2 = math.sqrt(h1)
h2 = round(h2, 4)
print("Hypotenuse rounded off to the thousandth: %s" %(h2))
h2 = math.ceil(h2)
print("Hypotenuse rounded up the nearest integer: %s" %(h2))

print("\n--- Exercise 2: Distance ---\n")

a = (3, -6)
b = (-8, 5)

d1 = (a[0] - a[1])
d2 = math.pow(d1, 2)
d3 = (b[0] - b[1])
d4 = math.pow(d3, 2)

d5 = d2 + d4

d6 = math.sqrt(d5)

d6 = round(d6, 3)
print("Hypotenuse rounded off to the thousandth: %s" %(d6))
d6 = math.floor(d6)
print("Hypotenuse rounded down to the nearest integer: %s "%(d6))
