my_file = open("dna.txt")
my_dna = my_file.read().rstrip("\n")

#Count the number of each base
A_count = my_dna.count("A")
T_count = my_dna.count("T")

#get the sum of those counts
AT_count = A_count + T_count

#find the length of the dna string
length = len(my_dna)

#calculate the percentage of AT
percent = (AT_count/length) * 100

#Print a cute output
print("The AT content of your DNA sequence is " + str(percent) + " percent")
