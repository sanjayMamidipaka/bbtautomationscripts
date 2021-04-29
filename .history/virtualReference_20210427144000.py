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
masterdatafinal['Attribute(1)'] = np.nan #H
masterdatafinal['Equals'] = np.nan #I
masterdatafinal['Master data type(1)'] = np.nan #J
masterdatafinal['Attribute(2)'] = np.nan #K
masterdatafinal['Comment'] = np.nan #L

column_names = list(masterdatafinal.columns)
df1 = pd.DataFrame(index=[0,1,2,3],columns=masterdatafinal.columns) #adds 3 empty rows above 
masterdatafinal = df1.append(masterdatafinal, ignore_index=True) #re-adds column names under 4 empty rows
masterdatafinal.iloc[3] = column_names



print(masterdatafinal.head())