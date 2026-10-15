                #       Library
                #           ↓
                #       Package
                #           ↓
                #       Module
                #           ↓
                #       Function   
                
                 

        #   A library is a collection of modules (example : NumPy, Pandas, Django, Flask, FastAPI, OpenCV, Requests) A library may consist of one or more packages, modules, and other resources.




    #   Python imports the entire random module.You access functions using random.function_name

# import random    # random is module(A module is a Python file with useful code inside it.)  [example : random, math, os, time, datetime, json, sys, re, collections]

# coin = random.choice(["heads","tails"])     # choice() is a function inside the random module which picks random item. [example : choice(), print(), min(), max()]
# print(coin)






# import random

# number = random.randint(1,10)    
# print(number)





# import random

#cards = random.shuffle(["Jack","King","Queen"]) #   This return None because the list itself gets shuffled directly.

# cards = ["Jack","King","Queen"]
# random.shuffle(cards)
# for card in cards:
#     print(card)




        # Python imports only choice function from random module . You can access it by function_name


# from random import choice

# coin = choice(["head","tail","tie"])

# print(coin)






# import statistics

# print(statistics.mean([100, 90, 85]))   # prints average






        #       sys is a built-in Python module that lets your program interact with the Python interpreter and the operating system. [sys, os, platform, subprocess]
        #       sys.argv (argv means argument vector . It is a list that stores everything typed after running a Python script from the terminal.)
        #       python test.py apple banana orange => here test.py is file name , after running sys.argv , it becomes ['test.py', 'apple', 'banana', 'orange']





# import sys


# print("Hello, my name is", sys.argv[0]) # sys.argv[0] means get the script filename. Python automatically stores the script name as the first item.     # ex. test.py
# print("Hello, my name is", sys.argv[0]) # sys.argv[0] means get the script filename.      # ex. test.py
# print("Hello, my name is", sys.argv[1]) # sys.argv[1] means get the first command-line argument entered by the user , ex. apple
# print("Hello, my name is", sys.argv[2]) # sys.argv[2] means get the second command-line argument entered by the user , ex. banana


# sys.exit()
# print(sys.argv)
# print()
# print(sys.version)
# print()
# print(sys.platform)
# print()
# print(sys.path)
# print()
# print(sys.stdin)
# print()
# print(sys.stdout)
# print()
# print(sys.getsizeof(5))
# print()
# print(sys.executable)
# print()
# print(sys.modules)


# try:
#         print("Hello, my name is", sys.argv[1])       
# except IndexError:
#         print("Too few arguments")


# if len(sys.argv) < 2:
#         print("Too few arguments")
# elif len(sys.argv) > 2:
#         print("Too many arguments")
# else:
#         print("Hello, my name is", sys.argv[1])




# if len(sys.argv) < 2:
#     sys.exit("Too few arguments...")

# for arg in sys.argv[1:] :       # using slices so that file name doesn't get printed
#     print("Hello, my name is : ",arg)







                # Package - A package is a collection of related Python modules stored in a directory hierarchy. [numpy, panda, django etc ] 
                # PyPI (Python Package Index) - PyPI is the official online repository where Python packages are published and shared.
                # pip (Pip Installs Packages) - pip is Python's package manager used to install, update, and remove Python packages.




        # we install cowsay using terminal (pip install cowsay) and check using (pip list) , we can uninstall using (pip uninstall cowsay)




# import cowsay
# cowsay.cow("Hello!")
# print(dir(cowsay)) # check version functions

# import sys


# if len(sys.argv) == 2 :
#     cowsay.cow("Hello!, " + sys.argv[1])    # cowsay.cow() expects one message string as its argument, so we use '+' and not ' , '
#     cowsay.trex("Hello!, " + sys.argv[1])
#     cowsay.tux("Hello!, " + sys.argv[1])
#     cowsay.stimpy("Hello!, " + sys.argv[1])
#     cowsay.dragon("Hello!, " + sys.argv[1])









                    # API (Application Programming Interface) - An API is a set of rules that allows different software applications to communicate and exchange data with each other(server, website, database, or service). 

                    #       Python program → sends HTTP request → API server → returns JSON data → you use it





            # GET (read data)


# import json     # using json so that we can read json file more easily using json.dumps
# import requests   #   The most common tool Python uses to talk to APIs is requests. It's used for GET, POST, PUT/PATCH, DELETE data
# import sys

# if len(sys.argv) != 2 :
#     sys.exit()

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# # print(json.dumps(response.json(), indent=2))    # this gives us json data where in "results[]" dictionary there is trackName which gives us song name of that artist

# o = response.json()
# for result in o["results"]:
#     print(result["trackName"]) # only printing trackName





        # Better version 
        
# import json
# import requests
# import sys

# if len(sys.argv) != 2:
#     sys.exit("Usage: python songs.py artist")

# url = "https://itunes.apple.com/search"

# params = { # Standard way of constructing query
#     "entity": "song",
#     "limit": 50,
#     "term": sys.argv[1]
# }

# try:
#     response = requests.get(url, params=params, timeout=10)
#     response.raise_for_status()
#     data = response.json()

# except requests.RequestException as e:
#     sys.exit(f"Request failed: {e}")

# for result in data.get("results", []): # give me results, if doesn't exist- give me empty list
#     print(result.get("trackName", "Unknown")) # give me trackName, if doesn't exist- give me Unknown





        # response contains :

            # response.status_code
            # response.headers
            # response.text - Returns decoded text
            # response.json() - Parses JSON
            # response.content - Returns raw bytes






# import json
# import requests

# response = requests.get("https://api.github.com")
# print(response.status_code)
# print(json.dumps(response.json(),indent=2))






        # Status Code



# | Code | Meaning                      |
# | ---- | ---------------------------- |
# | 200  | Success                      |
# | 201  | Created                      |
# | 400  | Bad request                  |
# | 401  | Unauthorized (wrong API key) |
# | 403  | Forbidden                    |
# | 404  | Not found                    |
# | 500  | Server error                 |








        # POST (send data)



# import requests

# url = "https://httpbin.org/post"

# data = {
#     "name": "John",
#     "age": 20
# }

# response = requests.post(url, json=data)

# # print(response.json())  #   .json() converts that JSON into a Python dictionary.
# print(response.text)










# import requests

# api_key = "YOUR_API_KEY"
# city = "London"

# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

# response = requests.get(url)    # GET /weather?q=London&appid=abc123 to the weather server.

# if response.status_code == 200:
#     data = response.json()  #   converts JSON into a Python dictionary.

#     print("Weather:", data["weather"][0]["description"])
#     print("Temperature:", data["main"]["temp"])
# else:
#     print("Error:", response.status_code)









# import requests

# url = "https://api.twitter.com/2/tweets"

# headers = {     #   This is authentication.
#     "Authorization": "Bearer YOUR_TOKEN"    # Bearer - Whoever possesses this token is allowed access.
# }

# response = requests.get(url, headers=headers)

# print(response.json())







                # Create your own library and use it




    # created saying.py library



# import sys
# from saying import hello

# if len(sys.argv) == 2:
#     hello(sys.argv[1])


# from saying import goodbye

# if len(sys.argv) == 2:
#     goodbye(sys.argv[1])






# # import saying
# # saying.hello("Scribe")






        # Make actual sound


# import cowsay
# import pyttsx3        # Python text-to-speech (TTS) library. It converts text into spoken audio using the speech engine already available on your operating system.

# engine = pyttsx3.init()
# engine.setProperty("rate", 150)    # Slower speech
# engine.setProperty("volume", 1.0)  # Maximum volume
# this = input("What's this? :")
# cowsay.cow(this)
# engine.say(this) # tells the speech engine what to say
# engine.runAndWait()   # processes that request and waits until the speech has finished before the program exits. Without runAndWait(), the text is queued but may never be spoken because the program ends too soon.


