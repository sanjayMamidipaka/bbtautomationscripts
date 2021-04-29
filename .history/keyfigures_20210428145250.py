import pandas as pd
import numpy as np
import csv
import xlsxwriter

plevelspath = '/Users/sanjaymamidipaka/Downloads/CFGSNA2_PLEVELS_ATTRS_2020-12-02_15_09.csv'
keyfigurespath = '/Users/sanjaymamidipaka/Downloads/CFGSNA2_KEYFIGURES_2020-12-02_15_09.csv'
plevels = pd.read_csv(plevelspath, delimiter=';')
keyfigures = pd.read_csv(keyfigurespath, delimiter=';')
keyfiguresfinal = pd.DataFrame();

keyfigures = keyfigures.drop_duplicates(subset='ID', keep="first")
keyfigures.reset_index(inplace=True)
keyfiguresfinal['Status'] = 'SAP IBP' #A
keyfiguresfinal['Key Figure ID'] = keyfigures['ID'] #B
keyfiguresfinal['Status'] = 'SAP IBP'
keyfiguresfinal['Base Planning ID'] = keyfigures['Base Planning Level'] #C
keyfiguresfinal['Description'] = ''


#Vlookups
plevelsidanddescription = plevels[['Planning Level', 'Description']]
plevelsidanddescription = plevelsidanddescription.drop_duplicates(subset='Planning Level', keep="first")
#print(plevelsidanddescription)
keyfiguresbaseplanningid = pd.DataFrame(keyfiguresfinal['Base Planning ID'])
#print(keyfiguresbaseplanningid)
#print(keyfiguresbaseplanningid.columns)

for i in range(len(keyfiguresbaseplanningid)):
    this1 = plevelsidanddescription.loc[plevelsidanddescription['Planning Level'] == keyfiguresbaseplanningid['Base Planning ID'][i],['Description']]
    keyfiguresfinal['Description'][i] = str(this1).replace('Description\n')
print(keyfiguresfinal)

#keyfiguresfinal.to_excel("/Users/sanjaymamidipaka/Downloads/output1234.xlsx")



