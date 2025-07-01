"""
Given two integer variables a and b, and a boolean variable flag. The task is to check the status and return accordingly.

Return True for the following cases:

Either a or b (not both) is non-negative and the flag is false.
Both a and b are negative and the flag is true.
Otherwise, return False.

"""


"""
class Solution:
    def checkStatus(self, a, b, flag):
        if flag:
            return a < 0 and b < 0
        else:
            return (a < 0 < b) or (b < 0 < a)

# Test cases
obj = Solution()
print(obj.checkStatus(-1, -5, True))   
print(obj.checkStatus(3, -1, False))   
print(obj.checkStatus(-3, -1, False))  
print(obj.checkStatus(3, 2, False))  
"""


"""
    Given a positive integer x. Your task is to check, if it is even or odd (Any number that gives zero as remainder when divided by 2 is an even number)

"""

"""
def checkOddEven(x):
    if (x % 2 == 0):
        return True

    else:
        return False

"""


"""
    There are two friends, John and Smith, and the parameters j_angry and s_angry to indicate if each is angry. You are in trouble if both of them are angry or no one of them is angry.
    Now, complete the function which returns true if you are in trouble, else return false

"""
"""
def friends_in_trouble(j_angry, s_angry):
    if j_angry == True and s_angry == True:
        return True
    elif j_angry == False and s_angry == False:
        return True
    return False

print(friends_in_trouble(False, False))
"""


"""
You are given a number n. The number n can be negative or positive. If n is negative, print numbers from n to 0 by adding 1 to n in the neg function. If positive, print numbers from n-1 to 0 by subtracting 1 from n in the pos function.
Note:- You don't have to return anything, you just have to print the array.

"""


"""
def pos(n):
    if n == 0:
        print("already Zero")
    else:
        while n > 0:
            n -= 1
            print(n, end=" ")

def neg(n):
    if n == 0:
        print("already Zero")
    else:
        while n <= 0:
            print(n, end=" ")
            n += 1

pos(4)
neg(-777)
"""


"""
    You are given a number  and you have to print your answer according to the following:
    If the number is divisible by 3, you print "Fizz" (without quotes)
    If the number is divisible by 5, you print "Buzz" (without quotes)
    If the number is divisible by both 3 and 5, you print "FizzBuzz" (without quotes)
    In any other case, you print the number itself

    Note: You should add a newline character after print() statement.
"""


"""
def fizzBuzz(number):
    if number%3==0 and number%5 ==0:
        print("FizzBuzz")
    elif number%5==0:
        print("Buzz")
    elif number%3==0:
        print("Fizz")
    else:
        print(number)

fizzBuzz(3)     # Output: Fizz
fizzBuzz(5)     # Output: Buzz
fizzBuzz(15)    # Output: FizzBuzz
fizzBuzz(1)     # Output: 1
fizzBuzz(30)    # Output: FizzBuzz
fizzBuzz(13)    # Output: 13
fizzBuzz(10)    # Output: Buzz
fizzBuzz(6)     # Output: Fizz
fizzBuzz(0)     # Output: FizzBuzz  (0 is divisible by both 3 and 5)
fizzBuzz(-3)    # Output: Fizz
fizzBuzz(-5)    # Output: Buzz
fizzBuzz(-15)   # Output: FizzBuzz
fizzBuzz(8)     # Output: 8

"""



"""
    Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).

"""

""""
def printIncreasingPower(x):
    i=1
    while (i**2)<=x:
        print (i**2, end = " ")
        i+=1
        

printIncreasingPower(10)
"""


"""

You are given a number N, you need to print its multiplication table.
Note: Please go through the range function to understand why it's useful in for loops.

"""


"""
def multiplicationTable(N):
    for i in range(1,11):
        print(N*i,end=" ")

multiplicationTable(6)

"""


"""
Given a number x, the task is to print the from x to 0 in decreasing order in a single line.

"""

"""
def printInDecreasing(x):
    while (x >= 0):
        print(x ,end= " ")
        x -= 1

printInDecreasing(10)
"""

