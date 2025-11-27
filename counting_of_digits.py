n=5873
num=n
count = 0
while num>0:
    num = num//10
    count+=1
print(count)



from math import *

n1=123456

def count_of_digits(n):
    num =n
    return(int(log10(num)+1))


print(count_of_digits(n1))