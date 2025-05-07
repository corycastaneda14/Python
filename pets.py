'''Create the Pet Class:
Define a Pet class with attributes: kind (e.g., dog, cat), breed, and name.
Implement get and set methods for each of these attributes.
Add a method called print_details that prints the details of the pet.
Create Instances:
Create three objects of the Pet class with different kinds, breeds, and names.

Call the print_details method for each object that you created

Demonstrate a Special Method or Function:
Choose three of the following and demonstrate its use with the Pet class instances:

__name__: Display the name of the class.
type(): Show the class used to instantiate a pet object.
__module__: Return the module name in which the Pet class is defined.
__bases__: Display the base classes of the Pet class (if any).
isinstance(): Check if an instance is of the Pet class.'''
class Pet:#Defines pet class
    def __init__(self,kind,breed,name):
        self.__kind=kind#Variable
        self.__breed=breed#Variable
        self.__name=name#Variable
    def get_kind(self):#Accessing variable
        return self.__kind#Returns variable
    def get_breed(self):#Accessing variable
        return self.__breed#Returns variable
    def get_name(self):#Accessing variable
        return self.__name#Returns variable
    def set_kind(self,kind):#Sets variable
        self.__kind=kind
    def set_breed(self,breed):#Sets variable
        self.__breed=breed
    def set_name(self,name):#Sets variable
        self.__name=name
    def print_details(self):#Prints
        print("Kind:",self.__kind)
        print("Breed:",self.__breed)
        print("Name:",self.__name)
        
pet1 = Pet("Cat", "Tuxedo", "Cleo")#Pet 1 information
pet2 = Pet("Dog", "Poodle", "Fluffy")#Pet 2 information
pet3 = Pet("Rabbit", "Cottontail", "Cocoa")#Pet 3 information

pet1.print_details()#Prints pet 1
pet2.print_details()#Prints pet 2
pet3.print_details()#Prints pet 3
print("Class name using __name__:", Pet.__name__)#Displays class name
print("Type of pet1:", type(pet1))#Shows the class used to instantiate a pet object
print("Is pet2 an instance of Pet?", isinstance(pet2, Pet))#Checks if an instance is of the pet class