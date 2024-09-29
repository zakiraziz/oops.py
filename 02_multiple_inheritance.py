class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.language} and the salary is {self.salary}")

class coder: 
     language = "python"
     def printlanguage(self):
          print(f"Out of all the language here is your language: {self.language}")


class programmer(Employee):
         company = "ITC Infotech"
         def show(self):
           print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee( )
b = programmer()


b.show()
b.printLanguages()
b.showLanguages()
