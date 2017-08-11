from my_math import power

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Square all of hte numbers that we have

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("power")    # naming it "power"
args = parser.parse_args()      # returns data from the options specified (echo)
print("Power is: %i" % args.power)

for number in data:
    print(power(number, int(args.power)))
