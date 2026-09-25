# Dictionary til oversættelse fra bogstaver til morsekode
morseCode = {"A":".-",
             "B":"-...",
             "C":"-.-.",
             "D":"-..",
             "E":".",
             "F":"..-.",
             "G":"--.",
             "H":"....",
             "I":"..",
             "J":".---",
             "K":"-.-",
             "L":".-..",
             "N":"-.",
             "M":"--",
             "O":"---",
             "P":".--.",
             "Q":"--.-",
             "R":".-.",
             "S":"...",
             "T":"-",
             "U":"..-",
             "V":"...-",
             "W":".--",
             "X":"-..-",
             "Y":"-.--",
             "Z":"--..",
             "Æ":".-.-",
             "Ø":"---.",
             "Å":".--.-",
             " ":""}

# Dictionary til oversættelse fra morsekode til bogstaver. Tomt oversættes til mellemrum.
morseCodeReverse = {}

# Denne funktion oversætter et enkelt bogstav (letter) med opslag i dictionay (code) hvis muligt
def translate(letter, code):
    letter = letter.upper()
    if letter in morseCode:
        return code[letter]
    else:
        return "?"


# Denne funktion oversætter en vilkårlig tekststreng til morsekode
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def encodeMessage(message, code):
    oversat = ""
    for letter in message:
        oversat += translate(letter, code)+"/"
    return oversat
    print(encodeMessage("A", morseCode))




# Denne funktion oversætter en korrekt formatteret morsebesked til bogstaver
# '/' markerer nyt bogstav
# '//' markerer nyt ord
def decodeMessage(message, code):
    pass

print(encodeMessage("Viktor er sej", morseCode))