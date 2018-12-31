# Parent class
class Dog:

    # Class attribute
    species = 'mammal'
    is_hungry = True;

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {}.".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def species(self):
        return "And they're all {}, of course.".format(self.species)

    def eat(self):
        self.is_hungry = False

    def walk(self):
        return "{} is walking!".format(self.name)



# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Pets class
class Pets():
    def __init__(self, dogs):
        self.dogs = dogs
    def printDogs(self):
        for x in self.dogs:
            print(x.description())
    def feed(self):
        for x in self.dogs:
            x.eat()
    def petsFed(self):
        fed = True
        for x in self.dogs:
            if x.is_hungry == True:
                fed = False
        if fed == False:
            print("My dogs are hungry")
        else:
            print("My dogs are not hungry")

    def walk(self):
        for dog in self.dogs:
            print(dog.walk())


pet1 = Pets([Dog('Tom', 6), Dog('Fletcher', 7), Dog('Larry', 9)])
print("I have {} dogs.".format(len(pet1.dogs)))
pet1.printDogs()
print("And they're all mammals, of course.")
pet1.feed()
pet1.petsFed()
pet1.walk()
