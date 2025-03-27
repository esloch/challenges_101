#Python Slicing in Python - www.101computing.net/python-slicing-in-python/

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

firstCharacter = alphabet [0]
lastCharacter = alphabet [25]
print(alphabet)
print("First character:" + firstCharacter)
print("Last character:" + lastCharacter)

posA = alphabet.find("A")
posC = alphabet.find("C")
print("Letter A is at position: " + str(posA))
print("Letter C is at position: " + str(posC))

if "@" in alphabet:
  print("Letter @ is in the alphabet!!!")
else:
  print("Letter @ is not in the alphabet!!!")

posAt = alphabet.find("@")  
print("The position of @ in the alphabet is: " + str(posAt))

#String Slicing:
print("The first 5 letters of the alphabet are: " + alphabet[:5])
print("The last 5 letters of the alphabet are: " + alphabet[-5:])
print("The letters in between are: "  + alphabet[5:-5])
