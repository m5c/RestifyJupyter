"""
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.correlation import Correlation
from restify_mining.plotters.correlation_plotter import plot_correlation
from restify_mining.plotters.extractors.animal_label_maker import AnimalLabelMaker
from restify_mining.plotters.extractors.label_maker import LabelMaker
from restify_mining.plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.plotters.extractors.methodology_pretime_extractor import \
    MethodologyPretimeExtractor


def cell_08() -> None:
    """
    Jupyter cell 07. See markdown description.
    :return: None
    """
    # the kind of labels we want:
    label_maker: LabelMaker = AnimalLabelMaker()
    # whether we want to override the label list to outliers only
    # outliers: bool = True
    outliers: bool = False

    # Load all participant objects (specifies skills, codename, control-group) from csv file
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants()

    # C: Time spent on task familiarization VS quality of individual application refactorings
    file_name_marker: str = "08-"
    tc_pass_rate_to_pre_meth_time: Correlation = Correlation(assessed_population,

                                                             MethodologyPassrateExtractor("tc"),
                                                             MethodologyPretimeExtractor("tc"),
                                                             label_maker,
                                                             outliers)

    ide_pass_rate_to_pre_meth_time: Correlation = Correlation(assessed_population,
                                                              MethodologyPassrateExtractor("ide"),
                                                              MethodologyPretimeExtractor("ide"),
                                                              label_maker,
                                                              outliers)

    # Compute the perfect plot dimensions
    plot_dimensions = tc_pass_rate_to_pre_meth_time.dimension.fuse(
        ide_pass_rate_to_pre_meth_time.dimension)

    # Plot both correlations
    plot_correlation(tc_pass_rate_to_pre_meth_time, file_name_marker, plot_dimensions)
    plot_correlation(ide_pass_rate_to_pre_meth_time, file_name_marker, plot_dimensions)

    # D: Impact of specific skills on time / quality (better app or better methodology based?)
