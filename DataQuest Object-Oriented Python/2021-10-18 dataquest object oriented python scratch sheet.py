#!/usr/bin/env python3

## DataQuest.io
## Python for DataScience: Intermediate
## Object-Oriented Python

## Pt 1 Introduction

l = [1, 2, 3]
s = "string"
d = {"a": 1, "b": 2}

print(type(l))
print(type(s))
print(type(d))

## Pt 2 Classes and Objects
#- An entity that stores data
#- Object’s class defines properties that objects in that class will have
#- e.g. there are thousands of Tesla cars. Each car is similar in that they are manufactured by Tesla.
#	- Each car, an object. Tesla, the class.
#	- Each car object belongs to the Tesla class
#	- Design defines what the car is, what it does, how it does it
#		- The design =/= the car. 
#		- Similar to Python, there are class definitions.
#		- The cars’ designs are the class’ definitions.

## Pt 3 Defining a Class
#def a_function():
#	# deets here
#	pass

#class MyClass:
#	# deets here
#	pass
	
# a_function and MyClass would spit out errors if not for the "pass" statement
# https://docs.python.org/3/reference/simple_stmts.html#pass
# empty functions/classes are a no-no
# pass statement is useful as a placeholder while building out a function/class

## Pt 4 Instantiating a Class
#	- “Instantiation”
#		- “Instantiate an object of that class”
#		- Verb: represent as or by an instance
#			- Have an instance
#			- Be represented by an actual example

my_int = int("3")
# int("3") instantiates object of int class
# my_int assigns object to a variable

# example exercise

#my_instance = MyClass()
#
#print(type(my_instance))

#Pt 5 Creating Methods

# methods allow objects to perform actions

my_string = "hello"
my_list = [1, 2, 3]

# list.append() and str.format() are both methods
# i.e. they can perform actions to/on objects
print(my_list)
my_list.append(4)
print(my_list)

print(my_string)
my_string = my_string.replace("h","H")
print(my_string)

# One class' method cannot be used with another
#my_string.append("!")
# the above would return an error

#class MyClass:
#	def greet():
#		return "hello"
#	def first_method():
#		return "This is my first method"
	
#an_instance = MyClass()
#
#print(an_instance)

# Pt 6 Understanding "self"

# what happens when I try calling one of those methods?

#an_instance.greet()
# the above returned the error below

#Traceback (most recent call last):
#  File "2021-10-18 dataquest object oriented python scratch sheet.py", line 94, in <module>
#    an_instance.greet()
#TypeError: greet() takes 0 positional arguments but 1 was given

# verify that python is inserting an instance argument via str type
# create an str object
s = "MY STRING"

# call 'str.title() directly
# instead of 's.title()

result = str.title(s)
print(result)

# exploring "self"

class ExampleClass:
	def print_self(self):
		print(self)
mc = ExampleClass()

print(mc)
mc.print_self()
# the above statements both return:
# <__main__.ExampleClass object at 0x7fead001ca90>
# ...

# exercise: adding self to MyClass

class MyClass:
	def first_method(self):
		return "This is my first method"
	
my_instance = MyClass()
result = my_instance.first_method()

# Pt 7
# Creating a method that accepts an arg

class EggClass:
	def return_string(self, string):
		return string
	
mc_hammer = EggClass()
result = mc_hammer.return_string("Can't touch this")
print(result)

class MykaLass:
	def method_man(self):
		return "Method man with a selfie argument"
	def return_redman(self, input_list):
		return input_list
	
high_incident = MykaLass()
result = high_incident.return_redman(['eggs', 'milk', 'fertilzer'])
print(result)
	
# Pt 8
# Attributes and the Init Method

string_1 = "This is a string"
# string_1 instantiate's the object, a str
# The string itself is the attribute

an_int = int("3")
# int() method converts the string to an integer
# the integers is converted and stored in an object, the variable in this case

# init method

class AppleRock:
	def __init__(self, string):
		print(string)
# the above defines a class, AppleRock
# defines init method as accepting two arg, self and string
# calls the print function to act on the string arg
		
appleseeds = AppleRock("Hola!")
# AppleRock class is called/run in object appleseeds; a str arg is passed through
# the init method runs on the string, in this case the str is printed

class AppleRock2:
	def __init__(self, string):
		self.an_attribute = string
		## this clas takes a string and simply saves it as an attribute which can be called later; no output alone from it

an_appleseed = AppleRock2("Hola Chica")
## inputs data to the AppleRock2 class
print(an_appleseed.an_attribute)
## outputs the data stored in AppleRock2 class


## exercise
# create class, create init method in class that takes self arg and a list arg; store list arg as attribute
# call print function to output attribute
class Listly:
	def __init__(self, initial_data):
		self.data = initial_data

stuff_and_thangs = Listly([1, 2, 3, 4, 6])

print(stuff_and_thangs.data)

# pt 9
# creating an append method

# standard append method
zed_list = [1, 2, 3, 4]
# a list
zed_list.append(5)
# list class' append method
print(zed_list)
# call print fn to output results

# to recreate this method; need to add one extra item to a list
# one way is to use brackets and add (+) that item to the existing list

woo_list = [1, 2, 3]
woo_item = 42
print(woo_list)
woo_item_list = [woo_item]
woo_list = woo_list + woo_item_list
print(woo_list)

#exercise
# define append method with self, new_item args
# implement append method so that it appends provided arg to list stored in self.data
# outside of the class, create an instance of the class, provide a list, print the attribute
# call the append method to add a value; re-print the stored attribute

class Listly2:
	def __init__(self, initial_data):
		self.data = initial_data
		
	def append(self, new_item):
		self.data = new_item
		
a_real_listing = Listly2([1, 2, 3, 4, 5])
print(a_real_listing.data)
a_real_listing.append(6)
print(a_real_listing.data)

class Listly3:
	def __init__(self, initial_data):
		self.data = initial_data
		
	def append(self, new_item):
		self.data = self.data + [new_item]
		
		
b_real_listing = Listly3([1, 2, 3, 4, 5])
print(b_real_listing.data)
b_real_listing.append(6)
print(b_real_listing.data)

# pt 10
# creating, updating an attribute
# exercise: add a counter that stores len as an attribute and updates it when value appended

class AClassAct:
	def __init__(self, initial_data):
		self.data = initial_data
		self.length = 0
		for item in self.data:
			self.length += 1
	
	def append(self, new_item):
		self.data = self.data + [new_item]
		self.length += 1
		
bad_act_list = AClassAct([1, 2, 4, 5, 6])
print(bad_act_list.data)
print(bad_act_list.length)
bad_act_list.append(99)
print(bad_act_list.data)
print(bad_act_list.length)
