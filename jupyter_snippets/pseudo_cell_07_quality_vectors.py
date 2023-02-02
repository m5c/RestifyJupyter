"""
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.correlation import Correlation
from restify_mining.plotters.correlation_plotter import plot_correlation
from restify_mining.plotters.extractors.bs_passrate_extractor import BsPassrateExtractor
from restify_mining.plotters.extractors.bs_time_extractor import BsTimeExtractor


def cell_07() -> None:
    """
    Jupyter cell 07. See markdown description.
    :return: None
    """

    # Load all participant objects (specifies skills, codename, control-group) from csv file
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants()

    # Create a correlation bundle for the desired metrics
    bs_time_quality: Correlation = Correlation(assessed_population, BsTimeExtractor(),
                                               BsPassrateExtractor(), True)

    # Create the group bundle (sample points bundled by control groups)
    plot_correlation(bs_time_quality)