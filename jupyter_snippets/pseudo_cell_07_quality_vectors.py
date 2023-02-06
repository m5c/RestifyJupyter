"""
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.correlation import Correlation
from restify_mining.plotters.correlation_plotter import plot_correlation
from restify_mining.plotters.extractors.application_passrate_extractor import ApplicationPassRateExtractor
from restify_mining.plotters.extractors.methodology_pretime_extractor import MethodologyPretimeExtractor
from restify_mining.plotters.extractors.application_time_extractor import ApplicationTimeExtractor
from restify_mining.plotters.extractors.methodology_time_extractor import MethodologyTimeExtractor


def cell_07() -> None:
    """
    Jupyter cell 07. See markdown description.
    :return: None
    """

    # Load all participant objects (specifies skills, codename, control-group) from csv file
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants()

    # Create several correlation bundles for desired metrics and plot them.
    # A: BookStore + Xox: Time VS Quality
    file_name_marker: str = "07-A-"
    bs_time_quality: Correlation = Correlation(assessed_population,
                                               ApplicationPassRateExtractor("bookstore"),
                                               ApplicationTimeExtractor("bookstore"), True)
    plot_correlation(bs_time_quality, file_name_marker)
    xox_time_quality: Correlation = Correlation(assessed_population,
                                                ApplicationPassRateExtractor("xox"),
                                                ApplicationTimeExtractor("xox"),
                                                True)
    plot_correlation(xox_time_quality, file_name_marker)

    # B: Time spent on task familiarization VS time spent for individual application refactorings
    file_name_marker: str = "07-B-"
    tc_pretasktime_tasktime: Correlation = Correlation(assessed_population,
                                                    MethodologyPretimeExtractor("tc"),
                                                    MethodologyTimeExtractor("tc"),
                                                    False)
    plot_correlation(tc_pretasktime_tasktime, file_name_marker)

    ide_pretasktime_tasktime: Correlation = Correlation(assessed_population,
                                                    MethodologyPretimeExtractor("ide"),
                                                    MethodologyTimeExtractor("ide"),
                                                    False)
    plot_correlation(ide_pretasktime_tasktime, file_name_marker)

    # B: Time spent on task familiarization VS quality of individual application refactorings
    file_name_marker: str = "07-C-"
    # 2x more... Do the same with quality...
