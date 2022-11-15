# Task 1
print('Task 1:')
class Person:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
    def __str__(self):
        i = str(self.age)
        j = str(self.height)
        return(self.name + ' ' + i + ' ' + j)
    def walk(self,meters):
        temp = str(meters)
        print(self.name + ' walks for ' + temp + ' m!')
    def say_hello(self):
        print('Hello!')

p = Person('John',18,180)
print(p)
p.walk(30.0)
p.say_hello()

# Task 2
print('Task 2:')
class Dog(Person):
    def __init__(self,name,color,age,owner):
        self.name = name
        self.color = color
        self.age = age
        self.owner = owner
    def bark(self):
        print('bark! bark! bark!')
    def sit(self):
        print(self.name + ' has sat down!')
    def __str__(self):
        i = str(self.age)
        return (self.name + ' ' + self.color + ' ' + i + ' ' + self.owner)

d = Dog('doggy','white',1,'Tim')
print(d)
d.walk(50.0)
d.say_hello()
d.bark()
d.sit()

# Task 3
print('Task 3:')
class Car(Person):
    distance_counter = 0.0
    gasoline_consumption = 8
    gasoline_tank = 50.0
    def __init__(self,title,owner,topSpeed):
        self.title = title
        self.owner = owner
        self.topSpeed = topSpeed
    def __str__(self):
        i = str(self.distance_counter)
        j = str(self.gasoline_consumption)
        k = str(self.gasoline_tank)
        return(self.title + ' ' + self.owner + ' ' + i + ' ' + j + ' ' + k + ' ' + self.topSpeed)
    def move(self,speed,duration):
        self.distance_counter += speed * duration
        self.gasoline_tank -= self.gasoline_consumption
    def refuel(self,liters):
        self.gasoline_tank += liters

c = Car('Audi','Me','120km/h')
print(c)
c.say_hello()
c.move(100,5)
print(c)
c.refuel(10)
print(c)