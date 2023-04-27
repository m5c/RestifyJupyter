"""
This module reads participant skills from the participantskills.csv file, computes then a boxplot
distribution representation per skill and group and fuses all resulting representation into a png
file. The output file is stored in:
"generated-plots/boxplot.png"
Author: Maximilian Schiedermeier
"""

from restify_mining.data_objects import participant_filter_tools
from restify_mining.data_objects.participant import Participant
from restify_mining.markers.skills_markers import skill_tags, palette
from restify_mining.box_plotters.skill_box_plotter import skill_plot_box


def extract_control_groups_boxplot(population: list[Participant]) -> None:
    """
    Creating the boxplot comes down to ordering all raw skill values of all participants into the
    order required by the plotter. The statistical markers are then extracted automatically.
    Namely, the required order is: all values for skill 1 of participants of group 1, all values
    for skill 1 of participants of group 2, ... all values for skill 2 of participants of group 1,
    and so on...
    :param population: as a subset of participants to analyze (should match a control group).
    :return: None.
    """
    plotter_skill_values = []
    control_groups: list[str] = participant_filter_tools.extract_group_names(population)

    # To fill the plotter_skill_value list, first iterate over all skills in outer loop
    for skill_index in range(len(skill_tags)):

        # Next: per skill iterate over all participants ordered by control group in inner loop
        for control_group in control_groups:
            control_group_population = participant_filter_tools \
                .filter_population_by_group(population, control_group)

            # Append the value every participant of the current control group has for the current
            # skill
            plotter_skill_values.append(
                participant_filter_tools.get_skill_values_by_index(control_group_population,
                                                                   skill_index))

    # Finally feed the long list of all skill values in the order, required by the box plotter
    skill_plot_box(plotter_skill_values, palette, len(control_groups),
             "generated-plots/02-cgroups_skills_boxplot.png")
