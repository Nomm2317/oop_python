class Student:

  #constucter
  def __init__ (self,name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade

  def get_grade(self):
    return self.grade
  
#this is going to add sutdent to a couse
class Course():
  def __init__(self, name, max_students):
    self.name = name
    self.max_students = max_students 
    self.students = [] #is is ok to have a attrucure that is not define to the parameter

  #create a method that is going to add sutdent to the cousr
  def add_student(self, student):
    if len(self.students) < self.max_students: # is the length os student is less then the lenght of max student 
      self.students.append(student) # this going to add student to the list if student
      return True
    return False

  def get_average_grade(self):
    pass #this does nothing but it is going to be used later to get the average grade of the students in the course

s1 = Student("Jamie", 19, 100)
s2 = Student("jimmy", 19, 76)
s3 = Student("kat", 19, 85)


#look as this more
#what i want to do if have a loop where i dont have a hard list
course = Course("Math 30", 2)
for student in range(5):
  if course.add_student(student):
    print("student added")
  else:
    print("course is full")