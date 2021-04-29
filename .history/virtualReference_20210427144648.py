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
df1 = pd.DataFrame(index=[0,1,2,3,4],columns=masterdatafinal.columns) #adds 3 empty rows above 
masterdatafinal = df1.append(masterdatafinal, ignore_index=True) #re-adds column names under 4 empty rows
masterdatafinal.iloc[3] = column_names
masterdatafinal.iloc[4] = column_names

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('/Users/sanjaymamidipaka/Downloads/virtualReference_goal_output.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
masterdatafinal.to_excel(writer, sheet_name='Virtual & Reference Tables', index=False, startrow=1, header = False)

# Get the xlsxwriter objects from the dataframe writer object.
workbook = writer.book
worksheet = writer.sheets['Virtual & Reference Tables']
#change size of columns to fit column names
worksheet.set_column(0, len(column_names), 15)

#merge 'referenced attributes heading'
worksheet.merge_range(5, 0, 5, 6, 'Master Data', workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bold': True, 'color': 'red', 'bg_color': 'white'
, 'font_size': 20}))

print(masterdatafinal.head())
workbook.close()