"""
    To store a frequency into dictionary
"""

# Method 1 - Iterating over an empty dict if a key is already in dict increase the count else add the key 


sample_list = [4, 2, 7, 4, 9, 2, 7, 4, 1, 3, 9, 2, 6, 7, 3]
frequency_map ={}
for i in range(0,len(sample_list)):
    if sample_list[i] in frequency_map:
        frequency_map[sample_list[i]]+=1
    else:
        frequency_map[sample_list[i]]=1

print(frequency_map)
