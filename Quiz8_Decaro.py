"""
Quiz 8: Recursive finction
November 16, 2020
Tyler Decaro
24140389
"""

# Exercise 1: summation

print("---exercise 1: summation---\n")


def summation(number):
    if number <= 1:
        return number
    else:
        s = number + summation(number-1)
        return s


summate = int(input("Enter a number to summate: "))
y = summation(summate)
print(y)

# Exercise 2: reverse string

print("---exercise 2: Reversed String---\n")


def rev_string(p):
    if len(p) == 0:
        return p
    else:
        return rev_string(p[1:]) + p[0]


string = input("Enter a word to reverse: ")
r = rev_string(string)
print(r)

this = input("This is just so it displays the previous function")
print(this)
