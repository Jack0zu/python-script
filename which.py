# Script Name	: which.py
# Author		:	Jack zu
# Created		:	24 June 2016
# Last Modified	:	24 June 2016
# Version		:	1.0
# Modifications	:
#
#
# Description	: which returns the pathname of the files wiich would be executed in the current enviroment.

import os	# Import the os module
import sys  # Import the sys module


def which(f):
	try:
		path =  os.getenv('PATH').split(";")
		for p in path:
			if os.path.isfile( os.path.join(p,f)):
				print os.path.join(p,f)
				return 0
	except Exceptions as e:
		print e
	
if __name__ == '__main__':
	if len(sys.argv) < 2:
		# print usage 
		print "[-]Usage: " + str(sys.argv[0]) +  ' <filename>' 
		exit(1)
	
	for f in sys.argv[1:]:
		which(f)