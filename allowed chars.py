# string
def charcheck(allowedStr):
    userinput = input("What is your operator? ")
    allowstr = allowedStr
    
    #Iterate all allowed characters in userinput, return if true, reject with current allowStr when false.
    if all(ch in allowstr for ch in userinput):
        return userinput
    else:
        print("Char is not allowed, Allowed: ",allowstr)
        charcheck(allowstr)
    
charcheck("+-:/^")

