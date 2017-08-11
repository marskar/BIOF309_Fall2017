import argparse
from my_math import power

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Square all of hte numbers that we have

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--power",
                    help="The power to raise the number to",
                    type=int,
                    required=True)  # Add type
args = parser.parse_args()      # returns data from the options specified
print("Power is: %i" % args.power)

for number in data:
    print(power(number, args.power))  # we no longer need to change to int
