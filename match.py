import fnmatch 

import os 

matches =['*deb']

list_of_match=[]


for dir_path,dir_name,fil_name in os.walk("/home/amardeep/Downloads"):
	for match in matches:
		for filename in fnmatch.filter(fil_name,match):
			list_of_match.append(os.path.join(dir_path,filename))




print(list_of_match)