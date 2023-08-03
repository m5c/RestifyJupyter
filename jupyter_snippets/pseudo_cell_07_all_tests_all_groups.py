"""
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.scatter_plotters import unit_test_plotter


def cell_07() -> None:
    """
    Jupyter cell 07. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    # The effective sample set is reduced, so it does not contain outliers (scammers)
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants(True)

    # Visualize test results in 2D plot and safe to disk
    for app in ["bs", "xox"]:
        unit_test_plotter.plot_all_average_group_results(app, assessed_population)
