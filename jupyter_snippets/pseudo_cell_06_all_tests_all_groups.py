"""
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters import unit_test_plotter


def cell_06() -> None:
    """
    Jupyter cell 06. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants()

    # Visualize test results in 2D plot and safe to disk
    unit_test_plotter.plot_all_average_group_results(assessed_population)
