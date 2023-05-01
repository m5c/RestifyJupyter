"""
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
from restify_mining.scatter_plotters.extractors.methodology_time_passrate_tradeoff_extractor \
    import \
    MethodologyTimeToPassRateTradeoffExtractor
from restify_mining.scatter_plotters.extractors.summed_skill_extractor import SummedSkillExtractor


def cell_16() -> None:
    """
    Jupyter cell 16. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants()

    # Before we construct the tradeoff, we need to normalize the task solving times
    norm_population: list[NormalizedParticipant] = participant_normalize_tools.normalize(
        assessed_population)

    # PASS 1:
    # Use xox branded application time passrate tradeoff extractor for red/yellow, then for
    # green/blue
    app: str = ""
    for app in ["tc", "ide"]:
        skill_to_quality: Correlation = Correlation(norm_population,
                                                    MethodologyTimeToPassRateTradeoffExtractor(app),
                                                    SummedSkillExtractor(app), AnimalLabelMaker(),
                                                    False)
        file_name_marker: str = "16-"
        plot_correlation_with_auto_dimensions(skill_to_quality, file_name_marker)

        # Run pearson test for liner correlation of values:
        tradeoffs: list[float] = MethodologyTimeToPassRateTradeoffExtractor(app).extract(
            norm_population)

        # Create plots that put normalized population in relation to total skill score of population
        total_skills: list[int] = SummedSkillExtractor(app).extract(norm_population)

        # Computed person correlation between values:
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html
        print(
            "Pearson test for linear correlation between submission quality (tradeoff) and "
            "participant skills, " + app + ":")
        res: PearsonRResult = stats.pearsonr(tradeoffs, total_skills)
        print(res)
        print(
            "Note: Linear correlation result (\"statistic\") is only significant if \"pvalue\" is "
            "smaller than 0.05.")
