# Incompatible types in assignment


def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = input("Number: ") # returns str... not int
meow(number)
