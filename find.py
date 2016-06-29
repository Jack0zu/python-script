# Script Name	: which.py
# Author		:	Jack zu
# Created		:	29 June 2016
# Last Modified	:	29 June 2016
# Version		:	1.0
# Modifications	:
#
#
# Description	: find script to implement linux find.


import os
import sys

def find(dir,name):
	for r,d,f in os.walk(dir):
		if name in f:
			print os.path.join(r,name)

if __name__ == '__main__':
	if len(sys.argv) < 4:
		# print usage 
		print "[-]Usage: " + str(sys.argv[0]) +  ' <dir> -name <file_name>' 
		exit(1)
	
	find(sys.argv[1],sys.argv[3])
