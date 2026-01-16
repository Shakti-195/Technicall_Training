# # create a list  of 5 numbers .Print the first element ,last element  of the list 

# numbers = [10,20 ,30 ,40 ,50]

# print ("First element :",numbers[0])
# print("last element :",numbers[-1])
# print ("the numbers of the list are:")

# print(numbers)


# take a list of numbers and find the sum  and average  using built in functions

# print("enter 5 numbers:")
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# num5 = int(input())

# print("The number is more than two-digit")
# total = num1 + num2 + num3 + num4 + num5
# average = total / 5     
# print("Sum of numbers:", total)
# print("Average of numbers:", average)


# create a list of fruits.Add a new fruit using .append() and insert  one at position 2 using .insert()

# fruits = ['apple', 'banana', 'cherry']
# fruits.append('orange')
# fruits.insert(2, 'kiwi')
# print("Updated fruit list:", fruits)

# Remove  an element from   a list using .remove() and  delete the last element using .pop().
# fruits = ['apple', 'banana', 'cherry', 'date']
# fruits.remove('banana')
# fruits.pop()
# print("Updated fruit list after removal:",fruits)

# create a list  with duplicate numbers.Use .count() to check how many times a number appears.
# numbers = [10, 20, 30, 20, 40, 20, 50]
# count = numbers.count(20)
# print ("The number 20 appears ",count ,"times in the list.")

# searching and sorting 

# write a program to check if a number exits in a list or not.

# numbers = [10,20,30,40,50]
# search_num = int(input("Enter a number to search:"))
# if search_num in numbers:
#     print(f"{search_num},exists in the list.")
# else:
#     print(f"{search_num},does not exist in the list.")

# create a list of 5 integers.Use .index( to find the position of a given number.

# numbers = [10,20,30,40,50]

# position = numbers.index(30)
# print("The position of 30 in the list is :",position)


# Sort a list in  ascending and descending order using .sort() and .reverse()

# numbers = [50,20,40,10,30]
# numbers.sort()
# print("List in ascending order:",numbers)
# numbers.reverse()
# print("List in descending order:",numbers)

# Reverse a list using .reverse() method.
numbers = [10,20,30,40,50]
numbers.reverse()
print("Reversed list:",numbers)

