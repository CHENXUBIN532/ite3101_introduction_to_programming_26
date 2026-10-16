list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print(a, "is greater than", b)
    elif b > a:
        print(b, "is greater than", a)
    else:
        print(a, "and", b, "are equal")
