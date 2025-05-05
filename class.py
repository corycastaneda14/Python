'''Class Creation: Design a class named Person with the following data: name, address, age, and phone number.
Accessor and Mutator Methods: Write get and set methods for each piece of data. These methods allow you to access and change the data safely.
Creating Instances: Write a program that creates three instances (objects) of the Person class. Use one instance for your made-up information and the other two for imaginary friends or family members.
Display Data: Print out the information stored in each instance. Ensure the output is formatted and easy to read.
'''
class Person:#Defines person class
    def __init__(self,name, address,age, phone):
        self._name=name#Variable
        self._address=address#Variable
        self._age=age#Variable
        self._phone=phone#Variable
    def get_name(self):#Accessing variable
        return self._name#Returns variable
    def get_address(self):#Accessing variable
        return self._address #Returns variable
    def get_age(self):#Accessing variable
        return self._age #Returns variable
    def get_phone(self):#Accessing variable
        return self._phone #Returns variable
    def set_name(self,name):#Sets variable
        self._name=name
    def set_address(self,address):#Sets variable
        self._address=address
    def set_age(self,age):#Sets variable
        self._age=age
    def set_phone(self,phone):#Sets variable
        self._phone=phone
    
def main():#Main function
        person1=Person("Cory Castaneda","747 South Ct","18","8157731234")#Information for person 1
        print(person1.get_name())#Prints name
        print(person1.get_address())#Prints address
        print(person1.get_age())#Prints age
        print(person1.get_phone())#Prints phone number
        person2=Person("Alex Smith","123 Main St","20","8157772425")#Information for person 2
        print(person2.get_name())#Prints name
        print(person2.get_address())#Prints address
        print(person2.get_age())#Prints age
        print(person2.get_phone())#Prints phone number
        person3=Person("Joe Johnson", "545 Diaz Rd","24","8152374567")#Information for person 3
        print(person3.get_name())#Prints name
        print(person3.get_address())#Prints address
        print(person3.get_age())#Prints age
        print(person3.get_phone())#prints phone number
        

main()#Runs program
    