def count(sequence, item):
    char = item
    total = 0
    for i in sequence:
        if i == char:
            total += 1
        return total
