import pandas as pd
import xlsxwriter
import numpy as np

def vragen_ophalen():                                           #haal de vragen op uit de tekst bestand 
    vragenlijst = pd.read_excel("assets/vragenlijst.xlsx")
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)
    pd.set_option("display.max_rows", None)
    df_2 = pd.DataFrame(vragenlijst)
    return vragenlijst
    
def resultaten_opslaan(data):
    # data = [username, procent_iat, procent_se, procent_fict, procent_bdam]
    with xlsxwriter.Workbook("uitkomst.xlsx") as uitkomst:
        worksheet = uitkomst.add_worksheet()

        for row, col in enumerate(data): 
            worksheet.write_row(row,0,data)
            worksheet.write_row(0,1,"IAT") #,"FICT","SE","BDaM"
            worksheet.write_row(1,1,"FICT")
            worksheet.write_row(2,1,"SE")
            worksheet.write_row(3,1,"BDAM")

def resultaten_ophalen(user_name):                                    #haal de vragen op uit de tekst bestand 
    test_obj = {'specialisatie'}
    return test_obj
    # return antwoorden    

def main():
    print('sorteerhoed')

if __name__ == "__main__":
    main()
