"""
Scripts for hyperparameters saving and loading
"""
import csv
import os
import utils.readit as rit
import json

class HyperparameterSaving():
    """A model for saving hyperparameters"""
    def __init__(self, filepath, fields, multivalues_fields_list):
        """
        :param filepath: obtain filepath to load and store the hyperparameters upon instancing
        :param fields:
        :param fields_list:
        """
        self.filepath = filepath
        self.fields = fields
        self.multivalues_fields_list = multivalues_fields_list

        # Load the hyperparameters, if file not exist, create a default one
        self.load()

    def load(self):
        """Load the hyperparameters from the file"""

        # If the file doesn't exist, I don't do anything and just return.
        # The initial file will be created within save() function.
        if not self.filepath.exists():
            return

        # Open the file and read the raw hyperparameters
        with open(self.filepath, 'r') as fh:
            raw_hyperparameters = json.load(fh)

        # Fill the loaded hyperparameters into the self.fields
        for key in self.fields:
            if key in self.multivalues_fields_list:
                if key in raw_hyperparameters and 'values' in raw_hyperparameters[key]:
                    raw_hyperparameter = raw_hyperparameters[key]['values']
                    self.fields[key]['values'] = raw_hyperparameter
            else:
                if key in raw_hyperparameters and 'value' in raw_hyperparameters[key]:
                    raw_hyperparameter = raw_hyperparameters[key]['value']
                    self.fields[key]['value'] = raw_hyperparameter

    def save(self):
        """Save the hyperparameters to the file
        if the file dose not exist, it will create an initial file."""
        with open(self.filepath, 'w') as fh:
            json.dump(self.fields, fh)

    def set(self, key, value):
        """Set the value or values in fields"""

        if key in self.fields:
            if key in self.multivalues_fields_list:
                self.fields[key]['values'] = value
            else:
                self.fields[key]['value'] = value
        else:
            raise KeyError("Bad key or wrong variable type")