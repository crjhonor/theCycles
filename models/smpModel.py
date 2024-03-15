"""
This is the model of the statistic monthly analysis page.
"""
import utils.datareading as drd
import pandas as pd
import numpy as np

class Monthly_Analyse_MA:
    """Function to analyse the monthly average of trading target"""
    def __init__(self, target):
        """
        :param target: The target wanted to analyse
        """
        self.target = target
        print("We are here with the target: ", self.target, ".")
        self.data = drd.get_trading_data(self.target).returnData

    def show_me(self):
        """Function to show me the results"""
        data = self._preprocess_data(self.data)

    def _preprocess_data(self, data):
        """
        Preprocess the dataset
        :param data:
        :return:
        """

        # Transform daily data into monthly data
        data_daily = data[['TARGET', 'DATE', 'CLOSE']].set_index("DATE")
        data_month = data_daily.resample("M").last()
        # Obtain log return of the monthly close
        data_month['logr'] = np.log(data_month['CLOSE']/data_month['CLOSE'].shift(1))

        return data

