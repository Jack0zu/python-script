# Script Name	: sftp_put.py
# Author		:	Jack zu
# Created		:	18 July 2016
# Last Modified	:	18 July 2016
# Version		:	1.0
# Modifications	:
#
#
# Description	: Monitor a folder and call sftp_put script.


import os	# Import the os module
import sys  # Import the sys module
import time

sys.path.append("c:\shell")

import sftp_put

UPLOAD_FOLDER='./01_SW/Video/' #/opt/sftp/01_SW/Video/
if __name__ == '__main__':
	if len(sys.argv) < 6:
		# print usage 
		print "[-]Usage: " + str(sys.argv[0]) +  ' <monitor dir> <backup_folder> <ip> <sftp user> <sftp passwd>' 
		exit(1)
	(cmd,monitor_folder,backup_folder,ip,user,passwd) = sys.argv[0:6]
	
	index = 0
	sshd = None
	sftpd = None
	while True:
		
		if(sshd == None):
			print "Opening ssh"
			sshd = sftp_put.ssh_connect(ip, user, passwd)
		
		if(sshd == None):
			print "ssh connect fail,try again"
			continue
		
		if(sftpd == None):
			print "Opening sftpd"
			sftpd = sftp_put.sftp_open(sshd)
			
		if(sftpd == None):
			print "sftpd fail,try again"
			sftp_put.ssh_close( sshd )
			continue
		for r,d,f_list in os.walk(monitor_folder):
			for f in f_list:
				ret = sftp_put.sftp_put( sftpd, os.path.join(r,f), UPLOAD_FOLDER + os.path.basename(f))
				#cmd ="C:\Python27\python c:\shell\sftp_put.py " + ip + " " + user + " " + passwd +" \"" + os.path.join(r,f) + "\""
				#print "aa %s bb " % (cmd)
				#os.system(cmd)#upload file
				print ret
				if None == ret:
					print "sftp_put fail,close sftp and ssh"
					sftp_put.sftp_close(sftpd)
					sftp_put.ssh_close( sshd )
					sftpd = None
					sshd = None
					continue
				cmd = "move \"" + os.path.join(monitor_folder,f) + "\" " + os.path.join(backup_folder,str(index))
				print cmd
				os.system(cmd)
				index += 1
				if(index >10):
					index = 0
				
		time.sleep(3) # sleep 3s
		
		