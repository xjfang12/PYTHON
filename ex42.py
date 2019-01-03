<<<<<<< HEAD
## Animal is-a object (yes, sort of confuing) look at the extra credit
class Animal(object):
    pass

## Class Dog is inherit from class Animal,
class Dog(Animal):

    def __init__(self, name):
        ## Class Dog has-a attribute name, get from instance argument
        self.name = name


## Class Cat is inherit from class Animal
class Cat(Animal):

    def __init__(self, name):
        ## Class Cat has-a attribute name, get from instance argument
        self.name = name

## Class Person is-a object look at the extra credit
class Person(object):

    def __init__(self,name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Class Employee is inherit from class Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        ## use Class Employee's __init__ funciton
        super(Employee, self).__init__(name)
        ## Class Employee has-a attribute salary
        self.salary = salary

## Class Fish is-a object
class Fish(object):
    pass

## Class Salmon is inherit from class Fish
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Mary has a pet, satan
mary.pet = satan

## frank is-a Employee, and his salary is 120000
frank = Employee("Frank",120000)

## frank has-a pet, rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is-a Halibut
=======
## Animal is-a object (yes, sort of confuing) look at the extra credit
class Animal(object):
    pass

## Class Dog is inherit from class Animal,
class Dog(Animal):

    def __init__(self, name):
        ## Class Dog has-a attribute name, get from instance argument
        self.name = name


## Class Cat is inherit from class Animal
class Cat(Animal):

    def __init__(self, name):
        ## Class Cat has-a attribute name, get from instance argument
        self.name = name

## Class Person is-a object look at the extra credit
class Person(object):

    def __init__(self,name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Class Employee is inherit from class Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        ## use Class Employee's __init__ funciton
        super(Employee, self).__init__(name)
        ## Class Employee has-a attribute salary
        self.salary = salary

## Class Fish is-a object
class Fish(object):
    pass

## Class Salmon is inherit from class Fish
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Mary has a pet, satan
mary.pet = satan

## frank is-a Employee, and his salary is 120000
frank = Employee("Frank",120000)

## frank has-a pet, rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is a Salmon
crouse = Salmon()

## harry is-a Halibut
>>>>>>> 2e988e5953e37978d1ddd41d49b7acfffc11b0b1
harry = Halibut()