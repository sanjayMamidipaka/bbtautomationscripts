import pandas as pd
import numpy as np
import csv
import xlsxwriter

masterdatatypes = pd.read_csv('/Users/sanjaymamidipaka/Downloads/CFGSNA2_MASTERDATATYPES_2020-12-02_15_09.csv', delimiter=';')
masterdatatypes = masterdatatypes.loc[(masterdatatypes['Type'] == 'Virtual') | (masterdatatypes['Type'] == 'Reference')]
masterdatafinal = pd.DataFrame();
masterdatafinal['SUPPLY'] = np.nan #A
masterdatafinal['MD Type'] = masterdatatypes['Type'] #B
masterdatafinal['Virtual / Reference table Name'] = masterdatatypes['Description'] #C
print(masterdatafinal.head(30))