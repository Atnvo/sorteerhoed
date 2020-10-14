import ast

def main():
    print("""\
                
  _    _                                           _    _              
 | |  | |                                         | |  | |             
 | |__| |  __ _  _ __  _ __  _   _   _ __    ___  | |_ | |_  ___  _ __ 
 |  __  | / _` || '__|| '__|| | | | | '_ \  / _ \ | __|| __|/ _ \| '__|
 | |  | || (_| || |   | |   | |_| | | |_) || (_) || |_ | |_|  __/| |   
 |_|  |_| \__,_||_|   |_|    \__, | | .__/  \___/  \__| \__|\___||_|   
   _____               _      __/ | | |      _                       _ 
  / ____|             | |    |___/  |_|     | |                     | |
 | (___    ___   _ __ | |_  ___   ___  _ __ | |__    ___    ___   __| |
  \___ \  / _ \ | '__|| __|/ _ \ / _ \| '__|| '_ \  / _ \  / _ \ / _` |
  ____) || (_) || |   | |_|  __/|  __/| |   | | | || (_) ||  __/| (_| |
 |_____/  \___/ |_|    \__|\___| \___||_|   |_| |_| \___/  \___| \__,_|
                                                                       
INF1V                                                                       

                """)
    True
    while True:
        try:
            print('\n')
            x = input("MENU Selecteer een keuze \nq: quit\n1: vragenlijst \n2: laatste uitslag tonen\nkeuze: ")
            if (x == 'q'): 
                exit()
            if (x == '1'):
                vraag_en_antwoord(vragen_ophalen())
            if (x == '2'):  
                toon_resultaten()
        except (ValueError):
            print("Oops! selectie niet gevonden.  Probeer opnieuw...")

def vragen_ophalen():                                           #haal de vragen op uit de tekst bestand 
    with open('meerkeuzevragen.txt', 'r') as file:              #Open de text bestand
        contents = file.read()                                  #sla de daqta op in een variable
        data = ast.literal_eval(contents)                       #zet de data om in een dictionary
        file.close()                                            #sluit de file
    return data                                                 #stuur de data terug

def vraag_en_antwoord(data_type):
    ingevoerde_antwoord = {}
    for key, value in data_type.items():
        print('\n')
        print(str(key))                                         #print de vraag
        for nummer, x in value.items():                         #loop door de nummer en antwoord
            print(' '+ str(nummer) + ": " + str(x))             #print de nummer en antwoord optie
        try:
            ingevoerde_antwoord[str(key)] = input('Antwoord: ')
        except (ValueError):
            print("Oops! verkeerd invoer.  Probeer opnieuw...")

    with open('antwoorden_gebruiker.txt', 'w') as f:            #open de antwoorde file
        f.write(str(ingevoerde_antwoord))                       #schrijf de antwoorden in de file
        # for ant in ingevoerde_antwoord:
        f.close()   

def toon_resultaten():                                          #Toon de resultaten van de quiz
    with open('antwoorden_gebruiker.txt', 'r') as file:         #Open de text bestand
        contents = file.read()                                  #Lees de inhoud en sla het in een variable op   
        file.close()                                            #sluit de file
    print(str(contents))                                        #print de resultaat nqar de console

if __name__ == "__main__":
    main()
