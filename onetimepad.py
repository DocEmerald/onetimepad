import secrets
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def createKey(length):
    string = []
    for i in range(length):
        string += secrets.choice(alphabet)
    return string
def encodeMessage(message, key):
    encodedMessage = ""
    for i in range(len(message)):
        msgindex = ((ord(message[i]))-96)
        keyindex = ((ord(key[i]))-96)
        if ((msgindex+keyindex)%26) == 0:
            encodedIndex = 26
        else:
            encodedIndex = ((msgindex+keyindex)%26)
        encodedMessage += chr(encodedIndex+96)
    return(encodedMessage)
def decodeMessage(message, key):
    decodedMessage = ""
    for i in range(len(message)):
        msgindex = ((ord(message[i]))-96)
        keyindex = ((ord(key[i])-96))
        if (msgindex-keyindex) > 0:
            decodedIndex = (msgindex-keyindex)
        else:
            decodedIndex = (26+(msgindex-keyindex))
        decodedMessage += chr(decodedIndex+96)
    return(decodedMessage)
