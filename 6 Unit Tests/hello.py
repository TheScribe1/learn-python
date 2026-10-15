def main():
    name = input("What is you name ? : ")
    print(hello(name))

def hello(to = "world"):
    return f"Hello, {to}"   # output need to be return to test

if __name__ == "__main__" :

    main()