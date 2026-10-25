def is_prime(x):
    if x <2:
        return False
    if x >2:
        for n in range(2,x):
            x%n !=0
            return True
     