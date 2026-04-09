#Task: The Number Investigator

userInput = int(input("Please enter your round number here: "))

for i in range (userInput):
    if userInput == 0:
        kind = " is a-Zero number.\n"
        break
    elif userInput % 2 == 0:
        classification = "Even"
        if userInput > 0:
            total_positive = 0
            i = 1
            for i in range (userInput):  
                total_positive += (i+1)
                kind = "Positive"
        else: 
            kind = "Negative"
    elif userInput % 2 == 1:
        classification = "Odd"
        if userInput > 0:
            total_positive = 0
            i = 1
            for i in range (userInput):
                total_positive += (i+1)
                kind = "Positive"
        else: 
            kind = "Negative"

print(f"Result: {classification}, {kind}. Total 1-{userInput} adalah {total_positive}.")
        