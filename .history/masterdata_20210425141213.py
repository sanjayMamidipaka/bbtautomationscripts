import pandas as pd
import numpy as np
import csv
import xlsxwriter

p#re_conversion_file = csv.reader(open('/Users/sanjaymamidipaka/Downloads/csv_files/CFGSNA2_TIMEPROFILE_2020-12-02_15_09.csv'), delimiter=';')
plevels = pd.read_csv('/Users/sanjaymamidipaka/Downloads/CFGSNA2_PLEVELS_ATTRS_2020-12-02_15_09.csv')
print(plevels.head(30))
