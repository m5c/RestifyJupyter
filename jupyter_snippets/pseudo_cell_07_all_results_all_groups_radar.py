"""
Author: Maximilian Schiedermeier
"""

from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.radar_plotters.radar_plotter import RadarPlotter
from restify_mining.unit_test_miners.all_groups_tests_miner import AllGroupsTestsMiner


def cell_07() -> None:
    """
    Jupyter cell 07. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    # The effective sample set is reduced, so it does not contain outliers (scammers)
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants(True)

    # Create a radar plot, where the spokes represent individual tests and the distance from the
    # center the average group success rate.
    for app in ["xox", "bs"]:
        RadarPlotter().radar_plot(AllGroupsTestsMiner(app), app, assessed_population)
