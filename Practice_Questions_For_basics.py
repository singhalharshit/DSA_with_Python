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