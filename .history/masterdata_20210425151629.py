import pandas as pd
import numpy as np
import csv
import xlsxwriter

masterdatatypes = pd.read_csv('/Users/sanjaymamidipaka/Downloads/CFGSNA2_MASTERDATATYPES_2020-12-02_15_09.csv', delimiter=';')
plevels = pd.read_csv('/Users/sanjaymamidipaka/Downloads/CFGSNA2_PLEVELS_ATTRS_2020-12-02_15_09.csv', delimiter=';')
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
masterdatafinal['']





print(masterdatafinal)