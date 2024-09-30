class Employee:
    a  = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self,value):
        self.ename = value.split(" ")[0]
        self.ename = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "zakir khan"
print(e.name)

e.show()