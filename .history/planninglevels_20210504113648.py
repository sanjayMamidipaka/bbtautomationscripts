import pandas as pd
import numpy as np
import csv
import xlsxwriter


class masterdata:
    def __init__(self, xlsxwriter):
        self.writer = xlsxwriter