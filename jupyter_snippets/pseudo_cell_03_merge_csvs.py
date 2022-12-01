"""
Author: Maximilian Schiedermeier
"""
from csv_tools import csv_merger


def cell_03() -> None:
    """
    Jupyter cell 05. See markdown description.
    This module updates the fused csv based on the current partial csv files found in
    "source-csv-files", persists the outcome to disk and displays the content.
    :return: None
    Author: Maximilian Schiedermeier
    """

    # Call the CSV merger, fuses all individual files based on participant group/codename as
    # key.
    # TODO: figure out why the produced CSV is not the correct fusion!
    csv_merger.build_merged_csv()

    # Print the result
    with open('source-csv-files/skills.csv', 'r', encoding="utf-8") as restify_csv:
        print(restify_csv)
