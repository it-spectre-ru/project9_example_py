# # 100+ Python challenging programming exercises for Python 3
 
# ## 1. Level description
# ### Level 1  Beginner 
# Beginner means someone who has just gone through an introductory Python course. He can solve some problems with 1 or 2 Python classes or functions. Normally, the answers could directly be found in the textbooks.
 

### Question 1
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
 
# Hints: 
# Consider use range(#begin, #end) method

l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))
 
# print(','.join(l))





### Question 2
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
 

# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
 
# x=int(input())
# print(fact(x))





### Question 3

# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Consider use dict()
 

# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
 
# print(d)




### Question 4
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple

# values=input()
# l=values.split(",")
# t=tuple(l)
# print(l)
# print(t)




### Question 5
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
 
# Hints:
# Use __init__ method to construct some parameters

# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
 
#     def getString(self):
#         self.s = input()
    
#     def printString(self):
#         print(self.s.upper())
 
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()





 
### Question 6

# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
 
# import math
# c=50
# h=30
# value = []
# items=[x for x in input().split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
 
# print(','.join(value))









# ### Level 2  Intermediate 
# Intermediate means someone who has just learned Python, but already has a relatively strong programming background from before. He should be able to solve problems which may involve 3 or 3 Python classes or functions. The answers cannot be directly be found in the textbooks.
 
# ### Level 3  Advanced. 
# He should use Python to solve more complex problem using more rich libraries functions and data structures and algorithms. He is supposed to solve the problem using several Python standard packages and advanced techniques.