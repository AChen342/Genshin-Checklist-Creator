import ChecklistOptions
from os import system, name

def clear():
    if name == 'nt':
        _ = system('cls')

if __name__=="__main__":
    quit = False; #This var is used to continue or end the program

    while quit == False:
        askLoop = 0 #Resets the variable to default value
        answerOne = 0 #Resets the variable to default value

        #Title and main prompt
        print("Welcome to the Genshin Impact Checklist Creation Tool", end="\n\n")
        print("What would you like to do?")
        print("1. Create checklist(s)")
        print("2. View checklist(s)")
        print("3. Delete checklist(s)")
        print("4. Quit")
        
        #Asks for user input
        while int(answerOne) == 0 or int(answerOne) > 4:
            try:
                answerOne = int(input("Type the number that matches your answer: "))
                clear()
            except:
                clear()
                print("Please enter a number. ")
            
        #Displays different prompts based on user input
        if int(answerOne) == 1: #User chooses to create checklists
            ChecklistOptions.userOptions.createChecklists()

        elif int(answerOne) == 2: #User chooses to view their checklists
            ChecklistOptions.userOptions.viewChecklist()

        elif int(answerOne) == 3:
            ChecklistOptions.userOptions.removeChecklist()
        
        else:
            quit = True; 
        