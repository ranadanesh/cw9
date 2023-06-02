import re

def validation():
    while True:
        password = str(input("Enter string to test: "))
        if re.findall(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$", password):
            print("match")
        else:
            print("not match")


validation()