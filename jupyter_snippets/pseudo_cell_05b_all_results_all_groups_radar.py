"""
Author: Maximilian Schiedermeier
"""

from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.radar_plotters.radar_plotter import RadarPlotter
from restify_mining.unit_test_miners.abstract_miner import AbstractMiner
from restify_mining.unit_test_miners.all_participants_all_tests_miner import \
    AllParticipantsAllTestsMiner


def cell_05b() -> None:
    """
    Jupyter cell 05b. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants()

    # Create a radar plot, where the spokes represent individual tests and the distance from the
    # center the average group success rate.
    RadarPlotter().radar_plot(AllParticipantsAllTestsMiner(), assessed_population)




