import pandas as pd
import numpy as np
import csv
import xlsxwriter
class Main:
    def __init__(self):
        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter('/Users/sanjaymamidipaka/Downloads/timeprofile_goal_output.xlsx', engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        timeprofile.to_excel(writer, sheet_name='Time Profile', index=False, startrow=1, header = False)

        # Get the xlsxwriter objects from the dataframe writer object.
        workbook  = writer.book
        worksheet = writer.sheets['Time Profile']
