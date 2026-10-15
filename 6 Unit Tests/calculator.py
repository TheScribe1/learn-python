def main():
    x = int(input("Enter the x : "))
    print("x squared is", square(x))


def square(x):
    return x + x    # Error

if __name__ == "__main__":
    main()