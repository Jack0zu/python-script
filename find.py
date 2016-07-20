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
import re

def find_by_name(dir,name):
	if(name.find(r"*") >=0  ):
		convert = name.replace(r"*",r".*")
		m = "^" + convert +"$"
		print m
		for r,d,f_list in os.walk(dir):
			for f in f_list:
				if(re.match(m,f)):
					print os.path.join(r,f)
		return
	
	for r,d,f in os.walk(dir):
		if name in f:
			print os.path.join(r,name)
def find_by_type(dir,isDir):
	for r,d,f in os.walk(dir):
		if isDir:
			print r
		else:
			for n in f:
				print os.path.join(r,n)
		
def usage():
	print "[-]Usage: " + str(sys.argv[0]) +  ' <dir> -name <file_name>' 
	print "        : " + str(sys.argv[0]) +  ' <dir> -type <f|d>' 
	exit(1)
if __name__ == '__main__':
	if len(sys.argv) < 4:
		# print usage 
		usage()

	if(sys.argv[2] == "-name"):
		find_by_name(sys.argv[1],sys.argv[3])
	elif (sys.argv[2] == "-type"):
		find_by_type(sys.argv[1],sys.argv[3]=="d")
	else:
		usage()