### This script renames all files in a directory.


import os

path = '/home/fox/'
dirs = os.listdir(path)

print("directory: ", dirs)


def rename_all():
    for item in dirs:
        if os.path.isfile(path + item):
            file_tuple = os.path.splitext(item)
            new_name = file_tuple[0] + " - 2018" + file_tuple[1]
            os.rename(path + item, path + new_name)
            print(new_name)
            	
            	
rename_all()
            	

                
