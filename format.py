"""
This script fixes the auto-corrupted jupyter notebook.
It searches for the multi line regex (illegal outputs statements for markdown cells) and wipes them.
"""

import re
with open('Restify.ipynb', 'r') as file:
    jupyter = file.read()
    outputs_tag_removed = re.sub(',\n\s+\"outputs\":\ \[\]', '', jupyter)
    print(outputs_tag_removed, file=open('Resitfy.ipynb', 'w'))
