#Q.1
class Circle():
  def __init__(self,radius):
    self.radius = radius
  def  getArea(self):
    return 3.14*self.radius*self.radius
  def getCircumference(self):
    return self.radius*2*3.14
x= Circle(8)
print(x.getArea())
print(x.getCircumference())

#Q.2
class Student():
  def __init__(self,name,roll,age,marks):
    self.name = name
    self.roll = roll
    self.age=age
    self.marks=marks
  def display(self,name,age):
    print (self.name)
    print (self.age)
  def setAge(self,age):
    self.age=age
    print(self.age)
  def setMarks(self,marks):
    self.marks = marks
    print(self.marks)
a=input("enter name: ")
b=int(input("enter rollno: "))
c=int(input("enter age: "))
d=int(input("enter marks: "))
s=Student(a,b,c,d)
s.display(a,b)
s.setAge(c)
s.setMarks(d)

#Q.3
class Temprature:
    def convertCelsius(c):
        fahrenheit = (c * 9/5) + 32
        print(fahrenheit)
        return fahrenheit
    def convertFahrenheit(f):
        celsius = (f - 32)*5/9
        print(celsius)
        return celsius
temp = Temprature
x = float(input("Enter the celsius: "))
y = float(input("Enter the fahrenheit: "))
temp.convertCelsius(x)
temp.convertFahrenheit(y)
print("Conversion")

#Q.4
class MovieDetails:
    def display(Artist_name,Movie_Name,Year_of_Release,Rating):
        print("Artist_name: ",str(Artist_name),'\n'"Movie_Name",str(Movie_Name),'\n'"Releasing date : ",str(Year_of_Release),'\n'"Rating out of 10: ",str(Rating))
        return
    def add(Director_name):
        print("Director_name: ",str(Director_name))
        return
dd = MovieDetails
dd.display("Rahul",'KKKG','12 March 2001','8/10')
dd.add("hulk")

#Q.5
class Animal:
   def animal_attribute(self,name,attri):
       print(name," has attribute to ",attri)

class Tiger(Animal):
   def show_attribute(self,name,attri):
       self.animal_attribute(name,attri)

T = Tiger()
T.show_attribute("Tiger","roar")

#Q.6

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())

#output :

#'A','B'
#'A','B'


#Q.7

class Shape:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self,l,b):
        area=l*b
        return area
class Rectangle(Shape):
    def __init__(self):
        pass
class Square(Shape):
    def __init__(self):
        pass

    
n=int(input("for area:-\for rectangle press 1, for square press 2:\n"))
if n==1:
    n1=int(input("enter length: "))
    n2=int(input("enter bredth: "))
    x=Shape(n1,n2)
    r=Rectangle()
    print("area of rectangle is:",r.area(n1,n2))
elif n==2:
    n1=int(input("enter lenth: "))
    x=Shape(n1,n1)
    y=Square()
    print("area of square is ",y.area(n1,n1))


