'''Assignment Part 1: Defining Classes
File 1: Write an Employee class with the following attributes:
Employee name
Employee number
Create a subclass named ProductionWorker that inherits from Employee. This subclass should include additional attributes:
Shift number (integer: 1 for day, 2 for night)
Hourly pay rate
Implement accessor and mutator methods (getters and setters) for each class.
Assignment Part 2: Implementing and Testing
Part 2: Write a script to:
Create an instance of ProductionWorker.
Prompt the user for each attribute's data.
Store and then display the data using the object's methods.'''
class Employee:#Employee class
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name#Variable
        self.__employee_number = employee_number#Variable
    def get_employee_name(self):#Accessing variable
        return self.__employee_name#Returns variable
    def get_employee_number(self):#Accessing variable
        return self.__employee_number#Returns variable
    def set_employee_name(self, name):#Sets variable
        self.__employee_name = name
    def set_employee_number(self, number):#Sets variable
        self.__employee_number = number
class ProductionWorker(Employee):#Production worker subclass
    def __init__(self, employee_name, employee_number, shift_number, hourly_pay):
        super().__init__(employee_name, employee_number)#Gets from superclass
        self.__shift_number = shift_number#Variable
        self.__hourly_pay = hourly_pay#Variable
    def get_shift_number(self):#Accessing variable
        return self.__shift_number#Returns variable
    def get_hourly_pay(self):#Accessing variable
        return self.__hourly_pay#Returns variable
    def set_shift_number(self, shift_number):#Sets variable
        self.__shift_number = shift_number
    def set_hourly_pay(self, hourly_pay):#Sets variable
        self.__hourly_pay = hourly_pay
def main():#Main function
    print("Enter employee details:")#Prints instructions
    name = input("Employee name: ")#Gets user input
    number = input("Employee number: ")#Gets user input
    shift = (input("Shift number (1 = Day, 2 = Night): "))#Gets user input
    pay = (input("Hourly pay rate: $"))#Gets user input
    worker = ProductionWorker(name, number, shift, pay)#Puts all information into one
    print("Employee Info")#Prints heading
    print("Name:", worker.get_employee_name())#Prints name
    print("Employee Number:", worker.get_employee_number())#Prints employee number
    print("Shift Number:", worker.get_shift_number())#Prints shift number
    print("Hourly Pay Rate: $", format(worker.get_hourly_pay()))#Prints hourly pay
main()


