"""
Helper module for loading of CSV file content into lists of objectes defined in the
restify_mining package.
"""
import csv

from restify_mining.assessed_participant import AssessedParticipant
from restify_mining.participant import Participant


def str2bool(textual_boolean: str):
    """
    Helper function to convert strings to boolean values. See: https://stackoverflow.com/a/715468
    :param textual_boolean: as string, either "PASS" or any upper lover case variation (
    interpreted as false) or anything else (true).
    :return: a boolean value, either TRUE or FALSE.
    """
    return textual_boolean.lower() in 'pass'


def load_all_participants() -> list[Participant]:
    """
    Loads all participants but restricts information to pre-study data, that is to say control
    group info, code name and self-declared skill estimations per participant.
    :return: Participant object that stores all participant information gathered before the
    actual study run.
    """
    participants = []
    with open('source-csv-files/skills.csv', 'r', encoding="utf-8") as opened_file:
        reader = csv.reader(opened_file)
        # Flag to skip first line which is only the CSV column markers
        first_line = True
        for row in reader:
            if first_line:
                first_line = False
            else:
                # first argument is name (likewise first column in csv), then come as many
                # numbers as remaining columns, starting at csv column 1, fused to a list.
                participants.append(Participant(row[0], [int(x) for x in row[1:]]))
    return participants


def load_all_assessed_participants() -> list[AssessedParticipant]:
    """
    Loads all participants but in contrast to previous method also includes all other experiment
    data, that is to say the participant success rate, the task order, the measured times,
    the preferred method, etc...
    :return: Assessed Participant object that stores everything we measured about every participant.
    """
    assessed_participants = []
    with open('generated-csv-files/restify.csv', 'r', encoding="utf-8") as opened_file:
        reader = csv.reader(opened_file)
        # Flag to skip first line which is only the CSV column markers
        first_line = True
        for row in reader:
            if first_line:
                first_line = False
            else:
                # first argument is name (likewise first column in csv), then come as many
                # numbers as remaining columns, starting at csv column 1, fused to a list.
                # Next the test results for xox, followed by test results for bookstore
                assessed_participants.append(
                    AssessedParticipant(row[0], [int(x) for x in row[29:36]],
                                        [str2bool(x) for x in row[5:12]],
                                        [str2bool(x) for x in row[13:24]]))
    return assessed_participants
