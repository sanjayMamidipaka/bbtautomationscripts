import pandas as pd
import numpy as np
import csv
import xlsxwriter
from timeprofile import timeprofile
from masterdata import masterdata

writer = pd.ExcelWriter('/Users/sanjaymamidipaka/Downloads/bbt_goal_output.xlsx', engine='xlsxwriter')

timeprofile_instance = timeprofile(writer)
timeprofile_instance.run()

masterdata_instance = masterdata(writer)
timeprofile_instance.run()

        
