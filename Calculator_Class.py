from ast import operator
from os import O_EXCL
import os.path


class Calculator:
    def __init__(self, numberOne, numberTwo, filename,operator):
        self.numberOne = numberOne
        self.numberTwo = numberTwo
        self.filename = filename
        self.answer = 0
        self.operator = operator
        
    def add(self):
       self.answer = self.numberOne + self.numberTwo
       return self.answer
   
    def subtract(self):
       self.answer = self.numberOne - self.numberTwo
       return self.answer

    def divide(self):
       self.answer = self.numberOne / self.numberTwo
       return self.answer

    def multiply(self):
       self.answer = self.numberOne * self.numberTwo
       return self.answer

   
    def saveToFile(self):        
        file = open(self.filename, 'a')
        if os.path.exists(self.filename):
            file.write('**********************************************\n')
            file.write("The answer to " + str(self.numberOne)+ " " + str(self.operator) + " " + str(self.numberTwo) + " = " + str(self.answer) +"\n")       
            file.write('**********************************************\n')
        else:
            file = open(self.filename, 'x')
            file.close()
        
        
    def printToConsole(self):
        print ("The answer is "  + str(self.answer))
        
