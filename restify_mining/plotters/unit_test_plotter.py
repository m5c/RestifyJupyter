"""
2D plotter module that creates visualizations of test success rates for population / population
subsets and for one or two selected applications.
Inspired by: https://stackoverflow.com/a/7230921
"""
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.unit_test_miners.all_groups_all_tests_miner import AllGroupsAllTestsMiner
from restify_mining.unit_test_miners.abstract_miner import AbstractMiner


def plot_all_average_group_results(population: list[AssessedParticipant]) -> None:
    """
    Creates a 2D plot of all individual participant test results. On Y axis (vertical) all
    participants, on X axis (horizontal) all unit tests. Created image shows a black square for
    failed tests, coloured square (matching control group colour) for passed tests.
    :param population: as the list of assessed participants.
    """
    mine_and_plot(AllGroupsAllTestsMiner(), True, population)


def build_linear_colour_map(with_control_groups: bool) -> LinearSegmentedColormap:
    """
    https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html
    Search for: "Directly creating a segmented colormap from a list"
    :return: The only kind of colormap that is actually useful. Produces gradients based on
    sample points.
    """
    if with_control_groups:
        list_colours: list[str] = ["black", "red", "black", "green", "black", "blue", "black",
                                   "yellow"]
    else:
        list_colours: list[str] = ["black", "white"]
    return LinearSegmentedColormap.from_list("mycmap", list_colours)


def mine_and_plot(miner: AbstractMiner, with_colours: bool, population: list[AssessedParticipant]):
    """
    Create 2D array, consisting of all participants (already ordered by control group) and test
    results for all individual unit tests (both apps, sequential. First all BookStore unit
    tests, then all Xox unit tests.
    :param miner: as the mining algorithm implementation to apply
    :param with_colours: true or false flag, indicated whether the output plot should highlight
    control groups
    :param population: as the population for which the plotter prints results
    """
    grid_values: list[list[float]] = miner.mine(population)

    # Enable group colour space if requested
    colour_map: ListedColormap
    if with_colours:
        # Look up amount of participants per control group, so we can tint the map by zones.
        group_zone_size: int = miner.colour_zone_size(population)

        # We use a custom heatmap that indicates group colours:
        # make a color map of fixed colors
        # colour_map: ListedColormap = matplotlib.colors.ListedColormap(
        #     ['black', 'blue', 'black', 'green', 'black', 'red', 'black', 'yellow'])
        colour_map: LinearSegmentedColormap = build_linear_colour_map(with_colours)

        # use amount per control group to create a "colorized" value grid
        # (colour map has zones, we add an offset to every participant, depending on their control
        # group, so they end up in the right colour map zone).
        grid_values: list[list[int]] = patch_control_group_colours(grid_values, group_zone_size)
    else:
        # If no colours are required, there is only one colour zone that is applied on all
        # participants
        group_zone_size = len(population)

        # Also if groups need not be indicates, the heatmap is greyscale only
        # colour_map: ListedColormap = matplotlib.colors.ListedColormap(['black', 'white'])
        colour_map: LinearSegmentedColormap = build_linear_colour_map(with_colours)

    # Actually plot the values
    plot_unit_test_heatmap(grid_values, colour_map, miner.x_axis_label(), miner.y_axis_label(),
                           miner.file_label())


def plot_unit_test_heatmap(grid_values: list[list[float]], colour_map: ListedColormap, x_label: str,
                           y_label: str, file_label: str) -> None:
    """
    Plots a heatmap representation of the unit test success results. Can be used either for
    control groups (average test result) or for individual participants.
    :param grid_values: 2D int array of results. Each cell has value between [0-1], indicating
    the success rate,
    where 0 is all fail and 1 is all pass. For individual tests and participants the provided
    array should only contain the values 0 and 1.
    See: https://stackoverflow.com/a/33282548
    """
    # Add the 2D heatmap
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.imshow(grid_values, cmap=colour_map, interpolation='nearest')

    # Actually show the figure
    plt.savefig("generated-plots/" + file_label + ".png")
    plt.show()


def bool_to_int(test_result):
    """
    Primitive bool-to-int converter. Converts true to 1 and false to 0.
    :param test_result as a boolean test result
    :return: a corresponding int value, either 0 or 1.
    """
    if test_result:
        return 1
    return 0


def patch_control_group_colours(grid_values: list[list[float]], group_zone_size: int) -> \
        list[list[int]]:
    """
    Adds an integer multiplication (*1, *2, *3, ...) to every value in received grid, to colorize
    values based on control group.
    :param grid_values: 2D bool array. Tells for every participant which tests passed / failed.
    :param group_zone_size: tells how many participants exist per control group (needed so
    this method knows the size of each colour zone).
    :return: 2D int array, indicating for every participant if failed (color zone offset+0) or
    passed (colour zone offset +1)
    """
    colourized_grid_values: list[list[float]] = []
    for participant_index, participant_results in enumerate(grid_values):
        colourized_participant_results: list[int] = []
        colour_zone_offset: int = (participant_index // group_zone_size) * 2
        for test_result in participant_results:
            colourized_participant_results.append(test_result + colour_zone_offset)
        colourized_grid_values.append(colourized_participant_results)
    return colourized_grid_values
