#1 open student.txt in read mode and print its content.


with  open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt","r") as f1:
    content = f1.read()
    print(content)

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
count =  0
with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "r") as f1:
    for line in f1:
        count += 1
print("Number of students:" , count)

# #6 Open students.txt in write mode and write 3 new student records. 
# with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "w") as f1:
#     f1.write("Ram\n")
#     f1.write("Mohan\n")
#     f1.write("Shyam\n")

#7 After writing, open the file again and print its content. 
# Step 1: Write student records
with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "w") as f:
    f.write("Ram\n")
    f.write("Shyam\n")
    f.write("Mohan\n")

# Step 2: Open again in read mode and print content
with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "r") as f:
    content = f.read()
    print(content)

# 8 Open students.txt in append mode and add a new student: "Karan, 23, Pune".
with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "a") as f:
    f.write("Karan, 23, Pune\n")

# 9 Verify that the new student was added at the end.
# Read the file and print its content to verify
with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "r") as f:
    content = f.read()
    print(content)


#10 Open the file in r+ mode and update the first student’s name from "Amit" to "Amit Kumar".
with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "r+") as f:
    lines = f.readlines()          # read all lines

    # update first student name
    if lines:
        lines[0] = "Amit Kumar\n"

    f.seek(0)                      # move cursor to beginning
    f.writelines(lines)            # write updated content
#11  Use r+ mode to move the cursor to the end of the file and add a new student "Sneha, 20, 
# Hyderabad".

with open(r"C:\Users\thaku\OneDrive\Desktop\Students.txt", "r+") as f:
    f.seek(0,2)
    f.write("Sneha,20,Hydrabad\n")

