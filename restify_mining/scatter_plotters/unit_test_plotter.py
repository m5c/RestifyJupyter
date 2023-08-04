"""
2D plotter module that creates visualizations of test success rates for population / population
subsets and for one or two selected applications.
Inspired by: https://stackoverflow.com/a/7230921
"""
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.markers.group_tint_markers import group_tints
from restify_mining.unit_test_miners.all_groups_tests_miner import AllGroupsTestsMiner
from restify_mining.unit_test_miners.abstract_miner import AbstractTestMiner


def plot_all_average_group_results(app: str, population: list[AssessedParticipant]) -> None:
    """
    Creates a 2D plot of all individual participant test results. On Y axis (vertical) all
    participants, on X axis (horizontal) all unit tests. Created image shows a black square for
    failed tests, coloured square (matching control group colour) for passed tests.
    :param app: as description of the app for which the average test results are requested.
    :param population: as the list of assessed participants.
    """
    mine_and_plot(AllGroupsTestsMiner(app), population)


def build_linear_colour_map() -> LinearSegmentedColormap:
    """
    https://matplotlib.org/stable/tutorials/colors/colormap-manipulation.html
    Search for: "Directly creating a segmented colormap from a list"
    :return: The only kind of colormap that is actually useful. Produces gradients based on
    sample points.
    """
    list_colours: list[str] = ["black", group_tints["red"], "black", group_tints["green"], "black",
                               group_tints["blue"],
                               "black",
                               group_tints["yellow"]]
    # Greyscale palette:
    # list_colours: list[str] = ["black", "white", "black", "white", "black", "white", "black",
    #                            "white"]

    return LinearSegmentedColormap.from_list("mycmap", list_colours)


def mine_and_plot(miner: AbstractTestMiner, population: list[AssessedParticipant]):
    """
    Create 2D array, consisting of all participants (already ordered by control group) and test
    results for app specific unit tests (the received abstract miner is branded to an app)
    :param miner: as the mining algorithm implementation to apply (parameterized to app)
    :param population: as the population for which the plotter prints results
    """
    grid_values: list[list[float]] = miner.mine(population)

    # Look up amount of participant-rows per control group, so we can tint the map by zones.
    # This is a heatmap, so there is only one coloured row per control group.
    group_zone_size: int = miner.colour_zone_size(population)

    # We use a custom heatmap that indicates group colours:
    colour_map: LinearSegmentedColormap = build_linear_colour_map()

    # use amount per control group to create a "colorized" value grid
    # (colour map has zones, we add an offset to every participant, depending on their control
    # group, so they end up in the right colour map zone).
    grid_values: list[list[int]] = patch_control_group_colours(grid_values, group_zone_size)

    # Get the x-tics from miner (miner is branded to app)
    x_tics: list[str] = miner.x_tics

    # Actually plot the values
    plot_unit_test_heatmap(grid_values, colour_map, miner.x_axis_label(), miner.y_axis_label(),
                           x_tics, miner.file_label())


def plot_unit_test_heatmap(grid_values: list[list[float]], colour_map: ListedColormap, x_label: str,
                           y_label: str, x_tics: list[str], file_label: str) -> None:
    """
    Plots a heatmap representation of the unit test success results. Can be used either for
    control groups (average test result) or for individual participants.
    :param grid_values: 2D int array of results. Each cell has value between [0-1], indicating
    the success rate,
    where 0 is all fail and 1 is all pass. For individual tests and participants the provided
    array should only contain the values 0 and 1.
    :param colour_map: as the colour map to use for plotting. This can be either a greyscale or
    coloured map.
    :param x_label: as the label to place below the x axis
    :param y_label: as the label to place left of the y axis
    :param x_tics: as the markers for the individual tics on x axis. This indicates the tests.
    :param file_label: as the name to use for persistence on disk.
    Based on pyplot heatmap examples, see: https://stackoverflow.com/a/33282548
    """
    # Add the 2D heatmap
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.imshow(grid_values, cmap=colour_map, interpolation='nearest', vmin=0.0, vmax=7.0)

    # Override the tics on X axis (individual tests)
    plt.xticks(range(len(x_tics)), x_tics)

    # rotate the tics a bit, so they take less space
    plt.xticks(fontsize=8, rotation=-55, ha='left', rotation_mode='anchor')

    # make more space toward bottom for xtics
    plt.gcf().subplots_adjust(bottom=0.35)

    # Actually show the figure
    plt.savefig("generated-plots/" + file_label + ".png", dpi=300)
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
