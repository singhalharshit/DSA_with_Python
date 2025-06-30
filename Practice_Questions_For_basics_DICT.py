"""

# 1. Create an empty dictionary and add 3 key-value pairs.

d = {}
d['name']='Harshit'
d['age']=25
d['gender']='male'

print(d)

"""

"""
# 2. Retrieve the value of a specific key.

student = {
    'name': 'Aarav',
    'age': 22,
    'course': 'Computer Science'
}

print(student['course'])

"""

"""
# 3. Update the value of an existing key.

student = {
    'name': 'Aarav',
    'age': 22,
    'course': 'Computer Science'
}

student['course']="Computer Science and Engineering"

print(student)

"""


"""
# 4. Delete a key from a dictionary.

student = {
    'name': 'Aarav',
    'age': 22,
    'course': 'Computer Science',
    'delete_key':'Delete this key0'
}

# del(student['delete_key'])
student.pop('delete_key')

print(student)
"""


"""
# 5. Check if a key exists in the dictionary.

student = {
    'name': 'Aarav',
    'age': 22,
    'course': 'Computer Science'
}


if 'name' in student.keys():
    print(True)
    
"""


"""
# 6. Iterate over keys and print them.


employee = {
    'id': 101,
    'name': 'Sneha',
    'age': 29,
    'department': 'Finance',
    'position': 'Manager',
    'salary': 75000,
    'full_time': True
}

# for i in employee.keys():
#     print(i)

for i in employee:
    print(i)

"""    


"""
# 7. Iterate over values and print them.

employee = {
    'id': 101,
    'name': 'Sneha',
    'age': 29,
    'department': 'Finance',
    'position': 'Manager',
    'salary': 75000,
    'full_time': True
}

# for i in employee.values():
#     print(i)
    
for i in employee:
    print(employee[i])

"""

"""
# 8. Iterate over key-value pairs and print them.

employee = {
    'id': 101,
    'name': 'Sneha',
    'age': 29,
    'department': 'Finance',
    'position': 'Manager',
    'salary': 75000,
    'full_time': True
}


for i,j in employee.items():
    print(f'{i}:{j}')
"""


"""
# 9. Get all keys as a list.

employee = {
    'id': 101,
    'name': 'Sneha',
    'age': 29,
    'department': 'Finance',
    'position': 'Manager',
    'salary': 75000,
    'full_time': True
}
keys_list = []

for i in employee:
    keys_list.append(i)

print(keys_list)

"""


"""
# 10. Get all values as a list.

employee = {
    'id': 101,
    'name': 'Sneha',
    'age': 29,
    'department': 'Finance',
    'position': 'Manager',
    'salary': 75000,
    'full_time': True
}
values_list = []

for i in employee:
    values_list.append(employee[i])

print(values_list)

"""


"""
# 11. Count the frequency of characters in a string and store in a dictionary.

text = "programming is fun"
frequency_mapper = {}


for i in text:
    if i in frequency_mapper:
        frequency_mapper[i]+=1
    else:
        frequency_mapper[i]=1

print(frequency_mapper)

"""

"""
# Additional Question for palindrome

num = 121
num_copy = num

rev=0

while num_copy>0:
    rem=num_copy%10
    rev = (rev*10)+rem
    num_copy=num_copy//10

if rev == num:
    print(True)
else: print(False)

"""


"""
# 12. Merge two dictionaries.


dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}


# dict1.update(dict2)
# print(dict1)

for i in dict2:
    dict1[i]=dict2[i]

print(dict1)

"""


"""
# 13. Sort a dictionary by values.

scores = {
    'Alice': 88,
    'Bob': 95,
    'Charlie': 78,
    'David': 92
}

sorted_items = []

temp_scores = scores.copy()
print(temp_scores)


while temp_scores:
    min_key = min(temp_scores, key=temp_scores.get)
    print(min_key)
    sorted_items.append((min_key, temp_scores[min_key]))
    temp_scores.pop(min_key)

print(sorted_items)

sorted_dict = dict(sorted_items)

print(sorted_dict)

"""

"""
# 14. Create a dictionary from two lists: one of keys, one of values.
keys = ['name', 'age', 'gender']
values = ['Harshit', 25, 'male']

d={}

for i in range(len(keys)):
    if i not in d:
        d[keys[i]]=values[i]
        

print(d)

"""

"""
# 15. Remove all duplicate values in a dictionary.

data = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20
}

d= {}

for i in data:
    if data[i] not in d.values():
        d[i]=data[i]

print(d) 
"""


"""
# 16. Swap keys and values in a dictionary.

data = {
    'name': 'Harshit',
    'age': 25,
    'gender': 'male'
}


d={}

for i in data:
    d[data[i]]=i

print(d)

"""


"""
# 17. Group words by their first letter using a dictionary.

words = ['apple', 'ant', 'banana', 'ball', 'cat', 'car', 'dog']
d={}

for i in words:
    if i[0] not in d:
        d[i[0]] = []
    d[i[0]].append(i)
    
print(d)

"""

"""
# 18. Convert a list of tuples to a dictionary.

data = [('a', 1), ('b', 2), ('c', 3)]
d={}

for i in data:
    d[i[0]]=i[1]

print(d)
"""

"""
# 19. Find the key with the maximum value.

marks = {
    'Math': 88,
    'English': 76,
    'Science': 91,
    'History': 67
}
max_key1 = max(marks, key=marks.get)
print(max_key1)

max_value = 0
max_key =''
for i in marks:
    if marks[i]>max_value:
        max_value = marks[i]
        max_key = i
        
print(max_key)
"""


"""

# 20. Find all keys that have a specific value.

data = {
    "a": 3,
    "b": 5,
    "c": 3,
    "d": 7,
    "e": 5,
    "f": 9
}

target_value = 5
l=[]

for i in data:
    if data[i]==target_value:
        l.append(i)
    
print(l)

"""


# 21. Create a nested dictionary representing student records (name, marks, grade). - didn't got the ask 


# 22. Access and update nested values in a dictionary.

students = {
    "student1": {"name": "Alice", "marks": 85, "grade": "A"},
    "student2": {"name": "Bob", "marks": 76, "grade": "B"},
    "student3": {"name": "Charlie", "marks": 92, "grade": "A"},
    "student4": {"name": "David", "marks": 64, "grade": "C"}
}

for key,value in students.items():
    if value.keys() == 'marks':
        