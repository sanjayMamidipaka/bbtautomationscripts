import pandas as pd
import numpy as np
import csv
import xlsxwriter


# class planninglevels:
#     def __init__(self, xlsxwriter):
#         self.writer = xlsxwriter

plevelspath = '/Users/sanjaymamidipaka/Downloads/CFGSNA2_PLEVELS_ATTRS_2020-12-02_15_09 (1).csv'
planninglevels = pd.read_csv(plevelspath, delimiter=';')

planninglevelsfinal = pd.DataFrame()
planninglevelsfinal['Planning Level ID'] = planninglevels['Planning Level'] #A
planninglevelsfinal['Planning Level'] = planninglevels['Description'] #B
planninglevelsfinal['Source Master Data Type'] = planninglevels['Master Data Type ID'] #C

new = planninglevels['Attribute ID'].str.split('-', n = 1, expand = True) #splits the string on the hyphen
print(new)
planninglevelsfinal['Attribute ID'] = new[0] #D
planninglevelsfinal['Attribute Name'] = new[1] #E
planninglevelsfinal['Is Root Attribute'] = planninglevels['Root'] #F
planninglevelsfinal['Conversion Source'] = planninglevels['Conversion Source'] #G
planninglevelsfinal['Conversion Target'] = planninglevels['Conversion Target'] #H
planninglevelsfinal['Comments  |  Modifications to do'] = np.nan #I
planninglevelsfinal['In CFG'] = np.nan

column_names = list(planninglevelsfinal.columns)
df1 = pd.DataFrame(index=[0,1,2,3],columns=planninglevelsfinal.columns) #adds 4 empty rows above 
planninglevelsfinal = df1.append(planninglevelsfinal, ignore_index=True) #re-adds column names under 4 empty rows
planninglevelsfinal.iloc[3] = column_names

# Convert the dataframe to an XlsxWriter Excel object.
keyfiguresfinal.to_excel(self.writer, sheet_name='Planning Levels', index=False, startrow=1, header = False)

 workbook = self.writer.book
worksheet = self.writer.sheets['KF General']

print(planninglevelsfinal.head())
