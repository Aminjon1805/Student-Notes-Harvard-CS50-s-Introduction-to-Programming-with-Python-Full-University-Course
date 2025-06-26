# Uncomment block in line 1408 in order to use

'''
import sys

from main import hello, goodbye  # Import code from your file

if len(sys.argv) == 2:
    hello(sys.argv[1])
else:
    pass
'''
#############################################################

# Uncomment block in line 1455 in order to use 

# Let's test square function by creating test_square function
# However, our testing code is bigger then oprating code
'''
# Testing code
from main import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("Error!!! 2^2 = 4")
    
    if square(3) != 9:
        print("Error!!! 3^3 = 9")


if __name__ == "__main__":
    main()

'''

"""
# In order to make it better we use assert
# assert - uses a boolean expression for checking

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9

if __name__ == "__main__":
    main()

"""
# If we catch error out terminal will give AssertionError
# Assertion error will give you huge error in terminal, so better also use try and axcept method.
#############################################################


'''
def main():
    test_square()

def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("square ")
    assert square(3) == 9

if __name__ == "__main__":
    main()

'''
#############################################################

'''
from main import square

# In order to test it with pytest we write in terminal this:
# py -m pytest practice.py

# In order to understand where is exacly error we split our numbers into positive, negative and zero. Also, we use loop to make it faster and less spaced.

def test_square_negative():
    for i in range(-10, 0, 1):
        assert square(i) == i**2

def test_square_positive():
    for i in range(1, 11):
        assert square(i) == i**2

def test_square_zero():
    assert square(0) == 0

'''
# The good thing about testing is that if one of the function fails it will check others too without stopping

#############################################################

'''
# Test hello program in line 1500

from main import hello

list_names = ["David", "John", "Lincoln", "Ibrahim", "Smb", ""]

def test_hello():
    for i in list_names:
        assert hello(i) == f"Hello, {i}"


def test_default():
    assert hello() == "Hello, world"
    
'''

#############################################################

