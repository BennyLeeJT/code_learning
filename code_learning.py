# line 1
# line 2
# line 3
print("am i on mars?")
print("""this is a really really really really
long long long loong looong looooog line of code dave""")

x = 100

def f():
    # without this, print(y) will fail because its not accessible outside function f
    # global y
    # y = 200
    global x
    x += 1
    print(x)
    

f()
# because its global, the print(x) will still work outside the function f
print(x)

# this will fail because y is encapsulated in function f, so its scope is there and not global
# y must be global for this to work
# print(y)


# if we do this, we face the problem of user inputting 0. so we want to control what the user inputs.
# a = input("type a number : ")
# b = input("type another number : ")
# must be integers, not strings, else runtime error
# a = int(a)
# b = int(b)
# print(a/b)

# let's try to catch the exception
a = input("type a number : ")
b = input("type another number : ")
a = int(a)
b = int(b)

try:
    print(a/b)

except ZeroDivisionError:
    print("2nd input cannot be zero. Try again.")
# this will not stop the program and will move to the next line.

# print(a/b) #test if it will run this. it did, so with try and except, it will not stop the program from running after an exception at the try part.
# it will just execute whatever code after that

# this is a string literal. trying to produce a docstring
'''
multi
lines
for
humans
to
read
'''


def square(n):
    '''Takes in a number n, returns the square of n'''
    return n**2

print(square.__doc__)


# Chapter 5. Containers
''' container here is a generic term to mean the data structure / data type to store information
such as arrays. but python doesn't use the term array.
Python has Lists, Tuples and Dictionaries '''

my_list = list(("Apple", "Orange", "Pear"))
my_list2 = ["Apple", "Orange", "Pear"]
print(my_list)
my_list.append("Banana")
print(my_list)

color_list = ["blue", "green", "yellow"]
print(color_list)
print(color_list[2])

color_list[2] = "red"
print(color_list)

color_list.pop()
print(color_list)

print("black" not in color_list)
print("green" not in color_list)
print("green" in color_list)

print(len(color_list))

new_list = ['Apple', 'Orange', 'Pear', 'Banana', 'Peach']
new_list[0:3]
print(new_list)

