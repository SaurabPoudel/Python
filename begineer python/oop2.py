class Employee:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    

Saurab = Employee("Saurab","Poudel",44000)
Srishti = Employee("Srishti","Poudel",44000)

print(Saurab.fname, Srishti.lname)