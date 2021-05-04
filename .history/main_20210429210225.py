import pandas as pd
import numpy as np
import csv
import xlsxwriter
from timeprofile import timeprofile
from masterdata import masterdata
from virtualReference import virtualReference

#Steps:
create class
add import    
change writer

writer = pd.ExcelWriter('/Users/sanjaymamidipaka/Downloads/bbt_goal_output.xlsx', engine='xlsxwriter')

timeprofile_instance = timeprofile(writer)
timeprofile_instance.run()

masterdata_instance = masterdata(writer)
masterdata_instance.run()

virtualReference_instance = virtualReference(writer)
virtualReference_instance.run()

        
