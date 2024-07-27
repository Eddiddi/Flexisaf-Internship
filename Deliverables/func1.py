#Write a program to create function func1() to accept a variable length of arguments and print their value.

def func1(*args):
    # Iterate through all arguments and print each one
    for arg in args:
        print(arg)
