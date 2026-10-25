def digit_sum (n):
    x = 0
    while n > 0:
        digit = n % 10
        x = x+digit
        n=n//10
    return x