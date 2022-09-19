"""
2D plotter module that creates visualizations of test success rates for population / population
subsets and for one or two selected applications.
Inspired by: https://stackoverflow.com/a/7230921
"""
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from restify_mining import participant_filter_tools, participant_stat_tools
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

    group_size: int = participant_stat_tools.extract_control_group_size(assessed_population)

    # use amount per control group to create a "colorized" value grid
    # (colour map has zones, we add an offset to every participant, depending on their control
    # group, so they end up in the right colour map zone).r
    colorized_grid_values: list[list[int]] = patch_colours_for_control_groups(grid_values,
                                                                              group_size)

    # We use  acustom heatmap that indicates group colours:
    # make a color map of fixed colors
    colour_map: ListedColormap = matplotlib.colors.ListedColormap(
        ['black', 'blue', 'black', 'green', 'black', 'red', 'black', 'yellow'])
    plot_unit_test_heatmap(colorized_grid_values, colour_map)


def plot_unit_test_heatmap(grid_values: list[list[int]], colour_map: ListedColormap) -> None:
    """
    Plots a heatmap representation of the unit test success results. Can be used either for
    control groups (average test result) or for individual participants. :param grid_values: 2D
    int array of results. Each cell has value between [0-1], indicating the success rate,
    where 0 is all fail and 1 is all pass. For individual tests and participants the provided
    array should only contain the values 0 and 1.
    See: https://stackoverflow.com/a/33282548
    """
    # Add the 2D heatmap
    plt.imshow(grid_values, cmap=colour_map, interpolation='nearest')

    # Actually show the figure
    plt.show()


def bool_to_int(test_result):
    if test_result:
        return 1
    return 0


def patch_colours_for_control_groups(grid_values: list[list[bool]], control_group_size: int) -> \
        list[list[int]]:
    """
    Adds an integer multiplication (*1, *2, *3, ...) to every value in received grid, to colorize
    values based on control group.
    :param grid_values: 2D bool array. Tells for every participant which tests passed / failed.
    :param control_group_size: tells how many participants exist per control group (needed so
    this method knows the size of each colour zone).
    :return: 2D int array, indicating for every participant if failed (color zone offset+0) or
    passed (colour zone offset +1)
    """
    colourized_grid_values: list[list[int]] = []
    for participant_index, participant_results in enumerate(grid_values):
        colourized_participant_results: list[int] = []
        colour_zone_offset: int = (participant_index // control_group_size) * 2
        for test_index, test_result in enumerate(participant_results):

            # Parse bool test result to 0 (failed) or 1 (passed)
            integer_result = bool_to_int(test_result)
            colourized_participant_results.append(integer_result + colour_zone_offset)
        colourized_grid_values.append(colourized_participant_results)
    return colourized_grid_values
