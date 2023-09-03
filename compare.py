# Compare Multimenu by Hansen 11 Nov 2022
import math

def menu(): # Main menu
    options = input("What do you want to do? Type help for options. ").lower()
    match options: # Compare the text in options for the options. Options also have the first letter as a shortcut
        case "weight" | "w":
            weight()
        case "height" | "h":
            height()
        case "calculator" | "c":
            calculator()
        case "exit" | "e":
            exit()
        case "help" | _:
            print("Pick a program: (W)eight, (H)eight, (C)alculator or type (E)xit to leave: ")
            menu()

def weight():
    print("How heavy are you in kilograms? ")
    userWeight = answerNum()
    pounds = round((float(userWeight)* 2.2),2)
    print("Your weight in pounds is", pounds)
    menu()

def height():
    userHeight = input("How tall are you in centimeters? ")
    feet = math.floor(int(userHeight) / 30)
    inch = (int(userHeight)-(feet*30)) % 12
    print(f"Your height in feet/inches is {feet}\"{inch}")
    menu()

def calculator():
    print("Input your first number.")
    x = answerNum()
    print("Input your second number.")
    y = answerNum()
    print("What do you want to do with these numbers? (+, -, *, ^, /)")
    mathOP = answerAllow("+-*^/")
    match str(mathOP):
        case "+":
            print("The answer is: ", x + y)
        case "-":
            print("The answer is: ", x - y)
        case "*":
            print("The answer is: ", x * y)
        case "^":
            print("The answer is: ", x ** y)
        case "/":
            if y == 0:
                print("Hey! That's illegal and may cause destruction of the universe you dummy!")
                calculator()
            else:
                print("The answer is: ", round(float(x/y),3))
        case "_"
            print("Please insert a valid operator.")
            
            
def answerStr(): # Lets user input anything.
    answer = input("Answer: ")
    return answer

def answerNum(): # Lets user input just numbers
    answerNum = input("Answer: ")
    if answerNum.isdigit():
        return int(answerNum)
    else:
        print("Please input numbers only.")
        answerNum()
        
def answerAllow(allowedStrings): # Checks if user is inputting the correct chars
    allowstr = allowedStrings
    userinput = input("Answer: ").strip()
    if userinput == "": # Apparently Py will also return blanks. This is to prevent that.
        print("Answer is blank, please insert an answer.")
        answerAllow(allowstr)
    if all(ch in allowstr for ch in userinput):
        return userinput
    else:
        print("Please only insert allowed characters, Allowed: ",allowstr)
        answerAllow(allowstr)
    
                
    menu()

def exit():
    print("Thank you!")

def main():
    name = input("Hi! What is your name? ").strip().title()
    print("Hello ", name, "!",sep="")
    menu()

main()