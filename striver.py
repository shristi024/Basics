import sys

def input(prompt=""):
    print(prompt, end="")
    value = sys.stdin.readline().rstrip("\n")
    print(value)
    return value

name = input("Enter your name: ")
fav1 = input("What is your favorite animal: ")
fav2 = input("What is your favorite color: ")
fav3 = input("What is your favorite number: ")

print(f"Hello {name}")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")