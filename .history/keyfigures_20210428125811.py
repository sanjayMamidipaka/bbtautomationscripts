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
keyfiguresfinal['Status'] = 'SAP IBP' #A
keyfiguresfinal['Key Figure ID'] = keyfigures['ID'] #B
keyfiguresfinal['Status'] = 'SAP IBP'
keyfiguresfinal['Base Planning ID'] = keyfigures['Base Planning Level'] #C

#Vlookups
keyfiguresLeftColumn = pd.DataFrame(list(pd.Series(keyfiguresfinal['Base Planning ID'])), columns=['Planning Level'])
planningLevelsRightColumns = plevels[['Planning Level', 'Description']]
mergedDescription = pd.merge(keyfiguresLeftColumn, planningLevelsRightColumns, on='Planning Level')
mergedDescription = mergedDescription.drop_duplicates(subset='Planning Level', keep="first")
print(mergedDescription.shape)





