def factorial(x):
    if x == 1:
        return 1
    else:
        total = 1
        while x > 1:
        total = total * x
        x = x-1
        return total
