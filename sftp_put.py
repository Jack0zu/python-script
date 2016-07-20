# Script Name	: sftp_put.py
# Author		:	Jack zu
# Created		:	18 July 2016
# Last Modified	:	18 July 2016
# Version		:	1.0
# Modifications	:
#
#
# Description	: upload via sftp
#				  first install paramiko module 
#				  Microsoft Visual C++ 9.0  Get it from http://aka.ms/vcpython27

import os	# Import the os module
import sys  # Import the sys module
import paramiko # import the paramiko module


def ssh_connect( _host, _username, _password ):
    try:
        _ssh_fd = paramiko.SSHClient()
        _ssh_fd.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
        _ssh_fd.connect( _host, username = _username, password = _password )
    except Exception, e:
        print( 'ssh %s@%s: %s' % (_username, _host, e) )
        return None
    return _ssh_fd

def sftp_open( _ssh_fd ):
    return _ssh_fd.open_sftp()

def sftp_put( _sftp_fd, _put_from_path, _put_to_path ):
	print "put ",_put_from_path," to ",_put_to_path
	ret = None
	try:
		ret = _sftp_fd.put( _put_from_path, _put_to_path )
	except Exception,e:
		print 'ERROR: sftp_put - %s' % e
	return ret
	
def sftp_get( _sftp_fd, _get_from_path, _get_to_path ):
	print "get ",_get_from_path," to ",_get_to_path
	return _sftp_fd.get( _get_from_path, _get_to_path )
def sftp_listdir( _sftp_fd,dir):
	
	return _sftp_fd.listdir( dir )
	
def sftp_close( _sftp_fd ):
    _sftp_fd.close()

def ssh_close( _ssh_fd ):
	_ssh_fd.close()


UPLOAD_FOLDER='./01_SW/Video/' #/opt/sftp/01_SW/Video/

def send(ip,user,passwd,file):
	sshd = None
	sftpd = None
	
	sshd = ssh_connect(ip, user, passwd)
	if(sshd == None):
		return None
	try:
		sftpd = sftp_open(sshd)
	except Exception,e:
		print 'ERROR: sftp_put  sftp_open - %s' % e
		ssh_close( sshd )
		return None	
	ret = None
	try:
			 ret = sftp_put( sftpd, file, UPLOAD_FOLDER + os.path.basename(file)  )
	except Exception, e:
			print 'ERROR: sftp_put - %s' % e
			
	sftp_close(sftpd)
	ssh_close( sshd )
	return ret
if __name__ == '__main__':
	if len(sys.argv) < 5:
		# print usage 
		print "[-]Usage: " + str(sys.argv[0]) +  ' <ip> <sftp user> <sftp passwd> files' 
		exit(1)
	(cmd,ip,user,passwd) = sys.argv[0:4]
	files = sys.argv[4:]
	print files
	sshd = ssh_connect(ip, user, passwd)
	sftpd = sftp_open(sshd)
	
	for file in files:
		try:
			sftp_put( sftpd, file, UPLOAD_FOLDER + os.path.basename(file)  )
		except Exception, e:
			print 'ERROR: sftp_put - %s' % e
	print sftp_listdir(sftpd,UPLOAD_FOLDER)
	sftp_close(sftpd)
	ssh_close( sshd )
	