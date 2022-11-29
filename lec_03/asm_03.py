# Task 1
print('Task 1:')
class Person:
    def __init__(self,name,age,height): # implicit return object
        self.__name = name
        self.__age = age
        self.__height = height
    def __str__(self):
        i = str(self.__age)
        j = str(self.__height)
        return(self.__name + ' ' + i + ' ' + j)
    def walk(self,meters):
        temp = str(meters)
        print(self.__name + ' walks for ' + temp + ' m!')
    def say_hello(self):
        print('Hello!')
    def get_name(self):
        return self.__name
    def get_height(self):
        return self.__height

p = Person('John',18,180)
print(p)
p.walk(30.0)
p.say_hello()

# Task 2
print('Task 2:')
class Dog(Person):
    def __init__(self,name,color,age,owner,height):
        Person.__init__(self,name,age,height)
        self.__color = color
        self.__owner = owner
    def bark(self):
        print('bark! bark! bark!')
    def sit(self):
        print(self.get_name() + ' has sat down!')
    def __str__(self):
        i = self.get_name()
        return (self.get_name()+ ' ' + self.__color + ' ' + i + ' ' + self.__owner + ' ' + self.get_height())

d = Dog('doggy','white',1,'Tim','100')
print(d)
d.walk(30.0)
d.say_hello()
d.bark()
d.sit()

# Task 3
print('Task 3:')
class Car(Person):
    __distance_counter = 0.0
    __gasoline_consumption = 8
    __gasoline_tank = 50.0
    def __init__(self,title,owner,topSpeed):
        self.__title = title
        self.__owner = owner
        self.__topSpeed = topSpeed
    def __str__(self):
        i = str(self.__distance_counter)
        j = str(self.__gasoline_consumption)
        k = str(self.__gasoline_tank)
        return(self.__title + ' ' + self.__owner + ' ' + i + ' ' + j + ' ' + k + ' ' + self.__topSpeed)
    def move(self,speed,duration):
        self.__distance_counter += speed * duration
        self.__gasoline_tank -= self.__gasoline_consumption
    def refuel(self,liters):
        self.__gasoline_tank += liters

c = Car('Audi','Me','120km/h')
print(c)
c.say_hello()
c.move(100,5)
print(c)
c.refuel(10)
print(c)