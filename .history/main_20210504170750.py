import pandas as pd
import numpy as np
import csv
import xlsxwriter
from timeprofile import timeprofile
from masterdata import masterdata
from virtualReference import virtualReference
from keyfigures import keyfigures
from planninglevels import planninglevels
from attributesaskf import attributesaskf
from attributes import attributes

#Steps:
# create class
# add import    
# change writer

writer = pd.ExcelWriter('/Users/sanjaymamidipaka/Downloads/bbt_goal_output(1).xlsx', engine='xlsxwriter')

timeprofile_instance = timeprofile(writer)
timeprofile_instance.run()

masterdata_instance = masterdata(writer)
masterdata_instance.run()

virtualReference_instance = virtualReference(writer)
virtualReference_instance.run()

attributes_instance = attributes(writer)
attributes_instance.run()

planninglevels_instance = planninglevels(writer)
planninglevels_instance.run()

keyfigures_instance = keyfigures(writer)
keyfigures_instance.run()

attributesaskf_instance = attributesaskf(writer)
attributesaskf_instance.run()

writer.book.close() #close the workbook



        
