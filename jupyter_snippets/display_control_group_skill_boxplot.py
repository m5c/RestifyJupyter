"""
This module reads participant skills from the participantskills.csv file, computes the a boxplot
distribution representation per skill and group and fuses all resulting representation into a png
file. The output file is stored in:
"generated-plots/boxplot.png"
"""

from restify_mining.participant import Participant
from restify_mining import participant_filter_tools
from csv_tools import file_load_utils
from restify_mining.skills import skill_tags, palette
from restify_mining.plotter import plot_box

# Load all participant objects (specifies skills, codename, controlgroup) from csv file
population: list[Participant] = file_load_utils.load_all_participants()

# Creating the boxplot comes down to ordering all raw skill values of all participants into the
# order required by the plotter. The statistical markers are then extracted automatically.
# Namely, the required order is: all values for skill 1 of participants of group 1, all values
# for skill 1 of participants of group 2, ... all values for skill 2 of participants of group 1,
# and so on...
plotter_skill_values = []
control_groups: list[str] = participant_filter_tools.get_group_names(population)

# To fill the plotter_skill_value list, first iterate over all skills in outer loop
for skill_index in range(len(skill_tags)):

    # Next: per skill iterate over all participants ordered by control group in inner loop
    for control_group in control_groups:
        control_group_population = participant_filter_tools.filter_population_by_group(population,
            control_group)

        # Append the value every participant of the current control group has for the current skill
        plotter_skill_values.append(
            participant_filter_tools.get_skill_values_by_index(control_group_population,
                                                               skill_index))

# Finally feed the long list of all skill values in the order, required by the box plotter
plot_box(plotter_skill_values, palette, len(control_groups), "generated-plots/fused-stats.png")
