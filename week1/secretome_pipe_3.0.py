#!/usr/bin/env python

import sys, getopt, subprocess, os, tempfile, shutil, time

#### This is a script designed to take a multiple protein fasta as input and provide the predicted secretome as
#### output. The program requires that signalp, tmhmm, targetp, chlorop, faSomeRecords, wolfpsort, and fasta_formatter
#### be on the users PATH. See those programs documentation for installation instructions.
#### Settings are for fungi change inputs for programs as necessary (targetp, and wolfpsort)

# Identify user input and provide help as necessary

if len(sys.argv) < 2:
	print """
	Usage: python Secretome_pipe.py [protein_file.fasta] [output_file_prefix]
	use -h or for help
	use "-check" to verify required programs.
	NOTE Fastas must have names of 20 char or less!!!!
		"""
	sys.exit(0)


if sys.argv[1] == "-check":
	def which(cmd):
		command = "which " + cmd	
		check = subprocess.call([command], stdout=subprocess.PIPE, stderr =subprocess.PIPE, shell=True)
		if check == 0:
			print cmd + " Present"
		else:
			print cmd + " Not in PATH or not installed."

	# this checks for the required executable
	which("signalp")
	which("tmhmm")
	which("targetp")
	which("chlorop")
	which("faSomeRecords")
	which("fasta_formatter")
	which("runWolfPsortSummary")
	
	sys.exit(0)
	
elif sys.argv[1] == "-h":
	print """
	Usage: python Secretome_pipe.py [protein_file.fasta] [output_file_prefix]

	**IMPORTANT Fasta names must be 20 char or less!!!**

	If you want to check for the necessary programs use 'python Secretome_pipe.py -check'
	This script takes a multi-fasta protein file as input and will generate the prediceted secretome
	as an output. All of the intermidiate files created by the various prediction programs are 
	stored in the directory created and have the output_file_prefix as a leader to the file name.
	
	##NOTE in the file tmhmmformat.pl set the follwoing lines as shown:
	
	$opt_html = 0;       # Make HTML output
	$opt_short = 1;      # Make short output format
	$opt_plot = 0;       # Make plots
	$opt_v1 = 0;         # Use old model (version 1)
	$opt_signal = 10;    # Cut-off used for producing a warning of possible
  		             # Signal sequence
	$opt_Nterm = 0;      # Number of bases to consider for signal peptides
    	                     # in the Nterm

	"""
	
	sys.exit(0)



########################################################## Main Code ###################################################################

#Global Variables
file_name = ''
if len(sys.argv) > 2:
	file_name = sys.argv[2]
pwd = os.getcwd() + "/"
dirname = pwd + file_name + "Secretome_files"
file_location = dirname + '/'
path = file_location + file_name

#Create Storage Folder for all files
try:
	os.makedirs(dirname)
except OSError:
	if os.path.exists(dirname):
		pass
	else:
		raise

# Removes carrige returns from fasta file
def singleline():		
	print "\nMaking fasta single line"
	file_in = sys.argv[1]	
	file_out = open(path + "singleline.fasta", "w")	
	command = ("fasta_formatter -i " + file_in + " -w 0")	
	p1 = subprocess.check_call([command], stdout=file_out, shell=True)
	print "Fasta now single line"
	file_out.close()

# use Signalp to idnetify sequences with signal peptides
def signalp():
	singleline()	
	command = ("signalp3.0 -t euk -short -m hmm " + path + "singleline.fasta | grep ' S ' > " + path + "signalpOUT.txt")	
	print "\nRunning SignalP"	
	signalpRUN = subprocess.check_call([command], shell=True)		
	print "SignalP Complete"
	
	# Generate the list of sequences with siganal peptides using the mature sequences
	
	print "\nCreating SignalP protein list"
	command_list = ("cut -d ' ' -f 1 " + path + "signalpOUT.txt") 	
	file_out4 = open(path + "goodlistSigP.txt", "w")
	tab = subprocess.check_call([command_list], stdout=file_out4, shell=True)
	file_out4.close()

# This function creates a fasta file containing the complete sequences with signal peptides
def sigpFasta():	
	command4 = ("faSomeRecords " + path + "singleline.fasta " + path + "goodlistSigP.txt " + path + "signalP_pass.fasta")
	print "\nRetreving SignalP fasta"	
	fastaRUN = subprocess.check_call([command4], shell=True)	

# This function runs tmhmm on the sequences with signal peptides inorder to check for transmembramne domains.
# NOTE this uses the mature sequences only so any TM regions in the signal peptide will be avoided/ignored	
def tmhmm(): 
	command = ("tmhmm -short " + path + "signalP_pass.fasta")
	file_out = open(path + "tmhmmOUT.txt", "w")
	print "\nRunning tmhmm on mature signalp sequences only"
	tmhmmRUN = subprocess.check_call([command], stdout=file_out, shell=True)
	file_out.close()	
	print "tmhmm complete"
	print "\nIdentifying sequences without tm regions."
	# This section of code parses the output from tmhmm and collects fastas with no TM regions	
	openfile = open(path + "tmhmmOUT.txt", "r")
	file_out2 = open(path + "tmhmmGoodlist.txt", "a")
	for line in openfile:
		if "\tPredHel=0\t" in line:					
			goodname = line.partition('\t')[0] + '\n'
			file_out2.write(goodname)
	openfile.close()
	file_out2.close()

#This function uses targetp to verify the destination of the signal peptide	
#NOTE for plant networks use -P over -N	
def targetp():
	ends = ("seqEnd.pl -l 70 " + path + "signalP_pass.fasta")
	file_out_end = open(path + "short.fasta", "w")
	endrun = subprocess.check_call([ends], stdout=file_out_end, shell=True)
	file_out_end.close()		

	command = ("targetp -N " + path + "short.fasta")
	file_out = open(path + "targetpOUT.txt", "w")
	print "\nRunning TargetP on SignalP pass seqeunces only"
	targetpRUN = subprocess.check_call([command], stdout=file_out, shell=True)
	print "TargetP complete"
	file_out.close()
	print "\nIdentifying sequences that are secreated."
	
	# Removes the leader info from the out file 
	lines = open(path + 'targetpOUT.txt').readlines()
	open(path + 'targetpOUT_parse.txt', 'w').writelines(lines[8:-2])	
	
	# Puts fastas identified as secreted "S" into goodlist
	openfile = open(path + "targetpOUT_parse.txt", "r")
	file_out2 = open(path + "targetpGoodlist.txt", "a")	
	for line in openfile:		
		if "S" in line:					
			goodname = line.partition(' ')[0] + '\n'
			file_out2.write(goodname)
	openfile.close()
	file_out2.close()

#runs wolfPsort with the fungi setting. change as necessary for you usage.
def wolfpsort():
	command = ("runWolfPsortSummary fungi < " + path + "singleline.fasta")
	file_out = open(path + "wolfPsortOUT.txt", "w")
	file_out2 = open(path + "wolfPsortErrorLog.txt", "w")	
	print "\nRunning WoLFPSORT"
	wolfRUN = subprocess.check_call([command], stdout = file_out, stderr=file_out2, shell=True)
	file_out.close()
	file_out2.close()	
	print "WoLFPSORT complete"
 	
	# Removes header from output file
	lines = open(path + 'wolfPsortOUT.txt').readlines()
	open(path + 'wolfPsortOUT_parse.txt', 'w').writelines(lines[1:])

	file_out2 = open(path + "wolfPsortGoodlist.txt", "a")
	# Places fastas with extracellualr location into good list
	searchValue = "extr"
	f = open(path + "wolfPsortOUT_parse.txt", "r+b")
	for line in f:
		if line.split()[1] == searchValue:				
			goodname = line.partition(' ')[0] + '\n'
			file_out2.write(goodname)
	f.close()

# this opens all the goodlist files and only collects fastas found in all four lists
#note jan 2013 this isnt working properly i will use individual sets until i get this going
# def set_from_file(path):
#     with open(path) as file:
#         return set(line.strip() for line in file)

# def secretome():
#     files = ["goodlistSigP.txt", "tmhmmGoodlist.txt", "targetpGoodlist.txt", "wolfPsortGoodlist.txt"]
#     data = [set_from_file(os.path.join(file_location, file_name + file)) for file in files]
#     with open(path + "secretome_pass.txt", "w") as newfile:
#        newfile.writelines(line + '\n' for line in set.union(*data) if line)



def secretome():
	file1 = set(line.strip() for line in open(path + "goodlistSigP.txt"))
	file2 = set(line.strip() for line in open(path + "tmhmmGoodlist.txt"))
	file3 = set(line.strip() for line in open(path + "targetpGoodlist.txt"))
	file4 = set(line.strip() for line in open(path + "wolfPsortGoodlist.txt"))
	newfile = open(path + "secretome_pass.txt", "w")
	for line in file1 & file2 & file3 & file4:
		if line:
			newfile.write(line + '\n')
#	file1.close()
#	file2.close()
#	file3.close()
#	file4.close()	
#	newfile.close()

# takes the collected fasta names and creates the file fasta file of the predicted secretome
def secFasta():
	command = ("faSomeRecords " + path + "singleline.fasta " + path + "secretome_pass.txt " + file_name + "secretome_pass.fasta")
	print "\nRetreving Secretome fasta"	
	fastaRUN = subprocess.check_call([command], shell=True)	
	print "\nSecretome identification Complete"

# main execution of the program in the proper order
def main():	
	signalp()
	sigpFasta()
	tmhmm()
	targetp()
	wolfpsort()
	secretome()
	secFasta()

main()

