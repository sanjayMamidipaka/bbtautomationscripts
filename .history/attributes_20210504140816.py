import pandas as pd
import numpy as np
import csv
import xlsxwriter


class attributes:
    def __init__(self, xlsxwriter):
        self.writer = xlsxwriter

    def run(self):
        attributesfinal = pd.DataFrame()

        # Convert the dataframe to an XlsxWriter Excel object.
        attributesfinal.to_excel(self.writer, sheet_name='Attribute as Key Figure', index=False, startrow=1, header = False)

        # Get the xlsxwriter objects from the dataframe writer object.
        workbook = self.writer.book
        worksheet = self.writer.sheets['Attribute as Key Figure']