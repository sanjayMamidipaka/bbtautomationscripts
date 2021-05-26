import pandas as pd
import numpy as np
import csv
import xlsxwriter


class attributesaskf:
    def __init__(self, xlsxwriter):
        self.writer = xlsxwriter

    def run(self):
        #attributesaskfpath = '/Users/sanjaymamidipaka/Downloads/CFGSNA2_ATTRIBUTES_AS_KEYFIGURE_2020-12-02_15_09.csv'

        masterdatapath = '/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_MASTERDATATYPES_2021-05-04_21_01.csv'
        plevelspath = '/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_PLEVELS_ATTRS_2021-05-04_21_01.csv'
        keyfigurespath = '/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_KEYFIGURES_2021-05-04_21_01.csv'
        attaskeyfigurepath = '/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_ATTRIBUTES_AS_KEYFIGURE_2021-05-04_21_01.csv'
        timeprofilepath = '/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_TIMEPROFILE_2021-05-04_21_01.csv'

        attributesaskf = pd.read_csv(attributesaskeyfigurepath, delimiter=';')

        attributesaskffinal = pd.DataFrame()
        attributesaskffinal['Master Data Type ID'] = attributesaskf['Master Data Type ID'] #A
        attributesaskffinal['Attribute ID'] = attributesaskf['Attribute ID'] #B
        attributesaskffinal['Target Planning Area'] = np.nan; #C
        attributesaskffinal['PERIODFR'] = attributesaskf['From Period'] #D
        attributesaskffinal['PERIODTO'] = attributesaskf['To Period'] #E
        attributesaskffinal['COMMENTS/MODIFICATIONS'] = np.nan #F

        column_names = list(attributesaskffinal.columns)
        df1 = pd.DataFrame(index=[0,1,2,3],columns=attributesaskffinal.columns) #adds 4 empty rows above 
        attributesaskffinal = df1.append(attributesaskffinal, ignore_index=True) #re-adds column names under 4 empty rows
        attributesaskffinal.iloc[3] = column_names

        # Convert the dataframe to an XlsxWriter Excel object.
        attributesaskffinal.to_excel(self.writer, sheet_name='Attribute as Key Figure', index=False, startrow=1, header = False)

        # Get the xlsxwriter objects from the dataframe writer object.
        workbook = self.writer.book
        worksheet = self.writer.sheets['Attribute as Key Figure']

        #change size of columns to fit column names
        worksheet.set_column(0, len(column_names), 15)
        #change colors
        cell_format = workbook.add_format({'bold': True, 'color': 'white', 'bg_color': 'red', 'valign': 'vcenter', 'align': 'center', 'text_wrap': True})
        for i in range(len(column_names)):
            worksheet.write(4,i, column_names[i], cell_format)
        #add pictures and format
        worksheet.merge_range(0, 0, 3, len(column_names)-1, 'Attribute As Key Figure Definition', workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bold': True, 'color': 'red', 'bg_color': 'white'
        , 'font_size': 15}))
        worksheet.insert_image(0,1,'/Users/sanjaymamidipaka/Downloads/csv_files/bizbrain.png')

        print(attributesaskffinal.head())
