"""
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.participant import Participant
from restify_mining.skill_extractors.extract_population_gaussian import extract_population_gaussian
from restify_mining.unit_test_miners.all_participants_all_tests_miner import AllParticipantsAllTestsMiner
from restify_mining.plotters.unit_test_plotter import mine_and_plot


def cell_01() -> None:
    """
    Jupyter cell 01. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    population: list[Participant] = file_load_utils.load_all_participants()

    # Compute, print and save gaussian skill distribution for entire test population to disk.
    extract_population_gaussian(population)
