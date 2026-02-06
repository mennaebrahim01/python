class Human:
    def eat(self):
        print("Human eats with manners")

class Mammal:
    def eat(self):
        print("Mammal eats instinctively")

class Employee(Human, Mammal):
    pass

e = Employee()
e.eat()

###when super used with multiple inheritance it follows MRO (searches for method according to the first class ) not just the direct parent
## in this example it follows human 
