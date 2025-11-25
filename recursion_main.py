def count_digits(n):
    if n>0 and n<10:
        return 1
    elif n==0:
        return 0

    smallN = int(n/10)
    smallAns = count_digits(smallN)
    ans = 1+smallAns
    return ans

count_digits(968)3er 