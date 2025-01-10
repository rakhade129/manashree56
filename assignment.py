# # 1. Print Statement 

# #Q1: Print the phrase "Hello, World!" using the print statement
# print("Hello, World!")

# #Q2: Print three different messages on separate lines. 
# print("THESE ARE")
# print("THREE")
# print("DIFFERENT SENTENCES")

# #Q3: Print three different messages on separate lines using one print statement.
# print("THESE ARE","THREE ", "DIFFERENT SENTENCES", sep='\n')

# #Q4: Concatenate and print two variables
# print("Manashree"+"Rakhade")

# #Q5: Print three words separated by a specific character ‘$’.
# print("three", "different","words",sep="$")

# #Q6: Print two messages on the same line using the end parameter.
# print("two","messages",end=" ")

# #Q7: Print a message with quotes around it.
# print('"message with quotes"')
 
 
# # Q8: Print the result of a Boolean expression.
# print(bool(1))
# print(bool(0))

# ###########################################  2.Type casting:  #############################################################
# #Q1: Convert an integer to a float. 
# x = 10
# y = float(x)
# print(y)

# #Q2: Convert a float to an integer. 
# x = 20.5
# y = int(x)
# print(y)

# #Q3: Convert a string to an integer. 
# x = "100"
# y = int(x)
# print(x,type(x))
# print(y,type(y))

# #Q4: Convert a string to a float.

# x = "100"
# y = float(x)
# print(x,type(x))
# print(y,type(y))

# #Q5: Convert an integer to a string. 
# x = 100
# y = str(x)
# print(x,type(x))
# print(y,type(y))

# #Q6: Convert a float to a string
# x = 10.0
# y = str(x)
# print(x,type(x))
# print(y,type(y))

# #Q7: Convert a binary string to an integer. 
# # x = bin
# # y = int(x)
# # print(x,type(x))
# # print(y,type(y))



# #3. Operators  
# # Q1. Create a program that takes two numbers as input and prints their sum.
# x = int(input("ENTER A NUMBER "))
# y = int(input("ENTER A NUMBER "))
# print(x+y)

# #Q2. Write a program that subtracts the second number from the first. Take these two numbers as input.
# x = int(input("ENTER A NUMBER "))
# y = int(input("ENTER A NUMBER "))
# print(y-x)

# # Q3.Create a program that multiplies two numbers taken as input.
# x = int(input("ENTER A NUMBER "))
# y = int(input("ENTER A NUMBER "))
# print(x*y)

# #Q4. Write a program that divides the first number by the second (non-zero) number. Take these two numbers as input.
# x = int(input("ENTER A NUMBER "))
# y = int(input("ENTER A NUMBER "))
# if (y!=0):
#    print(x/y)
# else:
#    print("enter a non zero number")

# #Q5. Create a program that performs floor division on two numbers. Take these two numbers as input.
# x = int(input("ENTER A NUMBER "))
# y = int(input("ENTER A NUMBER "))
# print(x // y)

# #Q6. Write a program that calculates the remainder when the first number is divided by the second (non-zero) number. Take these two numbers as input.
# x = int(input("ENTER A NUMBER "))
# y = int(input("ENTER A NUMBER "))
# print(x % y)

# #Q7.Create a program that calculates the result of raising the first number to the power of the second number. Take these two numbers as input. (exponention)
# x = int(input("ENTER A NUMBER "))
# y = int(input("ENTER A NUMBER "))
# print(y ** x)

#Q8.Write a program that calculates compound interest. Take the principal amount, rate of interest, and time as input.
# p = int(input("principal amount"))
# r = int(input("rate of interest"))        
# t = int(input("time"))
# n = int(input("number of times interest applied per time period"))
# print(p*(1+(r/n)**(n*t)))

# x = int(input("enter a number"))
# y = int(input("enter a number"))
# z = int(input("enter a number"))
# if x>y:
#     if x>z:
#         print(x,"is greatest number")
# elif y>x:
#     if y>z:
#         print(y, "is greatest number")
# else:
#     print(z,"is greatest number")

# x = int(input("enter a number"))
# y = int(input("enter a number"))
# z = int(input("enter a number"))
# if(x==y) and (y==z):
#     print("EQUAL")
# else:
#     print("not equal")

#=============================== table in for loop ==================================

a=int(input("enter a number:"))
for i in range(1,11):
    print(i*a)







    
    

 









