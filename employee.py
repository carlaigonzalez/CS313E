#  File: employee.py
#  Description: Create class and use inhertiance to calculate different salaries
#  Student Name:Carla Gonzalez
#  Student UT EID: Cig588
#  Course Name: CS 313E
#  Unique Number: 
#  Date Created: Sunday June 12th, 2022
#  Date Last Modified: Monday June 13th


#Create class for all types of employee where name, id and salary will be saved
class Employee:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.id = kwargs.get("id")
        self.salary = kwargs.get("salary")

    def __str__(self):
        return "Name: " + self.name + " Id: " + self.id + " Salary: " + str(self.salary)
   
#Create class of permanent employee which is a type of employee with benefits, that will inherit its variables
class Permanent_Employee(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs.get("benefits")

    def cal_salary(self):
        if self.benefits == ["health_insurance"]:
            return (self.salary * 0.9)
        elif self.benefits == ["retirement"]:
            return (self.salary * 0.8)
        elif self.benefits == ["retirement", "health_insurance"]:
            return (self.salary * 0.7)
        
    def __str__(self):
        return "Name: " + self.name + " Id: " + self.id + " Salary: " + str(self.salary) + " Benefits: " + str(self.benefits)

#Create class for manager, type of employee that gets bonus and will also inherit employee varibales
class Manager(Employee):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bonus = kwargs.get("bonus")

    def cal_salary(self):
        return (self.salary + self.bonus)

    def __str__(self):
        return "Name: " + self.name + " Id: " + self.id + " Salary: " + str(self.salary) + " Bonus: " + str(self.bonus)

#create class for temporary employee, type of employee that gets their salary depending on their hours and will also inherit employee variables
class Temporary_Employee(Employee) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hours = kwargs.get("hours")
        
    def cal_salary(self):
        return (self.salary * self.hours)



    def __str__(self):
        return "Name: " + self.name + " Id: " + self.id + " Salary: " + str(self.salary) + " Hours: " + str(self.hours)

#create class for consultant, which is a type of temporary employee that travels, and as such inherits temporary employee and employee variables  
class Consultant(Temporary_Employee) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.travel = kwargs.get("travel")
        
    def cal_salary(self):
        return((self.salary * self.hours) + (self.travel * 1000))
        

    def __str__(self):
        return "Name: " + self.name + " Id: " + self.id + " Salary: " + str(self.salary) + " Hours: " + str(self.hours) +" Travel:" + str(self.travel)


#create class for consultant manager, employee that is a manager and consultant, resulting in inheritance from employee, manager, temporary employee and consultant
class Consultant_Manager(Consultant, Manager):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        Consultant.__init__(self, **kwargs)
        Manager.__init__(self, **kwargs)
        
    
    def cal_salary(self):
        return (Consultant.cal_salary(self) + self.bonus)
        
        
    def __str__(self):
       return "Name: " + self.name + " Id: " + self.id + " Salary: " + str(self.salary) + " Bonus: " + str(self.bonus) + "Hours: " + str(self.hours) +" Travel:" + str(self.travel)




###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():
    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")
 
    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")
 
    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")
 
    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")
 
    ###################################
    print("Check Salaries")
 
    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]
 
    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]
 
    print("Emma's Salary is:", emma.cal_salary(), "\n")
 
    print("Sam's Salary is:", sam.cal_salary(), "\n")
 
    print("John's Salary is:", john.cal_salary(), "\n")
 
    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")
 
    print("Matt's Salary is:",  matt.cal_salary(), "\n")
 
 

if __name__ == "__main__":
  main()
