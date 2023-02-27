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

    # retrieve all time values for manual refactoring duration of bookstore, test if normal distributed
    red_group: list[AssessedParticipant] = participant_filter_tools.filter_population_by_group(assessed_population,
                                                                                               "red")
    green_group: list[AssessedParticipant] = participant_filter_tools.filter_population_by_group(assessed_population,
                                                                                               "green")
    blue_group: list[AssessedParticipant] = participant_filter_tools.filter_population_by_group(assessed_population,
                                                                                               "blue")
    yellow_group: list[AssessedParticipant] = participant_filter_tools.filter_population_by_group(assessed_population,
                                                                                               "yellow")

    # Create pairs of groups to extract time values. Each pair has a common app+methodology tuple.
    tc_bs_times: list[int] = []
    ide_xox_times: list[int] = []
    tc_xox_times: list[int] = []
    ide_bs_times:  list[int] = []

    # Red and yellow are identical except for task order
    for participant in red_group:
        tc_bs_times.append(participant.time_bs)
        ide_xox_times.append(participant.time_xox)
    for participant in yellow_group:
        tc_bs_times.append(participant.time_bs)
        ide_xox_times.append(participant.time_xox)

    # Green and blue are identical except for task order
    for participant in green_group:
        ide_bs_times.append(participant.time_bs)
        tc_xox_times.append(participant.time_xox)
    for participant in blue_group:
        ide_bs_times.append(participant.time_bs)
        tc_xox_times.append(participant.time_xox)

    # Run shapiro test for normal distribution
    tc_bs_stats = scipy.stats.shapiro(tc_bs_times)
    print(tc_bs_stats)
    ide_xox_stats = scipy.stats.shapiro(ide_xox_times)
    print(ide_xox_stats)
    ide_bs_stats = scipy.stats.shapiro(tc_xox_times)
    print(ide_bs_stats)
    tc_xox_stats = scipy.stats.shapiro(ide_bs_times)
    print(tc_xox_stats)
