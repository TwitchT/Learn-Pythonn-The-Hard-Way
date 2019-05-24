## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):
    
    def __init__(self, name):
        ## The dog has a name
        self.name = name
        
## Cat is-a animal
class Cat(Animal):
    
    def __init__(self, name):
        ## The cat has a name
        self.name = name
        
## Person is-a object
class Person(object):
    
    def __init__(self, name):
        ## The Person has a name 
        self.name = name
        
        ## Person has-a pet of some sort
        self.pet = None
        
## The empoyee is-a person
class Employee(Person):
    
    def __init__(self, name, salary):
        ## Super Employee, hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## The Employee has-a salary
        self.salary = salary
        
## The fish is-a object
class Fish(object):
    pass

## Salmon is-a fish
class Salmon(Fish):
    pass

## Halibut is-a fish
class Halibut(Fish):
    pass

# Rover is-a Dog
rover = Dog("Rover")

# Satan is-a Cat
satan = Cat("Satan")

# Mary is-a person
mary = Person("Mary")

# Satan is Mary's pet
mary.pet = satan

## Frank is-a Empoyee and his salary is 120000
frank = Employee("Frank", 120000)

# Rover is Frank's pet
frank.pet = rover

# Flipper is-a Fish
flipper = Fish()


# Crouse is-a Salmon
crouse = Salmon()

# Harry is-a Halibut
harry = Halibut()