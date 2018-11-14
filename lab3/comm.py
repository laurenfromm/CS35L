#!/usr/bin/python
"""
Implementation of comm command.
Lauren Fromm
404751250
"""

import sys
from optparse import OptionParser  

class comm: 
    def __init__(self,filename1, filename2):
	if filename1 == '-':
		 file1 = sys.stdin
		 file2 = open(filename2, 'r')
	elif filename2 == '-':
		 file2 = sys.stdin
		 file1 = open(filename1, 'r')
	elif filename1 != '-' and filename2 != '-':
		 file1 = open(filename1, 'r')
		 file2 = open(filename2, 'r')
	else:
		 print("Error reading files")
		 exit() 
	self.lines1 = file1.readlines()
	self.lines2 = file2.readlines()	
	self.col1 = []
	self.col2 = []
	self.col3 = []
	file1.close()
	file2.close()

    def output(self, hideCol1, hideCol2, hideCol3, isUnsorted):
 	 if isUnsorted:
		self.compU()
	 else:
		self.comp()
	 if hideCol1 == True:
		self.col1 = [''] * len(self.col1)
	 if hideCol2 ==True:
		self.col2 = [''] * len(self.col2)
	 if hideCol3 ==True:
		self.col3 = [''] * len(self.col3)
	 finalOutput = []
	 if (len(self.col1) != 0):
	 	for i in range(len(self.col1)):
			finalOutput.append(self.col1[i] 
			+ self.col2[i] + self.col3[i])
	 elif (len(self.col2) != 0):
		for j in range(len(self.col2)):
                        finalOutput.append(self.col1[j] 
			+ self.col2[j] + self.col3[j])
	 else:
		for l in range(len(self.col3)):
                        finalOutput.append(self.col1[l] 
			+ self.col2[l] + self.col3[l])
	 for k in range(len(finalOutput)):
	 	print(finalOutput[k]) 
	 return

    def comp(self):
	i=0
	j=0
	while(i < len(self.lines1) and j < len(self.lines2)):
			if (self.lines1[i] == self.lines2[j] 
			or (self.lines1[i] + '\n' == self.lines2[j]) 
			or (self.lines1[i] == self.lines2[j] + '\n')):
				self.col3.append(self.lines1[i])
                                self.col1.append('      ')
                                self.col2.append('      ')
				i=i+1
				j=j+1
			elif self.lines1[i] > self.lines2[j]:
				self.col2.append(self.lines2[j])
				self.col1.append('	')
				self.col3.append('')
				j=j+1
			else:
				self.col1.append(self.lines1[i])
				self.col2.append('')
				self.col3.append('')
				i=i+1
	if (i < j):
		while (i < len(self.lines1)):
			self.col1.append(self.lines1[i])
			self.col2.append('')
			self.col3.append('')
			i=i+1
	elif( j < i):
		while(j < len(self.lines2)):
			self.col2.append(self.lines2[j])
			self.col1.append('	')
			self.col3.append('')
			j=j+1
		
    def compU(self):
	for i in range(len(self.lines1)):
		for j in range(len(self.lines2)):
			if self.lines1[i] == self.lines2[j]:
				self.col3.append(self.lines1[i])
				self.col1.append('	')
				self.col2.append('	')
				del self.lines2[j]
				shared = True
				break
			else:
				shared = False
		if shared != True:
			self.col1.append(self.lines1[i])
			self.col2.append('')
			self.col3.append('')

	for k in range(len(self.lines2)):
		self.col1.append('	')
		self.col3.append('')
		self.col2.append(self.lines2[k])
	return
		
def main(): 
	version_msg = "%prog 2.0" 
	usage_msg = """%prog [OPTION]...FILE1 FILE2
Compare FILE1 and FIlE2 line by line.""" 
	parser = OptionParser(version=version_msg,
                          usage=usage_msg)
	parser.add_option("-1", action="store_true", dest="col1", 
		default=False, 
		help="Do not show column 1 (lines unique to FILE1)")
	parser.add_option("-2", action="store_true", dest="col2", 
		default=False, 
		help="Do not show column 2 (lines unique to FILE2)")
	parser.add_option("-3", action="store_true", dest="col3",
		default=False, 
		help="Do not show column 3 (lines shared by FILE1 and FILE2)")
	parser.add_option("-u", action="store_true", dest="unsorted",
		default=False, help="Files are unsorted.")
	options, args = parser.parse_args(sys.argv[1:]) 
	try:
		col1=bool(options.col1)
		col2=bool(options.col2)
		col3=bool(options.col3)
		unsorted=bool(options.unsorted)
	except: 
	    parser.error("invalid option: {0}". 	
			format(options.col1))
	if len(args) != 2:
		perser.error("Not enough arguments")
	file1 = args[0]
	file2 = args[1] 
	try:
		comparator = comm(file1, file2)
		comparator.output(col1,col2,col3,unsorted)
	except IOError as (errno, strerror): 
	    	parser.error("I/O error({0}): {1}". format(errno, strerror)) 

if __name__ == "__main__":
	main()
