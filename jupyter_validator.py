"""
Jupyter tends to auto corrupt its own cells.
This script tells you if there are issues.
See:
Source: Stackverflow - https://stackoverflow.com/a/56014817
And: https://github.com/jupyter/nbconvert/issues/1872

Essentially, there are markdown cells which carry the outputs tag, and this is an illegal combo.
Easiest is to just wipe all occurrences of:

Use the format.py script to fix the auto-corrupted notebook.
"""

import json

valid_keys = ['cell_type', 'metadata', 'source']
file_name = "Restify.ipynb"

with open(file_name) as f:
    data = json.load(f)

for index, cell in enumerate(data['cells'], 1):
    if cell['cell_type'] == 'markdown':
        extra_keys = [key for key in cell.keys() if key not in valid_keys]
        if extra_keys:
            print(
                f'Cell {index} has the following keys which are invalid for a markdown cell: '
                f'{extra_keys}')
            print('use the format.py script to un-corrupt the notebook.')
