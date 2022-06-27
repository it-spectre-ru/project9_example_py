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
 

n=int(input())
d=dict()
for i in range(1,n+1):
    d[i]=i*i
 
print(d)









# ### Level 2  Intermediate 
# Intermediate means someone who has just learned Python, but already has a relatively strong programming background from before. He should be able to solve problems which may involve 3 or 3 Python classes or functions. The answers cannot be directly be found in the textbooks.
 
# ### Level 3  Advanced. 
# He should use Python to solve more complex problem using more rich libraries functions and data structures and algorithms. He is supposed to solve the problem using several Python standard packages and advanced techniques.