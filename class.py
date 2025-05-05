'''Class Creation: Design a class named Person with the following data: name, address, age, and phone number.
Accessor and Mutator Methods: Write get and set methods for each piece of data. These methods allow you to access and change the data safely.
Creating Instances: Write a program that creates three instances (objects) of the Person class. Use one instance for your made-up information and the other two for imaginary friends or family members.
Display Data: Print out the information stored in each instance. Ensure the output is formatted and easy to read.
'''
class Person:
    def __init__(self,name, address,age, phone):
        self._name=name
        self._address=address
        self._age=age
        self._phone=phone
    def get_name(self):
        return self.name
    def get_address(self):
        return self._address 
    def get_age(self):
        return self._age 
    def get_phone(self):
        return self._phone 
    def set_name(self,name):
        self._name=name
    def set_address(self,address):
        self._address=address
    def set_age(self,age):
        self._age=age
    def set_phone(self,phone):
        self._phone=phone
    def get_info(self):
        return f"Name:{self._name} Address:{self._address} Age:{self._age} Phone Number:{self._phone}"
def main():
        person1=Person("Cory Castaneda","822 Hickory Ct","18","8159096413")
        person2=Person("Alex Smith","123 Main St","20","8157772425")
        person3=Person("Joe Johnson", "545 Diaz Rd","24","8152374567")
        print(person1.get_info())
        print(person2.get_info())
        print(person3.get_info())

main()
    