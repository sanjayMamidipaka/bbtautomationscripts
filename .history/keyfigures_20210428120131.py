import pandas as pd
import numpy as np
import csv
import xlsxwriter

plevelspath = '/Users/sanjaymamidipaka/Downloads/ZSAPIBP1C_PA_ATTRIBUTES_2021-04-16_15_02.csv'
plevels = pd.read_csv(plevelspath, delimiter=';')
keyfiguresfinal = pd.DataFrame();

keyfiguresfinal['Status'] = 'SAP IBP'
keyfiguresfinal['ID'] = 

print(plevels.head())