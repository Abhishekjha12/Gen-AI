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

best_friend = 'Anne'
print('My best friend is ', best_friend)

my_value = 15

age = 18
print(age)

a, b = '10', '20'
print(a + b)

print('To comment a line of code you # at the beginning of the line.')