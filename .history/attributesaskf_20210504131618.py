import pandas as pd
import numpy as np
import csv
import xlsxwriter


class attributesaskf:
    def __init__(self, xlsxwriter):
        self.writer = xlsxwriter

    def run(self):
        attributesaskfpath = '/Users/sanjaymamidipaka/Downloads/CFGSNA2_ATTRIBUTES_AS_KEYFIGURE_2020-12-02_15_09.csv'
        attributesaskf = pd.read_csv(attributesaskfpath, delimiter=';')

        attributesaskffinal = pd.DataFrame()
        attributesaskffinal['Master Data Type ID'] = attributesaskf['Master Data Type ID'] #A
        attributesaskffinal['Attribute ID'] = attributesaskf['Attribute ID'] #B
        attributesaskffinal['Target Planning Area'] = np.nan; #C
        attributesaskffinal['PERIODFR'] = attributesaskf['From Period'] #D
        attributesaskffinal['PERIODTO'] = attributesaskf['To Period'] #E
        attributesaskffinal['COMMENTS/MODIFICATIONS'] = np.nan #F

        column_names = list(planninglevelsfinal.columns)
        df1 = pd.DataFrame(index=[0,1,2,3],columns=planninglevelsfinal.columns) #adds 4 empty rows above 
        planninglevelsfinal = df1.append(planninglevelsfinal, ignore_index=True) #re-adds column names under 4 empty rows
        planninglevelsfinal.iloc[3] = column_names

