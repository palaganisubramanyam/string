'''
Write a Python Program to calculate the number of digits and letters in a string.

Problem Description:
The program takes a string and calculates the number of digits and letters in a string.

Problem Solution:
1. Take a string from the user and store it in a variable.
2. Initialize the two count variables to 0.
3. Use a for loop to traverse through the characters in the string and increment the first count variable each time a digit is encountered and increment the second count variable each time a character is encountered.
4. Print the total count of both the variables.
5. Exit.

Input & Output Format:
Input consists of a string
Output consists of two integers.
First output refers to the total count of the characters.
Second output refers to the total count of the digits.

Sample Input:
Cyfuno2020

Sample Output:
Characters: 6
Digits: 4
'''


user_input = input("Enter a string: ")
character_count = 0
digit_count = 0
for char in user_input:
    if char.isalpha():  # Check if the character is a letter
        character_count += 1
    elif char.isdigit():  # Check if the character is a digit
        digit_count += 1
print(f"Characters: {character_count}")
print(f"Digits: {digit_count}")
