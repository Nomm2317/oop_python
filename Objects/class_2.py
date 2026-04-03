class Cat():

  #constructor
  def __init__ (self, name, age):
    self.name = name
    self.age = age

  #getter method
  def get_name(self):
    return self.name
  
  def get_age(self):
    return self.age
  

  #setter method
  def set_name(self, name):
    self.name = name

  def set_age(self, age):
    self.age = age


c = Cat("kat", 90)
print(c.get_name())
c2 = Cat("timmy", 5)
print(c.get_age())