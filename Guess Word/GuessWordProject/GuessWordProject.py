import random

def loadWordList(path):
    lines=[]
    try:
        fileObj = open (path,"r")
        for line in fileObj:
            lines.append(line.rstrip())
    except:
        print(f"Error with file: {path}")
        return None
    return lines

def guessWord(mWord):
    asteriskWord = "*" * (len(mWord))

    # convert each character in asteriskWord to a list
    asteriskList = list(asteriskWord)  
    
    # repeat until all * have been converted to their matching letter
    while("*" in asteriskWord):       
        letterFound = False
        print("\n\n")
        print (asteriskWord)
        letter = input("Enter a letter to guess --> ")
        letter = letter[0]
        for i in range (len(asteriskList)):
            if letter == mWord[i]:
                asteriskList[i] = letter
                letterFound = True
        if  letterFound==False:
              print(f"{letter} is not in the mystery word")

        # convert list back to a string
        asteriskWord = "".join(asteriskList)
    print(f"\n\nCongradulations: you guessed the word {mWord}")


def main():
    wordList = loadWordList("D:\wordlist-1.txt")
    mysteryWord = wordList[random.randrange(0,len(wordList))]
    guessWord(mysteryWord)

main()
