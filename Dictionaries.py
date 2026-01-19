# 1 create a dictionaries 0f 5 countries and their capitals.print it .
countries_capitals = {'USA':'Washington, D.C.', 'France':'Paris', 'Japan':'Tokyo', 'India':'New Delhi', 'Germany':'Berlin'}
print("Countries and their capitals:",countries_capitals)

# 2 Access the capital of 'india ' from the dictionary
print("capital of India:",countries_capitals['India'])

# 3 Add a new key-value pair "japan":tokyo to the dixtionary
countries_capitals['Japan'] = 'Tokyo'
print("Updated countries and their capitals:",countries_capitals)

# 4 Update the capital of "USA" to "Washington" to "New York"
countries_capitals['USA'] = 'New York'
print("Updated countries and their capitals after changing USA's capital:",countries_capitals)

# 5 Delete the key "France"  using del
del countries_capitals['France']
print("Countries and their capitals after deleting France:",countries_capitals)

# 6 Create a ditionary of students and  marks . Use . keys() to print all students names
students_marks = {'Alice':85, 'Bob':90, 'Charlie':78, 'David':92}
print("Student names:",students_marks.keys())

# 7 Use .values () to print all marks 
print("Students marks:",students_marks.values())

# 8 Use .items () to print all key-value pairs
print("Students and their marks:",students_marks.items())

# 9 Use .get() to access the value of " Rahul" safely (if not foumd ,return "Not Found")
students_marks['Rahul'] = 88
print("Marks of Rahul:",students_marks.get('Rahul', 'Not Found'))
