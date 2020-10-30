import pandas as pd

def vragen_ophalen():                                           #haal de vragen op uit de tekst bestand 
    vragenlijst = pd.read_excel("assets/vragenlijst.xlsx")
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_rows", None)
    df_2 = pd.DataFrame(vragenlijst)
    return vragenlijst
    

def resultaten_ophalen(user_name):                                    #haal de vragen op uit de tekst bestand 
    test_obj = {'specialisatie': 'FICT', 'naam': 'Naam'}
    return test_obj
    # return antwoorden    

def main():
    print('sorteerhoed')


if __name__ == "__main__":
    main()
