"""
This module allows comparison of methodology fitness for a task by comparing the results of half
the total population to the remainder.
Example: Compare Xox IDE and Xox TouchCORE. Compare the two groups who solved Xox using IntelliJ
to the two groups who solved Xox using TouchCORE.
The metric for fittness is the time to quality ratio. That is to say fast solving with few
mistakes is considered better than slow solving with many mistakes.
Author: Maximilian Schiedermeier
"""
import scipy
from scipy.stats._morestats import ShapiroResult

from csv_tools import file_load_utils
from restify_mining.data_objects import participant_normalize_tools
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.normalized_participant import NormalizedParticipant
from restify_mining.data_objects.participant_filter_tools import filter_population_by_group
from restify_mining.scatter_plotters.extractors.application_time_passrate_tradeoff_extractor \
    import \
    ApplicationTimeToPassRateTradeoffExtractor
from restify_mining.utils.shapiro_interpreter import print_normal_dist_interpretation


def cell_12() -> None:
    """
    Jupyter cell 12. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants()

    # Before we construct the tradeoff, we need to normalize the task solving times
    norm_population: list[NormalizedParticipant] = participant_normalize_tools.normalize(
        assessed_population)

    # In a first step we compute the effective methodology fittness. We do not use a dedicated
    # extractor for this, because extractors are meant for combination. We are not interested
    # in a scatter here, but comparison of resulting normal distributions.
    # First divide the population into two subsets, where each subset combined the participants
    # of two control groups with the same task-methodology combination.
    green_blue_norm_population: list[NormalizedParticipant] = filter_population_by_group(
        norm_population, "green") + filter_population_by_group(norm_population, "blue")
    red_yellow_norm_population: list[NormalizedParticipant] = filter_population_by_group(
        norm_population, "red") + filter_population_by_group(norm_population, "yellow")

    # PASS 1:
    # Use xox branded application time passrate tradeoff extractor for red/yellow, then for
    # green/blue
    app: str = ""
    for app in ["xox", "bookstore"]:
        # compute effective quality to duration tradeoff for both subpopulations. green blue was
        # using touchcore (to refactor xox), if we extract for xox we get the touchcore results.
        green_blue_app_tradeoff: list[float] = ApplicationTimeToPassRateTradeoffExtractor(
            app).extract(
            green_blue_norm_population)
        # red yellow was using ide for xox, if we extract for xox we get the ide results
        red_yellow_app_tradeoff: list[float] = ApplicationTimeToPassRateTradeoffExtractor(
            app).extract(
            red_yellow_norm_population)

        # Run Shapiro-Wilk test on resulting tradeoffs (each group individually), to see if
        # distributions are normal
        # If they are, draw normalized curves for the four control groups. Also print mean /
        # deviation per group.
        green_blue_app_tradeoff_stats: ShapiroResult = scipy.stats.shapiro(green_blue_app_tradeoff)
        print_normal_dist_interpretation("Green Blue Normalized " + app + " Quality Tradeoff",
                                         green_blue_app_tradeoff_stats)
        red_yellow_app_tradeoff: ShapiroResult = scipy.stats.shapiro(red_yellow_app_tradeoff)
        print_normal_dist_interpretation("Green Blue Normalized " + app + " Quality Tradeoff",
                                         red_yellow_app_tradeoff)

    # Shapiro wilk test suggests the data is normal distributed. We therefore proceed with plot
    # of normal distributions for each series.
