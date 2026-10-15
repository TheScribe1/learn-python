# def main():
#     hello("world")
#     goodbye("world")


# def hello(name):
#     print(f"Hello, {name}")


# def goodbye(name):
#     print(f"Goodbye, {name}")

# if __name__ == "__main__":      #   Run main() only when this file is executed directly, not when it's imported by another file. Running main() means it excutes all the functions , just not any particular one
#     main()





# print(__name__) #   __name__ is a special variable automatically created by Python , you do not create it . Python automatically sets: __name__ = "__main__" . But if you predefined it , it will print that . Also if only this is imported it will print file name (saying).

# __name__ == "__main__"   -->   here __main__ is a pecial string used by Python, means if you run this file directly without importing it like library, it will run all, def main() to main(). also __main__ is unrelated to def main().