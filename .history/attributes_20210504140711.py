import pandas as pd
import numpy as np
import csv
import xlsxwriter


class attributes:
    def __init__(self, xlsxwriter):
        self.writer = xlsxwriter

    def run(self):