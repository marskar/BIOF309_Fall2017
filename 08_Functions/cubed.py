# Recall that the power function we used in class is:

# this code is not working

# TODO add new capability


def power(x, y):
    value = int(x)**int(y)
    return value

def cubed(num):
    number = int(num)
    result = power(number, 3)
    return result

file_connection = open("input.txt")
numbers = file_connection.read()

numbers_list = numbers.split()

output_connection = open("cubed-test.txt", 'w')

for item in numbers_list:
    cubed_number = cubed(item)
    output_connection.write(str(cubed_number) + "\n")

output_connection.close()
