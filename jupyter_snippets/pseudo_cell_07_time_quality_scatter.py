"""
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.correlation import Correlation
from restify_mining.plotters.correlation_plotter import plot_correlation
from restify_mining.plotters.extractors.full_label_maker import FullLabelMaker
from restify_mining.plotters.extractors.label_maker import LabelMaker
from restify_mining.plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.plotters.extractors.methodology_time_extractor import MethodologyTimeExtractor


def cell_07() -> None:
    """
    Jupyter cell 07. See markdown description.
    :return: None
    """
    # the kind of labels we want:
    label_maker: LabelMaker = FullLabelMaker()
    # whether we want to override the label list to outliers only
    outliers: bool = True
    # outliers: bool = False

    # Load all participant objects (specifies skills, codename, control-group) from csv file
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants()

    # Create several correlation bundles for desired metrics and plot them.
    # A: touchcore + ide: Time spent on task VS Quality
    file_name_marker: str = "07-"
    tc_time_quality: Correlation = Correlation(assessed_population,
                                               MethodologyPassrateExtractor("tc"),
                                               MethodologyTimeExtractor("tc"),
                                               label_maker,
                                               outliers)
    ide_time_quality: Correlation = Correlation(assessed_population,
                                                MethodologyPassrateExtractor("ide"),
                                                MethodologyTimeExtractor("ide"),
                                                label_maker,
                                                outliers)

    # Compute the perfect plot dimensions
    plot_dimensions = tc_time_quality.dimension.fuse(ide_time_quality.dimension)

    # Plot both correlations
    plot_correlation(tc_time_quality, file_name_marker, plot_dimensions)
    plot_correlation(ide_time_quality, file_name_marker, plot_dimensions)
