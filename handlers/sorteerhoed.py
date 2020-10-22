import pandas as pd

def main():
    print('ttt')

def vragen_ophalen():                                           #haal de vragen op uit de tekst bestand 
    vragenlijst = pd.read_excel("assets/vragenlijst.xlsx")
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_rows", None)
    df_2 = pd.DataFrame(vragenlijst)
    return vragenlijst                                                 #stuur de data terug

def resultaten_ophalen(user_name):                                    #haal de vragen op uit de tekst bestand 
    test_obj = {'specialisatie': 'SE', 'naam': 'Naam'}
    return test_obj
    # return antwoorden    

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
