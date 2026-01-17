#Q1. print Numbers (for loop)
# write a program to print numbers from 1 to 10 using a  for loop.

# for i in range (1,11):
#     print(i)

# Q2. Sum of Numbers (while loop)
# find the sum of first 10 natural numbers using a while loop.
# sum = 0
# i = 1

# while i<=10:
#      sum += i
#      i += 1
# print("Sum of first 10 natural numbers is:",sum)

# Q3. Multiplication table (for loop)
# Take a number as input and print its multiplication table up to 10
# num = int (input("Enter a number to print its multiplication table: "))

# for i in range (1,11):
#     print (f"{num} x {i} = {num * i}")

# Q4.Factorial (while loop)
# find rhe factorial f a number using a while loop.

# num = int (input("Enter a number to find its factorial :"))
# factorial = 1
# i = 1

# while i <= num:
#     factorial *= i
#     i += 1
# print (f"factorial of {num} is :{factorial}")

# Q5.Reverse a number (while loop)
# Take an integer as input and reverse its digits(e.g.,123 => 321)

# num = int (input ("Enter an integer to reverse its digits:"))
# reversed_num = 0 

# while num > 0:
#     digit = num %10
#     reversed_num = reversed_num *10 + digit
#     num //= 10
# print("Reversed number is:",reversed_num)

# Q6. Even Numbers (for loop with range)
# Print all even numbers between 1 and 50 .

# for i in range (1,51):
#     if i % 2 == 0:
#         print(i)
        
# Q7.Sum of Digits (while loop)
# Take a number s input and find the sum of its digts.

# num = int (input("Enter a number to find the sum of  its digits :"))
# sum_of_digits = 0

# while num > 0:
#     digit = num % 10
#     sum_of_digits += digit
#     num //= 10
# print("Sum of digits is:",sum_of_digits)        

# Q8.Fibonacci series (for loop)
# Print the first 10  terms of the fibonacci series.

a, b = 0, 1
print("Fibonacci series:")

for i in range (10):
    print(a, end = " ")
    a, b = b, a + b

