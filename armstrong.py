n=153


num=n
len_of_num=len(str(num))
arm = 0

while num>0:
    rem=num%10
    arm += rem**len_of_num
    num//=10

# if arm == n:
#     print(True)

print(True if arm ==n else False)