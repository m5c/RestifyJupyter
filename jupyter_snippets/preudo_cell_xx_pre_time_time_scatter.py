"""
This plot was prepared but not used for publication, for we could not identify any noteworthy
correlation in the plot.
Apart from one participant who was a scammer, we did not note any significant impact of the
preparation time on task solving time and quality of the outcome.
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.correlation import Correlation
from restify_mining.plotters.correlation_plotter import plot_correlation
from restify_mining.plotters.dimension import Dimension
from restify_mining.plotters.extractors.animal_label_maker import AnimalLabelMaker
from restify_mining.plotters.extractors.label_maker import LabelMaker
from restify_mining.plotters.extractors.methodology_pretime_extractor import \
    MethodologyPretimeExtractor
from restify_mining.plotters.extractors.methodology_time_extractor import MethodologyTimeExtractor


def cell_0x() -> None:
    """
    Jupyter cell 0X. See markdown description.
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

    # B: TC / IDE: Time spent on task familiarization VS time spent for refactoring
    file_name_marker: str = "07-B-"
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
