"""
This module produces two figures for time and correctness distributions of full entire experiment.
Each figure contains boxplot distributions for every group and every task, as well as
distibutions for combined groups with same methodology/application combination where only the
order differed.
"""
import numpy as np

from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.participant_filter_tools import filter_population_by_group
from restify_mining.markers import group_tint_markers
from restify_mining.box_plotters.generic_box_plotter import graphical_box_plot
from restify_mining.scatter_plotters.extractors.extractor import Extractor
from restify_mining.scatter_plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.scatter_plotters.extractors.methodology_time_extractor import \
    MethodologyTimeExtractor

include_fused: bool = True


def cell_10() -> None:
    """
    Jupyter cell 10. See markdown description.
    :return: None
    """

    # Step 1: Get hold of raw participant data, which we need to do whatever analysis. Divide
    # into groups.
    # The effective sample set is reduced, so it does not contain outliers (scammers)
    partitioned_population: list[list[AssessedParticipant]] = partition_population()

    # 2a) Extract times for individual methodologies, then produce plots
    box_plot(MethodologyTimeExtractor, partitioned_population, "Time [sec]",
             "generated-plots/10a-task-time-boxplot")
    # 2b) Extract correctness for individual methodologies, then produce plots
    box_plot(MethodologyPassrateExtractor, partitioned_population, "Test Passrate [%]",
             "generated-plots/10b-task-passrate-boxplot")


def partition_population() -> list[list[AssessedParticipant]]:
    """
    Creates a list of list where every outer list represents participants of a group. The outcome
    has 6 entries, the last two ones each representing the fused participants of previous groups
    with matching tasks (only order different). The inner list entries are the assessed
    participant objects. The partitioned population has the scammer(s) already filtered.
    """
    all_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants(True)

    partitioned_population: list[list[AssessedParticipant]] = [
        filter_population_by_group(all_population, "red"),
        filter_population_by_group(all_population, "green"),
        filter_population_by_group(all_population, "blue"),
        filter_population_by_group(all_population, "yellow")]

    # We also are interested in "fused" participant sets, each of which represents the union of
    # groups who did the exact same tasks but in inverted order.
    # I.e. we join red and yellow to an orange group, and we join blue and green to a turquoise
    # group.
    partitioned_population.append(partitioned_population[0] + partitioned_population[3])
    partitioned_population.append(partitioned_population[1] + partitioned_population[2])

    return partitioned_population


def box_plot(extractor_class: Extractor.__class__,
             partitioned_population: list[list[AssessedParticipant]], label_name: str,
             filename: str):
    methodology_metric = {}

    # Extract the conversion metric information from participant data.
    for methodology in ["tc", "ide"]:
        extractor: Extractor = extractor_class(methodology)
        methodology_metric[methodology] = extract_methodology_metric(
            extractor,
            partitioned_population)

    # Step 4: produce reference point (so that plots have same axis scaling)
    # this also prints numeric stats data to console.
    graphical_box_plot(methodology_metric["tc"], methodology_metric["ide"], include_fused,
                       group_tint_markers.group_tints.values(), label_name, filename)


def extract_methodology_metric(extractor: Extractor,
                               subdivided_population: list[list[AssessedParticipant]]) \
        -> list[list[float]]:
    """
    Consumes subdivisions of the full population and extracts for every subdivision the sample
    values of interest.
    :return: ..
    """
    all_extracted: list[list[float]] = []
    for index in range(0, len(subdivided_population)):
        all_extracted.append(extractor.extract(subdivided_population[index]))

    # print stats
    print(extractor.filename_segment() + " for red/green/blue/yellow/orange/turquoise "
                                         "in " + extractor.axis_label())
    for item in all_extracted:
        print(str(np.mean(item)))

    # return extracted values
    return all_extracted
