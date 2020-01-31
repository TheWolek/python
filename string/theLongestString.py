# Napisz funkcje przyjmującą liste łańcuchów
# i zwracającą najdłuższy z nich
def theLongest(wordList):
    listOfLengths = []
    for word in wordList:
        listOfLengths.append((len(word),word))
    
    listOfLengths.sort()
    return listOfLengths[-1][1]

print(theLongest(['book','shop','pl']))