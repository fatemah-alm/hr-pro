from datetime import datetime
from unicodedata import name


class Employee:
   #Employee class here
    def __init__(self, name, age, salary, employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year

    def get_working_years(self):
        return datetime.today().year - int(self.employment_year)

    def __str__(self):
        working_years = str(self.get_working_years())
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working years:  {working_years}'


        


class Manager(Employee):
    #Manager class here
    def __init__(self, name, age, salary, employment_year, bonus_percentage):
       Employee.__init__(self, name, age, salary, employment_year)
       self.bonus_percentage = bonus_percentage
   
    def get_bonus(self):
        return float(self.bonus_percentage) * int(self.salary)
    def __str__(self):
        working_years = str(self.get_working_years())
        bonus = str(self.get_bonus())
        return f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Working years:  {working_years}, bonus:{bonus}'

        
def main():
	# main code here
    employees = []
    managers = []
    print('welcome to HR Pro 2022')

    while True:
     print('Options:\n1. Show Employees \n2. Show Managers\n3. Add An Employee\n4. Add A Manager\n5. Exit')
     choice = input('What would you like to do? ')
     print('-----------------')

     match str(choice):
         case "1":
             print('Employees\n')
             for i in employees:
              print(i)
         case "2":
             print('Managers\n')
             for i in managers:
              print(i)
         case "3":
             name = input('Name: ')
             age = input('Age: ')
             salary = input('Salary: ')
             employment_year= input('Employement year: ')
             employees.append(Employee(name, age, salary, employment_year))
             print('Employee added succesfully!\n----------------')
         case "4":
             name = input('Name: ')
             age = input('Age: ')
             salary = input('Salary: ')
             employment_year= input('Employement year: ')
             bonus=input('Bonus Percentage: ')
             managers.append(Manager(name, age, salary, employment_year, bonus))
             print('Manager added succesfully!\n----------------')

         case "5":
             break

     if (choice == "5"):
        break

if __name__ == '__main__':
	    main()
