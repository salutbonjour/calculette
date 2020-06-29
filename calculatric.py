resultat = ""
prout = "                 "
def calculette():
    global prout
    global resultat
    print(" _____________________\n"
          "|  _________________  |\n"
          "| |{}{}| |\n"
          "| |_________________| |\n"
          "|  ___ ___ ___   ___  |\n"
          "| | 7 | 8 | 9 | | + | |\n"
          "| |___|___|___| |___| |\n"
          "| | 4 | 5 | 6 | | - | |\n"
          "| |___|___|___| |___| |\n"
          "| | 1 | 2 | 3 | | * | |\n"
          "| |___|___|___| |___| |\n"
          "| | . | 0 | C | | / | |\n"
          "| |___|___|___| |___| |\n"
          "|_____________________|".format(resultat,prout))

    Calculatrice = True

    while Calculatrice:

        truc = input("|+|-|*|/|")
        truc = str(truc)

        if str(truc) == '+':
            x = int(input("Nombre 1 = "))
            y = int(input("Nombre 2 = "))
            resultat = x + y
            vcalculette()
        if str(truc) == '-':
            x = int(input("Nombre 1 = "))
            y = int(input("Nombre 2 = "))
            resultat = x - y
            vcalculette()
        if str(truc) == '*':
            x = int(input("Nombre 1 = "))
            y = int(input("Nombre 2 = "))
            resultat = x * y
            vcalculette()
        if str(truc) == '/':
            x = int(input("Nombre 1 = "))
            y = int(input("Nombre 2 = "))
            resultat = x / y
            vcalculette()
        if str(truc) == 'c':
            break


def vcalculette():
    global prout
    global resultat
    resultat = str(resultat)
    caca = len(resultat) #3
    caca = int(caca)
    prout = 17 - caca
    if prout == 17:
        prout = "                 "
    if prout == 16:
        prout = "                "
    if prout == 15:
        prout = "               "
    if prout == 14:
        prout = "              "
    if prout == 13:
        prout = "             "
    if prout == 12:
        prout = "            "
    if prout == 11:
        prout = "           "
    if prout == 10:
        prout = "          "
    if prout == 9:
        prout = "         "
    if prout == 8:
        prout = "        "
    if prout == 7:
        prout = "       "
    if prout == 6:
        prout = "      "
    if prout == 5:
        prout = "     "
    if prout == 4:
        prout = "    "



    calculette()
calculette()
