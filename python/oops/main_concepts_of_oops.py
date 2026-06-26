#Object creation
class Student:
    def __init__(self, name, roll_no, branch,age):
        # Assign the passed arguments to the object properties (using standard lowercase naming)
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.age = 20

    def tell_details(self):
        print(f"My name is {self.name}, my roll number is {self.roll_no}, and my branch is {self.branch},my age is{20}.")


student1 = Student('Yoga', '101', 'Mathematics',20)


student1.tell_details()

class Student:
    def __init__(self, name, roll_no, branch, age):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.age = int(age) 

    def tell_details(self):
      
        future_age = self.age + 10
        
        print(f"My name is {self.name}.")
        print(f"Current age: {self.age}")
        print(f"Age after 10 years: {future_age}")

student1 = Student('Yoga', '101', 'Mathematics', 20)

student1.tell_details()


#Inheritence example 
class Employee:
    def work(self):
        print('working')
class Manager(Employee):
    pass
m = Manager()
m.work()

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
Employee = Employee('Ram',50000)
Employee.salary = 80000
print(Employee.salary)

class Employee:
    def __init__(self,name):
        self.name = name
        self.__salary = 50000
emp = Employee('Ram')
print(emp._Employee__salary)

#Encapsulation
class Student:
    def __init__(self, name):
        self.name = name
        self.__mark = 0  # Private variable

    def set_mark(self, mark):
        if 0 <= mark <= 100:
            self.__mark = mark
        else:
            print("Mark should be between 0 and 100")

    def get_mark(self):
        return self.__mark


# Create object
student1 = Student("Ram")

# Set mark
student1.set_mark(85)

# Get mark
print("Student Name:", student1.name)
print("Mark:", student1.get_mark())

class Employee:
    def __init__(self):
       self.__salary = 50000  #private variable
    def get_salary(self):
        return self.__salary
emp = Employee()
print(emp.get_salary())

class employee:
    def __init__(self,salary):
       self.__salary=50000
    def get_salary(self):
        return (self.__salary)  
    def update_salary(self,salary):
        if salary >0:
            self.__salary=salary
            return self.__salary
        return print("invalid salary")
emp = employee(50000)
print(emp.update_salary(50000))
print(emp.get_salary())

from abc import ABC, abstractmethod
class Employee(ABC):
 @abstractmethod
 def work(self):
    pass
class HR(Employee):
    def work(self):
        return "Recruiting"
class Developer(Employee):
    def work(self):
        return "Software Developing"
hr = HR()
dev = Developer()

print(hr.work())
print(dev.work())

#super()
#super error In Python, super() is used to call the parent class's methods or constructor from a child class.

























        
    




        



        





        