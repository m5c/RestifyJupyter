"""
This module reads participant skills from the participantskills.csv file, computes the gaussian
distributions per skill and creates a plot. The output file is stored in:
"generated-plots/gaussian.png"
Author: Maximilian Schiedermeier
"""

from restify_mining.data_objects import participant_stat_tools
from restify_mining.markers import skills_markers
from restify_mining.data_objects.participant import Participant
from restify_mining.plotters.skill_plotter import plot_gaussian
from csv_tools import file_load_utils

# Load all participant objects (specifies skills, codename, control-group) from csv file
population: list[Participant] = file_load_utils.load_all_participants()

# Compute a gaussian distribution (defined by mean and standard dev) for every skill and produce
# plot
mean_scores = participant_stat_tools.build_mean_skills(population)
stddev_scores = participant_stat_tools.build_standard_deviation_skills(population)

# Plot gaussian curves for all participant skills
for index in range(len(skills_markers.skill_tags)):
    plot_gaussian(mean_scores[index], stddev_scores[index], skills_markers.palette[index])
