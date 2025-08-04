'''Problem Statement: Write a Python program that:
        1.   Creates a dictionary where student names are keys and their marks are values.
        2.   Asks the user to input a student's name.
        3.   Retrieves and displays the corresponding marks.
        4.   If the student’s name is not found, display an appropriate message.'''


dict = {'alice':60, 'mike':90, 'john':67, 'nick':78, 'bob': 85}
name = input("Enter the name of the student: ").lower()
if name in dict:
  print(f"{name.capitalize()}'s marks: {dict[name]}")
else:
  print("Student not found.")
