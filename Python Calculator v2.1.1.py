myStr = "{} + {} = {}!"

def makeEquation(a, b, operation):
    if operation == "Addition":
        print(myStr.format(a, b, (int(a + b))))
    elif operation == "Subtraction":
        print(myStr.format(a, b, (int(a - b))))
    elif operation == "Multiplication":
        print(myStr.format(a, b, (int(a * b))))
    elif operation == "Division":
        print(myStr.format(a, b, (int(a / b))))
       


myStr = str(input("How would you like your equation message to look like? (must be formatted like {} + {} = {})"))
operation = str(input("What is the math operation?"))
a = float(input("What is the first number of the operation?"))
b = float(input("What is the second number of the operation?"))
if myStr == "" and operation == "Addition":
    myStr = "{} + {} = {}"
if myStr == "" and operation == "Subtraction":
    myStr = "{} - {} = {}"
if myStr == "" and operation == "Multiplication":
    myStr = "{} x {} = {}"
if myStr == "" and operation == "Division":
    myStr = "{} / {} = {}"    
    
makeEquation(a, b, operation)

confirmation = str(input("Is an extra step nesseccary? [Y/N]"))

if confirmation == "Y":
    myStr = str(input("How would you like your equation message to look like? (must be formatted like {} + {} = {})"))
    operation = str(input("What is the math operation?"))
    print("Your first number is " + str(a) + ", this is due to you choosing multistep.")
    b = float(input("What is the second number of the operation?"))
    if myStr == "" and operation == "Addition":
        myStr = "{} + {} = {}!"
    if myStr == "" and operation == "Subtraction":
        myStr = "{} - {} = {}!"
    if myStr == "" and operation == "Multiplication":
        myStr = "{} x {} = {}!"
    if myStr == "" and operation == "Division":
        myStr = "{} / {} = {}!"    
        
    makeEquation(a, b, operation)

elif confirmation == "N":
        print("Hope I helped!")
    
