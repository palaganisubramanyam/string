'''
Write a Python Program to remove the nth index character from a non-empty string.
Input & Output Format:
Input consists of a string and one integer.
The first input consists of a string.
The second input refers to the index position.
The output consists of a string.
Sample Input:
cyfuno
4
Sample Output:
cyfuo
'''


user_input = input("Enter a string: ")
index_to_remove = int(input("Enter the index of the character to remove: "))
if 0 <= index_to_remove < len(user_input):
    new_string = user_input[:index_to_remove] + user_input[index_to_remove + 1:]
    print("Resulting String:", new_string)
else:
    print("Invalid index. Please enter a valid index.")
