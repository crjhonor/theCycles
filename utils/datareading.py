"""
Script for data reading functions. The data reading functions should be shared among all the models if the same form of
dataset is required to obtain. But I should leave the data preprocess to the datapreprocess.py
"""
from pathlib import Path
import xlrd
import utils.readit as rit
import numpy as np
import pandas as pd

class get_trading_data:
    def __init__(self, indexWanted):
        self.dataDirName = rit.data_Path
        self.indexWanted = indexWanted
        self.readFilename = Path(self.dataDirName, self.indexWanted+'.xls')
        self.workSheet = self._readFiles()
        self.returnData = self._generate_data()

    def _readFiles(self):
        labelWorkbook = xlrd.open_workbook(self.readFilename)
        workSheet = labelWorkbook.sheet_by_index(0)
        # print('Reading LABEL FILE...<DONE!>...')
        return workSheet

    def _generate_data(self):
        """Function to read the daily trading data"""
        workSheet = self.workSheet

        # Create the empty DataFrame to store the return data.
        returnData = pd.DataFrame(columns=['TARGET', 'DATE', 'HIGH', 'LOW', 'CLOSE'])
        returnData['DATE'] = [xlrd.xldate_as_datetime(dt.value, 0) for dt in workSheet.col(2)[1:-6]]
        returnData['TARGET'] = self.indexWanted
        returnData['HIGH'] = [cl.value for cl in workSheet.col(4)[1:-6]]
        returnData['LOW'] = [cl.value for cl in workSheet.col(5)[1:-6]]
        returnData['CLOSE'] = [cl.value for cl in workSheet.col(6)[1:-6]]
        return returnData