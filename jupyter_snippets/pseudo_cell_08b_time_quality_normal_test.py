"""
Author: Maximilian Schiedermeier
"""
import scipy.stats

from csv_tools import file_load_utils
from restify_mining.data_objects import participant_filter_tools
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.extractors.full_label_maker import FullLabelMaker
from restify_mining.plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.plotters.extractors.methodology_time_extractor import MethodologyTimeExtractor
from restify_mining.plotters.scatter_series import ScatterSeries
from restify_mining.skill_extractors import participant_stat_tools


def cell_08b() -> None:
    """
    Jupyter cell 07. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants()

    # retrieve subgroups, so we can easily form groups of interests for value extraction
    # There is always two groups who share a common methodology and application.

    # retrieve all time values for manual refactoring duration of bookstore, test if normal
    # distributed
    red_group: list[AssessedParticipant] = participant_filter_tools.filter_population_by_group(
        assessed_population,
        "red")
    green_group: list[AssessedParticipant] = participant_filter_tools.filter_population_by_group(
        assessed_population,
        "green")
    blue_group: list[AssessedParticipant] = participant_filter_tools.filter_population_by_group(
        assessed_population,
        "blue")
    yellow_group: list[AssessedParticipant] = participant_filter_tools.filter_population_by_group(
        assessed_population,
        "yellow")

    # Create pairs of groups to extract time values. Each pair has a common app+methodology tuple.
    tc_bs_times: list[int] = []
    tc_bs_rates: list[float] = []
    ide_xox_times: list[int] = []
    ide_xox_rates: list[float] = []
    tc_xox_times: list[int] = []
    tc_xox_rates: list[float] = []
    ide_bs_times: list[int] = []
    ide_bs_rates: list[int] = []

    # Red and yellow are identical except for task order
    for participant in red_group + yellow_group:
        tc_bs_times.append(participant.time_bs)
        tc_bs_rates.append(participant.test_percentage_bs)
        ide_xox_times.append(participant.time_xox)
        ide_xox_rates.append(participant.test_percentage_xox)

    # Green and blue are identical except for task order
    for participant in green_group + blue_group:
        ide_bs_times.append(participant.time_bs)
        ide_bs_rates.append(participant.test_percentage_bs)
        tc_xox_times.append(participant.time_xox)
        tc_xox_rates.append(participant.test_percentage_xox)

    # Run shapiro test for normal distribution
    tc_bs_time_stats = scipy.stats.shapiro(tc_bs_times)
    tc_bs_rates_stats = scipy.stats.shapiro(tc_bs_rates)
    print_normal_dist_interpretation(
        "TC BookStore duration", tc_bs_time_stats.pvalue)
    print_normal_dist_interpretation(
        "TC BookStore quality", tc_bs_rates_stats.pvalue)

    ide_xox_time_stats = scipy.stats.shapiro(ide_xox_times)
    ide_xox_rates_stats = scipy.stats.shapiro(ide_xox_rates)
    print_normal_dist_interpretation(
        "IDE Xox duration", ide_xox_time_stats.pvalue)
    print_normal_dist_interpretation(
        "IDE Xox quality", ide_xox_rates_stats.pvalue)

    ide_bs_time_stats = scipy.stats.shapiro(tc_xox_times)
    ide_bs_rates_stats = scipy.stats.shapiro(tc_xox_rates)
    print_normal_dist_interpretation(
        "IDE BookStore duration", ide_bs_time_stats.pvalue)
    print_normal_dist_interpretation(
        "IDE BookStore quality", ide_bs_rates_stats.pvalue)

    tc_xox_time_stats = scipy.stats.shapiro(ide_bs_times)
    tc_xox_rates_stats = scipy.stats.shapiro(ide_bs_rates)
    print_normal_dist_interpretation(
        "TC Xox duration", tc_xox_time_stats.pvalue)
    print_normal_dist_interpretation(
        "TC Xox duration", tc_xox_rates_stats.pvalue)


def print_normal_dist_interpretation(context: str, pvalue: float) -> None:
    """
    Herper function to print p value and interpretation for a given context.
    :param context: as descriptive string to use when printing message.
    :param pvalue: as the p-value for null hypothesis that samples come from normal
    distribution.
    :return: None.
    """
    if pvalue >= 0.05:
        interpretation: str = "\nCannot reject Null-Hypothesis. Found no evidence to assume " \
                              "the samples could not come from a normal distribution."
    else:
        interpretation: str = "\nNull-Hypothesis rejected. Data suggests the samples do not " \
                              "come from a normal distribution."
    print("------\np-value for " + context + ": " + str(pvalue) + interpretation)
