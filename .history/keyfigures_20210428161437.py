import pandas as pd
import numpy as np
import csv
import xlsxwriter

plevelspath = '/Users/sanjaymamidipaka/Downloads/CFGSNA2_PLEVELS_ATTRS_2020-12-02_15_09.csv'
keyfigurespath = '/Users/sanjaymamidipaka/Downloads/CFGSNA2_KEYFIGURES_2020-12-02_15_09.csv'
attaskeyfigurepath = '/Users/sanjaymamidipaka/Downloads/CFGSNA2_ATTRIBUTES_AS_KEYFIGURE_2020-12-02_15_09.csv'
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
keyfiguresfinal





print(keyfiguresfinal)
#keyfiguresfinal.to_excel("/Users/sanjaymamidipaka/Downloads/output1234.xlsx")



