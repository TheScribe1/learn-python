            #   File I/O means File Input/Output.

                    # Input = reading data from a file
                    # Output = writing data to a file



                #  Write


# name = input("Enter a name : ")

# file = open ("names.txt", "a")  # open() function opens a file - open(filename, mode) - "a" → append mode.
# file.write(f"{name}\n")     # write() - writes data to a file. \n gives next line after each name
# file.close()    # close() - Closes the file after writing. it's important to save all changes, free system resources, prevents file corruptions





            # Best Practice




# name = input("Enter a name: ")

# with open("names.txt", "a") as file:    # with - Automatically closes the file, less chance of forgetting close()
#     file.write(f"{name}\n")





                #   Read




# with open("names.txt", "r") as file:    # "r" → read mode.
#     lines = file.readlines()    #   readlines() - reads all the lines in list with \n 

# for line in lines:
#     print(line, end="") # end="" - to remove that extra \n

    


            # Another way to read 



# with open("names.txt", "r") as file:
#     for line in file:
#         print(line.rstrip())    # rstrip - removes extra \n







            # sort content and print using list



# names = []

# with open("names.txt") as file:     # if you open a file to read it you don't need to specify "r", it's default
#     for line in file:
#         names.append(line.rstrip())

# # for name in sorted(names):
# for name in sorted(names, reverse=True):    # sort in reverse
#     print(name)





            # Another way to sort content and print



# with open("names.txt") as file:
#     for line in sorted(file):
#         print(line.rstrip())






# with open("students.csv") as file:
#     for line in file:
#         # row = line.rstrip().split(",")
#         # print(f"{row[0]} is in {row[1]}")
#         name, house = line.rstrip().split(",")    #another way
#         print(f"{name} is in {house}")







            #       sort by name




# students = []   # list (a list can contain many dict inside it)

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name" : name, "house" : house}    # Dictionary
#         students.append(student) # add dict in list


# def get_name(student):
#     return student["name"]  # taking name 

# # for student in sorted(students, key=get_name):
# for student in sorted(students, key=lambda student : student["name"]):  # alternative for get_name function . ( lambda parameter: expression ) A lambda in Python is a way to create a small anonymous function (a function without a name) in a single line.
#     print(f"{student['name']} is in {student['house']}")






                # sort by name if there is multiple ' , ' in csv




# import csv

# students = []   

# with open("students.csv") as file:
#     reader = csv.reader(file)   # csv.reader() - reads a CSV file and converts each row into a list of fields, correctly handling commas, quotes, and other CSV formatting rules.
#     for name , home in reader:  # we did directly because we know there are only two variable or else we would've use index (for row in reader:)
#         students.append({"name" : name, "home" : home}) # index[0] , index[1]....

# for student in sorted(students, key=lambda student : student["name"]): 
#     print(f"{student['name']} is from {student['home']}")







# import csv

# students = []   

# with open("students.csv") as file:
#     reader = csv.DictReader(file)   # csv.DictReader() - automatically creates dictionaries from column names, which is often the most convenient way to work with CSV files.
#     for row in reader:
#         students.append({"name" : row["name"], "home" : row["home"]}) 

# for student in sorted(students, key=lambda student : student["name"]): 
#     print(f"{student['name']} is from {student['home']}")


 



    # Write csv data



# import csv

# name = input("What's your name? ")
# home = input("Where's your home? ")

# with open("students.csv","a", newline="") as file:
#     writer = csv.DictWriter(file, fieldnames=["name", "home"])
#     writer.writerow({"name": name, "home": home})



