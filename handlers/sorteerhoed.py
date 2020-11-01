import pandas as pd
import xlsxwriter
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_rows", None)
df = pd.DataFrame(pd.read_excel("assets/resultaten.xlsx"))

def vragen_ophalen():                                           #haal de vragen op uit de tekst bestand 
    vragenlijst = pd.read_excel("assets/vragenlijst.xlsx")
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_rows", None)
    df_2 = pd.DataFrame(vragenlijst)
    return vragenlijst
    
def resultaten_opslaan(data):
    new_df = df.append({"naam": str(data[0]),
                        "iat": str(data[1]),
                        "fict": str(data[2]),
                        "se": str(data[3]),
                        "bdam": str(data[4])},
                        ignore_index = True)

    new_df.to_excel("assets/resultaten.xlsx", index=False)

def resultaten_ophalen(user_name):                                    #haal de vragen op uit de tekst bestand 
    test_obj = {'specialisatie'}
    return test_obj
    # return antwoorden    

def main():
    print('sorteerhoed')

if __name__ == "__main__":
    main()
