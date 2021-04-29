import pandas as pd
import numpy as np
import csv
import xlsxwriter

plevelspath = '/Users/sanjaymamidipaka/Downloads/ZSAPIBP1C_PA_ATTRIBUTES_2021-04-16_15_02.csv'
keyfigurespath = '/Users/sanjaymamidipaka/Downloads/6_7_CFGSNA2_KEYFIGURES_2020-12-02_15_09.xlsx'
plevels = pd.read_csv(plevelspath, delimiter=';')
keyfigures = pd.read_csv(keyfigurespath, delimiter=';')
keyfiguresfinal = pd.DataFrame();

keyfiguresfinal['Status'] = 'SAP IBP'
keyfiguresfinal['ID'] = keyfigures['ID']

print(plevels.head())