        #   A Regular Expression (Regex) is a sequence of characters that defines a search pattern.



                # | Pattern   | Meaning             |    |
                # | --------- | ------------------- | -- |
                # |  \d       | digit               |    |
                # |  \D       | non-digit           |    |
                # |  \w       | word char           |    |
                # |  \W       | non-word            |    |
                # |  \s       | whitespace          |    |
                # |  \S       | non-whitespace      |    |
                # |  .        | any char            |    |
                # |  +        | one or more         |    |
                # |  *        | zero or more        |    |
                # |  ?        | optional            |    |
                # |  {n}      | exactly n           |    |
                # |  {m,n}    | range               |    |
                # |  ^        | start               |    |
                # |  $        | end                 |    |
                # |  []       | char set            |    |
                # |  [^]      | negated set         |    |
                # |  ()       | capture group       |    |
                # |  (?:)     | non-capture group   |    |
                # |  (?P<x>)  | named group         |    |
                # |  (?=x)    | lookahead           |    |
                # |  (?!x)    | negative lookahead  |    |
                # |  (?<=x)   | lookbehind          |    |
                # |  (?<!x)   | negative lookbehind |    |
                # | `         | `                   |    |





            # Email pattern


# import re   #   re = regular expression
# email = input("Enter your email address : ").strip()

# if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):   # re.search(pattern, string, flags=0) #  \w = [a-zA-Z0-9_]
#     print("Valid")
# else:
#     print("Invalid") 






        # Name placement


            # ( ) = group [A normal group captures the matched text and gives it a group number.]
            # (?: ) = non capturing Group [the regex still groups the pattern together, but it does not store the result.]


# import re

# name = input("Enter your name : ").strip()

# if matches := re.search(r"^(.+), *(.+)$", name): # ( := )walrus operation - It simply assigns a value to a variable and returns that value.
#     name = matches.group(2) + " " + matches.group(1)
# print(f"Hello, {name}")





        # username extract from URL


import re 

url = input("Enter URL : ").strip()

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(?P<username>[a-z0-9_]+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group("username"))