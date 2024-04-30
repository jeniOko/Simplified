class Mammal:
    def move(self):
        print("They walk")

    def reproduce(self):
        print("They give birth")


class Birds:
    def move(self):
        print("They fly")
      
    def reproduce(self):
        print("They lay eggs")


class Dog(Mammal): #inherits from Mammal class
    def bark(self):
        print("Dogs bark")


class Cat(Mammal):
    pass  


class Dove(Birds): #inherits from Birds class
    pass


class Eagle(Birds):
    def heights(self):
        print("They fly so high")


puppy = Dog()
print("The characteristics of a puppy are :")
puppy.bark()
puppy.move()
puppy.reproduce()


bird1 = Eagle()
print("The characteristics of an Eagle are :")
bird1.move()
bird1.reproduce()
bird1.heights()
