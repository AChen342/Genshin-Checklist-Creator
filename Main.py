import ChecklistOptions
import colorama
from os import system, name
from colorama import Fore, Back, Style
colorama.init(autoreset=True) #Initializes colorama, which makes the color codes work

def clear():
    if name == 'nt':
        _ = system('cls')

if __name__=="__main__":
    askLoop = 0 #This var is used to continue or end the program

    while int(askLoop) == 0 or int(askLoop) == 1:
        askLoop = 0 #Resets the variable to default value
        answerOne = 0 #Resets the variable to default value

        #Title and main prompt
        print(Fore.BLUE + Style.BRIGHT + "Welcome to the Genshin Impact Checklist Creation Tool", end="\n\n")
        print("What would you like to do?")
        print(Fore. GREEN + "1. Create checklist(s)")
        print(Fore.YELLOW + "2. View checklist(s)")
        print(Fore.RED + "3. Delete checklist(s)")
        
        #Asks for user input
        while int(answerOne) == 0 or int(answerOne) > 3:
            try:
                answerOne = int(input("Type the number that matches your answer: "))
                clear()
            except:
                clear()
                print("Please enter a number. ")
            
        #Displays different prompts based on user input
        if int(answerOne) == 1: #User chooses to create checklists
            ChecklistOptions.userOptions.createChecklists()
            while int(askLoop) == 0 or int(askLoop) > 2:
                print("Would you like to go back to home screen?")
                print("[\t1. Yes\t|\t2. No\t]")
                askLoop = input("Type in number matching your answer: ")
                print("="*36)
        elif int(answerOne) == 2: #User chooses to view their checklists
            ChecklistOptions.userOptions.viewChecklist()
        else:
            ChecklistOptions.userOptions.removeChecklist()

        if int(askLoop) == 2:
            end = input("<Press enter to close>")
        