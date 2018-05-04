from math import sqrt as squareRoot
def specialInput(type,under,prompt):
    error = "Please enter a(n) " + type + " greater than 0, below " + str(under) + ".\n"
    while True:
        i = raw_input(prompt)
        try:
            if type == "integer":
                i = int(i)
            elif type == "decimal":
                i = float(i)
            if under == 0:
                return i
            elif i >= under:
                print error
            else:
                return i
        except Exception:
            print error
def solveForX(e,n,z):
    return [e + squareRoot((z*e)/n), e - squareRoot((z*e)/n)]
criticalValues = [3.84,5.99,7.81,9.49,11.07,12.59,14.07,15.51,16.92,18.31,19.68,21.03,22.36,23.68,25.00,26.30,27.59,28.87,30.14,31.41]
while True:
    degrees = specialInput("integer",21,"Please enter how many degrees of freedom you are working with, or a number less than zero to quit: ")
    if degrees <= 0:
        break
    if raw_input("(L)ooking for a limit? ").lower() in "limit":
        expectedPrompt = "\nPlease enter expected value: "
        e = specialInput("decimal",0,expectedPrompt)
        result = solveForX(e,degrees+1,criticalValues[degrees-1])
        print "Your limits are " + str(result[0]) + " and " + str(result[1]) + "."
    else:
        total = 0
        for n in range(degrees+1):
            expectedPrompt = "\nPlease enter expected value " + str(n+1) + ": "
            outcomePrompt = "Please enter outcome value " + str(n+1) + ": "
            e = specialInput("decimal",0,expectedPrompt)
            o = specialInput("decimal",0,outcomePrompt)
            total += ((o-e)**2)/e
        resultString = "\n\nThe result is " + str(total) + ", which is "
        if total <= criticalValues[degrees-1]:
            resultString += "less than or equal to " + str(criticalValues[degrees-1]) + ".\nTherefore, your data set can be considered 'random.'\n\n"
        else:
            resultString += "greater than " + str(criticalValues[degrees-1]) + ".\nTherefore, your data set cannot be considered 'random.'\n\n"
        print resultString
