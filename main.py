import Calculator_Class
import os.path


counter = 0

while True:
    numberOne = int(input("please enter a number: "))
    numberTwo = int(input("please enter a number: "))
    operator = input("please enter an operator: ")
    filename = input("please enter a filename: ")
    answer = 0

    
    Calculator = Calculator_Class.Calculator(numberOne, numberTwo, filename, operator)

    if operator == '+':
        Calculator.add()
    elif operator == '-':
        Calculator.subtract()
    elif operator == '/':
        Calculator.divide()
    elif operator == '*':
        Calculator.multiply()
    else:
        print("please enter a valid operator")
        operator = input("please enter an operator: ")

    Calculator.printToConsole()
    Calculator.saveToFile()
    user_continue = input("would you like to do another sum? (yes/no: ")

    if user_continue == 'yes' or user_continue == 'Yes':
        continue
    else:
        break
    
    