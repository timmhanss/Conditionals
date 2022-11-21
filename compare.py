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
    userWeight = input("How heavy are you in kilograms? ")
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
    x = int(input("Input your first number: "))
    y = int(input("Input your second number: "))
    mathOP = input("What do you want to do with these numbers? (+, -, *, ^, /)")
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
    menu()

def exit():
    print("Thank you!")

def main():
    name = input("Hi! What is your name? ").strip().title()
    print("Hello ", name, "!",sep="")
    menu()

main()