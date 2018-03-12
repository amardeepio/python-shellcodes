import os 
import subprocess 


def commands(*args):

	for command in args :
		p= subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
		out=p.stdout.read()
		print (out)




commands("df -h","ls -l /home/amardeep/process", "ps")