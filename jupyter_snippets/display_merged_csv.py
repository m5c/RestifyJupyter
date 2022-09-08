"""
This module updates the fused csv based on the current partial csv files found in
"source-csv-files", persists the outcome to disk and displays the content.
"""
from csv_tools import csv_merger

# Call the CSV merger, fuses all individual files based on participant group/codename as key.
csv_merger.build_merged_csv()

# Print the result
restify_csv = open("generated-csv-files/restify.csv", "r").read()
print(restify_csv)
