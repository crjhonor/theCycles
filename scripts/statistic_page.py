"""
The functional page of statistical analysis to the cycles.
"""

import os
from pathlib import Path
import tkinter as tk
import tkinter.ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import utils.readit as rit
import utils.widgets as w
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import utils.persistencesave as psave
from models import smpModel

class StatisticMonthlyPage(ttk.Frame):
    """The function of statistical analysis to monthly cycles.
    Design of the StatisticMonthlyPage GUI:
    - Left Frame
        - Target Select
        - MA Function:
            Mean of Log Return
        - Graphic Type:
            Single Table
        - Analyse Button
    - Right Frame
        - Output window"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.columnconfigure(0, weight=1)
        self.filepath = os.path.join(rit.temp_Path, rit.smp_filename)
        self.filepath = Path(self.filepath)

        # Load the hyperparameters
        self.psave = psave.HyperparameterSaving(
            filepath=self.filepath,
            fields=rit.statistic_monthly_page_fields,
            multivalues_fields_list=rit.statistic_monthly_page_multivalues_fields_list
        )
        self._load_hyperparameters()

        # Main Frame with Model Name
        self.main_frame = ttk.LabelFrame(parent, text="Statistical Monthly")
        self.main_frame.grid(sticky=tk.W+tk.E)
        for col in range(2):
            self.main_frame.columnconfigure(col, weight=1)

        # Left frame
        self.left_frame = ttk.LabelFrame(self.main_frame, text="hyperparameters")
        self.left_frame.grid(row=0, column=0, sticky=tk.W+tk.E)

        self.target_select_cbx = w.LabelInput(
            self.left_frame, "Select the Target",
            input_class=w.ValidatedCombobox,
            var=self._hyper_params['smp select the target'],
            input_args={'values': rit.indexesAll.iloc[0, ].to_list(), 'bootstyle': 'success'}
        )
        self.target_select_cbx.grid(row=0, column=0, padx=5, sticky=tk.W)

        self.MA_Function_select_cbx = w.LabelInput(
            self.left_frame, 'Select the MA Function',
            input_class=w.ValidatedCombobox,
            var=self._hyper_params['smp select the MA function'],
            input_args={'values': ['Mean of Log Return'], 'bootstyle': 'success'}
        )
        self.MA_Function_select_cbx.grid(row=1, column=0, padx=5, sticky=tk.W)

        self.Graphic_Types_select_cbx = w.LabelInput(
            self.left_frame, 'Select the Graphic Type',
            input_class=w.ValidatedCombobox,
            var=self._hyper_params['smp select the graphic type'],
            input_args={'values': ['Single Table'], 'bootstyle': 'success'}
        )
        self.Graphic_Types_select_cbx.grid(row=2, column=0, padx=5, sticky=tk.W)

        ttk.Label(self.left_frame, text="Press the Action").grid(row=6, column=0, padx=5, sticky=tk.W)
        self.analyse_btn = ttk.Button(
            self.left_frame,
            text="ANALYSE",
            command=lambda: self._analyse(),
            bootstyle=(SUCCESS, OUTLINE)
        )
        self.analyse_btn.grid(row=7, column=0, padx=5, sticky=tk.W+tk.E)

        # Right frame, model output frame
        self.right_frame = ttk.LabelFrame(self.main_frame, text="visualise results")
        self.right_frame.grid(row=0, column=1, sticky=tk.W+tk.E)

        # Visualizing Outputs
        self.figure = Figure(figsize=(15, 8), dpi=100)
        self.canvas_tkagg = FigureCanvasTkAgg(self.figure, self.right_frame)
        self.canvas_tkagg.get_tk_widget().grid(row=0, column=0, sticky=tk.W+tk.E)

        # Textual Outputs, I am trying to create a notebook for it, and the first tab will be "Results"
        self.nb = ttk.Notebook(self.right_frame, bootstyle="info")
        self.nb_tab1 = ttk.Frame(self.nb)
        self.nb_tab2 = ttk.Frame(self.nb)
        self.nb.add(self.nb_tab1, text="textual results", underline=3, sticky=tk.E)
        self.nb.add(self.nb_tab2, text="more information", underline=3, sticky=tk.E)
        self.nb.grid(row=1, column=0, sticky=tk.W+tk.E)

        self.textResults = w.LabelInput(
            self.nb_tab1, '-'*200,
            field_spec={'type': 'BoundText'},
            var=self._hyper_params['smp textual results'],
            input_args={'width': 135, 'height': 7}
        )
        self.textResults.pack()

        self.moreInfo = w.LabelInput(
            self.nb_tab2, '-'*200,
            field_spec={'type': 'BoundText'},
            var=self._hyper_params['smp more information'],
            input_args={'width': 135, 'height': 7}
        )
        self.moreInfo.pack()

    def _load_hyperparameters(self):
        """Load hyperparameters into dictionary"""

        vartypes = {
            'bool': tk.BooleanVar,
            'int': tk.IntVar,
            'float': tk.DoubleVar
        }
        self._hyper_params = dict()
        for key, data in rit.statistic_monthly_page_fields.items():
            vartype = vartypes.get(data['type'], tk.StringVar)
            if key in rit.statistic_monthly_page_multivalues_fields_list:
                self._hyper_params[key] = vartype(value=data['values'])
            else:
                self._hyper_params[key] = vartype(value=data['value'])

        # Add a trace on the variables so they get stored when changed.
        for var in self._hyper_params.values():
            var.trace_add('write', self._save_settings)

    def _save_settings(self, *_):
        """Save the current settings to file."""

        for key, variable in self._hyper_params.items():
            self.psave.set(key, variable.get())

        self.psave.save()

    def _analyse(self):
        """Calling the data reading function and analysis function"""

        if self._hyper_params['smp select the MA function'].get() == "Mean of Log Return":
            model = smpModel.Monthly_Analyse_MA(
                target=self._hyper_params['smp select the target'].get()
            )
            model.show_me()
