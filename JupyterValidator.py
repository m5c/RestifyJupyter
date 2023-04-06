"""
Jupyter tends to auto corrupt its own cells.
This script at least tells you which cell it is...
Source: Stackverflow - https://stackoverflow.com/a/56014817
"""

import json

valid_keys = ['cell_type', 'metadata', 'source']
filename = "Restify.ipynb"

with open(filename) as f:
    data = json.load(f)

for index, cell in enumerate(data['cells'], 1):
    if cell['cell_type'] == 'markdown':
        extra_keys = [key for key in cell.keys() if key not in valid_keys]
        if extra_keys:
            print(f'Cell {index} has the following keys which are invalid for a markdown cell: {extra_keys}')
            print('Open the file in VIM and remove those corrupted tags.')
            print('vim '+filename)