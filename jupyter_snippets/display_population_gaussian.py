"""
This module reads participant skills from the participantskills.csv file, computes the gaussian
distributions per skill and creates a plot. The output file is stored in:
"generated-plots/gaussian.png"
"""

from restify_mining import participant_stat_tools
from restify_mining.participant import Participant
from restify_mining.plotters.skill_plotter import plot_gaussian
from csv_tools import file_load_utils

# Load all participant objects (specifies skills, codename, controlgroup) from csv file
population: list[Participant] = file_load_utils.load_all_participants()

# Compute a gaussian distribution (defined by mean and standard dev) for every skill and produce
# plot
mean_scores = participant_stat_tools.build_mean_skills(population)
stddev_scores = participant_stat_tools.build_standard_deviation_skills(population)

# Plot gaussian curves for all participant skills
for index in range(len(skills.skill_tags)):
    plot_gaussian(mean_scores[index], stddev_scores[index], skills.palette[index])
