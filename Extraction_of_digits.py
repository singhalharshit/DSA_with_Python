"""
    Playing with digits 
    1- Reversing (Palindrome)
    2- Counting the Digits
    3- Armstrong Number
    4 - To find the factors or divisors
"""

'''
1- Reversing

n=5873

num=n
reversed_num=0
while num>0:
    last_digit = num%10
    reversed_num= reversed_num * 10 + last_digit
    num=num//10

print("Reversed num is: ", reversed_num)

'''

'''
2- Counting the Digits

num=123456789
count_of_digits = 0

num_copy = num

while num_copy > 0:
    rem=num_copy%10
    count_of_digits+=1
    num_copy = num_copy//10


print('Total Count of Digits', count_of_digits)


# Another way to do the same is by taking the log and then adding 1 to and then converting it to integer

import math

n=123456789
num=n
val = math.log10(num)
print(int(val+1))

'''

'''
# 3 - Armstrong Number

armstrong_number = 123
copy_number=armstrong_number
total_digits = 0
while copy_number>0:
    rem=copy_number%10
    total_digits+=1
    copy_number = copy_number//10
copy_number=armstrong_number
check = 0
while copy_number>0:
    raised_to_power= copy_number%10
    raised= raised_to_power**total_digits
    check += raised
    copy_number = copy_number//10

if check == armstrong_number:
    print(check,True)
else:
    print(check,False)
        
'''

# 4 - To find the factors or divisors


num=10
l=[]

for i in range(1,num+1):
    if num%i==0:
        l.append(i)

print("The factors are", l)

# By List comprehensions

l1= [i for i in range(1,num+1) if num%i==0]
print(l1)