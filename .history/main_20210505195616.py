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

writer = pd.ExcelWriter('/Users/sanjaymamidipaka/Downloads/Energizer_2021-05-05_21_29_Test_output.xlsx', engine='xlsxwriter')

energizerpaths = ['/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_MASTERDATATYPES_2021-05-04_21_01.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_PLEVELS_ATTRS_2021-05-04_21_01.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_KEYFIGURES_2021-05-04_21_01.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_ATTRIBUTES_AS_KEYFIGURE_2021-05-04_21_01.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_TIMEPROFILE_2021-05-04_21_01.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer Production_ZSAPIBP1C_2021-05-04_21_01/ZSAPIBP1C_PA_ATTRIBUTES_2021-05-04_21_01.csv']



natureswaypaths = ['/Users/sanjaymamidipaka/Downloads/natureswaydata/CFGSNA2_MASTERDATATYPES_2020-12-02_15_09.csv', 
        '/Users/sanjaymamidipaka/Downloads/natureswaydata/CFGSNA2_PLEVELS_ATTRS_2020-12-02_15_09.csv', 
        '/Users/sanjaymamidipaka/Downloads/natureswaydata/CFGSNA2_KEYFIGURES_2020-12-02_15_09.csv',
        '/Users/sanjaymamidipaka/Downloads/natureswaydata/CFGSNA2_ATTRIBUTES_AS_KEYFIGURE_2020-12-02_15_09.csv',
        '/Users/sanjaymamidipaka/Downloads/natureswaydata/CFGSNA2_TIMEPROFILE_2020-12-02_15_09.csv',
        '/Users/sanjaymamidipaka/Downloads/natureswaydata/CFGSNA2_PA_ATTRIBUTES_2020-12-02_15_09.csv']

energizertestpaths = ['/Users/sanjaymamidipaka/Downloads/Energizer_2021-05-05_21_29_Test/ZSAPIBP1C_MASTERDATATYPES_2021-05-05_21_29.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer_2021-05-05_21_29_Test/ZSAPIBP1C_PLEVELS_ATTRS_2021-05-05_21_29.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer_2021-05-05_21_29_Test/ZSAPIBP1C_KEYFIGURES_2021-05-05_21_29.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer_2021-05-05_21_29_Test/ZSAPIBP1C_ATTRIBUTES_AS_KEYFIGURE_2021-05-05_21_29.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer_2021-05-05_21_29_Test/ZSAPIBP1C_TIMEPROFILE_2021-05-05_21_29.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer_2021-05-05_21_29_Test/ZSAPIBP1C_PA_ATTRIBUTES_2021-05-05_21_29.csv']

energizerproductionspaths = ['/Users/sanjaymamidipaka/Downloads/Energizer_2021-05-05_21_32_Production/ZSAPIBP1C_MASTERDATATYPES_2021-05-05_21_32.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer_2021-05-05_21_32_Production/ZSAPIBP1C_PLEVELS_ATTRS_2021-05-05_21_32.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer_2021-05-05_21_32_Production/ZSAPIBP1C_KEYFIGURES_2021-05-05_21_32.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer_2021-05-05_21_32_Production/ZSAPIBP1C_ATTRIBUTES_AS_KEYFIGURE_2021-05-05_21_32.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer_2021-05-05_21_32_Production/ZSAPIBP1C_TIMEPROFILE_2021-05-05_21_32.csv',
        '/Users/sanjaymamidipaka/Downloads/Energizer_2021-05-05_21_32_Production/ZSAPIBP1C_PA_ATTRIBUTES_2021-05-05_21_32.csv']

timeprofile_instance = timeprofile(writer, energizerproductionspaths)
timeprofile_instance.run()

masterdata_instance = masterdata(writer, energizerproductionspaths)
masterdata_instance.run()

virtualReference_instance = virtualReference(writer, energizertestpaths)
virtualReference_instance.run()

attributes_instance = attributes(writer, energizertestpaths)
attributes_instance.run()

planninglevels_instance = planninglevels(writer, energizertestpaths)
planninglevels_instance.run()

keyfigures_instance = keyfigures(writer, energizertestpaths)
keyfigures_instance.run()

attributesaskf_instance = attributesaskf(writer, energizertestpaths)
attributesaskf_instance.run()

writer.book.close() #close the workbook



        
