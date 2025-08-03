'''Problem Statement: Write a Python program that:
    1.   Takes user input and writes it to a file named output.txt.
    2.   Appends additional data to the same file.
    3.   Reads and displays the final content of the file.
'''

with open("output.txt", 'a') as file2:
    txt = input("Enter text to write to the file: ")
    file2.write(txt + "\n")
    txt1 = input("Enter additional text to append: ")
    file2.write(txt1 + "\n")

with open("output.txt", 'r') as file3:
    print("Final content of output.txt:")
    final = file3.readlines()
    for line in final:
        print(line.strip())
