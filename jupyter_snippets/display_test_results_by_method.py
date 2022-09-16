"""
Jupyter pseudo module to plot a2D grid with all unit test results of all participants.
"""

from csv_tools import file_load_utils
from restify_mining.assessed_participant import AssessedParticipant
from restify_mining.plotters import unit_test_plotter

# Load all participant objects (specifies skills, codename, control-group) from csv file
assessed_population: list[AssessedParticipant] = file_load_utils.load_all_assessed_participants()

# Visualize test results in 2D plot
unit_test_plotter.plot_all_test_results(assessed_population)
# unit_test_plotter.plot_grid()
