import pandas as pd
import numpy as np
import csv
import xlsxwriter

masterdatatypes = pd.read_csv('/Users/sanjaymamidipaka/Downloads/CFGSNA2_MASTERDATATYPES_2020-12-02_15_09.csv', delimiter=';')
print(masterdatatypes.columns)
print(masterdatatypes.loc[(masterdatatypes['Type'] == 'Virtual') | (masterdatatypes['Type'] == 'Reference')]['Type'])