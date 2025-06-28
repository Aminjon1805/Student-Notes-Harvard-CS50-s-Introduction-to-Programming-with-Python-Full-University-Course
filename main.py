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
###################################################################
# Funcitons for asking how many times to meow
'''
def meow():
    times = int(input("Type times: "))
    while times < 0:
        times = int(input("Please type positive integer: "))

    for _ in range(times): # print("meow\n") * times, end="") 
        print("meow!!!") 

        
meow()
'''
###################################################################

'''
# Another type

def meow(times):
    while times < 0:
        print("Please type positive integer")
        break
    
    for _ in range(times):
        print("meow")

meow(10)

# We can also change our while to if, you can try by yourself

'''

###################################################################

# You know all this code is hard to understand let's make it clear

# First we will split our question into parts:
'''
    1) Get number from user and check whether it is positive or negative => funciton for getting and checking correctness

    2) Second fucntion will use that number to print meow

    3) Third fucntion is combintion of this two functions

# This is needed because as prorammer you are responsible make your code easier to understand for your coworkers and also it will make your job easier for debugging.

'''

# Result
'''

# Main fucntion
def main():
    number = get_number()
    meow(number)


# Get number from user and check
def get_number():
    while True:
        n = int(input("How many times: "))
        if n > 0:
            break

    return n


# Meow n times
def meow(n):
    for _ in range(n):
        print("meow!!!")


# Call function
main()

'''
###################################################################

'''
# List is colection of elements which is ordered by index, which starts from zero. [elem_1, elem_2, ...., elem_n] - this way creating list.

list_of_std = ["Harry", "Zuko", "Avatar"]
#                |        |        |
#                0        1        2   They are ordered this way



# If you want to call any of them you will use indexes
print(list_of_std[0]) # I called Harry
print(list_of_std[1]) # Zuko
print(list_of_std[2]) # Avatar

'''

###################################################################

'''
# We can call them by for loop
list_of_std = ["Harry", "Zuko", "Avatar"]

for std in list_of_std: # we use range() only for integers
    print(std)

'''

###################################################################

'''
# len(name_of_list or string) gonna show lenghth of it

print(len([1, 2, 3, 4])) # length of this list is 4
print(len("smth")) # length of this string is 4

'''

###################################################################

'''
# Experimanting with for loop and lists

list_of_std = ["Harry", "Zuko", "Avatar"]

for i in range(len(list_of_std)):
    print(i + 1, list_of_std[i], sep=") ")

# Output

# 1) Harry
# 2) Zuko
# 3) Avatar

'''
###################################################################

# In for loop - range(a, b, c) take three value
# a - begin with, by default it is 0. We can change it
# b - end point , where our loop gonna finish. Typed by user
# c - is jumping , by default it is 1. We can change it

###################################################################

'''
# Dictionary - key and value. Denoted by {}

# Suppose you must manage who is in which house in 

# {key: value}
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Draco"]) # from dictionry called student give my value of the key called "Draco"

print(students["Harry"]) # from dictionry called student give my value of the key called "Harry"

'''
###################################################################

"""
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

'''
# How to get all keys
for student in students:
    print(student)

'''

'''
# How to get all values
for student in students:
    print(students[student])
'''


'''
# How to get key and value
for student in students:
    print(student, students[student], sep=' => ')
    
'''

'''
# Better way to get key and value
for k, v in students.items(): # Items() help to get key and value
    print(k, v, sep=" => ")

'''
"""

###################################################################

"""
# What happens when we put method items() in dict

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}


print(students.items())
# result: dict_items([('Hermione', 'Gryffindor'), ('Harry', 'Gryffindor'), ('Ron', 'Gryffindor'), ('Draco', 'Slytherin')])


# So python will create list in which each key and value in tuple in the list.
"""

###################################################################

# None - absence of the value

###################################################################

"""
# If except of key and value you also have another value, how to organize them ???

students = [
    {"name": "Harry", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Hermione", "house": "Gryffindor", "patronus":"Stug"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Smth"},
    {"name": "Draco", "house": "Slytherin", "patronus": "Evil"}
]

'''
print(students[0]["name"]) # Harry
print(students[1]["name"]) # Hermione
print(students[2]["name"]) # Ron
print(students[3]["name"]) # Draco

'''

'''
for student in students:
    print(student["name"], student["house"], student["patronus"],sep=', ')
    
'''

"""

###################################################################

# Creating squares through loop
'''
def main():
    num = user_num()
    make_square(num)

def make_square(n):
    for _ in range(n):
        print("#" * n)

def user_num():
    number = int(input("Type number: "))
    return number

main()

'''

'''
# Creating squares through loop inside loop

def main():
    user_size = get_size()
    print_square(user_size)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end=" ")
        print()


def get_size():
    number = int(input("Size: "))

    return number

main()

'''
##################################################################

# try and except used to hendle your error

# For example in this portion of code it cause an error:
# number = int(input("Typy number: "))
# print(number)
# Error: 



'''
# In order to handle it as we said we use try except:

try:
    number = int(input("Integer: "))
    print(number)

except ValueError:
    print("Please type integer!")


'''

##################################################################

# SyntaxError cannot be solved through try except mathod. It is like you didn't close breakets. You fix it in code by filling needed things

# What about other errors like runtime error, this errors occure when user type smth that is not allowed which can broke you code, then you must handle every situations that can broke whole system.

##################################################################

'''
# In order to catch specific error error you must include name of the error, but if you want to catch any of them that can happen you can just write except without name of error.

try:
    number = int(input("Integer: "))
    print(number)

except :
    print("Please type integer!")

'''

##################################################################

'''
# Lets move print(number) beyound the try axcept
try:
    number = int(input("Integer: "))
    
except:
    print("Please type integer!")

print(number)

# After doing it we will see (NameError: name 'number' is not defined) which says that i can not find number even there is number. Because when error happens it do not give any value to number it goes to except block also do not give any value to our numbers that why our code do not know what is number.

'''

'''
# How to solve put else

try:
    number = int(input("Integer: "))
    
except:
    print("Please type integer!")

else:
    print(number)

# If there gonna be no error our code go directly to else block.

'''

##################################################################

'''
# Let's check for being true again and again

while True:
    try:
        number = int(input("Type number: "))

    except:
        print("Please type number!")
    
    else:
        print("number", number, sep=" is ")
        break

'''
##################################################################

'''
# pass - if you want to ignore smth you can pass it by pass

while True:
    try:
        number = int(input("Type number: "))
        print(number)
        break
    except:
        pass

'''

##################################################################

# Create funciton for the asking number

'''
def get_int():
    while True:
        try:
            return int(input("Type number: "))
        except:
            pass

print(get_int())

'''

##################################################################

# Prompt - where I will start tommorow. (4h 49m)

# When we use we do not need input function in order to ask user

'''
def main():
    x = get_int("What is x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            pass

main()

'''
##################################################################

# Labraries, modules - used in order to reuse code 

# When you install python interpreter you automatically will get some modules and in order to use them you can import them by import. You can not get them like print() or other stuff, you can get them by importing.

'''
# Example coint flip
import random # I import random from default files in python

choice = random.choice(["heads", "tails"])

print(choice)

'''

##################################################################

# Check how many times does it appear
'''
import random

head_count = 0
tail_count = 0

counter = 0
limit = 2000

while counter <= limit:
    if random.choice(["head", "tail"]) == "tail":
        tail_count += 1
    
    else:
        head_count += 1
    
    counter += 1
    

print(f"Head count = {head_count} = {head_count/ limit}",
       f"Tail count = {tail_count} = {tail_count/ limit}",head_count / tail_count ,sep="\n")

'''

##################################################################

# When I write import random, I import everything from that module. If i want to import specific thing i will use from module import smth


'''
# It is same as we have done before

from random import choice

print(choice([1, 2, 3]))

'''

##################################################################

# random.randint(a, b) - between a and b inclusive

# Give you random number from 1 to 10 inclusive

'''
import random

number = random.randint(1, 10)

print(number)

'''

##################################################################

# random.shuffle(x) - randomize the order of the collection of elements

'''
import random

cards = ["jack", "queen", "king"]

random.shuffle(cards)

print(cards)

'''

##################################################################

# STATISTIC MODULE IN THE PYTHON
 

'''
import statistics

print(statistics.mean([1, 2, 3, 4, 5])) # mean() function for mean

'''

##################################################################

# Command-line argument is external input you give a program at the moment you run it, right in the command line (terminal).

# like you write in terminal: py main.py, but you will add some features from you like: py main.py Bruce => It may use it and will return hello, Bruce depend on your code

# New module will help us to add smth more in the command line this module called - sys.

# From sys we will use function argv - standart argumnet vector. It wil will turn command line into list whih every word is element

'''
import sys

print("Hello", sys.argv[1], sep=", ") # in terminal we can write python main.py Aminjon => Result: Hello, Aminjon

'''

##################################################################

# sys.exit("message if you want") will exit the program immediately without going to other lines after itself.

'''
import sys

if len(sys.argv) < 2:
    sys.exit("Too many arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print('Hello, my name is', sys.argv[1])

'''

##################################################################

'''

# Working with list - slice

my_list = [1, 2, 3, 4, 5]

# my_list[from:to]
print(my_list[1:]) # [1:] means from index 1 till end
print(my_list[1:5]) # this is same as [1:]
print(my_list[0:5:2]) # [a:b:c] - c means jumping
print(my_list[-1]) # negative index start from end, [-1] last elem
print(my_list[::-1]) # give us reverse version of the list

'''
##################################################################

# Packages - A package is a folder (directory) that contains modules (Python files) and a special __init__.py file.

# PyPI(Python Package Index) - you can look at python packages

# cowsay - package in python

# How to download packages:
#                         in terminal: pip install package_name

# Ex: pip install cowsay - Gonna give you cowsay library

"""

import cowsay # New package we download, now we using it
import sys  # We already know it

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])


"""
# Result
'''
| Hello, Aminjon |
  ==============
              \
               \
                 ^__^
                 (oo)\_______
                 (__)\       )\/\
                     ||----w |
                     ||     ||
'''

##################################################################

"""
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.trex("Hello, " + sys.argv[1])

"""
##################################################################

# API's - Application Programming Interface allows one software (program) to talk to another software/system.

# requests - is library used to make web request or internet using python code

# JSON - JSON stands for JavaScript Object Notation.It’s a lightweight, readable format for storing and exchanging data, especially between programs over the internet.

'''
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Exit")

# We will get our web search, but in JSON form 
json_response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

# We will use .json() function in puthon to turn JSON into Python
python_response = json_response.json()

# Let's print it
print(python_response)

#Let's make it more readable through json library
clear_response = json.dumps(python_response, indent=2)

# Show result
print(clear_response)

'''

############################################################

# Give TrackNames of the artist


'''
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("ERROR!")


response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])


clear_response = response.json()

counter = 0

for i in clear_response["results"]:
    if i["artistName"].lower() == sys.argv[1].lower():
        counter += 1
        print(counter, i["trackName"], sep=") ")

'''

############################################################

# Now in new version we gonna remove repeated once

'''
import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("ERROR!")


response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])


clear_response = response.json()

counter = 0
empty_list = []

for i in clear_response["results"]:
    if i["artistName"].lower() == sys.argv[1].lower():
        if i["artistName"] not in empty_list:
            empty_list.append(i['trackName'])

for i in empty_list:
    counter += 1
    print(counter, i, sep=") ")

'''

############################################################

# Creating yours python modules and packages

'''
def main():
    hello("World")
    goodbye("World")


def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")
 
main()

'''


############################################################

# After importing some functions like hello, goodbye or main from our main.py to another python file and then after running our code we will see that function main() which is called in the main.py will be running even in amother python file, how to solve it???

'''
def main():
    hello("World")
    goodbye("World")


def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")


# Our main.py will be runned if its name will be called
if __name__ == "__main__": # This syntax is constant
    main()

'''

# So in order your python file to run when it is called you must in include that if statement.

############################################################

'''
# UNIT TESTS - testing your code by coding

def main():
    x = int(input("x: "))
    print("x^2", square(x), sep=" = ")

def square(number):
    return number * number


if __name__ == "__main__":
    main()

'''

############################################################

# In reality you can use pytest in order to make your job easier

# pytest - you can dowload and use it.

# unit - test which we used - is helpful for unit, i mean for fucntions.

# Let's use pytest

# Look documentation for more information


'''
def main():
    x = int(input("x: "))
    print("x^2", square(x), sep=" = ")

def square(number):
    return number * number


if __name__ == "__main__":
    main()

'''

############################################################

# Let's create hello name programm and test it with pytest

'''
def main():
    name = input("Name: ")
    print(hello(name))


def hello(smb_name = "world"):
    return f"Hello, {smb_name}"


if __name__ == "__main__":
    main()

'''
############################################################

# How to make directory through terminal?
# Type in terminal: mkdir forlder_name, example: mkdir test

# How to create python file inside directory(folder):        code folder_name/file_name.py

# Now let's create test folder which inside all our test fucntions in python file.

# Now we gonna put all our test inside that file.
# code test/test_code.py => will create test_code.py inside test folder

# By creaeting __init__.py file inside directory(folder) we say to the python that this folder is package: code test/__init__.py

############################################################

# ========================== NEW ==========================#

'''
# Working with files

# Before talking about files let's go with lists

# by using .append(smth) we will add new element to our list

list = [] # This is empty list
list.append("Bob") # Now we add Bob to our list
list.append("Ali") # will be added as last element
list.append("Sayvali") # will be added as last element

# As you see they are not sorted alphabeticaly
print(list) # ['Bob', 'Ali', 'Sayvali']

# We use function sorted(list_elem) to get sorted list
sorted_list = sorted(list)
print(sorted_list) # ['Ali', 'Bob', 'Sayvali']

'''

############################################################

# Programm that will save names to a list
'''
names = []

for _ in range(3):
    names.append(input("Name: "))

for name in names:
    print(f"Hello, {name}")

'''
# Te problem with is problem is that if I run this code again all names will be disapear.

# Would it be nice to save informatoin, that is why we need file i/o.

# How to save name in file in order to save them again and again?

############################################################

# we will use open - read documentation for more info

'''
name = input("Name: ")

# open("name_of_file.txt", "operation")
file = open("name.txt", "w") # "w" is operation means write

# We use write(...) to write smth inside the file
file.write(name)

# close() function closes file and save it
file.close()

'''

# After running the code check it by: code name.txt

# However, there is mistake. If we run our code sacond time and write name we will see that previous name was vanished. 

# Why???

# Reason behind is "w" - it not only means to write, but also to recreate the file. So, every time you running code you overwrite your file's text.


# How to solve ?
############################################################

# We will use append - "a" as operation of open() function

'''
name = input("Name: ")

file = open("name.txt", "a")

file.write(f"{name}")

file.close()

'''

# It worked, but there is one error - file add everything in one line. We can solve it by putting "\n" backslash n.

'''
name = input("Name: ")

file = open("name.txt", "a")

file.write(f"\n{name}")

file.close()

'''


############################################################

# We can forget to close our file which lead to info leak

# How to solve it ?

# You don't need to close file everytme if you will use - with. 

# More pythonic is using with - means I want to open and close file.

'''
name = input("Name: ")

with open("name.txt", "a") as file:
    file.write(f"{name}\n")
'''

# how to read it and show it in terminal?

'''
with open("name.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello", line, end="", sep=", ")

'''

# OR

'''
with open("name.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,", line.strip())

'''

# OR

# Not recommended
'''
with open("name.txt", "r") as file:
    for line in file:
        print("hello,", line.strip())

'''
############################################################

# in open("smth.txt", "r") - "r" is defualt, so you don't need to include it. Check documentation!!!

'''
names = []

with open("name.txt") as file: 
    for i in sorted(file):
        names.append(i.rstrip())


for name in sorted(names):
    print(f"Hello, {name}")

'''
############################################################

# sorted(iterable, reversed=True) - reverse the order

'''
names = []

with open("name.txt") as file: 
    for i in sorted(file, reverse=True):
        names.append(i.rstrip())


for name in sorted(names):
    print(f"Hello, {name}")

'''

############################################################

# .txt is used for typing some data, but if you want row and column format i mean structured better to use .csv

# How to work with .csv ?

# split("character") - split into pieces by charecter

'''
counter = 0

with open("students.csv") as file:
    for line in file:
        counter += 1
        row = line.rstrip().split(",")
        print(f"{counter}) {row[0]} <=> {row[1]}")

'''

# More understandible
"""
counter = 0

with open("students.csv") as file:
    for line in file:
        counter += 1
        name, hounse = line.rstrip().split(",")
        print(f"{counter}) {name} <=> {hounse}")

"""


############################################################

# The only case we don't put () in fuction when we assign variable as function. Ex:

"""
def hello(name):
    return f"Hello, {name}"

x = hello # Now x is hello function
y = hello("smb") # Now y is return value of function

print(x("smb"))  # Hello, smb
print(hello("smb"))  # Hello, smb

"""
############################################################

# Using dictionary to sort them by anything
'''
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        
        student = {"name": name, "house": house}
        students.append(student)

# sorted(list, key = fucntion, reversed = False)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

'''

############################################################

# lambda function - no name function. one-line, no-name function used for simple tasks, often passed directly as arguments.

# We give argument and instantly we use it in lambda

# lambda arguments: expression

'''
square = lambda x, y: x*y

print(square(2, 4)) # result is 4

# OR

print((lambda x, y: x * y)(2, 4))

'''
############################################################

# We can change get_name function with lambda function

'''
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.strip().split(",")
        
        student = {"name": name, "house": house}
        students.append(student)


for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

'''

############################################################

# 8h lecture notes from cs50 python.
# Now it is end
# I start Data Structure & Algorithms join me in new repo.