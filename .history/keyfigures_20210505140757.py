import pandas as pd
import numpy as np
import csv
import xlsxwriter

class keyfigures:
    def __init__(self, xlsxwriter):
        self.writer = xlsxwriter

    def run(self):
        plevelspath = '/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_PLEVELS_ATTRS_2021-05-04_21_01.csv'
        keyfigurespath = '/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_KEYFIGURES_2021-05-04_21_01.csv'
        attaskeyfigurepath = '/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_ATTRIBUTES_AS_KEYFIGURE_2021-05-04_21_01.csv'
        plevels = pd.read_csv(plevelspath, delimiter=';')
        keyfigures = pd.read_csv(keyfigurespath, delimiter=';')
        attaskeyfigure = pd.read_csv(attaskeyfigurepath, delimiter=';')
        keyfiguresfinal = pd.DataFrame();

        keyfigures = keyfigures.drop_duplicates(subset='ID', keep="first")
        keyfigures.reset_index(inplace=True)
        keyfiguresfinal['Status'] = 'SAP IBP' #A
        keyfiguresfinal['Key Figure ID'] = keyfigures['ID'] #B
        keyfiguresfinal['Status'] = 'SAP IBP'
        keyfiguresfinal['Base Planning ID'] = keyfigures['Base Planning Level'] #C


        #Vlookup (1st time)
        plevelsidanddescription = plevels[['Planning Level', 'Description']]
        plevelsidanddescription = plevelsidanddescription.drop_duplicates(subset='Planning Level', keep="first")
        keyfiguresbaseplanningid = pd.DataFrame(keyfiguresfinal['Base Planning ID'])
        keyfiguresbaseplanningid.columns = ['Planning Level']
        merged_description = pd.merge(keyfiguresbaseplanningid, plevelsidanddescription, on=['Planning Level'], how='left')

        keyfiguresfinal['Base Planning Description'] = merged_description['Description'] #D
        keyfiguresfinal['Key Figure Name'] = keyfigures['Name'] #E
        keyfiguresfinal['Key Figure Description'] = keyfigures['Description'] #F
        keyfiguresfinal['Stored'] = keyfigures['Stored Key Figure'] #G
        keyfiguresfinal['Calculated'] = keyfigures['Calculated Key Figure'] #H
        keyfiguresfinal['Alert'] = keyfigures['Alert Key Figure'] #I
        keyfiguresfinal['Helper'] = keyfigures['Helper Key Figure'] #J
        keyfiguresfinal['Att Transformation'] = keyfigures['Attribute Transformation'] #K
        keyfiguresfinal['Att as Key Figure'] = '' #L

        #Vlookup (2nd time)
        attkeyfigvals = list(attaskeyfigure['Attribute ID'])
        for i in range(len(keyfiguresfinal['Key Figure ID'])):
            if keyfiguresfinal['Key Figure ID'][i] in attkeyfigvals:
                keyfiguresfinal['Att as Key Figure'][i] = 'x'

        #continuation
        keyfiguresfinal['L Script'] = keyfigures['L Script'] #M
        keyfiguresfinal['Used in Key Figures'] = keyfigures['Used in Key Figures'] #N
        keyfiguresfinal['Enable Planning Notes'] = keyfigures['Enable Planning Notes'] #O
        keyfiguresfinal['Planning Level for Planning Notes'] = keyfigures['Planning Level for Planning Notes'] #P
        keyfiguresfinal['Enable Fixing'] = keyfigures['Enable Fixing'] #Q
        keyfiguresfinal['Design Comments'] = np.nan #R
        keyfiguresfinal['Snapshot Key Figure'] = keyfigures['Snapshot Key Figure'] #S
        keyfiguresfinal['Aggregation Mode'] = keyfigures['Aggregation Mode'] #T
        keyfiguresfinal['Editable'] = keyfigures['Edit Allowed'] #U
        keyfiguresfinal['Disaggregation'] = keyfigures['Disaggregation Mode'] #V
        keyfiguresfinal['Proportionality'] = keyfigures['Proportionality'] #W
        keyfiguresfinal['Key Figure for Proportionality'] = keyfigures['Key Figure for Proportionality'] #X
        keyfiguresfinal['Disaggregation Expression'] = keyfigures['Disaggregation Expression'] #Y
        keyfiguresfinal['Period Weight Factor'] = keyfigures['Period Weight Factor'] #Z
        keyfiguresfinal['Input / Output to SCM operator'] = keyfigures['Input/Output for Supply Planning'] #AA
        keyfiguresfinal['Input / Output Forecast'] = keyfigures['Input/Output for TS Forecast Consumption'] #AB
        keyfiguresfinal['Convert Using'] = keyfigures['Convert Using'] #AC
        keyfiguresfinal['Aggregated Constraint'] = keyfigures['Aggregated Constraint'] #AD
        keyfiguresfinal['Display Format'] = keyfigures['Display Format'] #AE
        keyfiguresfinal['Hashtags'] = keyfigures['Hashtags'] #AF
        keyfiguresfinal['1'] = np.nan #AG
        keyfiguresfinal['2'] = np.nan #AH
        keyfiguresfinal['3'] = np.nan #AI
        keyfiguresfinal['4'] = np.nan #AJ
        keyfiguresfinal['5'] = np.nan #AK

        #Random Business Use Columns
        keyfiguresfinal['Integration Time Horizon'] = np.nan 
        keyfiguresfinal['Frequency of Integration'] = np.nan 
        keyfiguresfinal['Integration Notes'] = np.nan 
        keyfiguresfinal['Inbound (Y/N)'] = np.nan 
        keyfiguresfinal['Outbound (Y/N)'] = np.nan 
        keyfiguresfinal['Outbound extract planning level'] = np.nan
        keyfiguresfinal['Rule 1'] = np.nan 
        keyfiguresfinal['Rule 2'] = np.nan 
        keyfiguresfinal['History'] = np.nan 
        keyfiguresfinal['To be deleted'] = np.nan 
        keyfiguresfinal['Convert Using'] = np.nan 
        keyfiguresfinal['Ready to be Configured'] = np.nan 
        keyfiguresfinal['Date added to CFGSNA2'] = np.nan 
        keyfiguresfinal['Date added to SNA2'] = np.nan 
        keyfiguresfinal['Change History'] = np.nan 

        column_names = list(keyfiguresfinal.columns)
        df1 = pd.DataFrame(index=[0,1,2,3],columns=keyfiguresfinal.columns) #adds 4 empty rows above 
        keyfiguresfinal = df1.append(keyfiguresfinal, ignore_index=True) #re-adds column names under 4 empty rows
        keyfiguresfinal.iloc[3] = column_names


        #KF Calculations
        kfcalculationsfinal = pd.DataFrame();
        keyfigures = pd.read_csv(keyfigurespath, delimiter=';')
        kfcalculationsfinal['Status'] = 'SAP IBP' #A
        kfcalculationsfinal['KF ID'] = keyfigures['ID'] #B
        kfcalculationsfinal['Status'] = 'SAP IBP' 
        kfcalculationsfinal['Calculation Definitions'] = keyfigures['Calculation Definitions'] #C

        new = keyfigures['Input Key Figures'].str.split(',', n = 4, expand = True) #splits the string on the hyphen
        
        list1 = list(keyfigures['Input Key Figures'])
        for i in list1:
            print(i.count(','))


        kfcalculationsfinal['Input1'] =  keyfigures['Input Key Figures'] #D
        kfcalculationsfinal['Input1 Type'] = np.nan #E
        kfcalculationsfinal['Input2'] = keyfigures['Input Key Figures'] #F
        kfcalculationsfinal['Input2 Type'] = np.nan #G
        kfcalculationsfinal['Input3'] = keyfigures['Input Key Figures'] #H
        kfcalculationsfinal['Input3 Type'] = np.nan #I
        kfcalculationsfinal['Date'] = np.nan #J
        kfcalculationsfinal['Comment'] = np.nan #K


        # Create a Pandas Excel writer using XlsxWriter as the engine.
        #writer = pd.ExcelWriter('/Users/sanjaymamidipaka/Downloads/kf_general_goal_output.xlsx', engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        keyfiguresfinal.to_excel(self.writer, sheet_name='KF General', index=False, startrow=1, header = False)

        # Convert the dataframe to an XlsxWriter Excel object.
        kfcalculationsfinal.to_excel(self.writer, sheet_name='KF Calculations', index=False, startrow=1, header = False)

        # Get the xlsxwriter objects from the dataframe writer object.
        workbook = self.writer.book
        worksheet = self.writer.sheets['KF General']
        worksheet1 = self.writer.sheets['KF Calculations']
        #change size of columns to fit column names
        worksheet.set_column(0, len(column_names), 15)
        #change colors
        cell_format = workbook.add_format({'bold': True, 'color': 'white', 'bg_color': 'red', 'valign': 'vcenter', 'align': 'center', 'text_wrap': True})
        for i in range(len(column_names)):
            worksheet.write(4,i, column_names[i], cell_format)
        #add pictures and format
        worksheet.merge_range(0, 0, 3, len(column_names)-1, 'Key Figure Definition', workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bold': True, 'color': 'red', 'bg_color': 'white'
        , 'font_size': 20}))
        worksheet.insert_image(0,2,'/Users/sanjaymamidipaka/Downloads/csv_files/bizbrain.png')
        #worksheet.insert_image(0,0,'/Users/sanjaymamidipaka/Downloads/csv_files/natureswaylogo.png')

        #Do it again for KF Calculations
        column_names1 = list(kfcalculationsfinal.columns)
        worksheet1.set_column(0, len(column_names), 15)
        #change colors
        cell_format = workbook.add_format({'bold': True, 'color': 'white', 'bg_color': 'red', 'valign': 'vcenter', 'align': 'center', 'text_wrap': True})
        for i in range(len(column_names1)):
            worksheet1.write(4,i, column_names1[i], cell_format)
        #add pictures and format
        worksheet1.merge_range(0, 0, 3, len(column_names1)-1, 'Key Figure Calculations', workbook.add_format({'align': 'center', 'valign': 'vcenter', 'bold': True, 'color': 'red', 'bg_color': 'white'
        , 'font_size': 20}))
        worksheet1.insert_image(0,2,'/Users/sanjaymamidipaka/Downloads/csv_files/bizbrain.png')
        #worksheet1.insert_image(0,0,'/Users/sanjaymamidipaka/Downloads/csv_files/natureswaylogo.png')



