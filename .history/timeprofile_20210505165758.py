import pandas as pd
import numpy as np
import csv
import xlsxwriter

class timeprofile:
    def __init__(self, xlsxwriter, paths):
        self.writer = xlsxwriter
        self.paths = paths
    
    def run(self):
        # natures way
        timeprofile = pd.read_csv(self.paths[''], delimiter=';')
        
        timeprofile = pd.read_csv(timeprofilepath, delimiter=';')
        timeprofile.reset_index(drop=True, inplace=True)
        timeprofile.drop('ID', axis=1, inplace=True)
        timeprofile.rename(columns = {"Assigned Attributes": "Attributes"}, inplace = True)
        column_names = list(timeprofile.columns)
        start_of_attributes = column_names.index("Attributes")

        for i in range(len(column_names)-1, start_of_attributes, -1): #standardizes 'Attributes' column
            column_names[i] = 'Attributes'+ str(len(column_names)-i)
        timeprofile.columns = column_names
        df1 = pd.DataFrame(index=[0,1,2,3],columns=timeprofile.columns) #adds 4 empty rows above 
        timeprofile = df1.append(timeprofile, ignore_index=True) #re-adds column names under 4 empty rows
        timeprofile.iloc[3] = column_names

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        #writer = pd.ExcelWriter('/Users/sanjaymamidipaka/Downloads/timeprofile_goal_output.xlsx', engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        timeprofile.to_excel(self.writer, sheet_name='Time Profile', index=False, startrow=1, header = False)

        # Get the xlsxwriter objects from the dataframe writer object.
        workbook  = self.writer.book
        worksheet = self.writer.sheets['Time Profile']
        #change size of columns to fix column names better
        worksheet.set_column(0, len(column_names), 15)
        #merge attributes tables
        merge_format = workbook.add_format({'align': 'left', 'bold': True, 'color': 'white', 'bg_color': 'red'})
        worksheet.merge_range(4, start_of_attributes, 4, len(column_names)-1, 'Attributes', merge_format)
        #change colors
        cell_format = workbook.add_format({'bold': True, 'color': 'white', 'bg_color': 'red', 'valign': 'vcenter', 'align': 'center', 'text_wrap': True})
        for i in range(len(column_names)):
            worksheet.write(4,i, column_names[i], cell_format)
        #add pictures and format
        worksheet.merge_range(0, 0, 3, len(column_names)-1, 'Time Profile', workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bold': True, 'color': 'red', 'bg_color': 'white'
        , 'font_size': 20}))
        worksheet.insert_image(0,2,'/Users/sanjaymamidipaka/Downloads/csv_files/bizbrain.png')
        #worksheet.insert_image(0,0,'/Users/sanjaymamidipaka/Downloads/csv_files/natureswaylogo.png')
        #workbook.close()
        print(timeprofile.head(10))
