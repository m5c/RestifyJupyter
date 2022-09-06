"""
This module reads participant skills from the participantskills.csv file, computes the gaussian
distributions per skill and creates a plot.
"""
import csv

from restify_mining import skills
from restify_mining.participant import Participant
from restify_mining import participant_stat_tools
from restify_mining.plotter import plot_gaussian

# Load all participant skill objects from csv file
participants = []
with open('source-csv-files/partitionskills.csv', 'r', encoding="utf-8") as f:
    reader = csv.reader(f)
    # Flag to skip first line which is only the CSV column markers
    FIRST = True
    for row in reader:
        if FIRST:
            FIRST = False
        else:
            participants.append(Participant(row[0], [int(x) for x in row[1:]]))

# Compute a gaussian distribution (defined by mean and standard dev) for every skill and produce
# plot
skill_amount = len(participants[0].skills)
mean_scores = participant_stat_tools.build_mean_skills(participants)
stddev_scores = participant_stat_tools.build_standard_deviation_skills(participants)

# Plot gaussian curves for all participant skills
for index in range(skill_amount):
    plot_gaussian(mean_scores[index], stddev_scores[index], skills.palette[index])
