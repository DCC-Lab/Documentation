

[TOC]



# Getting started in Python

This document is for non-expert programmer scientists, such as biologists. It will explain what Python is and will show you what you have to do to get started.

Python is a computer language. It has been popular with scientists because it is free, fast, flexible and has all the features expected from modern programming languages.

## It is free

Python is available on any platform (Windows, macOS, Linux and everything you can think of, including Raspberry PI) and well supported. It comes on Linux and macOS by default (2.7 as of 2019), but can still be manually installed side by side with the version that comes with your system without interference.

Partly because it is free, there exists many different ways to "get Python on your computer". The best solution is to use [Anaconda](http://www.anaconda.com/), which will install everything for you (include specific modules that are commonly used).

The language still evolves and newer versions are released every year.

## Fast

Python offers reasonable performance for intense numerical computations.  There are multiple modules that are very powerful and offer high performance computations, such as `numpy`, `scipy`, etc...

Because Python is an "interpreted language", it does not require a complicated set up with a compiler.  This means you type your program into a text file, then you "run it with Python". It is very straightforward, as opposed to other languages which are admittedly much higher performance (C, C++, Objective-C, Swift, C#, etc...) but more complicated for beginners.

## Flexible

At the heart of Python, you will find `modules`.  Typically, in a Python script, you will have a command a the beginning that imports the code from a module:

```python
import numpy
# More code after this
```

This allows people to package their code into a module, then distribute them through community-supported sites such as http://pipy.org. Anybody can create modules that can be used by others, and anybody can upload them on pypi.org, which has made Python a very dynamic language that becomes more powerful as people create new modules.

As a comparison, Python modules are similar to MATLAB toolboxes that extend MATLAB.

## Modern language

Any task that is sufficiently complicated (image analysis, data analysis, etc...) will at some point require a strategy to hide the complexity of how it performs its job to make it manageable by others but also by the main programmer. A good modern computer language today is expected to support :

1. Object-oriented interface (i.e. classes)
2. Extendability (i.e. modules)
3. High performance numeric types (i.e. numpy and others)
4. Good interoperability with other languages
5. Good access to the Operating System facilities (network, files, etc...)
6. Good debugging, profiling and testing tools

Python offers all of that.

## Examples

1. Python is the language of choice at Google, and machine learning modules have been created (TensorFlow, PyTorch).
2. Python is the underlying language for scripting at Apple and can create windows and display dialogs
3. Very good image analysis, image segmentation modules exist and can be used by scientists.



# Basic programming

Before diving into Python, we need to at least survey the most important building blocks of any programming language: variables, arrays, and other types,  condition-statements, for-loops, while-loops, , functions (with arugments and return values), classes.

## Statement

```python
# A statement is anything on a single line
a = 1
# Indentation is important: there are no {} or () in Python loops (see below)
```

## Types

```python
int
float
bool
tuple
str
# and many others
```

## Variables

```python
# A comment appears after a '#'
a = 1 # This is an integer variable (can take any integer value)
b = 4.1 # This is a floating point variable (can take any floating point value)
isDone = True # A boolean value
name = 'Daniel' # This is a string of text
name = "Daniel" # Same thing
array = [4,5,6] # An ordered list of integers
array[0] # First element 4
array[2] # Last element 6
array[-1]# Also last element 6
otherArray = ["Daniel", "Cote","Ouchimama"] # An ordered list of strings
triplet = (1,2,3) # This is a triplet (called a tuple) made of three values
otherTriplet = (1.0, 2, "Daniel") # Triplet made of three values of different types
someRange = range(5) # Returns an array with 5 values, starting at 0 [0,1,2,3,4]
```

## If-statement

An `if-statement` will execute a block of indented code if a condition is true or another if a condition is false

```python
isDone = True

if isDone:
    print("Done")
else:
    print("Not done yet")
    
```

## For loops

The `for-loop` will execute the indented code `n` times, given by the number of elements in the array:

```python
for index in [0,1,2,3]: # The variable index will take all values from the array
    print(index)        # Notice the print command is indented by 4-spaces
# This will print:
# 0
# 1
# 2
# 3

for index in range(4):  # The variable index will take all values range(4)
    print(index)        # Notice the print command is indented by 4-spaces
# This will also print:
# 0
# 1
# 2
# 3
    
```

## While-loops

The `while-loop` will execute the indented code until a condition is not met anymore. 

```python
i = 0
while i < 4:
    print(i)
    i = i + 1 # Add 1 to i
    # Is i < 4? If yes, loop again, if not, leave while loop
    
isDone = False
while not isDone:
    # Do something
    isDone = computeStuffIncrementally() # May return True or False
    
```

## Functions

A function can be defined to simplify the code.  It accepts arguments that can be named, can have default values, and their type can be indicated. The way to call a function is to use the name of the function and name its arguments.

```python
def isGreaterThan10(someValue) -> bool: # Takes 1 argument (type is not known) returns 1 value (Boolean)
    if someValue > 10:
        return True
    return False

def printSomething(name:str = "Unknown"): # Default value is "Unknown"
    print(name) 
  
  
# Someone may call this function like this:
isGreaterThan10(someValue=11) # It is good practice to name the argument 
                              # because it is readable
isGreaterThan10(11)           # You may also do that (but don't)
isGreaterThan10("Daniel")     # Runtime error because "Daniel" is not a number

printSomething(name="Daniel") # Will print Daniel
printSomething("Daniel")      # Will also print Daniel
printSomething()              # Will print Unknown
printSomething(name=4)        # Will print 4
```

## Classes

An object (or a class) keeps the data and the methods to operate on that data together. 

For instance, we can have a project where we need to manage a list of people.  A `Person` would be a useful class because it keeps everything together: first and last name, date of birth, gender, etc...  If need be, it can manipulate that data to return something useful (such as age from the date of birth or the full name by concatenating the first and last names together):

```python
class Person:
  	# An __init__ function is defined to initialize the object and is usually
		def __init__(firstName:str, lastName:str, dateOfBirthYYYYMMDD:(int, int, int), isMale:bool):
      	# self refers to "this object".  In this __init__ function,
        # self.firstName defines a variable that is included (i.e. kept) in Person
        # Hence, self.firstName is the variable firstName in the object Person,
        # but firstName (without self. in front) is the variable that was 
        # passed as an argument
      	self.firstName = firstName
      	self.lastName = lastName
				self.dateOfBirth = dateOfBirthYYYYMMDD
        self.isMale = isMale

    # Other functions can be defined at will
    def fullName() -> str:
      	return self.firstName + " " +  self.lastName
    
    def gender() -> str:
      	if self.isMale:
          	return "Male"
        else:
          	return "Female"
          
    def age() -> float:
      	# Compute age from today's date and date of birth
        # For now, returns 18
        return 18
      
      
# Someone could do this:
daniel = Person(firstName = "Daniel", lastName="Côté", dateOfBirthYYYYMMDD=(1973,2,27), True)

print(daniel.fullName()) # Will print Daniel Côté
print(daniel.age()) # Will print 29 because I am 29.
```

The ability to define a class is an important feature of a language: not all languages allow it. 



