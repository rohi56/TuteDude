'''Problem Statement: Write a Python program that:
        1.   Creates a list of numbers from 1 to 10.
        2.   Extracts the first five elements from the list.
        3.   Reverses these extracted elements.
        4.   Prints both the extracted list and the reversed list'''
        
num = list(range(1,11))
print("Original list : ", num)
print("Extracted first five elements : ", num[:5])
print("Reversed Extracted elements : ", sorted(num[:5], reverse= True))
