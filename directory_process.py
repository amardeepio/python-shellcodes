import os 

path ="/home/amardeep/process"

def path_rec(path=path):
	path_list=[]
	for dir_path,dir_name, filenames in os.walk(path):
		for file in filenames:
			fullpath = os.path.join(dir_path,file)
			path_list.append(fullpath)


	return path_list

if __name__ == "__main__":

	print ("\nRecursive listing of all paths in a dir:")
	for path in path_rec():
		print(path)
