# check if a number is positive,even , zero ,odd

# num = int(input("Enter a number: "))

# if num >0:
#     print("The number is positive")
#     if num % 2 == 0:
#         print("The number is even")
#     else:
#         print("The nunber is odd")
# elif num == 0:
#     print("The number is zero")
# else:
#     print("The number is negative")
# ========================================================================================================================================
# check if a person is eligible to vote or not 

# age = int (input("Enter your age:"))
# if age >= 18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")
# ========================================================================================================================================

# check if number is even or odd by taking input from user

# num = int(input("Enter a number:"))
# if num%2 == 0:
#     print("The number is  even:")
# else:
#     print("The number is odd:")
# ========================================================================================================================================

# check whther which no is greater between two number by taking input from user

# num = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))

# if num > num2:
#     print("First number is greater")
# else:
#     print("Second number is greater")
# =======================================================================================================================================

# # check whether a number is divisible by 5
# num = int(input("Enter a number :"))
# if num % 5 == 0:
#     print("The number is divisible by 5")
# else:
#     print("The number is not divisible by 5")

# ======================================================================================================================================

# # check whether a year is leap year or not
# year = int(input("Enter a year :"))

# if (year % 4 == 0 and year %100 !=0 or year %400 ==0):
#     print("The year is leap year")
# else:
#     print("The year is not leap year")

# ======================================================================================================================================
# write a program to  display whether a given number is single-digit ,double-digit or more than two-digit

num =int(input("Enter a number:"))
if num >=0 and num <=9:
    print("The number is single-digit")
elif(num >=10 and num <=99):
    print("The number is double-digit")
else:
    print("The number is more than two=digits")
    