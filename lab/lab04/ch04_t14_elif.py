def greater_less_equal_5(answer: int) -> int:
    if answer > 5:
        return 1
    elif answer < 5:
        return -1
    else answer == 5:
        return 0


print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))
