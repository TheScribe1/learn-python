            # Type hints - Type hints are annotations that tell Python (and other programmers) what type of data a variable, parameter, or return value is expected to have.




# def add(a: int, b: int) -> int:     #  a: int (hinting a should be integer) | -> int: (return type should be integer) 
#     return a + b

# print(add(10, 20))
# # print(add("10", "20")) # type hints doesnot enforces 






# class Student:
#     def __init__(self, name: str, age: int):    # type hints can be multiple type
#         self.name = name
#         self.age = age

#     def introduce(self) -> str:
#         return f"My name is {self.name}"






# def meow(n: int) -> None:   # -> None: (return type can be int or None)
#     for _ in range(n):
#         print("meow") 

# number: int = int(input("Number: "))
# meows: str = meow(number)
# print(meows)    # meows variable prints None





# def meow(n: int) -> None:   # -> None: (return type can be int or None)
#     for _ in range(n):
#         # print("meow") # 1
#         return "meow\n" * n     # this doesnot returns None

# number: int = int(input("Number: "))
# meows: str = meow(number)
# # meow(number)    # 1 (directly calling doesnot prints extra space)
# print(meows, end="")    # end = "" (removes extra space)









                # Docstring - A docstring is a string written as the first statement inside a module, class, function, or method that describes what it does. 

                # People can read comment from source code but Python or IDEs can't read them , so we use docstring . They are also stored in __doc__




# def greet():
#     """Print a greeting."""
#     print("Hello")


# # help(greet) # shows doctring and function works
# # print(greet.__doc__)# shows only docstring










            # argparse  - A Python module used to parse and manage command-line arguments provided by the user when running a Python program.

            # sys.argv - we need to remember order of input and parse them manually , better for easy and small Command line works but argparse is CLI library who does all these automatically and use for bigger CLI projects 





# import argparse # read things typed after your program name.

# parser = argparse.ArgumentParser()  # This creates an object that knows how to read command-line arguments.
# parser.add_argument("name") #  we expect one argument called name.
# args = parser.parse_args()  # reading the arguments 
# print(f"Hello {args.name}") # args.name contains the name





# import argparse

# parser = argparse.ArgumentParser()

# parser.add_argument("name")   # name is positional argument , if input not given it will throw error
# parser.add_argument("age", type=int)    # without type=int, age will be string

# args = parser.parse_args()

# print(args.name)
# print(args.age)





# import argparse

# parser = argparse.ArgumentParser(description="Meow like a cat") # description - Describes the entire program. (--help - for checking)
# parser.add_argument("-n", default=1, help="number of times to meow", type=int)  # ( -n | --n ) optional arguments - if not given it will show None.   (default= )- if no input is given it will put default value. (required = True) - input is needed , if no input is given it will throw error. (help= ) - Describes one specific argument. 
# args = parser.parse_args()

# for _ in range(args.n):
#     print("Meow")






        # --verbose - is an optional flag that tells a program to display more detailed information about what it is doing.





# import argparse

# parser = argparse.ArgumentParser(
#     description="Backup files."
# )

# parser.add_argument(
#     "source", # variable
#     help="Source folder"
# )

# parser.add_argument(
#     "destination",  # variable
#     help="Destination folder"
# )

# parser.add_argument(
#     "--verbose",    # actual command-line option, name is not reserved. You can write --debug or anything. action is main
#     action="store_true", # if in command line --verbose appears, store true else false
#     help="Show detailed progress"
# )

# args = parser.parse_args()  # This is where the parser actually reads the command line.

# if args.verbose: # if true
#     print(f"[INFO] Reading files from {args.source}")

# # Simulate backup
# if args.verbose:
#     print("[INFO] Copying files...")

# if args.verbose:
#     print(f"[INFO] Saving files to {args.destination}")

# print("Backup completed.")  

# #   run : python meows.py photos backup --verbose





        # --output - is an optional argument that lets the user specify where the program should save its output (usually a file)



# import argparse

# parser = argparse.ArgumentParser(
#     description="Generate student report."
# )

# parser.add_argument(
#     "--output", # Unlike --verbose, this one expects a value.if not given file won't be created
#     help="Output file name"
# )

# args = parser.parse_args()

# report = """
# Student Report
# --------------
# Alice : 90
# Bob   : 85
# """

# if args.output: # if true
#     with open(args.output, "w") as file:     # Create a file name "fileName"
#         file.write(report)  # Write the report string into that file.

#     print(f"Report saved to {args.output}")

# else:
#     print(report)


# run : python meows.py --output report.txt







# import argparse

# parser = argparse.ArgumentParser(
#     description="Choose color from them"
# )

# parser.add_argument(
#     "--color",
#     choices=["red", "green", "blue"],
#     default=None
# )

# args = parser.parse_args()

# if args.color is None:
#     print("You didn't select any color.")
# else:
#     print(args.color)










                # Map - Return an iterator that applies a function to every item of an iterable.







# Basic syntax

# map(function, iterable)




# numbers = [1, 2, 3, 4]
# result = map(lambda x: x*x, numbers)
# print(result) # returns lazy(Python doesn't compute everything immediately.) iterator, waits for someone to ask for result 

# # print(next(result)) # ask to see result one at a time 
# # print(next(result)) 
# # print(next(result))

# print(list(result)) # to print all use list




        #using custom function

# def cube(x):
#     return x ** 3
# print(list(map(cube, [1,2,3])))


# print(list(map(str, [1,2,3])))  # using built-in function
# print(list(map(float, ["1","2","3"])))



        # Multiple iterables


# a = [1,2,3]
# b = [10,20,30]

# result = map(lambda x,y: x+y, a,b)
# print(list(result))





        # map vs list comprehension


# use map with existing function

# list(map(str, ids))
# list(map(int, values))
# list(map(json.loads, messages))
# list(map(datetime.fromisoformat, timestamps))



# When NOT to use map

# list(map(lambda x: x.name.upper().strip().replace("A","B"), users)) # hard to read




# numbers = [1,2,3]

# result = map(str,map(lambda x:x*x,numbers)) # usually not readable like list comprehension
# # result = [str(x*x) for x in numbers]    # instead use list comprehension
# print(list(result))





# numbers = [1,2,3,4]

# result = map(lambda x:x*x,filter(lambda x:x%2==0,numbers)) # hard to read
# # result = [x*x for x in numbers if x%2==0]   # use list comprehension

# print(list(result))






# def main():
#     yell("This", "is", "Python")

# def yell(*words):
#     uppercased = map(str.upper, words)
#     print(*uppercased)

# if __name__ =="__main__":
#     main()





                # filter() - Keep only the items for which a function returns True.


# filter(function, iterable)



    # using for loop normal use

# numbers = [1,2,4,6,7,9]
# result = []
# for n in numbers:
#     if n % 2 == 0:
#         result.append(n)

# print(result)




    # using filter


# def even(x):
#     return x % 2 == 0

# numbers = [1,2,3,4,5,6]
# result = filter(even, numbers) # filter works like for loop who keeps item which is true to condition
# print(result) # gives lazy iterator like map

# # print(next(result)) # shows one item

# # print(list(result))     # shows all item in list







                # reduce() - Repeatedly combine two values until only one value remains.




# reduce(function, iterable)


        # using normal loop

# numbers = [1,2,3,4]
# total = 0
# for n in numbers:
#     total += n

# print(total)



        # using reduce()


# from functools import reduce

# numbers = [1,2,3,4]
# total = reduce(lambda a,b: a+b, numbers)
# print(total)





    # Total revenue


# from functools import reduce

# orders = [
#     {"amount":100},
#     {"amount":200},
#     {"amount":300}
# ]

# total = reduce(
#     lambda total, order: total + order["amount"],
#     orders,
#     0 # The starting value(total = 0).
# )

# print(total)