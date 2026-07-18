class car:
    def __init__(self, brand, year):
      self.brand = brand
      self.year = year

car1 = car ("toyota", 2022)
print(car1.brand)
car1.year = 2023
print(car1.year)




class Book :
    def __init__ (self, title, author):
      self.title = title
      self.author = author
      Book1 = Book ("python basics", "jhon smith")
      print(Book1.title)
      Book1.author = "jane smith"
      print(Book1.author)


# (3) Dog class
class Dog:
    def __init__ (self, name, breed):
      self.name = name
      self.breed = breed
    def bark(self):
        print("woof")
dog1 = Dog("BUddy", "golden Retriver")
print(dog1.name)
dog1.bark()







# (4)Rectangle class
class  Rectangle:
    def __init__ (self ,length , width):
        self.length = length
        self.width = width
    def area(self):
      return self.length * self.width
rect1 = Rectangle(8,5)
print(rect1.area())




# (5) Employee class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
emp1 = Employee("david", 50000)
print(emp1.name, emp1.salary)
emp1.salary = 55000
print(emp1.salary)




#(6) Circle class
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def diameter(self):
        return  self.radius * 2
c1 = Circle(7)
print(c1.radius)
print(c1.diameter())




#(7) BankAccount class
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        account1 = BankAccoumt("sarah", 1000)
        print(account.balance)
        account1.balance += 500
        print(account1.balance)






#(8) Movie class
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
        movie1 = Movie("inception", 9)
        print(movie1.title,)
        movie1.ratng = 10
        print(movie1.rating)








#(9) phone class
class phone :
    def __init__(self, brand , price):
        sel.brand = brand
        self.price = price
        phone1 = phone(Apple, 999)
        print(phone1.price)
        phone1.price = 100
        print(phone1.price)






#(10) person class
class person :
    def __init__(self, first_name, Last_name):
        self.first_name = first_name
        self.Last_name = Last_name
        person1 = ("Emma", "Brown")
        person.full_name(P)

