"""
Application script for theCycles main script
"""

import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from utils.mainmenu import MainMenu
from scripts.statistic_page import StatisticMonthlyPage

class Application(tk.Tk):
    """The application root window"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("theCycles Project")
        self.columnconfigure(0, weight=1)

        # Loading the menus
        menu = MainMenu(self)
        self.configure(menu=menu)

        # Defining callbacks used in the menu
        event_callbacks = {
            "<<STATISTIC Monthly>>": self._to_statistic_monthly_page,
            "<<STATISTIC Daily>>": self._to_statistic_daily_page(),
            "<<DEEP LEARNING Simple Fully Connected Network>>": self._to_deep_learning_simple_fully_connected_network_page(),
            "<<DEEP LEARNING Recurrent Neutral Network>>": self._to_deep_learning_recurrent_neutral_network_page(),
            "<<DEEP LEARNING Encoder-Decoder Network>>": self._to_deep_learning_encoder_decoder_network_page(),
            "<<GENERATIVE Generative Model>>": self._to_generative_generative_model_page(),
            "<<QUIT>>": lambda _: self.quit()
        }
        for sequence, callback in event_callbacks.items():
            self.bind(sequence, callback)

        # Packing the default application frame when main.py is loaded
        self.mainpage = StatisticMonthlyPage(self)
        self.mainpage.grid(row=0, column=0, sticky=tk.W+tk.E)

        # The status bar
        self.status = tk.StringVar()
        self.status.set('Loading default page...')
        self.statusbar = ttk.Label(self, textvariable=self.status, bootstyle="info")
        self.statusbar.grid(row=99, padx=10, sticky=tk.W+tk.E)

    def _to_statistic_monthly_page(self, *_):
        pass

    def _to_statistic_daily_page(self, *_):
        pass

    def _to_deep_learning_simple_fully_connected_network_page(self, *_):
        pass

    def _to_deep_learning_recurrent_neutral_network_page(self, *_):
        pass

    def _to_deep_learning_encoder_decoder_network_page(self, *_):
        pass

    def _to_generative_generative_model_page(self, *_):
        pass

    def _to_status(self, text):
        self.status.set(text)