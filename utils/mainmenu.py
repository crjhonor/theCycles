"""
The Main Menu Class for theCycles project

## Menu Design for theCycles project

### STATISTIC

This menu refer to the analysis functions using traditional statistic methods such as sum and mean.

- Monthly (Switch to statistic monthly page which is analysing monthly frequency data)
- Daily (Switch to statistic daily page which is analysing daily frequency data)

### DEEP LEARNING

This menu refer to analysis using deep learning neutral network including state of art encoder-decoder or transformer
network applying to daily cycles.

- Simple Fully Connected Network
- Recurrent Neutral Network
- Encoder-Decoder network

### GENERATIVE

This menu refer to analysis function using the generative network which newly emerged amid the development of GPT3 or 4.

- Generative Model

### HELP

- About...

"""

import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox

class MainMenu(tk.Menu):
    """The Application's main menu"""

    def __init__(self, parent, **kwargs):
        """Constructor for main menu"""
        super().__init__(parent, **kwargs)

        # The STATISTIC menu
        statistic_menu = tk.Menu(self, tearoff=False)
        statistic_menu.add_command(
            label="Monthly Statistics",
            command=self._event('<<STATISTIC Monthly>>')
        )
        statistic_menu.add_separator()
        statistic_menu.add_command(
            label="Daily Statistics",
            command=self._event('<<STATISTIC Daily>>')
        )

        # The DEEP LEARNING menu
        deeplearning_menu = tk.Menu(self, tearoff=False)
        deeplearning_menu.add_command(
            label="Simple Fully Connected Network",
            command=self._event('<<DEEP LEARNING Simple Fully Connected Network>>')
        )
        deeplearning_menu.add_separator()
        deeplearning_menu.add_command(
            label="Recurrent Neutral Network",
            command=self._event('<<DEEP LEARNING Recurrent Neutral Network>>')
        )
        deeplearning_menu.add_separator()
        deeplearning_menu.add_command(
            label="Encoder-Decoder Network",
            command=self._event('<<DEEP LEARNING Encoder-Decoder Network>>')
        )

        # The GENERATIVE menu
        generative_menu = tk.Menu(self, tearoff=False)
        generative_menu.add_command(
            label="Generative Model",
            command=self._event('<<GENERATIVE Generative Model>>')
        )

        # The HELP menu
        help_menu = tk.Menu(self, tearoff=False)
        help_menu.add_command(
            label="About...",
            command=self._show_about
        )
        help_menu.add_separator()
        help_menu.add_command(
            label="Quit",
            command=self._event('<<QUIT>>')
        )

        # Add the menus to the main menu in order
        self.add_cascade(label="STATISTIC", menu=statistic_menu)
        self.add_cascade(label="DEEP LEARNING", menu=deeplearning_menu)
        self.add_cascade(label="GENERATIVE", menu=generative_menu)
        self.add_cascade(label='HELP', menu=help_menu)

    def _event(self, sequence):
        """Return a callback function that generates the sequence"""
        def callback(*_):
            root = self.master.winfo_toplevel()
            root.event_generate(sequence)
        return callback

    def _show_about(self):
        """Show the about dialog"""
        about_message = "theCycles Project"
        about_detail = (
            """By: CHEN RU JIE\n
            Date: March, 2024\n
            For: Analysing the cycle of trading.\n
            Version: 1.0.0"""
        )
        messagebox.showinfo(
            title="About",
            message=about_message,
            detail=about_detail
        )