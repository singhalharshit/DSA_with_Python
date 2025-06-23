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


# 16. Print only the unique numbers from a list.

my_list = [10, -5, 22, 0, 7, 10, -3, 14, 22, 8, 7, 19, -5, 3, 0, 14, 25, 18, 8, -1, 33, 19, 3, -7, 25, 18, 42, -1, 33, 5]
unique_list  = []

for i in range(len(my_list)):
    if my_list.count(my_list[i]):
        my_list.remove(my_list[i])
    else:
        unique_list.append(my_list[i])
        

print(unique_list)