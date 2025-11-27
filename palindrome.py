n=121


def check_palin(n):
    rev = 0
    num=n
    while num>0:
        rem = num%10
        rev = (rev*10) + rem
        num//=10
    return rev == n

print(check_palin(n))
