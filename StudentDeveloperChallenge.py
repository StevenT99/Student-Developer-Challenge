# Steven Thorpe
# Option 2 Complete the tasks in any order and in any language. You may use helper functions if desired.

import math 

# 1: Write a function that will reverse the given input string.For Example: function("string") -> "gnirts"

def problem_p1():
    sString = input("Give an input to reverse: ") 
    sString = sString [::-1]
    print(sString)

# 2: Write a function that accepts three integers as input and returns as output the largest of the three.For Example: function(1, 3, 2) -> 3

def problem_p2() :
    iNumber1 = int(input("Enter your first number: "))
    iNumber2 = int(input("Enter your second number: "))
    iNumber3= int(input("Enter your third number: "))
    iMax = max(iNumber1, iNumber2, iNumber3)
    print( "The largest number entered is " + str(iMax))

# 3: Write a function that calculates the factorial of an input integer using recursion.Factorial: n! = n * (n-1) * (n-2) * ... * 1, so 3! = 3 * 2 * 1 = 6For Example:function(3) = 6

def problem_p3() :
    iNumber = int(input("Input an integer: "))
    iFact = math.factorial(iNumber)
    print(iFact)

# Write a function that calculates the Nth entry of the Fibonaccisequence (Do not include 0 in the sequence).Fibonacci Sequence: 1, 1, 2, 3, 5, 8, ...
# The sequence is calculated by summing two numbers and adding the sum to the sequence.1 (the sequence starts with 1)1 + 0 = 1 
# (1 was the only element, so add 0, then put the result on the end of the sequence1, 11 + 1 = 21, 1, 21 + 2 = 31, 1, 2, 32 + 3 = 51, 1, 2, 3, 5etc.
# So your function should behave asfunction(1) -> 1function(2) -> 1function(3) -> 2function(4) -> 3function(5) -> 5etc.

def problem_p4() :
    iEntry = int(input("Enter a number to see it's subsequent value in the Fibonacci Sequence: "))
    iFibo1 = 1
    iFibo2 = 0
    iFibo3 = 0 
    
    for iFibo3 in range(1,iEntry) :
        iFibo3 = (iFibo1 + iFibo2)
        iFibo1 = (iFibo2)
        iFibo2 = (iFibo3)
    
    print("The entry for number " + str(iEntry) + " in the Fibonacci sequence is: " + str(iFibo3))

# Here is an input prompt in order to run each one of the 4 functons

functionNumber = 0

while (functionNumber != 5) :
    functionNumber = int(input("Enter a function 1-4 that you would like to see or enter 5 to stop: "))

    if (functionNumber == 1) :
        problem_p1()
    elif (functionNumber == 2) :
        problem_p2()
    elif (functionNumber == 3) :
        problem_p3()
    elif (functionNumber == 4) :
        problem_p4()

    
