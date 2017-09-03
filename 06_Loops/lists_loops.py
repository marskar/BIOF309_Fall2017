#lecture notes and examples from BIOF309 on list and loop methods

#to make a list
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
conserved_sites = [24, 56, 132]
print (apes[0])
first_site = conserved_sites[2]
print (first_site) #should get 132
print (apes) #should print as a list
print (apes.index("Pan troglodytes"))
print ("There are", len(apes), "apes")
apes.append("Pan paniscus")
print ("Now there are", str(len(apes)) + " apes")
#more list methods
ranks = ["kingdom","phylum","class","order","family","genus","species"]
print ("at the start:",'\n', ranks)
ranks.reverse()
print("after reversing:",'\n', ranks)
ranks.sort()
print ("after sorting:",'\n', ranks)
print (apes[-1]) #last ape

names = "melanogaster,simulans,yakuba,ananassae"
species = names.split(",") #this will split on the comma and make a list

#repetitive task can be automated with looping
for species in apes: #for looping
    print(species + " is an ape")

things = ["this thing","that thing","anything and everthing"]
apes.extend(things)

for species in apes:
    print(species + " is an ape")

#can use with lines in a file
seq = open("sequences1.txt","r")
for line in file:
    print (line[:9])
#use list[0] position to find first item
