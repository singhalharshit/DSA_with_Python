"""
# 1. Create a list of 10 integers. Print the first and last elements


l=[1,2,3,4,5,6,7,8,9,0]

print(l[0],l[-1])

"""


"""
# 2. Add 100 to the end of the list using append().

l=[1,2,3,4]
l.append(100)
print(l)

"""


"""
# 3. Insert 55 at position 5.

l=[10,11,12,13,14,15,16,17,18,19,20]
l.insert(5,55)
print(l)

"""

"""
# 4. Delete the 3rd item in the list using del.

l=[10,11,12,13,14,15,16,17,18,19,20]
del l[3]
print(l)

"""


"""
# 5. Remove the number 55 from the list using remove().

l = [10,11,12,13,14,55,15,16,17,18,19,20]
l.remove(55)
print(l)

"""


"""
# 6. Pop the last item and print it.

l = [10,11,12,13,14,55,15,16,17,18,19,20]
print(l.pop())

"""


"""
# 7. Reverse the list using slicing.

l = [10,11,12,13,14,55,15,16,17,18,19,20]
l1=l[::-1]
print(l1)

"""


"""
# 8. Slice the list to get the middle 4 elements.
l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]


x= len(l)//2
print(x)

print(l[x-2:x+2])

"""

"""
# 9. Print all even-indexed elements using a loop.

l = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]

even_indexed_item = []
for i in range(len(l)):
    if i%2==0:
        even_indexed_item.append(l[i])

print(even_indexed_item)

"""


"""
# 10. Create a list of 5 inputs from user and print it

l=[]

count =0

while count<5:
    user = input("Enter your value: ")
    l.append(user)
    count+=1

print(l)
    
"""


"""

# 11. Given a list of numbers, print the sum of all even numbers

l= [2, 5, 8, 11, 14, 17, 20, 23, 26, 29,32, 35, 38, 41, 44, 47, 50, 53, 56, 59,62, 65, 68, 71, 74, 77, 80, 83, 86, 89]
even_nums = 0

for i in l:
    if i%2==0:
        even_nums+=i
        
print(even_nums)

"""

"""
# 12. Find the max and min values in the list without using max() or min()

my_list = [17, -3, 45, 0, 22, 8, 91, -20, 64, 33,5, 70, -11, 84, 38, 19, -7, 99, 12, 31,55, -30, 40, 3, 76, 23, -15, 61, 2, -1]
biggest_number = 0
smallest_number = 0

for i in range(len(my_list)):
    if biggest_number>my_list[i]:
        pass
    else:
        biggest_number = my_list[i]
    if smallest_number<my_list[i]:
        pass
    else:
        smallest_number = my_list[i]

print(biggest_number,smallest_number)

"""

"""

# 13. Count how many times 10 occurs in a list

my_list = [10, 5, 3, 10, 7, 8, 10, 2, 14, 10, 6, 1, 10, 9, 12, 10, 11, 4, 10, 13, 10, 15, 10, 0, 10, 17, 19, 10, 18, 20]

count = 0

for i in my_list:
    if i==10:
        count+=1

print(count)

print("Count from the function",my_list.count(10))

"""


"""
# 14. Replace all even numbers in a list with 'EVEN'

my_list = [4, 7, 10, 13, 22, 5, 8, 19, 2, 11, 6, 15, 14, 3, 12, 9, 16, 1, 18, 20, 17, 21, 24, 23, 0, 26, 25, 27, 30, 28]

for i in range(len(my_list)):
    if my_list[i]%2==0:
        my_list[i]='EVEN'
    
print(my_list)

"""

"""
# 15. Create a list of squares from 1 to 20 using list comprehension.

l=[i**2 for i in range(1,21)]
print(l)

"""


"""
# 16. Print only the unique numbers from a list.

my_list = [10, -5, 22, 0, 7, 10, -3, 14, 22, 8, 7, 19, -5, 3, 0, 14, 25, 18, 8, -1, 33, 19, 3, -7, 25, 18, 42, -1, 33, 5]
unique_list  = []

for i in range(len(my_list)-1,-1,-1):
    if my_list.count(my_list[i]) >1:
        my_list.pop(i)
    else:
        unique_list.append(my_list[i])



# for i in my_list:
#     if i in unique_list:
#         pass
#     else:
#         unique_list.append(i)


print(unique_list)

l=[5, 42, -7, 33, -1, 18, 25, 3, 19, 8, 14, -3, 7, 0, 22, -5, 10]
l1=[10, -5, 22, 0, 7, -3, 14, 8, 19, 3, 25, 18, -1, 33, -7, 42, 5]
print(sorted(l) == sorted(l1))

"""


"""
# 17. Find the second largest number in the list.

my_list = [10, -5, 22, 0, 7, 10, -3, 14, 22, 8, 7, 19, -5, 3, 0, 14, 25, 18, 8, -1, 33, 19, 3, -7, 25, 18, 42, -1, 33, 5]

my_list.sort()
print(my_list[-2])

# l = sorted(my_list)
# print(l[-2])

"""


"""
# 18. Sort the list in ascending order without using .sort().

my_list = [10, -5, 22, 0, 7, 10, -3, 14, 22, 8, 7, 19, -5, 3, 0, 14, 25, 18, 8, -1, 33, 19, 3, -7, 25, 18, 42, -1, 33, 5]
sorted_list = []
i = len(my_list)

while i>0:
    sorted_list.append(min(my_list))
    my_list.remove(min(my_list))
    i-=1

print(sorted_list)

"""

"""
# 19. Merge two lists and remove duplicates

list1 = [8, 3, 12, 5, 7]
list2 = [4, 7, 9, 3, 10]
list3 = []

# print(set(list1+list2))

# Incase if output is also needed in list

for i in (list1+list2):
    if i not in list3:
        list3.append(i)

print(sorted(list3))

"""


"""
# 20. Create a list of only words that start with 'A' from a sentence

sentence = "An amazing artist arrived at the ancient arena after an adventure."
words_starting_with_a = [word for word in sentence.split() if word.lower().startswith('a')]

print(words_starting_with_a)

"""


"""
# 21. Remove duplicates from a list without using set()

numbers = [4, 2, 7, 2, 4, 9, 1, 7, 5, 9]
num_dup = []

for i in numbers:
    if i not in num_dup:
        num_dup.append(i)

print(num_dup)

"""


"""
# 22. Rotate a list right by k steps (e.g. [1,2,3,4,5], k=2  [4,5,1,2,3])

l=[14, 22, 7, 39, 18, 5, 11]
k=3
j=-(k)
for i in range(k):
    
    print(l[j])
    l.insert(i,l[j])
    l.pop(j)
    j+=1

print(l)

"""


"""
# 23. Find all pairs in a list that sum to a given number.

numbers = [2, 7, 4, 5, 1, 3, 6]
target_sum = 9
pair = []
seen = set()

for i in numbers:
    complement = target_sum - i
    if complement in numbers and complement not in seen:
        pair.append([i, complement])
        seen.add(i)
        seen.add(complement)

print(pair)

"""


"""
# 24. Check if a list is a palindrome.

num_list = [1, 2, 3, 2, 1]
rev_list=[]

for i in range(len(num_list)-1,-1,-1):
    rev_list.append(num_list[i])

if num_list == rev_list:
    print(True)
else:
    print(False)


# Additional Question for me - 24. Check if a num is a palindrome.


num = 121
rev_num = 0 

while num!=0:
    rem=num%10
    rev_num = (rev_num*10 )+rem
    num = num//10
    

print(rev_num) 

"""


"""
# 25. Find the frequency of each element and store it in a dictionary.

my_list = [4, 2, 4, 5, 2, 3, 4, 3, 5, 1]
d={}

for i in range(len(my_list)):
    if my_list[i] in d:
        d[my_list[i]] +=1
    else:
        d[my_list[i]] =1

print(d)

"""

"""
# 26. Find the common elements in two lists without using sets.

list1 = [3, 6, 2, 8, 4, 7]
list2 = [5, 4, 9, 2, 1, 6]
common_list = []
for i in list1:
    if i in list2:
        common_list.append(i)
    
print(common_list)

"""


"""
# 27. Flatten a nested list like [[1,2],[3,4],[5]] to [1,2,3,4,5].


l=[[1,2],[3,4],[5]]
l1=[]

for i in range(len(l)):
    for j in l[i]:
        l1.append(j)

print(l1)

"""

"""
# 28. Generate a list of prime numbers between 1 and 100.

import math

l=[]

for i in range(2,101):
    for j in range(2,math.isqrt(i)+1):
        if i%j==0:
            break
    else:
        l.append(i)

print(l)

"""


"""
# 29. Write a program that takes a list of marks and prints grade-wise result (like >=90: A, 80-89: B, etc.).


marks = [95, 82, 67, 88, 73, 91, 59, 77, 84, 100]

for i in marks:
    if i >= 90:
        print('Grade A')
    elif 80 <= i <= 89:
        print('Grade B')
    elif 70 <= i <= 79:
        print('Grade C')
    elif 60 <= i <= 69:
        print('Grade D')
    else:
        print('Grade F')

"""


"""
# 30. Group elements in a list by their frequency.

items = [4, 2, 4, 3, 2, 1, 3, 4, 5, 2, 1, 5, 5, 5]

freq_group = {}

for i in items:
    count = items.count(i)
    if count not in freq_group:
        freq_group[count] = []
    if i not in freq_group[count]:
        freq_group[count].append(i)

print(freq_group)
"""