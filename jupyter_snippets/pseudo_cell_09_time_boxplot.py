"""
This module produces two figures for time and correctness distributions of full entire experiment.
Each figure contains boxplot distributions for every group and every task, as well as
distibutions for combined groups with same methodology/application combination where only the
order differed.
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
    Jupyter cell 09. See markdown description.
    :return: None
    """
    # Step 1: Get hold of raw participant data, which we need to do whatever analysis. Divide
    # into groups.
    # The effective sample set is reduced, so it does not contain outliers (scammers)
    all_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants(True)
    partitioned_population: list[list[AssessedParticipant]] = [
        filter_population_by_group(all_population, "red"),
        filter_population_by_group(all_population, "green"),
        filter_population_by_group(all_population, "blue"),
        filter_population_by_group(all_population, "yellow")]

    # We also are interested in "fused" participant sets, each of which represents the union of
    # groups who
    # did the exact same tasks but in inverted order.
    # I.e. we join red and yellow to an orange group, and we join blue and green to a turquoise
    # group.
    partitioned_population.append(partitioned_population[0] + partitioned_population[3])
    partitioned_population.append(partitioned_population[1] + partitioned_population[2])

    # Step 2: Extract times and success rates for individual methodologies.
    # The produced dictionaries each hold two entries, one per methodology.
    application_task_times = {}
    for methodology in ["tc", "ide"]:
        # We extract to a list of lists: outer list entries represent the 6 groups (4 original +
        # 2 fused groups), inner entries the individual participants.
        extractor: Extractor = MethodologyTimeExtractor(methodology)
        application_task_times[methodology] = extract_methodology_metric(extractor,
                                                                         partitioned_population)

        print(
            "Conversion time for " + methodology + " task, red/green/blue/yellow/orange/turquoise "
                                                   "in seconds: ")
        for item in application_task_times[methodology]:
            print(str(np.mean(item)))

    # Step 4: produce reference point (so that plots have same axis scaling)
    time_plot_box(application_task_times["tc"], application_task_times["ide"],
                  group_tint_markers.group_tints.values(), "generated-plots/09-task-time-boxplot")


def extract_methodology_metric(extractor: Extractor,
                               subdivided_population: list[list[AssessedParticipant]]) \
        -> list[list[float]]:
    """
    Consumes subdivisions of the full population and extracts for every subdivision a the sample
    values of interest.
    :return: ..
    """
    all_task_times: list[list[float]] = []
    for index in range(0, len(subdivided_population)):
        all_task_times.append(extractor.extract(subdivided_population[index]))
    return all_task_times
