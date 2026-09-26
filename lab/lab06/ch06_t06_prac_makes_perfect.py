def cube(number=float) :
    return number**3

def by_three(number=float):
    if number % 3 ==0 :
       number=cube(number)
       return cube(number)
    else:
        return False