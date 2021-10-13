import datetime
from csv import DictWriter
from os import write
def logger(func):
    def inner(*args):
        currentime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(currentime)
        #print(f"({*args},{b})")
        result=func(*args)
        #print(result)
        with open("sum.log","r+") as file:
            headers=("timestamp", "input_params", "result")
            csv_writer=DictWriter(file, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerow({"timestamp":currentime,"input_params":(*args,),"result":result})
        return 
    return inner
@logger
def sum(a,b):
    return a+b
sum(2,4)
