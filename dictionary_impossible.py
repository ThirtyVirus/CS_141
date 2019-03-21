"""
Brandon Calabrese - Dictionary_Impossible
"""

"""Returns dictionary of values based on key file"""
def getKey(keyPath, reverse):
    #get key dictionary"""
    key = open(keyPath)
    encodeDict = {}
    for line in key:
        sort = line.split(" ")
        if reverse:
            encodeDict[sort[1].rstrip()] = sort[0].rstrip()
        else:
            encodeDict[sort[0].rstrip()] = sort[1].rstrip()
    return encodeDict

"""Encodes file of words and retruns as list of strings"""
def encode(path, keyPath):
        
    encodeDict = getKey(keyPath, False)

    """Makes list of strings for encoded message"""
    source = open(path)
    encodedWords = []
    for line in source:
        line = line.rstrip()
        sort = line.split(" ")
        lineString = ""
        for word in sort:
            lineString += str(encodeDict.get(word)) + " "
        encodedWords.append(lineString)
            
    """returns encoded message as list of strings (one string per line)"""
    return encodedWords

"""Decodes given list of strings, prints to screen"""
def decode(encodedList, keyPath):
    
    encodeDict = getKey(keyPath, True)
    decodedWords = []
    for line in encodedList:
        line = line.rstrip()
        sort = line.split(" ")
        lineString = ""
        for word in sort:
            lineString += str(encodeDict.get(word)) + " "
        print(lineString)

"""Simulates program, calls other functions"""
def simulate():
    print("Welcome to the Encoder 2000!")
  
    keyPath = input("Enter the name of the secret key file: ")
    path = input("Enter the name of the plain text file: ")
    
    print("Preparing to encode plain_text.txt using " + str(keyPath))   
    encodedList = encode(path,keyPath)
    
    print("The <word, encode_word> pairs are:")
    print(getKey(keyPath, False))

    print("Sending the encoded lines to the agent.")
    
    print("The encoded lines are: ")
    print(encodedList)

    print("The agent is decoding the lines.")
    print("The <encode_word, word> pairs are:")
    print(getKey(keyPath, True))  
    decode(encodedList, keyPath)
    
    print("Exiting the Encoder 2000!")
    
simulate()
