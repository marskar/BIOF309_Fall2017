def countdown_from_y_to_x(y, x):
    """greatest function ever"""
    n=y
    while(n>=x):
        print(n)
        n = n-1 #n -= 1

def sum_it(z,g):
    """please provide two integers, first bigger than second"""
    n=z
    all_numbers = []
    while(n>=g):
        #print(n)
        all_numbers.append(n)
        n = n-1 #n -= 1
    s=0
    for i in all_numbers:
        s = s + i
    if (z == 0) and (g==0):
        return s, "summation OF ZERO successful!"
    else:
        if (s == 0):
            return s, "summation FAILED"
        else:
            return s, "summation successful!"
