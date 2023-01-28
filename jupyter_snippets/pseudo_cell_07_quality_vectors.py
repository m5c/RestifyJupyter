"""
Author: Maximilian Schiedermeier
"""
from csv_tools import file_load_utils
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.correlation_plotter import plot_correlation
from restify_mining.quality_extractors.extract_unit_pass_rate import extract_unit_pass_rates_bs, \
    extract_refactor_times_bs


def cell_07() -> None:
    """
    Jupyter cell 07. See markdown description.
    :return: None
    """
    print("Yayyy")

    # Load all participant objects (specifies skills, codename, control-group) from csv file
    assessed_population: list[
        AssessedParticipant] = file_load_utils.load_all_assessed_participants()

    # Use correctness rate and time required per app and participant to draw a plot / tendency
    # vector. Actually draw two plots, one per app. Colourize the dots according to the group.
    # Sample, call like this:

    # Get all time values for manual refactoring task from participants
    x_axis_values = extract_unit_pass_rates_bs(assessed_population)
    y_axis_values = extract_refactor_times_bs(assessed_population)
    plot_correlation(x_axis_values, y_axis_values, "Tests passed (%)", "Refactoring time (s)")
