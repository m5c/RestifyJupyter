"""
Utils module to merge several csv files with common key column.
"""

import pandas as pd


def build_merged_csv():
    """
    Reads in all individual csv files and merges them based on the participant. control group and
    code name entry. Stores the resulting fused csv in the "generated-csv-files" directory.
    """
    # Merge the individual key files. Use participant code name as key.
    skill_csv = pd.read_csv("source-csv-files/skills.csv")
    control_group_csv = pd.read_csv("source-csv-files/controlgroups.csv")
    tests_csv = pd.read_csv("source-csv-files/tests.csv")
    intermediate1 = skill_csv.merge(control_group_csv, on="controlgroup")
    result = intermediate1.merge(tests_csv, on="codename")
    result.to_csv("generated-csv-files/restify.csv", index=None)
