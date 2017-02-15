my_dna = "ATCGGGGGATG"

A_count = my_dna.count("A")
T_count = my_dna.count("T")
Start_codons = my_dna.count("ATG")

my_change = my_dna.replace("GGGG", "cc")
print(my_change)


print("There are " + str(A_count) + " A's in my DNA sequence.")
print("There are " + str(T_count) + " T's in my DNA sequence.")

print("There are " + str(Start_codons) + " start codons in my DNA sequence." \
+ "and it starts at" + str(my_dna.find("ATG")))
