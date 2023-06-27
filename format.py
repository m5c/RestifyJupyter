"""
This script fixes the auto-corrupted jupyter notebooks, specifically removes empty outputs
properties (which are not legal for markdown cells).
"""

import re

with open('Restify.ipynb', 'r') as file:
    # Read original notebook file to string
    jupyter = file.read()

    # Run a regex based search and replace, wipe all empty outputs properties.
    outputs_tag_removed = re.sub(',\n\s+\"outputs\":\ \[\]', '', jupyter)

    # Overwrite original notebook file
    print(outputs_tag_removed, file=open('Restify.ipynb', 'w'))
