'''Problem Statement:  Write a Python program that:
    1.   Opens and reads a text file named sample.txt.
    2.   Prints its content line by line.
    3.   Handles errors gracefully if the file does not exist.'''
    


file = "C:\\python\\TudeDude\\TuteDude_Python\\Assignment4\\sample.txt"
try:
    with open(file, "r") as file1:
        print("Reading file content: ")
        for i, line in enumerate(file1, start=1):
            print(f"Line {i} : {line.strip()}")
except FileNotFoundError:
    print("Error: The file was not found.")
