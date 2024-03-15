"""
Here I position all the global variables of the project.
"""
import os
import numpy as np
import pandas as pd
from collections import namedtuple

# Global Variables -----------------------------------------------------------------------------------------------------
projectPath = '/home/Beta4090/PycharmProjects/theCycles'
PRO80_Path = '/run/user/1000/gvfs/smb-share:server=crjlambda-pc,share=dailytds'
temp_Path = "/home/Beta4090/PycharmProjects/theCycles/temp"
data_Path = "/run/user/1000/gvfs/smb-share:server=crjlambda-pc,share=profoundrnn_data"

# Variables for the dataset generation----------------------------------------------------------------------------------

# Read all the indexes
TD_indexes = pd.read_csv(os.path.join(PRO80_Path, 'ref_TD.csv'))
TD_yields_indexes = pd.read_csv(os.path.join(PRO80_Path, 'ref_yields.csv'))
TD_Currency_indexes = pd.read_csv(os.path.join(PRO80_Path, 'ref_Currency.csv'))
indexesAll = TD_indexes.join(TD_Currency_indexes, rsuffix='_Currency')
indexesAll = indexesAll.join(TD_yields_indexes, rsuffix='_yields')

indexWantedList = pd.read_csv('/home/Beta4090/PycharmProjects/ProfoundRNN_ext/indexWantedList.csv', index_col=0)
indexWantedList = indexWantedList.stack()
indexWantedList = indexWantedList.unstack(0)

indexWanted_CU0 = indexWantedList['indexWanted_CU0'].to_list()
indexWanted_RB0 = indexWantedList['indexWanted_RB0'].to_list()
indexWanted_SCM = indexWantedList['indexWanted_SCM'].to_list()
indexWanted_FINANCE = indexWantedList['indexWanted_FINANCE'].to_list()
indexWanted_default = indexWanted_FINANCE
indexList = list(np.unique(indexWanted_CU0 + indexWanted_RB0 + indexWanted_SCM + indexWanted_FINANCE))
indexList.sort()

# Variable for the triple dicer model.
TDM_SEQUENCE_LEN = 26  # stand for 25 trading days which are very close to one month
TDM_SEQUENCE_PAD = 999 # the int used for <pad>
TDM_MAX_ENCODER_LENGTH = 8
TDM_MAX_PREDICTION_LENGTH = 1
TDM_BATCH_SIZE = 4

FeatureConfig = namedtuple(
    "FeatureConfig",
    [
        "target",
        "index_cols",
        "static_categoricals",
        "static_reals",
        "time_varying_known_categoricals",
        "time_varying_known_reals",
        "time_varying_unkown_reals",
        "group_ids"
    ],
)

"""
Variables for the GUI---------------------------------------------------------------------------------------------------
"""

# elevenValues_dict = {
#     f"eleven_v{i}": {'type': 'str', 'value': indexWanted_default[i]} for i in range(11)
# }
fields = {
    # **elevenValues_dict,
    'indexWanted_default': {'type': 'str', 'values': indexWanted_default},
    'triple dicer count threshold': {'type': 'int', 'value': 44},
    'triple dicer count type': {'type': 'bool', 'value': False},
    'triple dicer stop flag': {'type': 'bool', 'value': False},
    'triple dicer predict date': {'type': 'str', 'value': ''},
    'triple dicer textual results': {'type': 'BoundText', 'value': 'Textual results will be here.'}
}
multivalues_fields_list = ['indexWanted_default']

# Variables for StatisticMonthlyPage
smp_filename = "smp_hyperparameters.json"
statistic_monthly_page_fields = {
    'smp select the target': {'type': 'str', 'value': 'CU0'},
    'smp select the MA function': {'type': 'str', 'value': 'Mean of Log Return'},
    'smp select the graphic type': {'type': 'str', 'value': 'Single Table'},
    'smp textual results': {'type': 'BoundText', 'value': 'Textual Results are coming in here.'},
    'smp more information': {'type': 'BoundText', 'value': 'Here will show more information.'}
}
statistic_monthly_page_multivalues_fields_list = []