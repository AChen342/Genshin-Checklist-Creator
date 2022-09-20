import numpy as np
import os
import colorama
from os import system, name
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def clear():
    if name == 'nt':
        _ = system('cls')

class character:
    def __init__(self, charName, charLevel):
        self.charName = charName
        self.charLevel = charLevel

    def calcAscendTimes(self):  #Finds out how many times the character will ascend and returns a variable integer called 'ascendTimes'

        levelCap = [20, 40, 50, 60, 70, 80, 90]
        counter = 0
        ascendTimes = 0

        while int(counter) < len(levelCap):
            if int(self.charLevel) > levelCap[counter]:
                ascendTimes = ascendTimes + 1
            counter = counter + 1
    
        return ascendTimes

    def totalExp(self): #
        expList = []
        totalExp = 0
        expFile = open("LevelStat.txt", "r")
        readExpFile = expFile.read()

        for line in readExpFile.split("\n"):
            expList.append(line)
        
        totalExp = expList[int(self.charLevel)-1]
        expFile.close()

        return totalExp

    def materialsNeed(self):
        separateHash = []
        separateComma = []
        storeMatName = []
        matsListed = []
        charMatsNeeded = []
        listCount = 1

        charMatFile = open("CharMat.txt", "r")
        readMatFile = charMatFile.read()

        for hashChar in readMatFile.split("#"):
            separateHash.append(hashChar)
        
        counter = 0
        while int(counter) < len(separateHash):
            for commaChar in separateHash[counter].split(","):
                separateComma.append(commaChar)
            counter = counter + 1
        charMatFile.close()

        matsListed = separateComma

        finder = matsListed.index(self.charName)
        while listCount <= 10:
            charMatsNeeded.append(matsListed[finder + listCount])
            listCount = listCount + 1

        return charMatsNeeded

    def numOfMatsNeeded(self):
        np.matAmounts = [[1, 0, 0, 0, 0, 3, 3, 0, 0, 20000], [0, 2, 6, 0, 2, 10, 15, 0, 0, 40000], [0, 3, 0, 0, 4, 20, 0, 12, 0, 60000], [0, 0, 3, 0, 8, 30, 0, 18, 0, 80000], [0, 0, 6, 0, 12, 45, 0, 0, 12, 100000], [0, 0, 0, 6, 20, 60, 0, 0, 24, 120000]]
        np.matTotal = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        counter = 0
        while counter < int(self.calcAscendTimes()):
            np.matTotal = np.add(np.matAmounts[counter], np.matTotal)
            counter = counter + 1
        
        return np.matTotal

class characterFile:
    def __init__(self, charName, charLevel, ascendTimes):
        self.charName = charName
        self.charLevel = charLevel
        self.ascendTimes = ascendTimes

    def checklistFile(self):
        if not(os.path.exists(str(self.charName) + "-" + str(self.charLevel) + "-" + str(self.ascendTimes) + ".txt")):
            charFile = open(str(self.charName) + "-" + str(self.charLevel) + "-" + str(self.ascendTimes) + ".txt", "x")
            charFile.write(str(self.charName) + "-" + str(self.charLevel) + "-" + str(self.ascendTimes) + "\n")
            charFile.close()

            if not(os.path.exists("CharFileList.txt")):
                charFile = open("CharFileList.txt", "x")
                charFile.close()

            charFile = open("CharFileList.txt", "a")
            charFile.write(str(self.charName) + "-" + str(self.charLevel) + "-" + str(self.ascendTimes) + ".txt\n")
            charFile.close()
            
            edit = checklist(self.charName, self.charLevel)
            edit.writeToChecklist()

            print("\nChecklist has been created.")
            next = input("<Press Enter to Return Home>")
            clear()
        
        else:
            print("\nChecklist has been created.")
            next = input("<Press Enter to Return Home>")
            clear()
class checklist:
    def __init__(self, charName, charLevel):
        self.charName = charName
        self.charLevel = charLevel
    
    def writeToChecklist(self):
        counter = 0
        materials = character(self.charName, self.charLevel)
        materialsList = materials.materialsNeed()
        materialsAmount = materials.numOfMatsNeeded()
        ascendTimes = materials.calcAscendTimes()

        openCharFile = open(str(self.charName) + "-" + str(self.charLevel) + "-" + str(ascendTimes) + ".txt", "a")
    
        while counter < len(materialsList):
            openCharFile.write("\n" + str(materialsList[counter]) + ": " + str(materialsAmount[counter]))
            counter = counter + 1
        
        levelExp = materials.totalExp()
        openCharFile.write("\n\nTo reach level " + str(self.charLevel) + ", you need " + str(levelExp) + " EXP.")
        openCharFile.write("\nThis is equivalent to: ")

        convertHeroWit = float(int(levelExp)/20000)
        convertAdvenExp = float(int(levelExp)/5000)
        convertWandAdvice = float(int(levelExp)/1000) 

        openCharFile.write("\n\n" + str(convertHeroWit) + " Hero's wit")
        openCharFile.write("\n" + str(convertAdvenExp) + " Adventurer's Experience")
        openCharFile.write("\n" + str(convertWandAdvice) + " Wanderer's Advice")

class userOptions:
    def createChecklists():
        setList = ["Beidou", "Ganyu", "Fischl"]
        userAnswer = 0
        userAnswerTwo = 0
        howMany = 0
        counter = 0
        charName = ""
        charLevel = 0

        print("Start making checklists?")
        while int(userAnswer) == 0 or int(userAnswer) > 2:
            print("[  1. Yes  |  2. No  ]")
            userAnswer = input("Type in number matching your answer: ")
        
        if int(userAnswer) == 1:        
            while (howMany == 0) or (howMany > 10):
                howMany = int(input("How many checklists would you like to make? (1-10): "))
                if howMany > 10:
                    print("Sorry, you can only make 10 checklists at a time.")
            clear()
            
            for i in range(howMany):
                userAnswerTwo = 0
                charLevel = 0
                print("Checklist #" + str(i+1))
                print("\nWhich character would you like to add to your list?")

                for j in range(len(setList)):
                    print(str(j + 1) + ". " + str(setList[j]))
                
                while int(userAnswerTwo) == 0 or int(userAnswerTwo) > 3:
                    userAnswerTwo = input("Type the number matching your choice: ")
                    if int(userAnswerTwo) > 3:
                        print("Sorry, there are only 3 characters available right now.")
            
                charName = setList[int(userAnswerTwo)-1]

                while int(charLevel) == 0 or int(charLevel) > 90:
                    charLevel = input("What level would you like " + str(charName) + " to be? (Lvl 1-90): ")
                    if int(charLevel) > 90:
                        print("The maximum possible level is 90.")
                
                calcAscend = character(charName, charLevel)
                ascendTimes = calcAscend.calcAscendTimes()

                create = characterFile(charName, charLevel, ascendTimes)
                create.checklistFile()

                counter = counter + 1

    def removeChecklist():
        Checklists = []
        answerFour = 0 
        removePos = 0
        a = 0
        i = 0

        if os.path.exists("CharFileList.txt"):
            charFile = open("CharFileList.txt", "r")
            for line in charFile:
                x = line.rsplit("\n")
                Checklists.append(x[0])
            charFile.close()

            print("="*36)
            print("Which checklist would you like to remove?\n")
            while i < len(Checklists):
                print(str(i+1) + ". " + str(Checklists[i]))
                i = i + 1
            i = 0

            while int(removePos) == 0 or int(removePos) > len(Checklists):
                print("\nType the number that matches the checklist you want to remove.")
                removePos = input("For example, if you want to remove the second checklist, type in '2'.    Answer: ")
                if int(removePos) > len(Checklists):
                    print("Checklist at this position does not exist.")
            while int(answerFour) == 0 or int(answerFour) > 2:
                print("Are you sure you want to remove '" + Checklists[int(removePos)-1] + "'?")
                answerFour = input("[\t1. Yes\t|\t2. No\t]\t\tAnswer: ")
            
            if int(answerFour) == 1:
                os.remove(Checklists[int(removePos)-1])
                Checklists.remove(Checklists[int(removePos)-1])
                    
                if len(Checklists) == 0:
                    os.remove("CharFileList.txt")
                
                    print("Successfully removed.")
                    next = input("<Press Enter to Return Home>")
                    clear()

                else:
                    os.remove("CharFileList.txt")
                    charFile = open("CharFileList.txt", "x")
                    while a < len(Checklists):
                        charFile.write(str(Checklists[a]) + "\n")
                        a = a + 1
                    charFile.close()
                    a = 0
                    charFile = open("CharFileList.txt", "r")
                    while i < len(Checklists):
                        print(str(i+1) + ". " + str(Checklists[i]))
                        i = i + 1
                    i = 0
                    print("\n")
                    print("*"*36)
                    print("Successfully removed.")
                    next = input("<Press Enter to return home>")
                    charFile.close()
            else:
                print("\n")
                print("*"*36)
                print("Action canceled.")
                print("Returned to home screen.")
                print("*"*36, end="\n")
                print("="*36)
        else:
            print("| Selected |>\t[" + Fore.RED + " 3. Delete Checklist " + Fore.RESET + "]")
            print("You have not created any checklists yet.\n")
            next = input("<Press Enter to Return Home>")
            clear()

    def viewChecklist():
        answerSix = 0
        while int(answerSix) == 0 or int(answerSix) == 1:
            answerSix = 0
            answerFive = 0
            i = 0
            storeFile = []
            if os.path.exists("CharFileList.txt"):
                charFile = open("CharFileList.txt", "r")
                for line in charFile:
                    x = line.rsplit("\n")
                    storeFile.append(x[0])
                charFile.close()

                print("\n====================================================")
                print("Which checklist would you like to view?\n")
                print("Checklists are named in this format:")
                print("[Character Name]-[Level]-[Ascension Level].txt")
                print("Example: Beidou-90-6.txt\n")
            
                while i < len(storeFile):
                    print(str(i+1) + ". " + str(storeFile[i]))
                    i = i + 1
                
                while int(answerFive) == 0 or int(answerFive) > len(storeFile):
                    answerFive = input("\nType the number corresponding to which checklist you would like to view.    ")
                    if int(answerFive) > len(storeFile):
                        print("The checklist you have selected does not exist.")

                print("-----------------------------------------")
                charFile = open(storeFile[int(answerFive)-1])
                print(charFile.read())
                print("-----------------------------------------")
                print("\nWhat would you like to do next?")

                while int(answerSix) == 0 or int(answerSix) > 2:
                    answerSix = input("[1. View another checklist   |   2. Back to homescreen]   :   ")
                print("\n")
                if int(answerSix) == 2:
                    break
            else:
                print("\nYou don't have any checklists created.")
                print("Returning back to homescreen.\n")
                break
