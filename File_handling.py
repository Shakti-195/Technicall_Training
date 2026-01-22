#1 open student.txt in read mode and print its content.


# with  open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt","r") as f1:
#     content = f1.read()
#     print(content)

# #2 Read only the first line of the file.
# with  open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt","r") as f1:
#     content = f1.readline()
#     print(content)

#3 Read all lines into a list and print them.

# with  open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt","r") as f1:
#     content = f1.readlines()
#     print(content)

#4 Loop through the file and print each line separately. 

# with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "r") as f1:
#     for line in f1:
#         print(line.strip())

# 5 Count the number of students (lines) in the file.
# count =  0
# with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "r") as f1:
#     for line in f1:
#         count += 1
# print("Number of students:" , count)

# # #6 Open students.txt in write mode and write 3 new student records. 
# # with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "w") as f1:
# #     f1.write("Ram\n")
# #     f1.write("Mohan\n")
# #     f1.write("Shyam\n")

# #7 After writing, open the file again and print its content. 
# # Step 1: Write student records
# with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "w") as f:
#     f.write("Ram\n")
#     f.write("Shyam\n")
#     f.write("Mohan\n")

# # Step 2: Open again in read mode and print content
# with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "r") as f:
#     content = f.read()
#     print(content)

# # 8 Open students.txt in append mode and add a new student: "Karan, 23, Pune".
# with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "a") as f:
#     f.write("Karan, 23, Pune\n")

# # 9 Verify that the new student was added at the end.
# # Read the file and print its content to verify
# with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "r") as f:
#     content = f.read()
#     print(content)


# #10 Open the file in r+ mode and update the first student’s name from "Amit" to "Amit Kumar".
# with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "r+") as f:
#     lines = f.readlines()          # read all lines

#     # update first student name
#     if lines:
#         lines[0] = "Amit Kumar\n"

#     f.seek(0)                      # move cursor to beginning
#     f.writelines(lines)            # write updated content
# #11  Use r+ mode to move the cursor to the end of the file and add a new student "Sneha, 20, 
# # Hyderabad".

# with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "r+") as f:
#     f.seek(0,2)
#     f.write("Sneha,20,Hydrabad\n")

# # 12 Open products.txt in read mode and display all product records
# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt","r") as f :
#     print(f.read())

# #13 Read and print only the first product from the file
# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "r") as f:
#     print(f.readline().strip())

# #14 Read all lines into a list and print the list

# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "r") as f:
#     lines = f.readlines()
#     print(lines)

# 15 Read the file line by line using a loop
# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "r") as f:
#     for line in f:
#         print(line.strip())

# 16 Count the total number of products (lines)
# count = 0
# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "r") as f:
#     for line in f:
#         count += 1

# print("Total products:", count)

    
# 17 Display only the product names
# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "r") as f:
#     for line in f:
#         data = line.split(",")
#         print(data[1].strip())

# 18  Display products whose price is greater than 10000 
# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "r") as f:
#     for line in f:
#         data = line.split(",")
#         if int(data[2].strip()) > 10000:
#             print(line.strip())

# 19 Open inventory.txt in write mode and write new data
# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "w") as f:
#     f.write("P201, Headphones, 2000, Electronics\n")
#     f.write("P202, Sofa, 28000, Furniture\n")
#     f.write("P203, Printer, 12000, Electronics\n")

# # 20 After writing, reopen the file and display its contents
# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "r") as f:
#     print(f.read())


# 21 Open the file in append mode and add:
# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "a") as f:
#     f.write("P204, Fan, 3500, Electronics\n")

# # 22 Verify that the new product is added at the end
# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "r") as f:
#     print(f.read())

#23 Update product name "Mouse" → "Wireless Mouse"

# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "r+") as f:
#     lines = f.readlines()

#     for i in range(len(lines)):
#         if "Mouse" in lines[i]:
#             lines[i] = lines[i].replace("Mouse", "Wireless Mouse")

#     f.seek(0)
#     f.writelines(lines)

# # 24 Using r+ mode, move cursor to end and add:

# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "r+") as f:
#     f.seek(0, 2)   # move cursor to end
#     f.write("P205, Bed, 45000, Furniture\n")

# #25 Count how many products belong to Electronics category
# count = 0
# with open(r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "r") as f:
#     for line in f:
#         if "Electronics" in line:
#             count += 1

# print("Total Electronics products:", count)

# # 26 Create expensive_products.txt and write products with price > 20,000

file = open (r"C:\Users\thaku\OneDrive\Desktop\inventory.txt", "r")
new_file =  open (r"C:\Users\thaku\OneDrive\Desktop\expensive_products.txt","w")

for line in file :
    data = line.strip().split(",")
    price = int (data[2])

    if price > 20000:
        new_file.write(line)

file.close()
new_file.close()