import os,os.path
def rename_all(dir_path, pattern, suffix):
    path='/home/neeraj/Bootcamp_training/file_csv/'+f'{dir_path}'
    print(os.listdir(path))
    for i,file in enumerate(os.listdir(path)):
        extention=os.path.splitext(file)[1]
        dst=path+pattern+ str(i) + suffix + str(extention)
        source=path+str(file)
        print(source,dst)
        os.rename(source,dst)
        print(file)


rename_all("Folder1/Folder2/","Test_file_","_renamed")