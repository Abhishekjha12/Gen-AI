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
num = [3,1,2,4,10,6]
num.sort() 
# To sort in reverse 
num.sort(reverse=True)
print(num)

#Sorted: also sort the list but it returns a new list without hampering the original list
sorted_numbers = sorted(num)
sorted_numbers = sorted(num, reverse=True) # to reverse sorting of number
print(num,sorted_numbers)