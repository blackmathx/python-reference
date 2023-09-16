# Bo Payton
# Python Language Reference - Classes and Objects






# self parameter is a reference to the current instance of the calss and used to access variables
# self does not have to be named 'self', but it is the first parameter in any function in the class
class Person:
	def __init__(self, name, age): # __init__() always executed when the class is being initiated. use it to initialize a class
		self.name = name
		self.age = age 
	
	def say_hello(self):
		print("Hello, my name is " + self.name)

	def __str__(self): # __str__() is a to-string method, without it the default is unreadable
		return f"{self.name}({self.age})"
	

# use the pass statement in a class because it can't be empty
class Misc:
	pass 

p2 = Person("Emil", 26)
print(p2.name, p2.age)
print(p2)
p2.say_hello()
p2.title = "sir"  # add a property that doesn't exist yet
print(p2.title)
p2.age = 27  # update the age 
print(p2)
del p2.title # delete the age property
del p2 # delete the object completely



########## Inheritance
class Student(Person):

	# if present, the child __init__() overrides the parent's __init__() which we call explicitly
	def __init__(self, fname, lname, age, likes):
		# call the parents __init__() like this to keep the inheritance of the parent class, then add the likes property
		super().__init__(fname + " " + lname, age) # Second way to call the parents __init__()
		self.likes = likes

	def welcome(self):
		print("Welcome", self.name)

	# override the parents function of the same name
	def say_hello(self):
		print("Hi, this is " + self.name)

s1 = Student("tabius", "muller", 23, "boys")
s1.say_hello()
print(s1.likes)
s1.welcome()




########## Inheritance Class Polymorphism example
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object
for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()


# TODO example of hidden properties