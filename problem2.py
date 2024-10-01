class Animals:
    pass

class pets(Animals):
    pass

class Dog(pets):

    @staticmethod
    def bark():
        print("Bow Bow!")

    
d = Dog()
d.bark()