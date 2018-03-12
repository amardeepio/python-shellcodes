import tarfile
import os 
import subprocess


tar = tarfile.open("files_dir.tar","w")


for direct_path,directory,files in os.walk("/home/amardeep/process"):
	for file in files:
		path=os.path.join(direct_path,file)
		tar.add(path)





	tar.close()
