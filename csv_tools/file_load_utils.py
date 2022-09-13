"""
Helper module for loading of CSV file content into lists of objectes defined in the
restify_mining package.
"""
import csv

from restify_mining.assessed_participant import AssessedParticipant
from restify_mining.participant import Participant


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
                assessed_participants.append(AssessedParticipant(row[0], [int(x) for x in row[1:]]))
    return assessed_participants
