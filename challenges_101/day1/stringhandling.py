#String Manipulation Techniques...

def left(string, numberOfCharacters):
    return string[:numberOfCharacters]

def right(string, numberOfCharacters):
    return string[-numberOfCharacters:]

def substr(string, start, numberOfCharacters):
    return string[start:start+numberOfCharacters]

def length(string):
    return len(string)
    
def locate(stringToFind, string):
    return string.find(stringToFind)
