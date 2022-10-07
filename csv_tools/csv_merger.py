"""
Utils module to merge several csv files with common key column.
"""

import pandas as pd
from pandas.api.types import CategoricalDtype


def build_merged_csv():
    """
    Reads in all individual csv files and merges them based on the participant. control group and
    code name entry. Stores the resulting fused csv in the "generated-csv-files" directory.
    """

    # Start by loading the individual key files.
    skill_csv = pd.read_csv("source-csv-files/skills.csv")
    control_group_csv = pd.read_csv("source-csv-files/controlgroups.csv")
    tests_csv = pd.read_csv("source-csv-files/tests.csv")
    time_csv = pd.read_csv("source-csv-files/time.csv")

    # Join control groups and participants.
    intermediate1 = skill_csv.merge(control_group_csv, on="controlgroup")

    # Add additional columns for measured time.
    intermediate2 = intermediate1.merge(time_csv, on="codename")

    # Add additional columns for test results.
    result = intermediate2.merge(tests_csv, on="codename")

    # Sort by control groups, so we have the order "Red, Green, Blue, Yellow"
    # Sort participants by animal names "Squid, Raccoon, Zebra, Fox, Unicorn, Turtle, Koala"
    # Prioritize group order, then sort participants per group alphabetically
    # Do this by converting control group to something ordered first.
    # See: https://stackoverflow.com/a/39223389
    result.controlgroup = pd.Categorical(result.controlgroup,
                                         categories=["red", "green", "blue", "yellow"],
                                         ordered=True)
    result.animal = pd.Categorical(result.animal,
                                         categories=["squid", "raccoon", "zebra", "fox", "unicorn", "turtle", "koala"],
                                         ordered=True)
    result.sort_values(["controlgroup", "animal"], axis=0, ascending=True, inplace=True)
    result.to_csv("generated-csv-files/restify.csv", index=None)
