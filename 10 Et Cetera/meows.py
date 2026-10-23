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










                # datetime - module is used to work with dates and times






# import datetime 

# print("Current date and time: ", datetime.datetime.now())




# from datetime import date

# print("Today's date: ", date.today())
# print("Today's date: ", datetime.date.today()) # same




# from datetime import datetime

# now = datetime.now()

# print("Date: ", now.date())  # Date only
# print("Time: ", now.time())  # Time only
# print("Hour: ", now.year)
# print("Month: ", now.month)
# print("Day: ", now.day)
# print("Hour: ", now.hour)
# print("Minute: ", now.minute)
# print("Second: ", now.second)





# from datetime import datetime

# now = datetime.now()

# print("Weekday Short: ", now.strftime("%a")) 
# print("Weekday Full: ", now.strftime("%A")) 

# print("DD-MM-YYYY: ", now.strftime("%d-%m-%Y")) # strftime() to convert a datetime object into a formatted string
# print("HH:MM:SS: ", now.strftime("%H:%M:%S"))
# print("DD/MM/YYYY HH:MM:SS", now.strftime("%d/%m/%Y %I:%M %p")) # H- 24hour , I- 12hour, p- AM/PM




# get the day of a month 
# import datetime

# d1 = datetime.datetime.now()
# print("Day of month: " ,d1.strftime("%d"))

# d2 = datetime.datetime(2026, 10, 15)
# print("Day of month: ", d2.strftime("%d"))





# Get the month name 
# import datetime as dt

# d1 = dt.datetime.now()
# print("Month name: ", d1.strftime("%b"))

# d2 = dt.datetime(2026, 10, 11)
# print("Month name: ", d2.strftime("%B")) # Full





# import datetime 


# d1 = datetime.datetime.now()
# print("Day number of the year: ", d1.strftime("%j"))
# print("Week number of the year: ", d1.strftime("%U"))

# d2 = datetime.datetime(2026, 10, 19, 16, 23, 33)
# print("Day number of the year: ", d2.strftime("%j"))
# print("Week number of the year: ", d2.strftime("%U"))





# # Parsing strings — Converting text into dates

# from datetime import datetime

# date_text = "23-10-2026"

# result = datetime.strptime(date_text, "%d-%m-%Y") #     strptime means string parse time.

# print(result)
# # 2026-10-23 00:00:00
# print(type(result))
# # <class 'datetime.datetime'>


# text = "23-10-2026 05:45 PM"
# result = datetime.strptime(
#     text, "%d-%m-%Y %I:%M %p"
# )
# print(result)
# # 2026-10-23 17:45:00






# import datetime

# dt1 = datetime.datetime(2026, 8, 10)
# dt2 = datetime.datetime(2026,7, 10)

# if(dt1 > dt2):
#     print("Date1 is greater")
# elif(dt1 < dt2):
#     print("Date2 is greater")
# else:
#     print("Both date are equal")





# import time as t

# local_datetime = t.localtime() # local time of your country (UTC+6)
# print("Local: ", local_datetime)
# print("UTC: ", t.gmtime()) # converts current system time into UTC time structure

# sec = t.time() # total number of seconds since January 1, 1970
# print("Timestamp: ", sec)






# Naive vs. aware datetime - (naive datetime has no time-zone information attached || aware datetime contains time-zone information sufficient to identify a particular moment in time)



# from datetime import datetime, timezone

# # Naive datetime
# dt1 = datetime(2026, 10, 23, 15, 0)

# # Aware datetime in UTC
# dt2 = datetime(2026, 10, 23, 15, 0, tzinfo=timezone.utc) # UTC gives us a common reference time. We add or subtract the timezone offset to get another country's local time.

# print(dt1)
# # 2026-10-23 15:00:00

# print(dt2)
# # 2026-10-23 15:00:00+00:00
# print(dt2.isoformat())





# from datetime import datetime, timezone, timedelta

# utc_now = datetime.now(timezone.utc) # gives current date time with utc

# print(utc_now)

# bd_fixed = timezone(timedelta(hours=6)) 

# dt = datetime(2026, 10, 23, 15, 0, tzinfo=bd_fixed) # gives that time with timezone info +06:00
# # dt = datetime.now(bd_fixed) # gives Bangladesh time

# print(dt)






# from datetime import datetime
# from zoneinfo import ZoneInfo

# # # with specific date time
# # dhaka = datetime(
# #     2026, 10, 23, 15, 0,
# #     tzinfo=ZoneInfo("Asia/Dhaka")
# # )

# # with Your timezone
# dhaka = datetime.now(ZoneInfo("Asia/Dhaka")) # Dhaka zone time
# new_york = dhaka.astimezone(ZoneInfo("America/New_York")) # .astimezone() - Convert a datetime between time zones

# print(dhaka)
# print(new_york)

# # # with UTC 
# # utc_time = datetime.now(ZoneInfo("UTC"))

# # dhaka_time = utc_time.astimezone(ZoneInfo("Asia/Dhaka"))
# # newyork_time = utc_time.astimezone(ZoneInfo("America/New_York"))

# # print(dhaka_time)
# # print(newyork_time)




# # ISO-formatted string
# from datetime import date, datetime

# d = date(2026, 10, 23)
# dt = datetime(2026, 10, 23, 15, 30)

# print(d.isoformat())
# # 2026-10-23

# print(dt.isoformat())
# # 2026-10-23T15:30:00





# import calendar
# # print full calendar
# print(calendar.calendar(2026, 2, 1, 5)) # year, width of each date column, number of lines per week, number of spaces between month columns

# # Print only the month's calendar
# year = 2026
# month = 10

# print(calendar.month(year, month))




# # Check Leap Year
# import calendar

# print(calendar.isleap(2024))  # True
# print(calendar.isleap(2025))  # False
# print(calendar.isleap(2000))  # True
# print(calendar.isleap(1900))  # False





# import calendar

# result = calendar.monthrange(2026, 10) # 2026, October

# print(result)      # (3, 31) - This tells us October 2026 starts on a Thursday (3) and contains 31 days
# print(result[0])   # 3
# print(result[1])   # 31




# # Find last day of a month
# import calendar

# year = 2026
# month = 2

# last_day = calendar.monthrange(year, month)[1]

# print(last_day)  # 28






# from datetime import datetime, timedelta        # timedelta represents a duration

# now = datetime.now() 

# minute = now + timedelta(minutes=30)
# tomorrow = now + timedelta(days=1)
# yesterday = now - timedelta(days=1)
# next_week = now + timedelta(weeks=1)
# duration = timedelta(days=2, hours=5, minutes=30)


# print("Now:", now)
# print("After 30 minutes:", minute)
# print("Tomorrow:", tomorrow)
# print("Yesterday:", yesterday)
# print("Next week:", next_week)
# print("Duration:", now + duration)





#  Subtract two dates

# from datetime import date

# start = date(2026, 10, 1)
# end = date(2026, 10, 23)

# difference = end - start

# print(difference)       # 22 days, 0:00:00
# print(difference.days)  # 22




# # Calculate someone age in days

# from datetime import date

# birthday = date(2005, 5, 10)
# today = date(2026, 10, 23)

# age_in_days = (today - birthday).days

# print(age_in_days)






# # Calculate the difference between two times

# from datetime import datetime

# start = datetime(2026, 10, 23, 9, 15)
# end = datetime(2026, 10, 23, 17, 45)

# duration = end - start

# print(duration)                 # 8:30:00
# print(duration.total_seconds()) # 30600.0









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