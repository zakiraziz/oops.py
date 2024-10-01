<<<<<<< HEAD
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j} ")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j):
        super().__init__(i, j)
        self.k = k

        def show(self):
            print(f"The vector is {self.i}i + {self.j}j + j {self.k}k")

a = TwoDVector(1,  2)
a.show()
b = ThreeDVector(5, 2, 3)
b.show()
=======
class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j} ")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j):
        super().__init__(i, j)
        self.k = k

        def show(self):
            print(f"The vector is {self.i}i + {self.j}j + j {self.k}k")

a = TwoDVector(1,  2)
a.show()
b = ThreeDVector(5, 2, 3)
b.show()
>>>>>>> 70d5edebdd396d3ad64e808feff1650df13b96a9
