# This program says hello and asks for my name.

# print('Hello, world!')
# print('What is your name?')  # Ask for their name.
# my_name = input('>')
# print('It is good to meet you, ' + my_name)
# print('The length of your name is:')
# print(len(my_name))
# print('What is your age?')  # Ask for their age.
# my_age = input('>')
# print('You will be' + str(int(my_age) + 1) + 'in a year.')
# print('You will be ' + str(int(my_age) + 1) + ' in a year.')
# print('You will be',str(int(my_age) + 1),'in a year.') # using , gives you space automatically
# print('You will be ' + str(34) + ' in a year.')

# print("Hello", end=' ')     # usually prints \n after output , so here without doing \n , we say print ' ' at end , after that my_name is prints
# print(my_name)


# print(*["Python"]*3, sep="--")
# print(*"Python"*3, sep="--")
# print("Python\n"*3, end= "")
    

# print("Hello, "Friend"")
# print('Hello, "Friend"')
# print("Hello, \"Friend\"")
# my_name = my_name.strip()
# print(f"Hello, {my_name}")

# my_name = my_name.capitalize()
# print(f"Hello, {my_name}")

# my_name = my_name.title()
# print(f"Hello, {my_name}")

# my_name = my_name.strip().title()
# print(f"Hello, {my_name}")

# my_name = my_name.upper()
# print(f"Hello, {my_name}")

# name = input("What's you name? ").strip().title()
# print(f"Hello, {name}")

# first, last = name.split()
# print(f"Hello, {first}")


# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# z = x+y
# print(z)



# x = float(input("Enter x: "))
# y = float(input("Enter y: "))
# z = x + y
# print(z)

# print(round(z,2)) # Round 2 decimal places

# print(f"{z:,}") # [,] means add thousand separators
# print(f"{z:,.2f}") # .2 means 2 decimal places & f = float






            # FUNCTION



     #   No parameters, no return value



# def greet():  # def -> define a function  |   greet() -> function name
#     print("Hello!")

# greet()






        #  Parameters, no return value 




# def greet(name):    # name -> parameter
#     print("Hello", name)

# greet("Hasan")  # "Hasan" -> Argument






        #   No parameters, returns a value



# def get_number():
#     return 100

# x = get_number()
# print(x)





        # Parameter function with return value



# def add(a, b): 
#     return a + b

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# sum = add(a, b)
# print(sum)






# def add(a, b):
#     return a + b

# result = add(10, 20)
# print(result)







        # Multiple returns



# def calculate(a, b):
#     return (a+b, a-b, a*b, a/b)

# x, y, z, xx = calculate(10, 5)
# print(x)
# print(y)
# print(z)
# print(xx)







# def hello(to):
# # def hello(to="World"):    # 1 (default parameter)
#     print("hello,",to)

# # hello()   # 1
# name = input("What's your name : ")
# hello(name)





# def abc(): # first stores main but not calling
#     name = input("What's your name : ")
#     hello(name)

# def hello(to): # then stores the hello function but not calling 
# # def hello(to="World"):    # 1
#     print("hello,",to)

# abc()  # lastly main() calls main and then hello





# def main():
#     x = int(input("Enter x : "))
#     print("x squared is ",square(x))

# def square(n):
#     return pow(n,2)

# main()






        # First class function


# def hello():
#     print("Hello")

# x = hello # first-class behavior | assigning func to another variable
# x() # call through variable
# # hello() # call through func





        #   Passing Function as Argument


# def add(a,b):
#     return a+b

# def calculate(func,a,b):
#     return func(a,b)

# print(calculate(add,3,4))




        #   Returning Function



# def outer():

#     def inner():
#         print("Hello")

#     return inner

# f = outer() # here outer() was called , return inner which becomes f = inner() | if it was f = outer - f would become outer() but it won't run or f won't become inner

# f() # here inner() is called and prints 






                # *args & **kwargs - are special kinds of function parameters that let a function accept a variable ~ number of arguments. 

                        # args and kwargs are not python keywords , * & ** tell Python how to collect the arguments. We can do this *anything, **anything.
                        # *args collects extra positional arguments into a tuple | **kwargs collects extra keyword arguments into a dictionary.



# def show(*args):
#     print(args)

# show(10, 20, 30)





# def show(*args):
#     for value in args:
#         print(value)

# show("apple", 25, True)





# def show(**kwargs):
#     print(kwargs)
#     print(kwargs["name"])

# show(name="Alice", age=25)




# def example(*args, **kwargs):
#     print(args)
#     print(kwargs)

# example(1, 2, 3, name="Alice", age=25)




# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)

# courses = ['Math', 'Arts']
# info = {'name': 'John', 'age': 22}

# # student_info(courses, info)   # if we don't use * & ** , args think both are tuple and kwargs becomes empty. So we need to unpack them | unpacking & args,kwargs looks same
# # student_info(*courses, info)    # *Unpacking one won't help, still it will think they are one
# student_info(*courses, **info)  # Unpacking both will help python to understand which are tuple and which are dict




# def tea_order(customer_name, tea_type, *args, **kwargs):
#     print(f"{customer_name} ordered a {tea_type} tea")
#     for arg in args:
#         print("    -Add:", arg)
#     for key, value in kwargs.items():
#         print("    -Add:", key, ":", value)

# tea_order("Alice", "green")
# tea_order("Bob", "black", sweetner="honey")
# tea_order("Tony", "black", milk="oat", sweetner="sugar")





                #   Lambda - A lambda function is a small anonymous function that can have any number of parameters but only one expression.



# we simply create one expression function like this with name
# def square(x):
#     return x * x

# print(square(5))



# We can simply use lambda with no name function once
# square = lambda x: x*x
# square(5)




        # Multiple parameters

# def add(a, b):
#     return a + b
# print(add(4,2))



# add = lambda a, b: a + b
# print(add(4,2))



        # No Parameters

# greet = lambda: "Hello"
# print(greet())



        # Without lambda using map

# def square(x):
#     return x * x

# numbers = [1,2,3]
# result = list(map(square, numbers))
# print(result)



        # with lambda

# numbers = [1,2,3]
# result = list(map(lambda x: x*x, numbers))
# print(result)




# check = lambda x: "Positive" if x>0 else "Negative"
# print(check(5))






                #   Closures - A closure is a function that remembers variables from its outer function, even after the outer function has finished executing

                # Use for (Factory functions, callbacks)




# def multiplier(n):      # outer func

#     def multiply(x):    # inner func
#         return x*n

#     return multiply    # returning func | this func goes to double

# double = multiplier(2) # double becomes multiply when multiplier triggers return multiply
# print(double(10)) # so multiply(10)




        # Create a discount function.


# def discount(percent):

#     def apply(price):
#         return price * (1 - percent)

#     return apply


# student = discount(0.20)
# vip = discount(0.50)

# print(student(100))
# print(vip(100))






                #   Decorators - A decorator is a function that takes another function, adds extra behavior, and returns the modified function.

                # Use for (Logging, authentication, caching)



# without parameters

# def add_sprinkles(func):
#     def wrapper(): 
#         print("*You add sprinkles 🎊*")
#         func() 
#     return wrapper

# def add_fudge(func):
#     def wrapper():
#         print("*You add fudge 🍫*")
#         func()
#     return wrapper    


# @add_sprinkles
# @add_fudge
# def get_ice_cream():
#     print(f"Here is your ice cream 🍧")

# get_ice_cream()





# With parameters

# import time
# from datetime import datetime, timedelta

# def time_dec(base_fn):
#     def enhanced_fn(*args, **kwargs): # we could use parameters but that will creates problem for those no arguments when calling
#         start_time = time.time()
#         result = base_fn(*args, **kwargs)  # *&**Unpacking 
#         end_time = time.time()
#         print(f"Task time: {end_time - start_time}")
#         return result
#     return enhanced_fn


# @time_dec
# def brew_tea(tea_type, steep_time):
#     print("Brewing tea...")
#     time.sleep(1)
#     print("Tea is ready!")

# @time_dec
# def make_matcha():
#     print("Brewing matcha...")
#     time.sleep(1)
#     print("Matcha is ready!")
#     return f"Drink match by {datetime.now() + timedelta(minutes=30)}"

# # brew_tea = time_dec(brew_tea)   # we can assign same name | but this makes it less obvious to someone reading code that base brew_tea function will be enhanced , so we use @time_dec decorator syntax

# brew_tea("Bubble tea", 2)   # we use *args for no key arguments    
# brew_tea(tea_type="Green", steep_time=1) # we use **kwargs for key arguments
# print(make_matcha())







                # Generators (yield) - A generator function uses yield to produce values one at a time instead of returning everything at once.

                # Large files, streaming, memory efficiency





# def gen_primes(start, end):
#     for num in range(start, end + 1):
#         if num < 2:
#             continue
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             yield num   # generators use yield instead of return. 

# for value in gen_primes(50, 100000):
#     print(value)




        # counting number with iterative

# def count_to(n):
#     numbers = []
#     count = 1
#     while count <= n:
#         numbers.append(count)
#         count += 1
#     return numbers

# number = int(input("Enter a number to count to: "))

# for n in count_to(number):
#     print(n)





        # counting number with generators


# def count_to(n):
#     count = 1
#     while count <= n:
#         yield count
#         count += 1

# number = int(input("Enter a number to count to: "))

# for n in count_to(number):
#     print(n)






# def read_file(file_path):
#     with open(file_path, "r", encoding="utf-8") as file:
#         for line in file:
#             yield line.strip()

# file_path = "D:\\Code\\Python\\1 Function & Variable\\test.txt"
# for line in read_file(file_path):
#     print(line)







                # Async (async/await) - Async - A function defined with async def that returns a coroutine and can suspend execution using await. || Await - An expression used inside an async function to suspend that coroutine until an awaitable operation completes, allowing the event loop to run other tasks in the meantime.
        
                # APIs, web servers, databases





# import asyncio

# async def say_hello(): # async def -> defines async function
#     print("Hello")

# async def main(): # main coroutine
#     await say_hello() # say_hello() creates a coroutine object without await. await run this coroutine and wait until it finishes. so we use await to call a function , without awaiting async function won't work. 

# asyncio.run(main()) # asyncio.run() -> takes that coroutine and starts an asyncio event loop to execute it






# import asyncio

# async def fetch_data():
#     print("Starting...")
#     await asyncio.sleep(3) # Pause this coroutine for 3 seconds so that other tasks can run but does not block the entire event loop
#     print("Finished...")
#     return 'data'
                
# async def main():
#     result = await fetch_data()
#     print(result)

# asyncio.run(main())






# import asyncio

# async def fetch_data(delay):
#     print("Fetching data...")
#     await asyncio.sleep(delay) 
#     print("Data fetched")
#     return {"data": "Some data"}

# async def main():
#     print("Start of main coroutine")
#     task = fetch_data(2)
#     result = await task
#     print(f"Received result: {result}")
#     print(f"End of main coroutine")

# asyncio.run(main())






# import asyncio

# async def fetch_data(delay, id):
#     print("Fetching data... id:", id)
#     await asyncio.sleep(delay)
#     print("Data fetched. id:", id)
#     return {"data": "Some data", "id": id}

# async def main():
#     task1  = fetch_data(2, 1)
#     task2 = fetch_data(2, 2)

#     result1 = await task1
#     print(f"received result: {result1}")

#     result2 = await task2
#     print(f"received result: {result2}")

# asyncio.run(main())





        # create_task() -  is used to schedule a coroutine for concurrent execution and obtain a Task object representing that coroutine.



# import asyncio

# async def fetch_data(id, sleep_time):
#     print(f"Coroutine {id} starting to fetch data.")
#     await asyncio.sleep(sleep_time)
#     return {"id": id, "data": f"Sample data from coroutine {id}"}


# async def main():
#     task1 = asyncio.create_task(fetch_data(1, 2)) # create_task() -> Start this coroutine as a task and let it run independently while I do other things
#     task2 = asyncio.create_task(fetch_data(2, 3))
#     task3 = asyncio.create_task(fetch_data(3, 1))

#     result1 = await task1
#     result2 = await task2
#     result3 = await task3

#     print(result1, result2, result3)

# asyncio.run(main())







# import asyncio
# import time


# async def fetch_data(param):
#     print(f"Do something with {param}")
#     time.sleep(param) # not asyncio.sleep, so BLOCKED EVENT LOOP, NOT YIELD. That's why it's takes 3 seconds
#     print(f"Done with {param}")
#     return f"Result of {param}"


# async def main():
#     task1 = asyncio.create_task(fetch_data(1))
#     task2 = asyncio.create_task(fetch_data(2))

#     result1 = await task1 # after result1, directly goes to result2 without printing (Task 1 fully completed) because result2 in queue 
#     print(f"Task 1 fully completed") 
#     result2 = await task2
#     print(f"Task 2 fully completed")
#     return [result1, result2]

# t1 = time.perf_counter()

# result = asyncio.run(main())
# print(result)

# t2 = time.perf_counter()
# print(f"Finished in {t2 - t1:.2f} seconds")






    

        # gather() ->  is used when you want to execute multiple awaitables concurrently and collect their results.





# import asyncio

# async def fetch_data(id, sleep_time):
#     print(f"Coroutine {id} starting to fetch data.")
#     await asyncio.sleep(sleep_time)
#     return {"id": id, "data": f"Sample data from coroutine {id}"}

# async def main():
#     results = await asyncio.gather(fetch_data(1,2), fetch_data(2,3), fetch_data(3, 1)) # gather() -> Run these coroutines/tasks concurrently and give me all their results together.

#     for result in results:
#         print(f"Received result: {result}")


# asyncio.run(main())






# import asyncio

# async def get_user():
#     return "David Cohen"

# async def get_orders():
#     return "Cheesy garlic butter shrimp"

# async def get_recommendations():
#     return "Garlic Beef Steak"


# async def get_dashboard():
#     user, orders, recommendations = await asyncio.gather(
#         get_user(),
#         get_orders(),
#         get_recommendations(),
#     )

#     return {
#         "user": user,
#         "orders": orders,
#         "recommendations": recommendations,
#     }

# async def main():
#     dashboard = await get_dashboard()
#     print(dashboard)

# asyncio.run(main())





        # TaskGroup() -> provides a structured way to create and manage related task, major advantages is structured error and cancellation handling.




# import asyncio

# async def fetch_data(id, sleep_time):
#     print(f"Coroutine {id} starting to fetch data.")
#     await asyncio.sleep(sleep_time)
#     return {"id": id, "data": f"Sample data from coroutine {id}"}

# async def main():
#     tasks = []

#     async with asyncio.TaskGroup() as tg: # Create a group of related tasks, and don't leave this block until the group is finished.
#         for i, sleep_time in enumerate([2, 1, 3], start=1):
#             task = tg.create_task(fetch_data(i, sleep_time))
#             tasks.append(task)

#     results = [task.result() for task in tasks]

#     for result in results:
#         print(f"Received result: {result}")

# asyncio.run(main())








# import asyncio, time

# async def fetch_data(param):
#     await asyncio.sleep(param)
#     return f"Result of {param}"


# async def main():
#     # Create Tasks Manually
#     task1 = asyncio.create_task(fetch_data(1))
#     task2 = asyncio.create_task(fetch_data(2))
#     result1 = await task1
#     result2 = await task2
#     print(f"Task 1 and 2 awaited results: {[result1, result2]}")

#     # Gather Coroutines
#     coroutines = [fetch_data(i) for i in range (1,3)]
#     results = await asyncio.gather(*coroutines, return_exceptions=True)
#     print(f"Coroutine Results: {results}")

#     # Gather Tasks
#     tasks = [asyncio.create_task(fetch_data(i)) for i in range(1, 3)]
#     results = await asyncio.gather(*tasks)
#     print(f"Task Results: {results}")

#     # Task Group
#     async with asyncio.TaskGroup() as tg:
#         results = [tg.create_task(fetch_data(i)) for i in range(1, 3)]
#         # All tasks are awaited when the context manager exits.
#     print(f"Task Group Results: {[result.result() for result in results]}")

#     return "Main Coroutine Done"


# t1 = time.perf_counter()

# results = asyncio.run(main())
# print(results)

# t2 = time.perf_counter()
# print(f"Finished in {t2 - t1:.2f} seconds")







        # Synchronization


# import asyncio

# shared_resource = 0

# lock = asyncio.Lock() # asyncio.Lock ensures that only one coroutine at a time can execute the protected section of code

# async def modify_shared_resource():
#     global shared_resource
#     async with lock: # important (Everything inside protected by Lock)
#         print(f"Resource before modification: {shared_resource}")
#         shared_resource += 1
#         await asyncio.sleep(1)
#         print(f"Resource after modification: {shared_resource}")

# async def main():
#     await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

# asyncio.run(main())










                # LIST [] - ( ordered, stores any data types , mutable[can change after creation] )

  



# bucket = ['apple','orange', 300.00 , False , 5 , 'Taka']
# print(bucket)

# print(bucket.index(False))  # check index
# print(bucket[0]) # index (0, 1, 2, 3, 4, 5)
# print(bucket[4])
# print(bucket[-1])   # negative index (-6, -5, -4, -3, -2, -1) (-1 is end)
# bucket[0] ='Grape'  #Unlike Strings lists are mutable
# print(bucket)

# print(bucket[0:4])  # Slicing (start from 0, stop before 4)
# bucket.append('Banana') #adds from end
# print(len(bucket))  # length
# print(bucket)

# print("apple" in bucket,"pine" in bucket)    # Membership - Check whether something exists.


# for index, item in enumerate(bucket, start = 1):    # enumerate - It gives you both the index and the value while looping.
#     print(index, item)


# fruits = ["apple", "banana"]
# e = enumerate(fruits)
# print(e)        # Like map(), it returns a lazy iterator
# print(list(e))  # use list to see output but every item is in tuple

# print(bucket.count("apple"))    # count occurrences





            # Note : Methods that modify an object in place usually return None in Python. So modify first then print it.


# marks = [23 , 65 , 12 , 45 ,77 , 90]
# print(sum(marks))
# marks.sort()
# marks.reverse()

# marks.insert(4, 56)     #(index , item)- Insert at a specific position.
# print(marks)

# print(marks.pop(3)) # index-3 , Removes by index

# marks.remove(23)     #(item) remove by value not index
# print(marks)

# marks.extend([1,2,3])
# print(marks)

# marks.append(["Milk", "Bread"]) #   the whole list becomes one item , where extends adds them individually
# print(marks)

# marks.clear()   # removes everything
# print(marks)





# cart = [
#     "Mouse",
#     "Keyboard",
#     "Laptop"
# ]

# backup = cart.copy()

# cart.append("Mouse pad")

# print(backup)
# print(cart)





        # 10% discount



# prices = [100,200,300]

# discounted = [price * 0.9 for price in prices]
# print(discounted)





        #   Nested List




# matrix = [
#     [1,3,5],
#     [2,4,6],
#     [3,6,9]
# ]

# for i in range(len(matrix)):
#     print(matrix[i])

# for row in matrix:
#     for num in row:
#         print(num)




        # List comprehension



# emails = [
#     "Alice@Example.com",
#     "BOB@Example.com"
# ]

# lower = [email.lower() for email in emails]    # list comprehension
# print(lower)








         # Tuple () - (ordered, stores any data types , immutable[cannot change])

         # Design principle: If data should not change after creation, make it immutable.







# a  = (1)        # this is int        
# print(type(a))

# b = (1,)    # you need to add a comma to make it tuple
# b = 5,      # Packing means creating a tuple without explicitly using parentheses
# print(type(b))

# empty1 = ()      # empty tuple

# box = (1, 4 , 342 , 2 , True , 'String' , 4.5 , 4)
# print(box)
# print(box[4])   # index of 4th item
# print(box[-1])  # last item
# print(box.count(4))     #(item) total counts of am item
# print(box.index(4))     # index of first occured item

# tuple1 = (1, 3, 2 )
# tuple2 = (2 , 1 , 4)
# concatenated = tuple1 + tuple2
# print(concatenated)
# print(tuple1*3)
# print(2 in tuple1)      # true or false
# print(len(tuple1))
# print(min(tuple2))
# print(max(tuple2))
# print(tuple2[0:2])

# a , b, c = tuple1   #(1, 3, 2 ) Unpacking
# print(a,b,c)
# print(b)


# data = ("Alice",[1, 2, 3])      # The list inside the tuple changed
# data[1].append(4)
# print(data)


# numbers = (10, 20, 30, 40, 50)
# first, *middle, last = numbers  # Extended Unpacking    
# print(first)
# print(middle)   # becomes list because of *
# print(last)



# students = (    # Nested tuples
#     ("Alice", 90),
#     ("Bob", 85),
#     ("Charlie", 95)
# )
# print(students[1][0])




# board = {}  # Dictionary

# board[(1, 1)] = "White Rook"   # List can't do this , tuple does because of immutable, Dictionary keys must be hashable.
# board[(8, 8)] = "Black Rook"
# print(board)




                #   User Login



# def authenticate(username, password):
#     if username == "alice" and password == "secret":
#         return True, 101, "Alice"
#     return False, None, None


# success, user_id, name = authenticate("alice", "secret")

# if success:
#     print(f"Welcome {name} (ID: {user_id})")
# else:
#     print("Invalid credentials")






 




                 #Dictionary (mutable) - stores key-value pairs. Dict-Keys are immutable






# marks = {
#     "Physics": 89,
#     "Health": 60,
#     "Chemistry": 100,
#     0 : "Math", # key can be int, tuple, string | not list (mutable)
#     "list":[2 , 3 , 1]
# }

# d = {}    #empty dictionary
# d = dict()      # empty dictionary

# print(marks,type(marks))
# print(marks["Health"])  #if not available gives KeyError, looks by hash in memory, not index
# print(marks.get("Mango",))  # get() - if not available gives None , not KeyError
# print(hash("Health"))   # hash changes for security
# print(marks.get("Mango","Not found")) # with default message
# print(marks["list"])
# print(marks.items())  # item = key : value
# print(marks.keys())
# print(marks.values())

# marks.update({"Health": 99})    
# print(marks)

# marks.update({"Chemistry": 90, "English": 88})  # update & add multiple key : value together
# print(marks)

# marks.pop("Health")     #pops specific item
# print(marks)

# marks.popitem()     #pops last item
# print(marks)

# marks["Geometry"] = 90   # another way to Add new key:value
# print(marks)



        # Unpacking(**) - works with dictionaries (or other mapping objects)


# def greet(name, age):
#     print(f"{name} is {age}")

# person = {
#     "name": "Alice",
#     "age": 25
# }

# # greet(person)   # TypeError, can't directly call dict, greet(person["name"], person["age"])

# greet(**person) # Unpacking



        # Search

# marks = {
#     "Physics": 89,
#     "Health": 60,
#     "Chemistry": 100,
#     0 : "Math",
#     "list":[2 , 3 , 1]
# }
# ask = input("Enter the word you want know of : ")
# print(marks[ask])


        # Add 

# list = {}
# friends = input("Enter your friends name : ")
# language = input("Enter the language : ")
# list.update({friends:language})
# print(list)






                # User Record



# user = {
#     "id": 101,
#     "username": "alice",
#     "email": "alice@example.com",
#     "is_admin": False,
#     "last_login": "2026-07-19"
# }

# print(user["username"])
# print(user.get("phone", "No phone number"))
# print ("--------------")
# for key, value in user.items():
#     print(f"{key}: {value}")





                # User updates profile


# user = {
#     "name": "Alice",
#     "email": "old@email.com"
# }

# request_data = {
#     "email": "new@email.com"
# }

# user.update(request_data)
# print(user)







# user = {}

# # if "country" not in user:     # instead of this, try setdefault()
# #     user["country"] = "Bangladesh"

# user.setdefault(    #   setdefault() only inserts the key if it doesn't already exist.    
#     "country",
#     "Bangladesh"
# )

# user.setdefault(     # this won't be inserted
#     "country",
#     "India"
# )

# print(user)





                # Create many keys at once

# keys = [
#     "name",
#     "email",
#     "age"
# ]

# user = dict.fromkeys(
#     keys,
#     None
# )

# print(user)





        # Dictionary Comprehension


# even = {
#     i : i*i
#     for i in range(10)
#     if i % 2 == 0
# }

# for key, value in even.items(): # prints in nextline
#     print(f"{key} : {value}")




                # Nested Dictionary


# user = {
    
#     "id" : 101,

#     "profile" : {
#         "name" : "Alice",
#         "age" : 25
#     },

#     "address" : {
#         "city" : "Sylhet",
#         "country" : "Bangladesh"
#     }
# }

# print(user["profile"]["name"])





        # List of Dictionary (JSON style)




# products = [
#     {
#         "id":1,
#         "name":"Laptop"
#     },

#     {
#         "id":2,
#         "name":"Mouse"
#     }
# ]

# for product in products:
#     print(product["name"])





        # Dictionary of Lists - Useful when one key maps to many values



# students = {
#     "science":[
#         "Alice",
#         "Bob"
#     ],

#     "arts":[
#         "John",
#         "Emma"
#     ]
# }

# print(students["arts"])






        #  Simple Caching System



# database = {
#     101:"Alice",
#     102:"Bob"
# }

# cache = {}

# user_id = 101

# if user_id in cache:
#     print("Cache hit")
# else:
#     print("Database hit")
#     cache[user_id] = database[user_id]










                #  Set(unordered, mutable, only unique value, uses hashing internally)

                # example : Username, email account







# s = set()   #empty set
# empty = {}  # even though dict and set uses {} , this will shows only dict
# print(type(s))

# s1 = {6 ,1, 5.2 , True, 7 ,-4 ,3, 5, 9, 5 , 'Eng'}    #set doesn't take repeatitive items and doesn't maintains order
# s2 = {-4 , 5, 6, 1, 9}
# print(s1)

# s1.add('Che') # add item
# print(s1)

# s1.clear()    # clear set
# print(s1)

# s1.remove("English")  # if item not available shows KeyError
# s1.pop() #pop not preferred , it removes random item
# s1.discard("Eng") # removes item , if not available doesnot shows error . Preferred
# print(s1)

# print(s1.union(s2))     #union joins two set
# print(s1 | s2) # another way to Union

# print(s1.intersection(s2))  #intersection takes common value
# print(s1 & s2)  # another way to intersection

# print(s1 - s2) # difference - items in first set only, common and uncommon of s2 removed from s1.

# print(s1 ^ s2)  # Symmetric difference - Items unique to each set.


# print(s2 <= s1) # Subset - everything in s2(subset) available in s1
# print(s2.issubset(s1))  # same     
# print(s2 < s1) # same     

# print(s1 >= s2) # Superset - s1 contains all elements of s2
# print(s1.issuperset(s2))
# print(s1 > s2) # superset

# required_permissions = {"read", "write"}
# user_permissions = {"read", "write", "delete"}
# print(required_permissions.issubset(user_permissions)) # Are all required permissions in the user's permissions?
# print(user_permissions.issuperset(required_permissions)) # Does the user have all the required permissions?


# a = {1,2}
# b = {3,4}
# print(a.isdisjoint(b))  # Disjoint - No common elements


# squares = {     #   Set Comprehension
#     x*x
#     for x in range(6)
# }
# print(squares)



# permissions = frozenset({    # A frozenset is immutable unlike set. Useful when the set should never change, or when you need to use a set as a dictionary key.
#     "read",
#     "write"
# })

# print(permissions.add("delete"))        # AttributeError


 
# users = {
#     "alice",
#     "bob",
#     "charlie"
# }

# print("alice" in users) # Membership test, uses hash to find so very faster than list






                # E-commerce site 



# A customer's shopping cart (order matters)
# cart = [
#     {"id": 1, "name": "Laptop"},
#     {"id": 2, "name": "Mouse"},
# ]

# One product's details (named attributes)
# product = {
#     "id": 1,
#     "name": "Laptop",
#     "price": 80000,
# }

# Screen resolution (fixed pair)
# resolution = (1920, 1080)

# Product categories (unique, unordered)
# tags = {"electronics", "computer", "sale"}



