'''Define a Pet Class:
Create private properties: owner_first_name, owner_last_name, pet_id, pet_name, and pet_type.
Set a default value for pet_type as "Dog".
Implement getter and setter methods for all properties.
Include a class variable vet_name set to the name of your veterinary office.
Add a method display_pet_info to print all details of the pet and owner.
Create Pet Objects:
Instantiate at least three pet objects with different details.
Show the use of setter methods for at least one pet object.
Implement Property Existence Check:
Write a function check_property that uses hasattr() to verify if a property exists in a pet object.
Display Information:
Use display_pet_info to print details for each pet.
Show three examples of check_property being used on various properties and pets.
show two examples of display_pet_info on different instances of pet that you create
'''
class Pet:#Defines pet class
    vet_name="Marengo Animal Hospital"
    def __init__(self,owner_first_name,owner_last_name,pet_id,pet_name,pet_type="Dog"):
        self.__owner_first_name=owner_first_name#Variable
        self.__owner_last_name=owner_last_name#Variable
        self.__pet_id=pet_id#Variable
        self.__pet_name=pet_name#Variable
        self.__pet_type=pet_type#Variable
    def get_owner_first_name(self):#Accessing variable
        return self.__owner_first_name
    def get_owner_last_name(self):#Accessing variable
      return self.__owner_last_name#Returns variable
    def get_pet_id(self):#Accessing variable
        return self.__pet_id#Returns variable
    def get_pet_name(self):#Accessing variable
     return self.__pet_name#Returns variable
    def get_pet_type(self):#Accessing variable
        return self.__pet_type#Returns variable
    
    def set_owner_first_name(self,first_name):#Sets variable
        self.__owner_first_name = first_name
    def set_owner_last_name(self,last_name):#Sets variable
        self.__owner_last_name=last_name
    def set_pet_id(self,pet_id):#Sets variable
        self.__pet_id=pet_id
    def set_pet_name(self,pet_name):#Sets variable
        self.__pet_name=pet_name
    def set_pet_type(self,pet_type):#Sets variable
        self.__pet_type=pet_type

    def display_pet_info(self):#Displays pet info
        print("Owner:",self.__owner_first_name, self.__owner_last_name)#Prints owner name
        print("Pet Id:",self.__pet_id)#Prints pet ID
        print("Pet Name:",self.__pet_name)#Prints pet name
        print("Pet Type:",self.__pet_type)#Prints pet type
        print("Vet Office: ",self.vet_name)#Prints vet name

def check_property(obj,prop_name):
     return hasattr(obj,prop_name)

pet1 = Pet("Cory", "Castaneda", "1", "Cleo", "Cat")#Information for pet 1
pet2 = Pet("John", "Smith", "2", "Cocoa", "Dog")#Information for pet 2
pet3 = Pet("Steve", "Johnson", "3", "Snowball", "Dog")#Information for pet 3

pet2.set_pet_name("Fluffy")#Changes pet 2 name

pet1.display_pet_info()#Displays pet info
pet2.display_pet_info()#Displays pet info
pet3.display_pet_info()#Displays pet info

print("Check if pet1 has __pet_name:", check_property(pet1, "_pet__pet_name"))#Property check
print("Check if pet3 has __owner_last_name:", check_property(pet3, "_pet__owner_last_name"))#Property check
print("Check if pet2 has __pet_id:", check_property(pet2, "_pet_id"))#Property check