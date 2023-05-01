"""
This module produces a figure for boxplots of group task time time distributions, per application.
It produces two figures, with 4 boxplots each. Every boxplot represents the distribution of a given group.
"""
import numpy as np

from csv_tools import file_load_utils
from restify_mining.box_plotters.time_box_plotter import time_plot_box
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.participant_filter_tools import filter_population_by_group
from restify_mining.markers import group_tint_markers
from restify_mining.scatter_plotters.extractors.application_time_extractor import ApplicationTimeExtractor
from restify_mining.scatter_plotters.extractors.extractor import Extractor


def cell_08a() -> None:
    """
    Jupyter cell 08a. See markdown description.
    :return: None
    """
    # Step 1: Get hold of raw participant data, which we need to do whatever analysis. Divide into groups.
    all_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants()
    red_population: list[AssessedParticipant] = filter_population_by_group(all_population, "red")
    green_population: list[AssessedParticipant] = filter_population_by_group(all_population, "green")
    blue_population: list[AssessedParticipant] = filter_population_by_group(all_population, "blue")
    yellow_population: list[AssessedParticipant] = filter_population_by_group(all_population, "yellow")

    # Step 2: We want two plots, so we iterate over both apps.
    application_task_times = {}
    max_task_time: int = 0
    for app in {"bookstore", "xox"}:

        print("Producing Boxplot for " + app)
        # Step 3: We need the sample values, used as input values for the boxplots.
        # We need four lists, for the four groups.
        # We don't produce the four lists of sampling points ourselves, but use an extractor: ApplicationTimeExtractor
        extractor: Extractor = ApplicationTimeExtractor(app)
        all_task_times: list[list[float]] = []
        all_task_times.append(extractor.extract(red_population))
        all_task_times.append(extractor.extract(green_population))
        all_task_times.append(extractor.extract(blue_population))
        all_task_times.append(extractor.extract(yellow_population))

        # Store value
        application_task_times[app] = all_task_times

        # Update hicore
        for group_task_times in all_task_times:
            max_task_time = max(max_task_time, max(group_task_times))

    # Step 4: produce reference point (so that plots have same axis scaling)
    for app in {"bookstore", "xox"}:

        # Step 4: Finally actually produce the figures, using the four lists with time samples
        time_plot_box(application_task_times[app], group_tint_markers.group_tints.values(), max_task_time, "generated-plots/08a-task-time-boxplot-"+app)