import pandas as pd
import numpy as np
import csv
import xlsxwriter

plevelspath = '/Users/sanjaymamidipaka/Downloads/CFGSNA2_PLEVELS_ATTRS_2020-12-02_15_09.csv'
keyfigurespath = '/Users/sanjaymamidipaka/Downloads/CFGSNA2_KEYFIGURES_2020-12-02_15_09.csv'
plevels = pd.read_csv(plevelspath, delimiter=';')
keyfigures = pd.read_csv(keyfigurespath, delimiter=';')
keyfiguresfinal = pd.DataFrame();

keyfiguresfinal['Status'] = 'SAP IBP' #A
uniqueIDVals = keyfigures['ID'].unique()
#vals = pd.DataFrame(list(uniqueIDVals), columns='UniqueIDs')
print(uniqueIDVals)
#print(pd.merge(pd.Series(uniqueIDVals, name='uniqueIDVals'), keyfigures, on=['uniqueIDVals','ID']))
# keyfiguresfinal = keyfiguresfinal
# keyfiguresfinal['Key Figure ID'] = keyfigures['ID'].unique() #B
# keyfiguresfinal['Status'] = 'SAP IBP'



#print(keyfiguresfinal.head())