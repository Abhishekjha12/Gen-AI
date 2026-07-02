# # Basic of List

# sample_list = [42,"Abhishek","GPT-4",True]
# empty_list = []
# empty_list2 = list() # this is list constructor

# # # Append in List
# # List = ["Abhishek"]
# # List.append("NLP")
# # print(List)
# # print(len(List)) # Return the length of list

# # List can be stored in nested list format, Like Matrix

# # matrix = [
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9],
# # ]
# # print(matrix[0][2])



# # LIST OPERATIONS

# # 1. Concatenation
# l1 = [3,4]
# print(l1,id(l1))
# l2 = [5,6]
# print(l1 + l2)

# l1 += [7,8]
# print(l1,id(l1))

# l1.extend([9,10])
# print(l1)

# l1.append(['a','b'])
# l1.extend(['X','Y'])

# print(l1)



# Iteration and MemberShip testing
# ip_list = ['192.168.0.1', '192.168.0.2', '10.0.0.1']

# # we can create a iterator and transact to each member

# for ip in ip_list:
#     print(f'Connect to {ip} ...')

# # Check if exist
# target_ip = '192.162.0.1'
# if target_ip in ip_list:
#     print(f'{target_ip} is in the list')

# prefix = '192'
# if prefix not in ip_list:
#     print(f'No Address with the prefix {prefix} is present')


# LIST GOTCHA

# l1 = [1,2,3]
# # l2 = l1
# # l2[0] = 'X'
# # l2.append(0)
# # print(l1,l2)

# # True copy method
# l3 = l1.copy()
# l3.append('abc')
# print(l3,l1)


# nums = [1,2,3,4,5,6,7]
# for n in nums:
#     if n < 5:
#         nums.remove(n)
# print(nums)


# new_list = []

# for n in nums:
#     if n >= 5:
#         new_list.append(n)
# print(new_list)




#LIST METHODS
#ESSENTIAL LIST METHOD

# l1 = list()
# print(dir(l1))

# ADDING ELEMENTs TO A LIST : append(), extend(), insert()
# list1 = [1, 2.2, 'abc']
# list1.append([5,7]) # Cannot add multiple item to the list using append
# print(list1)

# Extend: to extend the list with another list
# list1.extend(['X','Y'])
# print(list1)

#Insert : Allows us to extend the list by adding at any position
# years = [2021,2022,2024]
# years.insert(2,2023)  # (x,y) where x is the posiiton of index and y is the value to be inserted at that index
# print(years)

#Removing element from the list: Clear()

# l1 = ['a','b','c']
# # l1.clear()
# print(l1)

# Pop() : it remove element from a specific index but by default it remove from the last index
# x = l1.pop(1)

# print(x,l1)

# list.remove()

# l3 = [10,20,30,40]
# l3.remove(10)
# print(l3)

# l4 = [10,20,10,30]
# while 10 in l4:
#     l4.remove(10)

# print(l4)

# List.count()
# letter = list('abaca')
# print(letter)
# print(letter.count('a'))


# List.reverse() : reverses the element in place
# seq = [1,2,3,4]
# print(seq)
# seq.reverse()
# print(seq)

# List.sort(): inplace sorting method
# num = [3,1,2,4,10,6]
# num.sort() 
# To sort in reverse 
# num.sort(reverse=True)
# print(num)

#Sorted: also sort the list but it returns a new list without hampering the original list
# sorted_numbers = sorted(num)
# sorted_numbers = sorted(num, reverse=True) # to reverse sorting of number
# print(num,sorted_numbers)


#LIST Comprehension
# clicks = [10,2,5,4]
# double_clicks = []

# for c in clicks:
#     double_clicks.append(c*2)

# print(double_clicks)

# the above code can be compressed and easily be done through
# syntax for list comprehension = [expression for items in iterables]
# doubled_clicks = [c*2 for c in clicks]
# print(doubled_clicks)

# contributors = ['alice','bob','CHARLIE']
# formatted_names = [name.capitalize() for name in contributors]
# print(formatted_names)

# how to add when creating list using list comprehension
# [expression for item in iterable if condition]
# nums = [1,4,7,9,14,15,21]
# divisible_by_seven = [n for n in nums if n%7 ==0]
# print(divisible_by_seven)\

# ai_team = ['alice','bob','Thomas']
# data_team = ['alice','suresh','Thomas']

# shared_skills = [name for name in ai_team if name in data_team]
# print(shared_skills)





# Challenge #1

# Write a Python script that removes all occurrences of a given element from a list.

# l1 = [10,11,12,10,14,19]
# while 10 in l1:
#     l1.remove(10)
# print(l1)

# Challenge #2
# Write a Python script that removes all duplicate elements from a list.

# l1 = [10,10,11,11,12]
# l2 = []

# for num in l1:
#     if num not in l2:
#         l2.append(num)

# print(l2)

# Challenge #3
# Given the string nums = '10,20,30,40,50', write a Python script that converts it into a list of integers: [10, 20, 30, 40, 50].

# nums = '10,20,30,40,50'
# l1 = nums.split(",")
# print(l1)
# l1 = [int(item) for item in l1]
# print(l1)


# Challenge #4

# Write a Python script that finds all numbers between 1500 and 3200 (inclusive) that are divisible by 7 but not multiples of 5.

# Print the results as a comma-separated sequence on a single line.
# l1 = range(1500,3201)
# l1 = [n for n in l1 if n%7==0 and n %5 != 0]
# print(l1)

# Challenge #5

# Write a program that prompts the user for a string containing multiple words separated by spaces and prints the words in reverse order.

# s = "My name is Andrei"
# ns = s.split(" ")
# ns.reverse()

# # ns.pop(",")

# print(" ".join(ns))



# # Challenge #6

# # Write a Python program that takes a hyphen-separated sequence of words as input and prints them in alphabetical order, maintaining the hyphen separation.

# # Example:

# # Input: "green-red-yellow-black-white"

# # Output: "black-green-red-white-yellow"

# word = "green-red-yellow-black-white"
# order = word.split("-")
# order.sort()

# print("-".join(order))

# Challenge #7

# Write a Python program that takes a sequence of words separated by spaces and prints the words with their letters reversed. Do not use list comprehension.

# Example:

# Input: "I love cats and dogs"

# Output: "I evol stac dna sgod"

# s = "I love cats and dogs"

# word = s.split()
# # print(word)

# new_word = []

# # print(new_word)

# for words in word:
#     new_word.append(words[::-1])

# # print(new_word)

# result = " ".join(new_word)

# print(result)   



# Challenge #8

# Modify the previous challenge by using list comprehension instead.

# s = "I love cats and dogs"

# word = s.split()

# new_word = [word[::-1] for word in word]

# result = " ".join(new_word)

# print(result)   



#Challenge 9
# Given a list of words, write a Python script that generates a list of tuples where each tuple contains a word and its length. Use list comprehension if possible.

# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']

# Expected Result: [('Python', 6), ('Java', 4), ('C++', 3), ('Golang', 6), ('Solidity', 8), ('Bash', 4)]

s = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']

result = [[word,len(word)] for word in s]
print(result)