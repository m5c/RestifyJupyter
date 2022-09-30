"""
Jupyter pseudo module to plot a 2D grid with all unit test results of all participants.
"""

from csv_tools import file_load_utils
from restify_mining.assessed_participant import AssessedParticipant
from restify_mining.miners.all_participants_all_tests_miner import AllParticipantsAllTestsMiner
from restify_mining.plotters.unit_test_plotter import mine_and_plot

# Load all participant objects (specifies skills, codename, control-group) from csv file
assessed_population: list[AssessedParticipant] = file_load_utils.load_all_assessed_participants()

# Create a 2D plot of all individual participant test results. On Y axis (vertical) all
# participants, on X axis (horizontal) all unit tests. Created image shows a black square for
# failed tests, coloured square (matching control group colour) for passed tests.
with_colours: bool = True
mine_and_plot(AllParticipantsAllTestsMiner(), with_colours, assessed_population)
