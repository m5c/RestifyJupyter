"""
Helper module for loading of CSV file content into lists of objectes defined in the
restify_mining package.
"""
import csv

from restify_mining.participant import Participant


def load_all_participants() -> list[Participant]:
    participants = []
    with open('source-csv-files/skills.csv', 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        # Flag to skip first line which is only the CSV column markers
        FIRST = True
        for row in reader:
            if FIRST:
                FIRST = False
            else:
                participants.append(Participant(row[0], [int(x) for x in row[1:]]))
    return participants
