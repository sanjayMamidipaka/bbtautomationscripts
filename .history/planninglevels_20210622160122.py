import pandas as pd
import numpy as np
import csv
import xlsxwriter


class planninglevels:
    def __init__(self, xlsxwriter, paths):
        self.writer = xlsxwriter
        self.paths = paths

    def run(self):
        #natures way
        #plevelspath = '/Users/sanjaymamidipaka/Downloads/CFGSNA2_PLEVELS_ATTRS_2020-12-02_15_09 (1).csv'

        planninglevels = pd.read_csv(self.paths[1], delimiter=';')

        planninglevelsfinal = pd.DataFrame()
        planninglevelsfinal['Planning Level ID'] = planninglevels['Planning Level'] #A
        planninglevelsfinal['Planning Level'] = planninglevels['Description'] #B
        planninglevelsfinal['Source Master Data Type'] = planninglevels['Master Data Type ID'] #C

        new = planninglevels['Attribute ID'].str.split('-', n = 1, expand = True) #splits the string on the hyphen
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
        planninglevelsfinal.to_excel(self.writer, sheet_name='Planning Levels', index=False, startrow=1, header = False)

        # Get the xlsxwriter objects from the dataframe writer object.
        workbook = self.writer.book
        worksheet = self.writer.sheets['Planning Levels']

        #change size of columns to fit column names
        worksheet.set_column(0, len(column_names), 15)
        #change colors
        cell_format = workbook.add_format({'bold': True, 'color': 'red', 'valign': 'vcenter', 'align': 'center', 'text_wrap': True})
        for i in range(len(column_names)):
            worksheet.write(4,i, column_names[i], cell_format)
        #add pictures and format
        worksheet.merge_range(0, 0, 3, len(column_names)-1, 'Planning Levels', workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bold': True, 'color': 'red'
        , 'font_size': 20}))
        worksheet.insert_image(0,2,'/Users/sanjaymamidipaka/Downloads/csv_files/bizbrain.png')

        print(planninglevelsfinal.head())
