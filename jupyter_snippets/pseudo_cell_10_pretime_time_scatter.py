"""
This module contains pseudo jupyter cells that were created, but ultimately not used for
publication. Where applicable
the reason is provided as comment in the function description.
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.scatter_plotters.correlation import Correlation
from restify_mining.scatter_plotters.correlation_plotter import plot_correlation
from restify_mining.scatter_plotters.dimension import Dimension
from restify_mining.scatter_plotters.extractors.animal_label_maker import AnimalLabelMaker
from restify_mining.scatter_plotters.extractors.label_maker import LabelMaker
from restify_mining.scatter_plotters.extractors.methodology_pretime_extractor import \
    MethodologyPretimeExtractor
from restify_mining.scatter_plotters.extractors.methodology_time_extractor import \
    MethodologyTimeExtractor


def cell_10() -> None:
    """
    This plot crates x/y correlations between the time participants spent for task preparation (
    familiarization by
    watching video instructions) and quality of the outcome.
    We excluded the plot from the notebook and publication, for there is no noteworthy correlation.
    :return: None
    """
    # the kind of labels we want:
    label_maker: LabelMaker = AnimalLabelMaker()
    # whether we want to override the label list to outliers only
    # outliers: bool = True
    outliers: bool = False

    # Load all participant objects (specifies skills, codename, control-group) from csv file
    # This plot shows all participants, so we include scammers. How,ever they are labeled in the
    # plot.
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants(False)

    # B: TC / IDE: Time spent on task familiarization VS time spent for refactoring
    file_name_marker: str = "10-"
    tc_pre_meth_time_to_refactor_time: Correlation = Correlation(assessed_population,
                                                                 MethodologyPretimeExtractor("tc"),
                                                                 MethodologyTimeExtractor("tc"),
                                                                 label_maker,
                                                                 outliers)

    ide_pre_meth_time_to_refactor_time: Correlation = Correlation(assessed_population,
                                                                  MethodologyPretimeExtractor(
                                                                      "ide"),
                                                                  MethodologyTimeExtractor("ide"),
                                                                  label_maker,
                                                                  outliers)

    dimension: Dimension = tc_pre_meth_time_to_refactor_time.dimension.fuse(
        ide_pre_meth_time_to_refactor_time.dimension)

    # Plot both correlations
    plot_correlation(tc_pre_meth_time_to_refactor_time, file_name_marker, dimension)
    plot_correlation(ide_pre_meth_time_to_refactor_time, file_name_marker, dimension)
