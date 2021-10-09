import os
import os.path
from posix import listdir
def list_file(dir_path,nested=True):
    path='/home/neeraj/Bootcamp_training/file_csv/'+f'{dir_path}'
    if nested==True:
        for root,dir,file in os.walk(path):
            for f in file:
                if f.endswith(".txt"):
                    print(f)
    else:
        for i,file in enumerate(os.listdir(path)):
            if file.endswith(".txt"):
                print(file)

#list_file("Folder1",False)
list_file("Folder1")