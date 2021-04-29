import pandas as pd
import numpy as np
import csv
import xlsxwriter

masterdatatypes = pd.read_csv('/Users/sanjaymamidipaka/Downloads/CFGSNA2_MASTERDATATYPES_2020-12-02_15_09.csv', delimiter=';')
masterdatatypes = masterdatatypes.loc[(masterdatatypes['Type'] == 'Virtual') | (masterdatatypes['Type'] == 'Reference')]
masterdatafinal = pd.DataFrame();
masterdatafinal['SUPPLY'] = np.nan
masterdatafinal['MD Type'] = masterdatatypes['Type']
masterdatafinal['Virtual / Reference table Name'] = master
print(masterdatafinal.head())