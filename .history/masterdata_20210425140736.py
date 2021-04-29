import pandas as pd
import numpy as np
import csv
import xlsxwriter

masterdatatypes = pd.read_excel('/Users/sanjaymamidipaka/Downloads/2_CFGSNA2_MASTERDATATYPES_2020-12-02_15_09.xlsx', engine='openpyxl')
plevels = pd.read_excel('/Users/sanjaymamidipaka/Downloads/5_CFGSNA2_PLEVELS_ATTRS_2020-12-02_15_09.xlsx')
print(masterdatatypes.head(30))
