"""
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.correlation import Correlation
from restify_mining.plotters.correlation_plotter import plot_correlation
from restify_mining.plotters.extractors.animal_label_maker import AnimalLabelMaker
from restify_mining.plotters.extractors.application_passrate_extractor import \
    ApplicationPassRateExtractor

from restify_mining.plotters.extractors.methodology_passrate_extractor import \
    MethodologyPassrateExtractor
from restify_mining.plotters.extractors.methodology_pretime_extractor import \
    MethodologyPretimeExtractor
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
    # A: BookStore + Xox: Time spent on task VS Quality
    file_name_marker: str = "07-A-"
    bs_time_quality: Correlation = Correlation(assessed_population,
                                               ApplicationPassRateExtractor("bookstore"),
                                               ApplicationTimeExtractor("bookstore"),
                                               AnimalLabelMaker(),
                                               True)
    plot_correlation(bs_time_quality, file_name_marker)
    xox_time_quality: Correlation = Correlation(assessed_population,
                                                ApplicationPassRateExtractor("xox"),
                                                ApplicationTimeExtractor("xox"),
                                                AnimalLabelMaker(),
                                                True)
    plot_correlation(xox_time_quality, file_name_marker)

    # B: TC / IDE: Time spent on task familiarization VS time spent for refactoring
    file_name_marker: str = "07-B-"
    tc_pre_meth_time_to_refactor_time: Correlation = Correlation(assessed_population,
                                                                 MethodologyPretimeExtractor("tc"),
                                                                 MethodologyTimeExtractor("tc"),
                                                                 AnimalLabelMaker(
                                                                 ),
                                                                 True)
    plot_correlation(tc_pre_meth_time_to_refactor_time, file_name_marker)

    ide_pre_meth_time_to_refactor_time: Correlation = Correlation(assessed_population,
                                                                  MethodologyPretimeExtractor(
                                                                      "ide"),
                                                                  MethodologyTimeExtractor("ide"),
                                                                  AnimalLabelMaker(
                                                                  ),
                                                                  True)
    plot_correlation(ide_pre_meth_time_to_refactor_time, file_name_marker)

    # C: Time spent on task familiarization VS quality of individual application refactorings
    file_name_marker: str = "07-C-"
    tc_pre_meth_time_to_pass_rate: Correlation = Correlation(assessed_population,
                                                             MethodologyPretimeExtractor("tc"),
                                                             MethodologyPassrateExtractor("tc"),
                                                             AnimalLabelMaker(),
                                                             True)
    plot_correlation(tc_pre_meth_time_to_pass_rate, file_name_marker)

    ide_pre_meth_time_to_pass_rate: Correlation = Correlation(assessed_population,
                                                              MethodologyPretimeExtractor("ide"),
                                                              MethodologyPassrateExtractor("ide"),
                                                              AnimalLabelMaker(),
                                                              True)
    plot_correlation(ide_pre_meth_time_to_pass_rate, file_name_marker)

    # D: Impact of specific skills on time / quality (better app or better methodology based?)
