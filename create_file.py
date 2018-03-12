import os 

import subprocess

file = open("myfile.txt","w")

word = "linux is awesome"


x =0


for x in range(2000):

	x=x+1
	file.write("%s\n" % word)


subprocess.call(["ls", "-l", "/home/amardeep/process/myfile.txt"])
subprocess.call(["stat","-f","/home/amardeep/process/myfile.txt"])