    #   An exception is a runtime error that Python “throws” when something goes wrong, like dividing by zero or opening a file that doesn’t exist. Python uses try and except to handle errors safely.

   
    # try → code that may fail
    # except → handles error
    # else → runs if no error happens
    # finally → always runs


    # ZeroDivisionError → dividing by zero
    # ValueError → wrong type of value
    # TypeError → wrong type used in operation
    # FileNotFoundError → file not found



            # try-except


# try:  # try → code that may fail
#     x = int(input("Enter an integer : "))
#     print(F"x is {x}")
# except ValueError:    # except → handles error / ValueError → wrong type of value
#     print("That's not an integer")




        # try except else


# try:
#     x = int(input("Enter an integer : "))
# except ValueError:
#     print("That's not an integer")
# else:   # else → runs if no error happens
#     print(F"x is {x}")






# while True: 

#     try:
#         x = int(input("Enter an integer : "))
#     except ValueError:
#         print("That's not an integer")
#     else:   # if try is int than break
#         break
  
# print(F"x is {x}") # if try is int, print





        # pass



# try:
#     x = int(input("Enter a number: "))
#     print(10 / x)
# except ValueError:
#     pass    # pass is a null statement in Python. It is used as a placeholder when Python expects a block of code, but you don’t want to write anything yet.





            # raise



# try:
#     num = int(input("Enter a positive number: "))

#     if num <= 0:
#         raise ValueError("Not a positive number")   #   raise is used to manually trigger an exception (error) in Python.

#     print("Valid number:", num)

# except ValueError as e: # ValueError message is saved in e
#     print("Error:", e)





        #   finally



# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# finally:    #   Run this code no matter what
#     print("This always runs")









# try:
#     num = input("Enter a positive number: ")

#     # convert input to integer
#     num = int(num)

#     # custom validation
#     if num <= 0:
#         raise ValueError("Number is not positive")

# except ValueError as e:
#     # if anything goes wrong, handle it
#     print("Error:", e)
#     pass  # ignore extra handling (do nothing extra)

# else:
#     # runs only if NO error happened
#     print("Success! You entered:", num)

# finally:
#     # always runs
#     print("Program finished (cleanup done)")