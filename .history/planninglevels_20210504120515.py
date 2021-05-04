import pandas as pd
import numpy as np
import csv
import xlsxwriter


# class planninglevels:
#     def __init__(self, xlsxwriter):
#         self.writer = xlsxwriter

plevelspath = '/Users/sanjaymamidipaka/Downloads/CFGSNA2_PLEVELS_ATTRS_2020-12-02_15_09 (1).csv'
planninglevels = pd.read_csv(plevelspath, delimiter=';')

planninglevelsfinal = pd.DataFrame()
print(planninglevelsf.head())
