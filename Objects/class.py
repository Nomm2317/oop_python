#this is a class called Dog
class Dog:

  def __init__(self, name) : #this a constructor that when eun is going to set up a new object and 
    self.name = name #this is going to set the name of the dog when we create a new dog object
    print(name)

  def add_one(self, x):
    return x + 1


  #this is a method -> a function that is inside a class
  def bark(self): #self is the parameter
    print("bark")

d = Dog("tim") #this is creatig the oject d in the class dog
print(d.name)

d2 = Dog("bob") #this is creating the object d2 in the class dog
print(d2.name)
#this is a d is in the class do and is going to use the method bark

d.bark() #this is calling the method bark from the class dog using the object d


print(d.add_one(5))
print(type(d))