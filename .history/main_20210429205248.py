import pandas as pd
import numpy as np
import csv
import xlsxwriter
from timeprofile import timeprofile

writer = pd.ExcelWriter('/Users/sanjaymamidipaka/Downloads/bbt_goal_output.xlsx', engine='xlsxwriter')

timeprofile_instance = timeprofile(writer)
timeprofile_instance.run()

        
