"""
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects import participant_normalize_tools
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.normalized_participant import NormalizedParticipant
from restify_mining.scatter_plotters.correlation import Correlation
from restify_mining.scatter_plotters.correlation_plotter import plot_correlation, \
    plot_correlation_with_auto_dimensions
from restify_mining.scatter_plotters.extractors.animal_label_maker import AnimalLabelMaker
from restify_mining.scatter_plotters.extractors.full_label_maker import FullLabelMaker
from restify_mining.scatter_plotters.extractors.methodology_time_passrate_tradeoff_extractor \
    import \
    MethodologyTimeToPassRateTradeoffExtractor
from restify_mining.scatter_plotters.extractors.summed_skill_extractor import SummedSkillExtractor
from restify_mining.scatter_plotters.scatter_series import ScatterSeries


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

        skill_to_quality: Correlation = Correlation(norm_population, MethodologyTimeToPassRateTradeoffExtractor(app), SummedSkillExtractor(app), AnimalLabelMaker(), False)
        file_name_marker: str = "16-"
        plot_correlation_with_auto_dimensions(skill_to_quality, file_name_marker)

        # # Compute normalized individual group tradeoffs
        # tradeoffs: list[float] = MethodologyTimeToPassRateTradeoffExtractor(app).extract(norm_population)
        #
        # # Create plots that put normalized population in relation to total skill score of population
        # total_skills: list[int] = SummedSkillExtractor(app).extract(norm_population)
        #
        print("all good.")
