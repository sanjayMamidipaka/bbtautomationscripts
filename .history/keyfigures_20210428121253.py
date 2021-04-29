import pandas as pd
import numpy as np
import csv
import xlsxwriter

plevelspath = '/Users/sanjaymamidipaka/Downloads/CFGSNA2_PLEVELS_ATTRS_2020-12-02_15_09.csv'
keyfigurespath = '/Users/sanjaymamidipaka/Downloads/6_7_CFGSNA2_KEYFIGURES_2020-12-02_15_09.xlsx'
plevels = pd.read_csv(plevelspath, delimiter=';')
keyfigures = pd.read_csv(keyfigurespath, delimiter=';')
keyfiguresfinal = pd.DataFrame();

keyfiguresfinal['Status'] = 'SAP IBP'
keyfiguresfinal['Key Figure ID'] = keyfigures['ID']

print(keyfiguresfinal.head())