import pandas as pd
import numpy as np
import csv
import xlsxwriter


class attributesaskf:
    def __init__(self, xlsxwriter):
        self.writer = xlsxwriter

    def run(self):
        CFGSNA2_ATTRIBUTES_AS_KEYFIGURE_2020-12-02_15_09.csv