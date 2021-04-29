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
masterdatafinal['Attribute'] = masterdatatypes['Attribute ID'] #D
masterdatafinal['Referenced Master data type'] = masterdatatypes['Master Data Type ID'] #E
masterdatafinal['Referenced Attribute'] = masterdatatypes['Referenced Attribute'] #F
masterdatafinal['Master data type'] = np.nan #G
masterdatafinal['Master data type'] = np.nan #G
masterdatafinal['Master data type'] = np.nan #G
masterdatafinal['Master data type'] = np.nan #G
print(masterdatafinal)