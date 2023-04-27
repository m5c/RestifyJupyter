"""
This module produces a figure for boxplots of group task time time distributions, per application.
It produces two figures, with 4 boxplots each. Every boxplot represents the distribution of a given group.
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.participant_filter_tools import filter_population_by_group
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
    for app in {"bookstore", "xox"}:

        print("Producing Boxplot for " + app)
        # Step 3: We need the sample values, used as input values for the boxplots.
        # We need four lists, for the four groups.
        # We don't produce the four lists of sampling points ourselves, but use an extractor: ApplicationTimeExtractor
        extractor: Extractor = ApplicationTimeExtractor(app)
        red_task_times: list[float] = extractor.extract(red_population)
        green_task_times:  list[float] = extractor.extract(green_population)
        blue_task_times: list[float] = extractor.extract(blue_population)
        yellow_task_times:  list[float] = extractor.extract(yellow_population)

        # Step 4: Finally actually produce the figures, using the four lists with time samples
