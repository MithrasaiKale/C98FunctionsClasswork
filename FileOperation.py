def CountWords():
    fileName=input("Input A File Please I need a file to work - ")
    numberOfWords=0
    file=open(fileName , "r")
    for y in file:
        words=y.split(" ")
        numberOfWords=numberOfWords +len(words)
    print("Number Of Words in this file is : " + str(numberOfWords))    

CountWords()