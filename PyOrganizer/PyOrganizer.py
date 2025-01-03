
import os, re, argparse

#Parses parameters
parser = argparse.ArgumentParser()

parser.add_argument('-l', required=False, type=int, help="Specifie how long password/word needs to be")
parser.add_argument('-o', required=False, type=str, help="Specifie name of output .TXT file which will be created")
parser.add_argument('-w', required=True, type=str, help="Path to wordlist which contains words/passwords")
parser.add_argument('-a', required=False, type=str, help="Passwords with included letters, remember that only words with THIS letters will be chosen")

#Parses saved in variables
args = parser.parse_args()
wordlist = args.w
lenght = args.l
alphabet = args.a
outputPath = args.o

outputFile = "outputWrodlist.txt"

#Wordlist variables (input/output)
if outputPath != None:
    outputFile = outputPath
    print("output provided...")

else:   
    os.system(f"touch {outputFile}")
    print("creating wordlist...")

outputList = open(f"{outputFile}", "w+")
r = re.findall('\w+', open(wordlist, encoding='latin-1').read())

def CopyFile(wordlist):
    #Loop to output wordlist in lines
    for word in wordlist:
        outputList.write(word + "\n")

def specificLettersAndLenght(wordlist):
    for word in wordlist:
        wordLen = len(word)

        for letter in [*alphabet]:

            #NEEDS POLISH, IT'S NOT WORKING PROPERLY
            if wordLen == lenght and letter in word:
                outputList.write(word + "\n")

def specificLetters(wordlist):
    for word in wordlist:        

        for letter in [*alphabet]:

            if letter in word:
                outputList.write(word + "\n")

def specificLenght(wordlist):
    for word in wordlist:
        wordLen = len(word)

        if wordLen == lenght:
            outputList.write(word + "\n")

if alphabet != None and lenght != None:
    specificLettersAndLenght(r)
    print("Letters and length...")

elif alphabet != None:
    specificLetters(r)
    print("Only letters...")

elif lenght != None:
    specificLenght(r)
    print("Only lenght...")

else:
    CopyFile(r)
    print("Coping file...")
