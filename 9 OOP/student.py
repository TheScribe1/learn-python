                # Object-Oriented Programming (OOP) is a programming paradigm that organizes software into objects instead of just functions.

                # An object contains:

                # Data (Attributes / Properties)
                # Behavior (Methods / Functions)




# def main():
#     student = get_student()
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")



# def get_student():
#     name = input("Name :")
#     house = input("House:")
#     return [name, house]    # A list is one way to group multiple values into a single object also mutable(house).


# if __name__ == "__main__":
#     main()






# def main():
#     student = get_student()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     print(f"{student['name']} from {student['house']}")



# def get_student():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student


# if __name__ == "__main__":
#     main()

    








                # Class - a blueprint that defines what an object should look like.
                # Object - An object is an instance of a class.
                # Constructor - The constructor(__init__) initializes the object 
                # Self - Self means this current object.
                # Attribute - Attributes are variables inside objects
                # Methods - Methods are functions inside a class






# class Student:  # Empty Student class (use Capital letter)
#     ...     #   Ellipsis(Python object). Here it's just a placeholder, similar to pass(do nothing).



# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")



# def get_student():
#     student = Student() # student (object)
#     student.name = input("Name :")     # name(attributes)
#     student.house = input("House :")     # house(attributes)
#     return student

# if __name__ == "__main__":
#     main()

    





        #  ( __init__, __str__ ) -->  They are called magic methods (also called dunder methods because of the double underscores).




# class Student:
#     def __init__(self, name, house):  # __init__ (a constructor, It runs immediately after an object is created.)  |  self means this current object
#         self.name = name
#         self.house = house


# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")


# def get_student():
#     name = input("Name :")
#     house = input("House :")
#     student = Student(name, house)
#     return student


# if __name__ == "__main__":
#     main()







        # (__str__) -> Returns a human-readable description of the object. (Called automatically when an object is converted to a string) 





# class Product:

#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.name} - ${self.price}"
    

# product = Product("Laptop", 999)
# print(product)










# class Student:

#     def __init__(self, name, house, patronus):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self.name = name
#         self.house = house
#         self.patronus = patronus


#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return "🦌"
#             case "Otter":
#                 return "🦦"
#             case "Jack Russell Terrier":
#                 return "🐕"
#             case _:
#                 return "🪄"


# def main():
#     student = get_student()
#     print("Expecto Patronum!")
#     print(student.charm())


# def get_student():
#     name = input("Name :")
#     house = input("House :")
#     patronus = input("Patronus: ")
#     return Student(name, house, patronus)
   

# if __name__ == "__main__":
#     main()









                # Properties - usually refer to a feature that lets you access methods like attributes while still controlling how values are read, modified, or validated. (getter, setter)


                # Decorator @ - A decorator is a callable that wraps a function or class to add, modify, or extend its behavior while preserving the original code.





# class Student:

#     def __init__(self, name, house, patronus):
#         if not name:
#             raise ValueError("Missing name")
        
#         self.name = name
#         self.house = house
        


#     def __str__(self):
#         return f"{self.name} from {self.house}"

#     #Getter
#     @property      # also call decorators
#     def house(self):
#         return self._house
    
#     #Setter
#     @house.setter     # decorator
#     def house(self, house):
#           if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#             self._house = house


# def main():
#     student = get_student()
#     student.house = "Number Four, Privet Drive"
#     print(student)

# def get_student():
#     name = input("Name :")
#     house = input("House :")
#     return Student(name, house)
   

# if __name__ == "__main__":
#     main()










                    # Class Method - A class method is a method that receives the class(cls) as its first argument instead of the object. 



        # instead of this

# import random

# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

#     def sort(self, name):
#         print(name, "is in", random.choice(self.houses))

# hat = Hat()
# hat.sort("Harry")




#         # Use this classmethod


# import random

# class Hat:
#       houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
#       @classmethod  # Decorator
#       def sort(cls, name):
#         print(name, "is in", random.choice(cls.houses))


# Hat.sort("Harry")






# class Student:

#     def __init__(self, name, house):
#         self.name = name
#         self.house = house

#     @classmethod
#     def from_csv(cls, line):
#         name, house = line.split(",")
#         return cls(name, house)

#     def display(self):
#         print(f"Name : {self.name}")
#         print(f"House: {self.house}")


# # Normal constructor
# s1 = Student("Alice", "Gryffindor")
# s1.display()

# print("-")






                # Inheritance   - a child class can use the code of a parent class instead of writing it again.





# class Wizard:   # Parent class
#     def __init__(self, name):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name

# class Student(Wizard):  # Child class of Wizard
#     def __init__(self, name , house):
#         super().__init__(name)  #   super() calls the parent class's method so the child class can reuse the parent's code instead of writing it again.
#         self.house = house

# class Professor(Wizard):        # Child class of Wizard
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject  

# wizard = Wizard("Dumbledore")
# student = Student("Harry", "Gryffindor")
# professor = Professor("Snape", "Potions")

# print(wizard.name)
# print(student.name, student.house)
# print(professor.name, professor.subject)





                # Operator Overloading - Operator overloading is the ability to give Python's built-in operators (such as +, -, *, ==, <) custom behavior for user-defined objects by implementing special methods.



# class Vault:
#     def __init__(self, galleons=0, sickles=0, knuts=0):
#         self.galleons = galleons
#         self.sickles = sickles
#         self.knuts = knuts

#     def __str__(self):
#         return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

#     def __add__(self, other):   # here self is potter and other is weasly
#         galleons = self.galleons + other.galleons
#         sickles = self.sickles + other.sickles
#         knuts = self.knuts + other.knuts
#         return Vault(galleons, sickles, knuts) 

# potter = Vault(100, 50, 25)
# print(potter)

# weasly = Vault(25, 50, 100)
# print(weasly)

# total = potter + weasly
# print(total)