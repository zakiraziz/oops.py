class Employee:
    salary = 234
    Incerement = 20

    @property
    def salaryAfterIncerment(self):
        return (self.salary + self.salary * (self.Incerement/100))
    
    @salaryAfterIncerment.setter
    def salaryAfterIncerement(self, salary):
        self.mncerement = ((salary/self.salary) -1)*100




e = Employee()
e.salaryAfterIncerement = 280.8
print(e.incerement)