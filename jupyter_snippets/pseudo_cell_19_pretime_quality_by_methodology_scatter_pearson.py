"""
Pseudo Cell to computes Pearson Coefficient for linear correlation between pre time and
effectiveness of refactoring per methodology.
Author: Maximilian Schiedermeier
"""
from scipy.stats import stats
from scipy.stats._stats_py import PearsonRResult

from csv_tools import file_load_utils
from restify_mining.data_objects import participant_normalize_tools
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.normalized_participant import NormalizedParticipant
from restify_mining.scatter_plotters.correlation import Correlation
from restify_mining.scatter_plotters.correlation_plotter import \
    plot_correlation_with_auto_dimensions
from restify_mining.scatter_plotters.extractors.animal_label_maker import AnimalLabelMaker
from restify_mining.scatter_plotters.extractors.methodology_pretime_extractor import \
    MethodologyPretimeExtractor
from restify_mining.scatter_plotters.extractors.methodology_time_passrate_tradeoff_extractor \
    import \
    MethodologyTimeToPassRateTradeoffExtractor
from restify_mining.scatter_plotters.extractors.summed_skill_extractor import SummedSkillExtractor


def cell_19() -> None:
    """
    Jupyter cell 19. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    # Aggregated analysis, so we exclude outliers
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants(True)

    # Before we construct the tradeoff, we need to normalize the task solving times
    norm_population: list[NormalizedParticipant] = participant_normalize_tools.normalize(
        assessed_population)

    # PASS 1:
    # Use app branded application time passrate tradeoff extractor for red/yellow, then for
    # green/blue
    methodology: str = ""
    for methodology in ["tc", "ide"]:
        # Run pearson test for liner correlation of values:
        tradeoffs: list[float] = MethodologyTimeToPassRateTradeoffExtractor(methodology).extract(
            norm_population)

        # Create tests that put normalized population effectiveness in relation to pretime of
        # population
        pre_times: list[int] = MethodologyPretimeExtractor(methodology).extract(norm_population)

        # Computed person correlation between values:
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html
        print(
            "Pearson test for linear correlation between submission quality (tradeoff) and "
            "methodology pre-time, " + methodology + ":")
        res: PearsonRResult = stats.pearsonr(tradeoffs, pre_times)
        print(res)
        print(
            "Note: Linear correlation result (\"statistic\") is only significant if \"pvalue\" is "
            "smaller than 0.05")
