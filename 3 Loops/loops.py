

# i = int(input("Enter a number : "))

# while i != 0:

#     print("Python")

#     i += 1  # python doesnot have i++ increment






# for i in [0,1,2]:
#     print("Python")


# for i in range(7):
#     print(f"Python {i}")





        # Ask until the value is positive



# while True:
#     n = int(input("Enter a number :"))
#     if n > 0:
#         break

# for i in range(n):
# # for _ in range(n):    # use ( _ ) when i value is not needed 
#     print(f"Python {i}")






# def cat():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("Enter n : "))
#         if n > 0:
#             break
#     return n


# def meow(n):
#     for _ in range(n):
#         print("Meow...")

# cat()




        # print square using nested loops


# def main():
#     n = int(input("Enter size of square : "))
#     print_square(n)

# def print_square(size): 
#     for i in range(size):   # print row
#         for j in range(size): # print column in that row
#             print("#", end = "") # python stops automatically printing \n because of end = ""
#         print() # prints \n after loop of j

# main()




        # print square using single loop string mulitplication



# def main():
#     n = int(input("Enter size of square : "))
#     print_square(n)

# def print_square(size): 
#     for i in range(size):   # print row
#         print("#" * size)   # string multiplication

# main()



        # print square
        # this kind of code are split into multiple smaller function for larger , reuseable , organized code 




# def main():
#     n = int(input("Enter size of square : "))
#     print_square(n)

# def print_square(size):   # printing rows repeatedly
#     for i in range(size):  
#         print_row(size)

# def print_row(width):     # printing one row
#     print("#"* width)  

# main()









# List 

# students = ["Henry", "Tony", "Blum"]

# print(students[0])
# print(students[1])
# print(students[2])

    
# for student in students:
#     print(student)

# for i in range(len(students)):  # range takes integer so we use length
#     print(i+1, students[i])








        # Dictionary


# students = {
#   "Hermione" : "Gryffindor",    # key : value
#   "Harry" : "Gryffindor",
#   "Ron" : "Gryffindor",
#   "Draco" : "Slytherin",
#  }

# print(students["Ron"])

# for student in students:
#     print(student, students[student], sep=", ")




    # List of Dictionary

# A list of dictionaries is used when you need to store multiple items (list) where each item has multiple named properties (dictionary).


# students = [
#     {"name" : "Hermione", "house" : "Gryffindor", "patronus" : "Otter"},
#     {"name" : "Harry", "house" : "Gryffindor", "patronus" : "Stag"},
#     {"name" : "Ron", "house" : "Gryffindor", "patronus" : "Jack Russell terrier"},
#     {"name" : "Draco", "house" : "Slytherin", "patronus" : None},   # None is clear than "" , it means no one forgot to input data
# ]

# for student in students:
#     print(student["name"], student["house"], student["patronus"], sep = ", ")











