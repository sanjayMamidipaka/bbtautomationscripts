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
baseplanningidval
print(plevels['Planning Level'][89])

#Vlookups
# for i in range(len(keyfiguresfinal['Base Planning ID'])):
#     baseplanningidval = keyfiguresfinal['Base Planning ID'][i]
#     if baseplanningidval != np.nan:
#         print(pd.DataFrame(plevels.loc[plevels['Planning Level'] == baseplanningidval]).iloc[0])
#continuation of column assignment
#keyfiguresfinal['Base Planning Description'] = mergedDescription['Description']
#print(keyfiguresfinal)






