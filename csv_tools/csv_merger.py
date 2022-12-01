"""
Utils module to merge several csv files with common key column.
Author: Maximilian Schiedermeier
"""

import pandas as pd
from pandas import DataFrame


def build_merged_csv():
    """
    Reads in all individual csv files and merges them based on the participant. control group and
    code name entry. Stores the resulting fused csv in the "generated-csv-files" directory.
    #TODO: FIND OUT WHY THIS DOES NOT MERGE TEST RESULTS CORRECTLY.
    """

    # Start by loading the individual key files.
    skill_csv: DataFrame = pd.read_csv("source-csv-files/skills.csv")
    control_group_csv: DataFrame = pd.read_csv("source-csv-files/controlgroups.csv")
    tests_csv: DataFrame = pd.read_csv("source-csv-files/tests.csv")
    time_csv: DataFrame = pd.read_csv("source-csv-files/time.csv")

    # Join control groups and participants.
    # intermediate1: DataFrame = skill_csv.merge(control_group_csv, on="controlgroup")
    #
    # # Add additional columns for measured time.
    # intermediate2: DataFrame = intermediate1.merge(time_csv, on="codename")
    #
    # # Add additional columns for test results.
    # result: DataFrame = intermediate2.merge(tests_csv, on="codename")
    result: DataFrame = skill_csv.merge(tests_csv, on="codename")


    # Sort by control groups, so we have the order "Red, Green, Blue, Yellow"
    # Sort participants by animal names "Squid, Raccoon, Zebra, Fox, Unicorn, Turtle, Koala"
    # Prioritize group order, then sort participants per group alphabetically
    # Do this by converting control group to something ordered first.
    # See: https://stackoverflow.com/a/39223389
    result.controlgroup = pd.Categorical(result.controlgroup,
                                         categories=get_group_order(control_group_csv),
                                         ordered=True)
    result.animal = pd.Categorical(result.animal,
                                   categories=["squid", "raccoon", "zebra", "fox", "unicorn",
                                               "turtle", "koala"],
                                   ordered=True)
    result.sort_values(["controlgroup", "animal"], axis=0, ascending=True, inplace=True)
    result.to_csv("generated-csv-files/restify.csv", index=None)


def get_group_order(control_group_csv: DataFrame) -> list[str]:
    """
    Helper method to provide list of control group names, ordered by index as noted in
    controlgroups.csv file.
    :return: list of control group strings, in order defined by corresponding csv file.
    """
    control_group_csv.sort_values("groupindex", ascending=True, inplace=True)
    return control_group_csv.controlgroup
