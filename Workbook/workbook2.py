# -*- coding: utf-8 -*-
"""ClassWk4_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15h1xzcU1zykt0q0CkjVZsk-MUNJnwCoJ
"""

#Polymorphism in Python
# Same function used for different purposes
#built-in functions

print(len("University"))

print(len(["MCA", "BCA", "CMS", "CME","MSC", "MSCSA", "MDS"]))

# using function for polymorphism
def prd(qty, price=0):
  return qty*price
print(prd(8,40))
print(prd(0))

# Polymorphism with class methods

class CS():
  def course(self):
    print("Im listing the programmes offered by CS")
  def PG(self):
    print("MCA","MSCSA")
  def UG(self):
    print("CMS", "BCA")
class DS():
  def course(self):
    print("Im listing the programmes offered by Data Science")
  def PG(self):
    print("MDS", "MSC_Stats")
  def UG(self):
    print("CMS")

obj_cs=CS()
obj_ds=DS()
for courses in (obj_cs,obj_ds):
    courses.course()
    courses.PG()
    courses.UG()

# Polymorphism with functions and objects

class CS():
  def course(self):
    print("Im listing the programmes offered by CS")
  def PG(self):
    print("MCA","MSCSA")
  def UG(self):
    print("CMS", "BCA")
class DS():
  def course(self):
    print("Im listing the programmes offered by Data Science")
  def PG(self):
    print("MDS", "MSC_Stats")
  def UG(self):
    print("CMS")


def funct(obj):
  obj.course()
  obj.PG()
  obj.UG()

obj_cs=CS()
obj_ds=DS()

funct(obj_cs) #function calls objects
funct(obj_ds)

#Polymorphism with inheritance
class CS():
  def course(self):
    print("Im listing the programmes offered by CS, DS and Stat")
  def PG(self):
    print("MCA","MSCSA")
  def UG(self):
    print("CMS", "BCA")
class DS(CS):
   def PG(self):
    print("MDS")
   def UG(self):
    print("CMS")
class Stats(CS):
  def PG(self):
    print("MSC")

obj_cs=CS()
obj_ds=DS()
obj_sta=Stats()

obj_cs.course()
obj_cs.PG()
obj_cs.UG()

obj_ds.PG()
obj_ds.UG()

obj_sta.PG()

print("CHRIST University")

print(xx)

"""Use Try block tests a block for errors
Except block helps to handle the error 
"""

try:
  print(xx)
except:
  print("There is an error")

try:
  print(123)
except NameError:  #if try block raises a Nameerror
  print("Variable is not defined")
except:  #for other types of error
  print("Try to find the error")

try:
  print("Im in I MCA A") # if there is no error in try block; else block will be executed
except:
  print("Try Again...")
else:
  print("This is a Trimester Course")

try:
  print("Im in I MCA A") # if there is no error in try block; else block will be executed
except:
  print("Try Again...")
else:
  print("This is a Trimester Course")

try:
  print(xx)
except:
  print("Try Again...")
finally:  #will be executed regardless of the try block raises an error
  print("This is a Trimester Course")

"""**Raise Keyword is used to raise an exception**"""

x=16
# x=18
if x<18:
  raise Exception("You are not eligible to Vote")

xx= 125
# xx="MCA"
if not type(xx) is str:
  raise TypeError("Integers are not allowed")