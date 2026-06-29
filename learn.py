# # # X =  1
# # # print("Hello world")

# # # a = 10
# # # print(a*2)

# # # b = 20
# # # print(b ** b)

# # # print("Bye")

# # # celcius_temp = 25
# # # print(celcius_temp)

# # # a,b,c,d = 1,2,3,4

# # # age, name  = 13, "Abhishek" ## so here age is automatically assigned data type integer and name as string


# # # PeP8 Naming convection

# # # ==========================================
# # # PYTHON NAMING CONVENTIONS
# # # DO vs DON'T EXAMPLES
# # # ==========================================

# # # ==========================================
# # # 1. VARIABLES -> snake_case
# # # ==========================================

# # # ✅ DO
# # user_name = "Abhishek"
# # student_age = 22

# # # ❌ DON'T
# # # UserName = "Abhishek"
# # # studentAge = 22
# # # STUDENTAGE = 22


# # # ==========================================
# # # 2. CONSTANTS -> UPPER_CASE
# # # ==========================================

# # # ✅ DO
# # PI = 3.14159
# # MAX_USERS = 100

# # # ❌ DON'T
# # # pi = 3.14159
# # # maxUsers = 100


# # # ==========================================
# # # 3. FUNCTIONS -> snake_case
# # # ==========================================

# # # ✅ DO
# # def calculate_salary():
# #     return 50000


# # def get_user_details():
# #     return "User Details"


# # # ❌ DON'T
# # # def CalculateSalary():
# # #     pass

# # # def getUserDetails():
# # #     pass


# # # ==========================================
# # # 4. CLASSES -> PascalCase
# # # ==========================================

# # # ✅ DO
# # class Student:
# #     pass


# # class BankAccount:
# #     pass


# # # ❌ DON'T
# # # class student:
# # #     pass

# # # class bank_account:
# # #     pass


# # # ==========================================
# # # 5. PRIVATE / PROTECTED VARIABLES
# # # ==========================================

# # class Employee:

# #     def __init__(self):

# #         # Public
# #         self.name = "Abhishek"

# #         # Protected
# #         self._salary = 50000

# #         # Private
# #         self.__password = "secret123"


# # emp = Employee()

# # # ❌ DON'T ACCESS PRIVATE VARIABLE DIRECTLY
# # # print(emp.__password)


# # # ==========================================
# # # 6. MODULE / FILE NAMES
# # # ==========================================

# # # ✅ DO
# # # user_service.py
# # # prompt_engineering.py
# # # vector_database.py

# # # ❌ DON'T
# # # UserService.py
# # # PromptEngineering.py
# # # VectorDatabase.py


# # # ==========================================
# # # 7. MULTIPLE ASSIGNMENT
# # # ==========================================

# # # ✅ DO
# # a, b, c = 10, 20, 30

# # print("\nMultiple Assignment")
# # print(a, b, c)


# # # ==========================================
# # # 8. SAME VALUE ASSIGNMENT
# # # ==========================================

# # # ✅ DO
# # x = y = z = 100

# # print("\nSame Value Assignment")
# # print(x, y, z)


# # # ==========================================
# # # 9. VARIABLE SWAPPING
# # # ==========================================

# # num1 = 10
# # num2 = 20

# # print("\nBefore Swap")
# # print(num1, num2)

# # # ✅ Pythonic Way
# # num1, num2 = num2, num1

# # print("After Swap")
# # print(num1, num2)

# # # ❌ DON'T (not wrong, but unnecessary in Python)
# # # temp = num1
# # # num1 = num2
# # # num2 = temp


# # # ==========================================
# # # 10. DYNAMIC TYPING
# # # ==========================================

# # value = 10
# # print("\nInitial Type:", type(value))

# # value = "Generative AI"
# # print("Updated Type:", type(value))

# # # Python allows this because it is dynamically typed.


# # # ==========================================
# # # 11. TYPE CHECKING
# # # ==========================================

# # name = "Abhishek"
# # age = 22
# # cgpa = 6.97

# # print("\nType Checking")
# # print(type(name))
# # print(type(age))
# # print(type(cgpa))


# # # ==========================================
# # # 12. SPECIAL (DUNDER) VARIABLES
# # # ==========================================

# # print("\nCurrent Module Name:")
# # print(__name__)

# # # Examples of dunder methods:
# # # __init__()
# # # __str__()
# # # __repr__()

# # # ❌ DON'T CREATE YOUR OWN RANDOM DUNDERS
# # # __myFunction__()


# # # ==========================================
# # # QUICK REVISION
# # # ==========================================

# # print("\n===== REVISION =====")

# # print("""
# # Variables  -> snake_case
# # Functions  -> snake_case
# # Classes    -> PascalCase
# # Constants  -> UPPER_CASE
# # Protected  -> _variable
# # Private    -> __variable
# # Files      -> snake_case.py

# # Examples:

# # ✅ user_name
# # ❌ UserName

# # ✅ calculate_salary()
# # ❌ CalculateSalary()

# # ✅ Student
# # ❌ student

# # ✅ MAX_USERS
# # ❌ maxUsers
# # """)

# # Data Types

# # Integer
# age = 40
# temperature = 20.1

# # Boolean
# print(age == 40)
# print(age < 30)

# # None

# # String: ordered sequence of characters, Stored in UTF-8 format
# model_name = 'Gemini'

# # Lists: ordered , mutable sequence of objects.  
# person = ['Dan', 78, 20.8, True]

# # Tuples: Ordered , immutable sequence of objects.
# coordinates = (40.728, -12.122)

# # Sets : Mutable Collection of unordered , unique objects
# ip_addressess = {'100.0.0.1', '80.2.3.6'} # Set Type

# # Frozen Set : Immutabe Collection of unordered unique objects
# frozen_user_ids = frozenset([1001,1002,1003])

# # Dictionaries : Collection of unordered key-value pair
# person = {'name':'Abhishek', 'age':'30', 'is_employed':True}




# Static vs Dynamic Typing

# #In Java
# int score;
# score = 10

# Python is dynamically typed

# score = 10 # int
# print(type(score))

# Operators and Mathematics

# a = 20
# b = 3

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Floor Division:", a // b)
# print("Modulus:", a % b)
# print("Power:", a ** b)

# print("Greater:", a > b)
# print("Equal:", a == b)

# print("Logical AND:", a > 10 and b < 5)

# fruits = ["Apple", "Banana"]

# print("Apple" in fruits)

# print((2 + 4) * 2 ** 3) ## exponation goes first, second goes the multiplication and then the addition


# Declare variables of the following types: int, float, bool, string, and list.

# Print each variable along with its type in the terminal.
# a = 5;
# print(type(a))

# b=5.3
# print(type(b))

# c = True
# d = False
# print(c is d)
# # print(type(c) && type(d))

# print('Abhishek')

# aa = ["Abhishek",12,3]
# print(aa)

# var_One = 10
# var_Two = 20

# """
# This is 
# an example of a multiline
# comment in Python.
# """

# my_str='Hello'
# print(str)

# best_friend = 'Anne'
# print('My best friend is ', best_friend)

# my_value = 15

# age = 18
# print(age)

# a, b = '10', '20'
# print(a + b)

# print('To comment a line of code you # at the beginning of the line.')

# String in Python

# model_summary = 'This is how AI revolutionize the Industry '
# print(model_summary)

# feedback = 'Press the # button to continue'

# print('AI says, I\'m here to assist you.')
# print("AI says, I'm here to assist you.")
# ai_response = """ Hello there
# this is one another way to write the code.
# thanks for watching this out
# """

# print(ai_response)

# print('\\ is essential for handling escape characters in python')








# USER INPUT IN PYTHON
# command = input('Ask your AI assisstant a question: ')
# print('Your question was:', command)

# Taking other data type as input
# iterations = input('Enter the number of iterations ')
# iterations = int(iterations)
# dataset = input('Enter the number of dataset ')
# dataset  = int(dataset)
# total=iterations * dataset
# print("Total processing time: ",total)

# CORE STRING OPERATIONS: INDEXING , SLICING , CONCATENATION

# message = 'Abhishek you are soo good!'
# print(message[1])
# print(message[8])
# print(message[-1])

# n = len(message)
# print(n)
# print(message[n-1])

# Strings are immutable in Python, so individual characters cannot be modified after the string is created.

# CONCATENATION
# greeting = 'Hello'
# role = 'AI Enthusiast'
# print(greeting + " " + role)

# print('version ' + str(4.0))

# tech = 'Machine Learning'
# print(tech[0:7]) # String slicing syntax = String[start : stop]
# print(tech[:7])
# print(tech[8:])
# print(tech[-4:])
# print(tech[0:14:2]) # starting from 0th index to 14th index every 2nd index will be displayed, since its even only 6 characters will be displayed
# print(tech[::-1]) # This reverse out string


# Common String method
# x = 10
# s = "abc"
# print(type(s), type(x))

# model_output = "AI is the future of everything"
# print(model_output.lower())
# print(model_output.upper())

# response = ' 🚀 Hello GenAI! 🤖 '
# print(response.split())
# print(response.split(' 🚀'))

# terms = ['AI', 'GENAI', 'CS', 'LLM', 'NLP']
# buzzwords_string = ', '.join(terms)
# print(buzzwords_string)

# url = "https://example.com"
# cleaned_url = url.removeprefix("https://")
# print(cleaned_url)

# file_name = 'State_of_ai_2025.pdf'
# cleaned_filename = file_name.removesuffix('.pdf')
# print(cleaned_filename)

# help(str)

# FORMATTED STRING: USING F-STRINGS FOR CLEAN OUTPUT
# model_name = 'GPT'
# version = 4
# print("Hello from " + model_name + '-' + str(version)+ '!')

# # Using F-String we can do like
# print(f'Hello from {model_name}-{version}!')

# token_used = 10
# cost_per_token = 0.001
# total_cost = f'{token_used * cost_per_token:.4f}'
# print(f'Total cost for this message: {total_cost}')

# FSTRING FORMATTING WITH = DEBUGGING

# name, age  = "Abhishek" , 23
# print(f'Your name is {name} and you are {age} years old')
# print(f'Your name is {name = } and you are {age = } years old')

# r = 13.3
# PI = 3.141592

# print(f'Area of circle with radius of {r} is {PI * r ** 2}')
# print(f'Area of circle with radius of {r = } is {PI * r ** 2 = }')

# Challenge #1

# A company has a revenue of 45,897,513.
# Calculate its profit, assuming profit is 12.7% of the revenue.
# Display the result rounded to two decimal places.

# r = 45897513
# print(f'Profit of the company is {45897213 * 0.127:.2f}')

# Challenge #2
# Consider the following string declaration which is part of the output of a Linux command.

# my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'

# Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.

# my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
# print(my_str.removeprefix('wlo1 Link encap:Ethernet HWaddr '))


# Challenge #3

# Display the following strings literally:

# It displayed: "You've got an error!"

# \n means a new line.

# \ is known as the escape character.
# msg = "It displayed: \"You've got an error!\""
# print(msg)

# print("\\n means a new line")
# print("\\ is know as the escape character.")



# Challenge #4

# Write a Python script to convert feet (ft) to centimeters (cm).

# Conversion: 1 ft = 30.48 cm

# Prompt the user to enter a value in feet.

# Display the result in centimeters with two decimal places, formatted using an f-string.

# prompt = float(input("Enter the value is feet "))
# conversion = prompt * 30.48
# print(f'The value in centimeter is {conversion:.2f}cm')

# Challenge #5

# Write a Python script to check if a string is a palindrome.

# s = input("Enter your string ")
# p = (s[::-1])
# print(f'Is {s} a palindrome? {s==s[::-1]}')

# Challenge #6

# Change the solution of the previous challenge to ignore whitespace and letter case when checking if a string is a palindrome.
# s = input("Enter your string ")
# p = (s[::-1])
# check = (s.replace(' ',''))
# print(check.upper())

# Challenge #7

# Write a Python script that extracts the first and last two characters from a user-entered string.

# Example:

# Input: 'Hello!'

# Output: 'Heo!'

# s = input("Enter your string ")
# fh = s[:2]
# sh = s[-2:]

# ns = fh + sh
# print(ns)

# Write a Python script that replaces all occurrences of the first character in a string with '$', except for the first occurrence itself.

# Example:

# Input: 'mama'

# Output: 'ma$a'

# s = input("Enter your string")
# char = s[0]
# ns = s[1:].replace(char, '$')
# print(char + ns)

#Alternate method
# s = input("Enter your string ")
# first_char = s[0]
# rest = s[1:]
# mr = rest.replace(first_char,"$")
# result = first_char + mr
# print(result)




# Challenge #9
# Write a Python program to remove the character at the nth index from a non-empty string.
# The nth index is provided by the user.
# n = int(input("Enter nth index character to remove"))
# ms = input("Enter your string")
# fp = ms[0:n]
# lp = ms[n+1:]
# ns = fp + lp 
# print(ns)


# Challenge #10

# Write a Python script that removes characters at odd index positions from a given string.

# s = input("Enter your string ")
# ns = s[::2]
# print(ns)



# Write a Python script that prompts the user for a circle's radius and calculates its area.

# Formula: Area = π * r² (π = 3.1415)

# Display the area with four decimal places using an f-string.

# r = int(input("Enter the value of radius of circle "))
# PI = 3.1415

# print(f'The Area of cicle with radius {r = } is {PI*r**2:.4f}')



# Challenge #12
# Write a Python script that counts the number of occurrences of a substring in a given string, ignoring letter case.

# s = input("Enter Your String ")
# n = int(input("Select Start of Substring "))
# m=int(input("Select End of String "))
# ss = s[n:m]
# new_subString = ss.lower()
# print(new_subString.count(s))


#Challenge 13
# Write a Python script to format a number using:

# US/UK format: A comma , as the thousands separator

# EU format: A period . as the thousands separator

# s = int(input("Enter the number string "))
# us_uk = (f'The numbers in US format is {s:,}')
# print(us_uk)

# eu = str(us_uk.replace(",","."))
# print(eu)
