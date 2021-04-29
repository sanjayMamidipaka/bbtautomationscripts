import pandas as pd
import numpy as np
import csv
import xlsxwriter

masterdatatypes = pd.read_csv('/Users/sanjaymamidipaka/Downloads/CFGSNA2_MASTERDATATYPES_2020-12-02_15_09.csv', delimiter=';')
plevels = pd.read_csv('/Users/sanjaymamidipaka/Downloads/CFGSNA2_PLEVELS_ATTRS_2020-12-02_15_09.csv', delimiter=';')
masterdatafinal = pd.DataFrame();
masterdatafinal['Status IBP'] = 'Status IBP'
masterdatafinal['Master Data Type'] = masterdatatypes['Type']
masterdatafinal['Status IBP'] = 'Status IBP'
masterdatafinal['Master Data Components'] = masterdatatypes['Components']
masterdatafinal['Master Data Type Name'] = masterdatatypes['Components']
print(masterdatafinal)