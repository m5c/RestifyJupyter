"""
Helper module for loading of CSV file content into lists of objectes defined in the
restify_mining package.
Author: Maximilian Schiedermeier
"""
import csv
from collections import Counter

import pandas as pd
from pandas import DataFrame
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.control_group import ControlGroup
from restify_mining.data_objects.participant import Participant


def str2bool(textual_boolean: str):
    """
    Helper function to convert strings to boolean values. See: https://stackoverflow.com/a/715468
    :param textual_boolean: as string, either "PASS" or any upper lover case variation (
    interpreted as false) or anything else (true).
    :return: a boolean value, either TRUE or FALSE.
    """
    return textual_boolean.lower() in 'pass'


def load_all_control_groups() -> dict[str, ControlGroup]:
    """
    Loads all control groups, including information on task and methodology order from external
    CSV file.
    :return: list of control group objects, ordered by index.
    """
    # load csv from disk
    control_group_csv: DataFrame = pd.read_csv("source-csv-files/controlgroups.csv")
    # sort by index field, to get expected group order
    control_group_csv.sort_values("groupindex", ascending=True, inplace=True)
    # iterate over entries and convert to control group objects.
    # see: https://stackoverflow.com/a/55616777
    control_groups: dict[str, ControlGroup] = {}
    for row in control_group_csv.iterrows():
        control_groups[row[1].controlgroup] = \
            ControlGroup(row[1].controlgroup, row[1].firstapp, row[1].secondapp,
                         row[1].firstmethodology, row[1].secondmethodology)
    return control_groups


def load_all_participants() -> list[Participant]:
    """
    Loads all participants but restricts information to pre-study data, that is to say control
    group info, code name and self-declared skill estimations per participant.
    :return: Participant object that stores all participant information gathered before the
    actual study run.
    """
    # first retrieve all control groups:
    control_groups: dict[str, ControlGroup] = load_all_control_groups()

    participants = []
    with open('source-csv-files/skills.csv', 'r', encoding="utf-8") as opened_file:
        reader = csv.reader(opened_file)
        # Flag to skip first line which is only the CSV column markers
        first_line = True
        for row in reader:
            if first_line:
                first_line = False
            else:
                control_group_name = row[1]
                # control_group : ControlGroup =
                # first argument is name (likewise first column in csv), then come as many
                # numbers as remaining columns, starting at csv column 1, fused to a list.
                participants.append(
                    Participant(row[0], control_groups[control_group_name],
                                [int(x) for x in row[3:]]))
    return participants

    # pylint: disable=too-many-locals


def load_all_assessed_participants(remove_outliers_flag: bool) -> list[AssessedParticipant]:
    """
    Loads all participants but in contrast to previous method also includes all other experiment
    data, that is to say the participant success rate, the task order, the measured times,
    the preferred method, etc...
    :return: Assessed Participant object that stores everything we measured about every participant.
    """
    # first retrieve all control groups:
    control_groups: dict[str, ControlGroup] = load_all_control_groups()

    assessed_participants = []
    with open('generated-csv-files/restify.csv', 'r', encoding="utf-8") as opened_file:
        reader = csv.reader(opened_file)
        # Flag to skip first line which is only the CSV column markers
        first_line = True
        for row in reader:
            if first_line:
                first_line = False
            else:
                # Note: extracting ranger in python is extremely counter-intuitive. The first
                # value in range is excluded, while the second is included (based pycharms C-Index)
                # If the index is the array index, starting at 0, the first value in range is
                # included and the second excluded.
                codename: str = row[0]
                control_group_name = row[1]
                control_group: ControlGroup = control_groups[control_group_name]
                skills: list[int] = [int(x) for x in row[3:11]]
                test_results_bs: list[bool] = [str2bool(x) for x in row[38:50]]
                test_results_xox: list[bool] = [str2bool(x) for x in row[30:38]]
                # [19] = C20
                time_bs: int = row[19]
                # [18] = C19
                time_xox: int = row[18]
                # [16] = C 17
                pre_time_tc: int = row[16]
                # [17] = C 18z
                pre_time_ide: int = row[17]

                # Amount of touchcore crashes observed in task solving.
                tc_crashes: int = row[20]
                # Total time a participant needed to recover from all touchcore crashes.
                crash_recovery_time: int = row[21]

                # first argument is name (likewise first column in csv), then the control group
                # details, then the skill vector. Next the test results for bookstore, followed
                # by test results for xox.
                # The last argument is the skill vector (self-declared by participant)
                assessed_participants.append(
                    AssessedParticipant(codename, control_group,
                                        skills,
                                        test_results_bs,
                                        test_results_xox,
                                        time_bs, time_xox,
                                        pre_time_tc,
                                        pre_time_ide,
                                        tc_crashes,
                                        crash_recovery_time))

    # remove outliers if requested
    if remove_outliers_flag:
        assessed_participants = remove_outliers(assessed_participants)

    return assessed_participants


def load_outliers() -> list[str]:
    """
    Helper function to load column entries of `outliers.csv` into a list of strings.
    :return: list of outlier strings, where each entry is in format "colour-animal".
    """
    # read csv to file, transform lines to comma separated values
    with open('source-csv-files/outliers.csv', 'r', encoding="utf-8") as file:
        outlier_csv_content = file.read().replace('\n', ', ')
    return outlier_csv_content.split(', ')


def remove_outliers(all_participants: list[AssessedParticipant]) -> list[AssessedParticipant]:
    """
    Strips the received list of assessed participants by all entries that match the outliers
    specified in outliers.csv
    """
    # get list of group-animal pairs to remote
    outlier_strings: list[str] = load_outliers()

    # iterate over participant list and remember all entries that have a matching outlier string
    for participant in all_participants:
        # check if participant string representation is in outlier string list
        sample_name: str = participant.group_name.lower()+"-"+participant.animal_name.lower()
        if sample_name in outlier_strings:
            print("Excluding outlier: "+sample_name)
            all_participants.remove(participant)

    # return remaining list
    return all_participants


def load_label_overrides() -> list[str]:
    """
    Parses the source-csv-files/labeloverride.csv for further use. Participants marked in
    this file will be the only ones labels, if such filtering is configured in the
    correlation plotter.
    :return: list of all override participant names.
    """
    # read csv to file, transform lines to comma separated values
    with open('source-csv-files/labeloverride.csv', 'r', encoding="utf-8") as file:
        override_csv_content = file.read().replace('\n', ', ')
    return override_csv_content.split(', ')


def load_stage_one_error_occurrences() -> dict[str, int]:
    """
    loads the "stageonefailcause.csv" file and returns a map representation, where for each kind of
    error the amount of occurrences is stored in the entries value.
    :return: dictionarry from type of error to amount of occurrences.
    """
    # read csv to file, store every line in list entry
    with open('source-csv-files/stageonefailcause.csv', 'r', encoding="utf-8") as file:
        stage_one_errors: list[str] = file.read().split('\n')

    # go over list (strip last empty entry) and reduce to value after first comma (error cause)
    stage_one_errors.pop()
    causes: list[str] = [entry.split(',')[1] for entry in stage_one_errors]

    # count amount of occurrences (transform list with duplicates to map/dics that lists amounts)
    unsorted_occurrences: dict[str, int] = Counter(causes)
    sorted_occurrences: dict[str, int] = dict(sorted(unsorted_occurrences.items()))

    return sorted_occurrences


def load_participant_feedback() -> list[str]:
    """
    Loads the participant feedback summary file form disk.
    :return: a list where every line is an entry.
    """
    with open('source-csv-files/participant-feedback-summary.csv', 'r', encoding="utf-8") as file:
        feedback: list[str] = file.read().split('\n')

    return feedback
