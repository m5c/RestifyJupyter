"""
This module produces a figure for boxplots of group task time distributions, for both application.
It produces one figures, with 8 boxplots each. Every boxplot represents the distribution of a
given group.
"""
import numpy as np

from csv_tools import file_load_utils
from restify_mining.box_plotters.time_box_plotter import time_plot_box
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.participant_filter_tools import filter_population_by_group
from restify_mining.markers import group_tint_markers
from restify_mining.scatter_plotters.extractors.extractor import Extractor
from restify_mining.scatter_plotters.extractors.methodology_time_extractor import \
    MethodologyTimeExtractor


def cell_09() -> None:
    """
    Jupyter cell 08a. See markdown description.
    :return: None
    """
    # Step 1: Get hold of raw participant data, which we need to do whatever analysis. Divide
    # into groups.
    # The effective sample set is reduced, so it does not contain outliers (scammers)
    all_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants(True)
    red_population: list[AssessedParticipant] = filter_population_by_group(all_population, "red")
    green_population: list[AssessedParticipant] = filter_population_by_group(all_population,
                                                                             "green")
    blue_population: list[AssessedParticipant] = filter_population_by_group(all_population, "blue")
    yellow_population: list[AssessedParticipant] = filter_population_by_group(all_population,
                                                                              "yellow")

    # Step 2: Extract times for individual apps
    application_task_times = {}
    for methodology in {"tc", "ide"}:

        extractor: Extractor = MethodologyTimeExtractor(methodology)
        all_task_times: list[list[float]] = []
        all_task_times.append(extractor.extract(red_population))
        all_task_times.append(extractor.extract(green_population))
        all_task_times.append(extractor.extract(blue_population))
        all_task_times.append(extractor.extract(yellow_population))
        application_task_times[methodology] = all_task_times

        print("Conversion time for " + methodology + " task, red/green/blue/yellow in seconds: ")
        for item in all_task_times:
            print(str(np.mean(item)))

    # Step 4: produce reference point (so that plots have same axis scaling)
    time_plot_box(application_task_times["tc"], application_task_times["ide"],
                  group_tint_markers.group_tints.values(), "generated-plots/09-task-time-boxplot")
