import datetime
from csv import DictWriter
from os import write
def logger(func):
    def inner(a,b):
        currentime=datetime.datetime.now()
        print(currentime)
        print(f"({a},{b})")
        result=func(a,b)
        print(result)
        with open("sum.log","r+") as file:
            headers=("timestamp", "input_params", "result")
            csv_writer=DictWriter(file, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerow({"timestamp":currentime,"input_params":(a,b),"result":result})
        return 
    return inner
@logger
def sum(a,b):
    return a+b
sum(2,4)
