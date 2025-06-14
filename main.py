# Student Notes: Harvard CS50’s Introduction to Programming with Python – Full University Course

# In order to run code remove ''' from top and bottom of each section.


#CHAPTER 1 - mini gretting project + str

'''
print("Hi, World!") # We use in terminal $ code file_name.py - this help us to open existed python file or even create new.

# By writing in terninal code like $ py existed_file_name.py we can run our code even without clicking to the button "Run". Also, you can change py into python which will do same stuff.

# Dollar sign ($) i used and maybe you will see in your terminal, it is indicate prompt where you can write your code.

# Argument - is input to a function that somehow influence its behavior.

# Bugs - mistakes (Ex: print("Hello, World)) => i didn't put second " . It is example of bugs that can be happen.

# SyntaxError - mistake at keybord

'''

 #################################################################
'''
# First way of greeting name
name = input("What is your name: ") # input method or function is used to get info from user !

print(f"Hi {name}") # f"" - let us to put our veriable (name) and text together, but variable must be inside the {}.

# Variables - can store a value. Container to store value.
# Single Equal Sign means it will give its value to it.

'''
##################################################################
  
'''
# Second way of greeting name
print(f"hi, {input("Your Name: ")}") # f"" - called fstring

# Comments are notes for coder and comments will not crash the computer! In order to comment we put hash (#) then any text we want.

'''

"""
This three (") or three (') is 
used to make multiline comments

"""
#################################################################

'''
# Third way of greeting name
name = input("Name: ")
print("Hi", name)

# Forth way of greeting name
name = input("Name: ")
print("Hi " + name)

'''
#################################################################

'''
# str - means string and string is text.

# Third way - we can use two times print, but we have visual error
name = input("Name: ")
print("Hello, ")
print(name)

'''

'''
How to solve it ???
1. If we look documentation priny fucntion can eccapt several stuff except the name veriables:

print(*object, sep = " ", end = '\n'm file = sys.stdout, flush = False )

You see how many argument have print() funtion has !!!

2. Learn to read documentetion!

'''
##########################################################
'''
print(*object, sep = " ", end = '\n'm file = sys.stdout, flush = False )


*objest - means that our function can accept any number of object.

sep = " " - it is a seperator and has default velue " " which
            means that it will leave space. It is changible. That is why they are seperated by default.

end = '\n' has default value inside -> \n , which we can change.
           \n means new line, so be default this print fucntion put everything to a new line. We can change it.

'''

##################################################################

'''
# Let's solve our problem, we will change the default arguments.
name = input("Name: ")

print("Hi, ", end="") # this print will not send the next print to the next line.

print(name)

'''
##################################################################

'''
# Let's use sep and end to check

print("Hi", end="???") # Result => Hi???Smb
print("Smb")

print("Hi", "Smth", sep="???") # Result => Hi???Smth

# sep = " " and end = "\n" => both called parametres

'''

##################################################################

'''
print('hello, "friend "') # that is how we can use " " inside ' '

'''

##################################################################
'''

# Better version of greeting programm(REMOVE WHITESPACE !!!)
# Capitalize the name

# User's name
name = input("Name: ")

# Remove whitespaces
name = name.strip() # .strip() is method used to remove spaces

# Capitalize user's name
name = name.capitalize() # .capitalize is method to capitalize

# Greet user
print(f"Hello, {name}")

# Problem with .capitalize() is that it will only capitalize first letter
'''
##################################################################

'''
# How to capitalize all letters?

# We will use method called .title()


# User's name
name = input("Name: ")

# Remove whitespaces
name = name.strip() # .strip() is method used to remove spaces

# Capitalize all word of user's name
name = name.title() 

# Greet user
print(f"Hello, {name}")
'''

#################################################################

'''
# We can use two methods at the same time

# User's name
name = input("Name: ")

# Remove whitespaces and capitalize all words
name = name.strip().title()

# Greet user
print(f"Hello, {name}")

'''

##################################################################

'''
# Shorter verion 

# User's name
name = input("Name: ").strip().title()

# Greet user
print(f"Hello, {name}")

'''

##################################################################

'''
# One line verion

print(f"Hello, {input("Name: ").strip().title()}")

'''

##################################################################

'''
# From all versions the best which shows clarity and clevernes

# User's name
name = input("Name: ").strip().title()

# Greet user
print(f"Hello, {name}")

'''

##################################################################

'''
# Controling spaces between first and last name

# User's name
name = input("Name: ").strip().title()

# Manipulating space between two words
first, last = name.split() # split devide the words by the sign between "". It has by default and we can write between breackets
("anything you want to write").



# Greet user
print(f"Hello, {first}")

'''

#CHAPTER 2 - integers + calculator mini project
##################################################################

# New type integer => int - numbers (no decimals only integer)

# We can do operations like: (+, -, *, % - remainder, ** - exponent)

##################################################################

# by typing python and push in in terminal you will get interactive mode which is like you python programm to run code, but it will imediatelly run your code when you push enter.

# In order to leave interactive mode type exit()

##################################################################

'''
# If we type some numbers in input() funtion we will get text not a number. In order to solve it we must just turn it into integer by typing int()

x = input("x : ")
int_x = int(x)

# Identifying type by the type() function
print(x , "=>", type(x)) # 15 => <class 'str'>
print(int_x, "=>", type(int_x)) # 15 => <class 'int'>

##################################################################

# example:

x = input("x = ")
y = input("y = ")

print("x + y = ",x + y) # it will just combine two strings into one

print("int(x) + int(y) = ",int(x) + int(y)) # Now it will turn str into int then add it


'''
##################################################################

# if you want to run programm which has very long name type only three letter then push tab button it will automaticaly write instead of you.

##################################################################

'''
# final simple addition

# x and y choose
x = int(input("x : "))
y = int(input("y : "))

# calculating summation
z = x + y

# show result
print(z)

'''
##################################################################

'''
# FLoat - real numbers like 1.002 

print(str("1")) # result will be 1 => type is string
print(float("1")) # result will be 1.0 => type is float
print(int("1")) # result is 1 => type is integer



# x and y choose
x = float(input("x : "))
y = float(input("y : "))

# calculating summation
z = x + y

# show result
print(z)

'''
##################################################################

'''
# Rounding float number to nearst integer and take one number
# In order to do that we use round() functoin which really look like: round(number[, ndigits])

# round(number[, ndigits]) as you see here there is no asterix it means it will take only one number. Square breakets inside the parametres of the funtion means smth is optional. ndigit will help you to round it accepting how many digits after dot. If you will not include ndigits by default it will turn it into integer.

# Example: 

# By default it turn it into integer
round(3.5) # result 4
round(3.4) # result 3

# Including ndigits
round(3.141519, 2) # result is 3.14
round(3.141519, 2) # result is 3.14

'''

##################################################################

'''
# Formatting numbers
x = 1000
y = 1000000

# This x and y not readible, but we can make it 
print(f"{x:,}") # result 1,000
print(f"{y:,}") # result 1,000,000

# New trick which is same with round(number, ndigit), but different 😂.
z = 2 / 3
print(f"{z:.2f}") # used to show two float points

'''



##################################################################

'''
# Fucntions

# We use def in order to create a function

# Function which will say hello to everyone

def hello(name: str):  # Name of our function is hello 
    if type(name) == int:  # Take attribute name as name of person
        return "Please write text" # We use return as result.
    
    else:
        return f"Hello, {name.capitalize()}"
    

print(hello("aminjon")) # way to call funtion


# Also, you can not call your function before the created function!
#It will give NameError 

# If you create a fucntion it does not mean you call it!

'''

###################################################################


'''
# However, here you can call function becfore functon.
def main():
    name = input("Name: ")
    hello(name)


def hello(my_attribute = "World"):
    print(f"Hello, {my_attribute}")


main()

''' 

###################################################################

'''
# However, here you can call function becfore functon.
def main():
    name = input("Name: ")
    hello(name)


def hello():
    print(f"Hello, {name}")


main()

# Here you function can not find the name variable because of scope. You can assume the fucntion as another space which is alsways distinct from outer space that why it will not recognize name because it was created outside the funtion

# You may probably ask why in privous version of code it worked even when it is outside. Because, we previously our function could take attribut, but in this portion of code it did not 

# Terminal will give you this problem :
                                  #TypeError: hello() takes 0 positional arguments but 1 was give



# This all stuf with errors are called scope!
'''
###################################################################

'''
# Function that return square of the given number

def square():
    x = int(input("x: "))
    return f"x^2 = {x**2}"

print(square())

'''

###################################################################
'''
# CONDITIONS ( >, >=, <, <=, ==, !=)

# > - greater
# >= - greater or equal 
# < - smaller
# <= - smaller or equal to
# == - equal
# != - not equal

# if - used to compare

x = float(input("x: "))
y = float(input("y: "))

if x < y:  # If statement x < y is true then next will work!
    print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x == y:
    print("x is equal to y")

else:
    None

'''

###################################################################
'''
# We can also use 'or' and 'and' in our if statement

x = int(input("x: "))
y = int(input("y: "))

if x < y or x > y:
    print("x is not equal to y")

else:
    print("They are equal!")
#############################################
    
# Better is:

if x != y:
    print("x is not equal to y")

else:
    print("They are equal!")


    
# Even this verion is good
if x == y:
    print("x is equal to y")

else:
    print("They are not equal!")
'''


###################################################################

'''
# Grading program

score = int(input("Your Score: "))

if 90 <= score <= 100: # You can also do this way
    print("Grade: A")

elif 80 <= score < 90:
    print("Grade: B")

elif 70 <= score < 80:
    print("Grade: C")

elif 60 <= score < 70:
    print("Grade: D")

else:
    print("Grade: F")

'''

###################################################################

'''
# BETTER VERSION
# Grading program

score = int(input("Your Score: "))

if score >= 90: # You can also do this way
    print("Grade: A")

elif score >= 80:
    print("Grade: B")

elif score >= 70:
    print("Grade: C")

elif score >= 60:
    print("Grade: D")

else:
    print("Grade: F")

'''
###################################################################

'''
# Even or odd program idetifier

def even_or_odd():
    num = int(input("Number: "))

    if num % 2 == 0:
        print("Even")

    else:
        print("Odd")


even_or_odd()


'''
###################################################################

'''
# Shorter version of our programm

def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


print(even_or_odd(2))

'''

###################################################################

# Use match
'''
# We will do exact if else, but with match.
name = input("Name: ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

'''
###################################################################

'''
# shorter match way
name = input("Name: ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")

    case "Draco":
        print("Slytherin")
    
    case _:
        print("Who!?")

'''
###################################################################


########################### LOOPS #################################

'''
# while loops 

counter = 0
while counter < 10:
    print("meow")
    counter = counter + 1

'''

###################################################################

'''
# for loop
# for loop is much more powerful than while loop. for loop can be used in numbers, lists, strings and others....

for i in range(1, 11):
    print("meow", i, sep="=>")

'''
###################################################################

'''
# There minor improvement if you are creating loop in which you do not need the value you can change it into _ .

for i in range(10): # Here we do not care about i 
    print("Cat")


# So we can replace it by _
for _ in range(10):
    print("Cat")

'''

###################################################################

'''
# But we can print smth several times in other way too
print("meow\n" * 3, end="")
# It is not good if your friend can not read it.

'''

###################################################################

# Simple meow programm
'''

times = int(input("times: "))

while times < 0:
    times = int(input("Please time positive integer: "))

print("meow\n" * times, end="")

'''

'''
# Another version
while True:
    n = int(input("n: "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

'''
