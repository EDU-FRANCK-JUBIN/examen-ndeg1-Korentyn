from easygui import *
import sys

def savefile(text):
    filename = filesavebox()
    if filename == None:
        return  # user selected Cancel
    output = open(filename, "a")  # a: append
    output.write(str(text))
    output.close()

message = "Bonjour êtes-vous en présence d'une personne victime d'un accident ou malaise ?"
title = "Bienvenue"
reponse = indexbox(message, title, choices=("Oui !", "Non"))

if (reponse == None or reponse == 1):
    sys.exit(0)
else:
    pass

message = "Bonjour êtes-vous en présence d'une personne victime d'un accident ou malaise ?"
title = "Bienvenue"
fieldNames = ["Nom", "Lieu", "Nombre de victimes","états des victimes","obstacles"]
reponse = multenterbox(message, title, fieldNames)

if (reponse == None):
    sys.exit(0)
else:
    pass

savefile(str(reponse))
