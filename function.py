def countwords():
    fileName=input("enter the filename:")
    numberofWords=0
    file=open(fileName,"r")
    for line in file:
        words=line.split()
        numberofWords=numberofWords+len(words)
    print("Numberofwords:")
    print(numberofWords)
countwords()