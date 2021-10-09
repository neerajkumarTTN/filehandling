# reading file

#file=open("Q1.txt")
#print(file.read())
with open ("Q1.txt") as file:
    print(file.read())
#writing file with w flag
with open("Q1.txt","w") as f:
    print(f.write("I am Neeraj Kumar\n"))
 #appending file 
with open("Q1.txt","a") as f:
    print(f.write("I am from deoria"))


