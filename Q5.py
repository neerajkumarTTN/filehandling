from os import replace

def replace_txt(filepath,search_term,new_term,replace_all=True):
    with open(filepath,"r") as file:
        reader=file.read()
    counter=0
    with open(filepath,"w") as file:
        print(reader)
        if replace_all==True:
            new_data=reader.replace(search_term,new_term)
            file.write(new_data)
            counter+=1
            return f"{search_term} replaced  {counter} times"
        else:
            new_data=reader.replace(search_term,new_term,1)
            file.write(new_data)
            counter+=1
            return f"{search_term} replaced {counter} times"
print(replace_txt("test.txt","Kumar","Maurya",replace_all=True))