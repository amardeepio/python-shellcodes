import tarfile
import os 



tar = tarfile.open("files_dir.tar","r")


show_list =tar.list()

print(show_list)