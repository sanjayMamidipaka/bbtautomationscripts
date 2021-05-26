import pandas as pd
import numpy as np
import csv
import xlsxwriter


class masterdata:
    def __init__(self, xlsxwriter, paths):
        self.writer = xlsxwriter
        self.paths = paths

    def run(self): #RENAME paattributes TO PA ATTRIBUTES
        

        masterdatatypes = pd.read_csv(self.paths[0], delimiter=';')
        paattributes = pd.read_csv(self.paths[5], delimiter=';')
        masterdatafinal = pd.DataFrame();
        masterdatafinal['Status IBP'] = '' #A
        masterdatafinal['Master Data Type'] = masterdatatypes['Type'] #B
        masterdatafinal['Status IBP'] = 'Status IBP' #A
        masterdatafinal['Master Data Components'] = masterdatatypes['Components'] #C
        masterdatafinal['Master Data Type Name'] = masterdatatypes['Name'] #D
        masterdatafinal['Master Data Type ID'] = masterdatatypes['Master Data Type ID'] #E 
        masterdatafinal['Src MD'] = np.nan #F
        masterdatafinal['Attribute ID'] = masterdatatypes['Attribute ID'] #G
        masterdatafinal['SrcAtt'] = np.nan #H
        masterdatafinal['Visibility Filter'] = np.nan #I
        masterdatafinal['Attribute Description'] = masterdatatypes['Attribute Description'] #J
        masterdatafinal['Is Key Attribute'] = masterdatatypes['Key'] #K
        masterdatafinal['Is Required Attribute'] = masterdatatypes['Required'] #L
        masterdatafinal['Data Format'] = masterdatatypes['Data Type'] #M
        masterdatafinal['Length'] = masterdatatypes['Length'] #N
        masterdatafinal['Decimal'] = np.nan #O
        masterdatafinal['Check Attribute'] = np.nan #P
        masterdatafinal['Check Master Data Type'] = np.nan #Q
        masterdatafinal['Attribute required for Virtual MD'] = np.nan # R
        masterdatafinal['Referenced Master Data Type'] = masterdatatypes['Referenced Master Data Type'] #S
        masterdatafinal['Join Condition'] = masterdatatypes['Join Conditions'] #T
        masterdatafinal['Referenced Attribute'] = masterdatatypes['Referenced Attribute'] #U
        masterdatafinal['Default Value if any'] = np.nan #V
        masterdatafinal['Is Hierarchy'] = np.nan #W
        masterdatafinal['PA Attribute'] = masterdatatypes['Used in Planning Area'] #X


        plevelsidanddescription = plevels[['Planning Level', 'Description']]
        plevelsidanddescription = plevelsidanddescription.drop_duplicates(subset='Planning Level', keep="first")
        keyfiguresbaseplanningid = pd.DataFrame(keyfiguresfinal['Base Planning ID'])
        keyfiguresbaseplanningid.columns = ['Planning Level']
        merged_description = pd.merge(keyfiguresbaseplanningid, plevelsidanddescription, on=['Planning Level'], how='left')
        
        
        #vlookup for last 3 tabs
        #get columns needed
        extracolumnspaattributes = paattributes[['Attribute ID','Business Meaning','Attribute Category','Planning Level Independent']]
        #
        extracolumnspaattributes = extracolumnspaattributes.drop_duplicates(subset='Attribute ID', keep="first")
        attributeidmasterdata = pd.DataFrame(masterdatafinal['Attribute ID'])
        keyfiguresbaseplanningid.columns = ['Planning Level']



        masterdatafinal['Business Meaning'] = paattributes['Business Meaning'] #Y
        masterdatafinal['Attribute Category'] = paattributes['Attribute Category'] #Z
        masterdatafinal['Planning Level Independent'] = paattributes['Planning Level Independent'] #AA
        masterdatafinal['Comments'] = np.nan #AB
        column_names = list(masterdatafinal.columns)
        df1 = pd.DataFrame(index=[0,1,2],columns=masterdatafinal.columns) #adds 3 empty rows above 
        masterdatafinal = df1.append(masterdatafinal, ignore_index=True) #re-adds column names under 4 empty rows
        masterdatafinal.iloc[2] = column_names
        
        # Convert the dataframe to an XlsxWriter Excel object.
        masterdatafinal.to_excel(self.writer, sheet_name='Master Data', index=False, startrow=1, header = False)

        # Get the xlsxwriter objects from the dataframe writer object.
        workbook = self.writer.book
        worksheet = self.writer.sheets['Master Data']
        #change size of columns to fit column names
        worksheet.set_column(0, len(column_names), 15)

        #change colors
        cell_format1 = workbook.add_format({'bold': True, 'color': 'white', 'bg_color': 'red', 'valign': 'vcenter', 'align': 'center', 'text_wrap': True})
        cell_format2 = workbook.add_format({'bold': True, 'color': 'red', 'bg_color': 'yellow', 'valign': 'vcenter', 'align': 'center', 'text_wrap': True})
        cell_format3 = workbook.add_format({'bold': True, 'color': 'white', 'bg_color': 'orange', 'valign': 'vcenter', 'align': 'center', 'text_wrap': True})
        cell_format4 = workbook.add_format({'bold': True, 'color': 'white', 'bg_color': 'green', 'valign': 'vcenter', 'align': 'center', 'text_wrap': True})
        formatType = [1,1,1,1,1,2,3,2,2,3,3,3,3,3,2,2,2,2,3,3,3,2,2,4,4,4,4,1]
        for i in range(len(formatType)):
            if formatType[i] == 1:
                worksheet.write(3,i, column_names[i], cell_format1)
            elif formatType[i] == 2:
                worksheet.write(3,i, column_names[i], cell_format2)
            elif formatType[i] == 3:
                worksheet.write(3,i, column_names[i], cell_format3)
            elif formatType[i] == 4:
                worksheet.write(3,i, column_names[i], cell_format4)
        print(masterdatafinal.head())

        #add pictures and format
        worksheet.merge_range(0, 0, 2, len(column_names)-1, 'Master Data', workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bold': True, 'color': 'red', 'bg_color': 'white'
        , 'font_size': 20}))
        worksheet.insert_image(0,2,'/Users/sanjaymamidipaka/Downloads/csv_files/bizbrain.png')
        #worksheet.insert_image(0,0,'/Users/sanjaymamidipaka/Downloads/csv_files/natureswaylogo.png')

        #workbook.close()