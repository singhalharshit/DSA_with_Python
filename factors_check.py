# n=20

# num =n
# factors = []

# for i in range(1,int(num/2)+1):
#     if num%i ==0:
#         factors.append(i)
# factors.append(num)
# print(factors)


'''
Docstring for factors_check
- Finding factors using sqrt logic
'''


from math import sqrt

n=40

num = n
factors = []

for i in range(1,int(sqrt(num))+1):
    if num%i ==0:
        factors.append(i)
        if i!=num//i:
            factors.append(num//i)
    
print(sorted(factors))