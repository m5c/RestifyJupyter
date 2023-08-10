"""
This module produces two figures for time and correctness distributions of full entire experiment.
Each figure contains boxplot distributions for every group and every task, as well as
distibutions for combined groups with same methodology/application combination where only the
order differed.
"""
import numpy as np

from csv_tools import file_load_utils
from restify_mining.box_plotters.time_box_plotter import box_plot
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.participant_filter_tools import filter_population_by_group
from restify_mining.markers import group_tint_markers
from restify_mining.scatter_plotters.extractors.extractor import Extractor
from restify_mining.scatter_plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
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
    # groups who did the exact same tasks but in inverted order.
    # I.e. we join red and yellow to an orange group, and we join blue and green to a turquoise
    # group.
    partitioned_population.append(partitioned_population[0] + partitioned_population[3])
    partitioned_population.append(partitioned_population[1] + partitioned_population[2])

    # 2a) Extract times for individual methodologies, then produce plots
    # box_plot(MethodologyTimeExtractor, partitioned_population, "Time [sec]",
    #          "generated-plots/09a-task-time-boxplot")
    # 2b) Extract correctness for individual methodologies, then produce plots
    box_plot(MethodologyPassrateExtractor, partitioned_population, "Test Passrate [%]",
             "generated-plots/09b-task-passrate-boxplot")


def box_plot(extractor_class: Extractor.__class__,
             partitioned_population: list[list[AssessedParticipant]], label_name: str,
             filename: str):
    methodology_times = {}

    # Extract the conversion metric information form participant data.
    for methodology in ["tc", "ide"]:
        extractor: Extractor = extractor_class(methodology)
        methodology_times[methodology] = extract_methodology_metric(
            extractor,
            partitioned_population)

    # Step 4: produce reference point (so that plots have same axis scaling)
    # this also prints numeric stats data to console.
    box_plot(methodology_times["tc"], methodology_times["ide"],
             group_tint_markers.group_tints.values(), label_name, filename)




def extract_methodology_metric(extractor: Extractor,
                               subdivided_population: list[list[AssessedParticipant]]) \
        -> list[list[float]]:
    """
    Consumes subdivisions of the full population and extracts for every subdivision a the sample
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
