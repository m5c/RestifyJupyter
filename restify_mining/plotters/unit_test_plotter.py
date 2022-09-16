"""
2D plotter module that creates visualizations of test success rates for population / population
subsets and for one or two selected applications.
Inspired by: https://stackoverflow.com/a/7230921
"""

import matplotlib.pyplot as plt

from restify_mining.assessed_participant import AssessedParticipant


def plot_all_test_results(assessed_population: list[AssessedParticipant]):
    # Extract covered control groups
    # control_groups: list[str] = participant_filter_tools.extract_group_names(assessed_population)

    # Create 2D array, consisting of all participants (already ordered by control group) and test
    # results for all individual unit tests (both apps, sequential. First all BookStore unit
    # tests, then all Xox unit tests.
    grid_values: list[list[bool]] = []
    for assessed_participant in assessed_population:
        grid_values.append(assessed_participant.all_test_results())
    histogram = convert_to_histogram(grid_values)

    # show histogram, 20 unit tests on x-axis, 28 participants on y-axis
    plot_histogram_grid(histogram[0], histogram[1], 20, 28)


def convert_to_histogram(cellOccurrences: list[list[bool]]) -> list[list[int]]:
    """
    Only works for discrete / integer input values.
    :return pair of histogram values (x and y), in form of a list
    """
    histogram_x: list[int] = []
    histogram_y: list[int] = []

    for participant_tests_index, participant in enumerate(cellOccurrences):
        for test_case_index, test_case in enumerate(participant):
            if test_case:
                histogram_x.append(test_case_index)
                histogram_y.append(participant_tests_index)

    return [histogram_x, histogram_y]


def plot_histogram_grid(histogram_x, histogram_y, x_range, y_range) -> None:
    """
    Grid plot function produces rectangular cells in 2D arrangement. Saturation of each cell
    marks the amount of occurrences for each cell position. Cell position occurrences are provided
    via two input arrays. Every pair of two values at the same position of these input arrays
    counts as an occurrence.
    See: https://matplotlib.org/stable/plot_types/stats/hist2d.html
    And: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.hist2d.html
    """

    # Define the actual values. Should be two arrays of same size. Every pair resulting form
    # values at same index positions counts for an occurrence in the final plot.
    x: list[int] = histogram_x
    y: list[int] = histogram_y

    # Select  2D cells (grid) as plot type
    fig, ax = plt.subplots()

    x_limit = len(x)
    y_limit = len(y)
    # Define range for both axis
    # ax.hist2d(x, y, [len(x), len(y)])
    ax.hist2d(x, y, [x_range, y_range])

    # Define viewport offset if needed - should be same as axis
    ax.set(xlim=(0, x_range-1), ylim=(0, y_range-1))

    plt.show()
