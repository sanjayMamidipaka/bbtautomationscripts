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
        attributesaskffinal['Target Planning Area'] = np.nan(); #C
                =attributesaskffinal['Attribute ID'] = attributesaskf['Attribute ID'] #B

