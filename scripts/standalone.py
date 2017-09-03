"""greatest modeule ever"""
def countdown_from_y_to_x(y, x):
    """greatest function ever"""
    n=y
    while(n>=x):
        print(n)
        n = n-1 #n -= 1

def sum_it(z,g):
    """NO, greatest function ever"""
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

my_result = sum_it(10,5)
print(my_result)
my_result = sum_it(20,5)
print(my_result)
my_result = sum_it(1000,5)
print(my_result)
#countdown_from_y_to_x(35,30)
#countdown_from_y_to_x(44,30)
#countdown_from_y_to_x(55,30)
