import pandas as pd
import numpy as np

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_rows", None)
df = pd.DataFrame(pd.read_excel("assets/resultaten.xlsx", index_col="naam"))

def vragen_ophalen():                                           #haal de vragen op uit de tekst bestand 
    vragenlijst = pd.read_excel("assets/vragenlijst.xlsx")
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_rows", None)
    df_2 = pd.DataFrame(vragenlijst)
    return vragenlijst
        
def resultaten_opslaan(data):
    print('-------------------------------')
    procenten = data[1]
    spec = procenten.index(max(procenten))
    new_df = df.append({"naam": str(data[0]),
                        "iat": str(procenten[0]),
                        "fict": str(procenten[1]),
                        "se": str(procenten[2]),
                        "bdam": str(procenten[3]),
                        "specialisatie": str(spec)},
                        ignore_index = True)
    new_df.to_excel("assets/resultaten.xlsx", index=False)

def procenten(data):
    # bijna honderd procent heb. 0.3 
    
    bijna_honderd = (data[0] + data[1] + data[2] + data[3])
    iat = data[0] / bijna_honderd * 100
    iat = int(iat)
    fict = data[1] / bijna_honderd * 100
    fict = int(fict)
    se = data[2] / bijna_honderd * 100
    se = int(se)
    bdam = data[3] / bijna_honderd * 100
    bdam = int(bdam)
   # fict = round(data[1] / (bijna_honderd * 100),2)
    #se = round(data[2] / (bijna_honderd / 100),2)
    #bdam = round(data[3] / (bijna_honderd / 100),2)
    print(bijna_honderd)
    specialisaties_lijst = [iat , fict , se ,bdam]
    print("Bijna honderd------------------" + str(bijna_honderd))
    return specialisaties_lijst
    #honderd_procent = (int(procenten[0])) + int(procenten[1]) + int(procenten[2]) + int(procenten[3])

def resultaten_ophalen(username):   
    # username = str(username.replace(" ", ""))
    data = df.iloc[[-1]]
    return data

def main():
    print('sorteerhoed')

if __name__ == "__main__":
    main()
