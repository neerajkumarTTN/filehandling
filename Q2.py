import pickle
class Students:
    def __init__(self,name,roll_no,course):
        self.name=name
        self.roll_no=roll_no
        self.course=course
    def __repr__(self):
        return (f"{self.name} {self.roll_no} {self.course}")
std1=Students("neeraj",1,"b.tech")
std2=Students("ajay",2,"b.com")
std3=Students("sumit",3,"mba")
std4=Students("rajj",4,"bca")

def savestudents(*args):
    with open("student.txt","wb") as file:
        for i in args:
            pickle.dump(i,file)
savestudents(std1,std2,std3,std4)

def readstudents():
    with open("class.pickle","rb") as file:
        a=pickle.load(file)
        b=pickle.load(file)
        c=pickle.load(file)
        d=pickle.load(file)
        a.__repr__()
        b.__repr__()
        c.__repr__()
        d.__repr__()
        
readstudents()

def readGenerator():
    with open("student.txt","rb") as file:
        for i in range(4):
            i=pickle.load(file)
            yield i
reader=readGenerator()
for i in reader:
    print(i)