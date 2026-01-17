# #1 create a set of 5 colors and print it.
# from enum import unique


# colors = {'red', 'blue', 'green', 'yellow', 'purple'}
# print("set of colors:",colors)

# #2 create a set of numbers with duplicates and check how python handles duplicates.
# numbers = {1,2,3,4,5,3,2,1}

# print ("set of numbers with duplicates:",numbers)

# #3 write a program to loop through a set and print each element.
# print ("looping through the set of colors:")

# for color in colors:
#     print(color)

# #4 create a set and use  .add() to insert a new element.
# colors.add('orange')
# colors.add('red')
# print("set of colors after adding new elements:",colors)

# #5 Remove an element using .remove() and .discard() and observe what happens if the element is not present.
# colors.remove('blue')
# colors.discard('pink')
# print("set of colors after removing elements:",colors)

# #6 Remove an element using .discard() and compare it with .remove()
# colors.discard('green')
# print("set of colors after discarding an element :",colors)

# #7 use .pop() to remove a random element from a set .
# removed_color =  colors.pop()
# print ("removed color:",removed_color)
# print("set of colors after pipping an element :",colors)

# #8 create two sets and find their union .
# set1 = {1,2,3}
# set2 = {4,5,6}

# union =set1.union(set2)
# print("Union of set1 and set2:",union)

# #9 create two sets and find their intersection.
# set3 = {1,2,3,4}
# set4 = [3,4,5,6]
# intersection = set3.intersection(set4)
# print("intersection of set3 and set4:",intersection)

# #10 create two sets and find the difference (A-B)
# set5 = {1,2,3,4}
# set6 = {3,4,5,6}
# difference = set5.difference(set6)
# print("Difference of set5 and set6 (set5 - set6):",difference)

# #11 use copy () to create a copy of a set and modify the copy .
# set7 = {'apple', 'banana', 'cherry'}
# set8 = set7.copy()
# set8.add('date')
# print("Original set (set7):",set7)
# print("Modified copy of the set (set8):",set8)


# #12 use .clear() to empty a set.
# set9 = {10,20,30,40}
# set9.clear()
# print("set9 after clearing all elements:",set9)

# #13 converts a list with duplicates into a set to remove duplicates.
# list_with_duplicates = [1,2,2,3,4,4,5]
# set_from_list = set(list_with_duplicates)
# print("set created from list to remove duplicates:",set_from_list)

# #14 check if a set is a subset of another set.
# setA = {1,2}
# setB = {1,2,3,4,5}
# is_subset = setA.issubset(setB)
# print("Is setA a subset of setB?:",is_subset)

# #15 write a program to find all unique characters in a string using a set.
# input_string = "hello,world!"
# unique_characters= set (input_string)

# print ("unique chacters in the string:",unique_characters)

#16 given two lists of students (cricket and football),find students who play both sports (intersection).
# cricket_players = ['Alice', 'Bob', 'Charlie', 'David']
# football_players = ['Charlie', 'David', 'Eve', 'Frank']

# cricket = set(cricket_players)
# football = set(football_players)
# both_sports = cricket.intersection(football)
# print("Students who play both cricket and football:",both_sports)

# #17 given two lists of students ,find students who play  only cricket(difference).
# only_cricket = cricket.difference(football)
# print("students who play only cricket :",only_cricket)

# #18 Take a sentence as input and print all unique words using a set .
# sentence = "This is a sample sentence with several words this is a test"
# words = sentence.lower().split()
# unique_words = set(words)
# print("unique words int the sentence:",unique_words)

# write a program to check if two sets are equal(ignoring order).
setX = {1,2,3,4}
setY = {4,3,2,1}
are_equal = setX == setY
print("Are setX and setY equal?:",are_equal)

# 20 create two sets and check if they have at least one common element in common(hint: use intersection).
setM = {'apple', 'banana', 'cherry'}
setN = {'cherry', 'date', 'fig'}
have_common_element = len(setM.intersection(setN)) > 0


print("Do setM and setN have at least one common element?:",have_common_element)







