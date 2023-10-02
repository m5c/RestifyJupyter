"""
Utils module to create box plots (skill distribution by group allocation).
Deeply inspired by: https://stackoverflow.com/a/10138308
"""
import itertools

import matplotlib.pyplot as plt
import numpy as np

from restify_mining.markers import skills_markers, group_tint_markers
from typing import TypeVar

# Define a generic, not bound to any implementation class
T = TypeVar("T")


def interleave_human_intuitive(entries_by_groups_dsl: list[T], entries_by_groups_ide: list[T]) -> \
        list[T]:
    """
    Helper function to interleave samples or colour series in a way that is most "logical" for
    humans. T represented entries and is most likely a list of values or a colour code.
    Target output lists is a rearranged list interleave of both input lists, structured as follows:
    -3 entries (sample lists or colours) for BookStore / DSL
    -3 entries (sample lists or colours) for BookStore / Manual
    -3 entries (sample lists or colours) for Xox / DSL
    -3 entries (sample lists or colours) for Xox / Manual
    each of the above lists contains in order:
    -entries from group who did that methodology / app combo as first task
    -combined entries from both group who did that methodology / app, in any order
    -entries from group who did that methodology / app combo as second task
    :param entries_by_groups_dsl: as list of sample lists for groups DSL values in order red,
    green, blue, yellow, orange, turquoise
    :param entries_by_groups_ide: as list of sample lists for groups manual values in order red,
    green, blue, yellow, orange, turquoise
    :return: one fused list, ordered as indicated above.
    """
    task_times_ordered: list[list[int]] = []
    # 3 sample lists for all BookStore / DSL data (red / combined orange / yellow)
    task_times_ordered.append(entries_by_groups_dsl[0])
    task_times_ordered.append(entries_by_groups_dsl[4])
    task_times_ordered.append(entries_by_groups_dsl[3])
    # 3 sample lists for all BookStore / Manual data (green / combined turquoise / blue)
    task_times_ordered.append(entries_by_groups_ide[1])
    task_times_ordered.append(entries_by_groups_ide[5])
    task_times_ordered.append(entries_by_groups_ide[2])
    # 3 sample lists for all Xox / DSL data (blue / combined turquoise / green)
    task_times_ordered.append(entries_by_groups_dsl[2])
    task_times_ordered.append(entries_by_groups_dsl[5])
    task_times_ordered.append(entries_by_groups_dsl[1])
    # 3 sample lists for all Xox / Manual data (yellow / combined orange / red)
    task_times_ordered.append(entries_by_groups_ide[3])
    task_times_ordered.append(entries_by_groups_ide[4])
    task_times_ordered.append(entries_by_groups_ide[0])
    # return single interleaved list, with 12 list entries.
    return task_times_ordered


def build_bundle_positions(with_fused: bool):
    """
    Helper functions to create spacing instructions for the boxplots in target figure.
    :return: list of float values, indicating the positioning of all boxplots on x-axis
    """
    # total amount of box-plots
    boxplot_amount: int = 12

    # amount of box-plots to place close per bundle
    bundle_size: int = 3

    # additional space to place between box-plots on transitioning to next bundle
    inter_bundle_additional_spacing: float = 0.7

    # shrink factor to apply. Higher number places the box-plots closer, while respecting
    # relative distancing resulting from previous factors. I.e. higher factor makes individual
    # box-plots wider while preserving spacing.
    density: float = 5

    undense_positions: list[int] = []
    for position in range(0, boxplot_amount):
        undense_positions.append(
            position + (position // bundle_size) * inter_bundle_additional_spacing)

    # apply density factor
    dense_positions = [i / density for i in undense_positions]

    # override intermediate positions, if no intermediate groups
    if not with_fused:
        dense_positions[2] = dense_positions[1]
        dense_positions[1] = (dense_positions[0]+dense_positions[2])/2
        dense_positions[5] = dense_positions[4]
        dense_positions[4] = (dense_positions[3]+dense_positions[5])/2
        dense_positions[8] = dense_positions[7]
        dense_positions[7] = (dense_positions[6]+dense_positions[8])/2
        dense_positions[11] = dense_positions[10]
        dense_positions[10] = (dense_positions[9]+dense_positions[11])/2

    return dense_positions


def extract_numeric_stats(samples: list[float], plot_data: dict) -> dict:
    """
    Pyplot makes it surprisingling inconvenient to just get the numeric statistic data of an
    already created boxplot. This little helper function adds the missing functionality.
    :param plot_data: as return dictionary of a previous plot command.
    :return: dictionary with all numeric values of a given boxplot, as numbers.
    """
    min: float = [round(item.get_ydata()[0], 1) for item in plot_data['caps']][::2][0]
    max: float = [round(item.get_ydata()[0], 1) for item in plot_data['caps']][1::2][0]
    lower: float = np.quantile(samples, 0.25)
    mean: float = np.quantile(samples, 0.5)
    average: float = np.average(samples)
    upper: float = np.quantile(samples, 0.75)
    return {'min': min, 'lower': lower, 'average': average, 'mean': mean,
            'upper': upper, 'max': max}


def print_numeric_table(stats_data: [dict], with_fused: bool) -> None:
    """
    Creates a nice MarkDown table with numeric values (rows) of every boxplot (columns)
    :param stats_data: as the dictionary with all raw numeric boxplot data.
    :return: None
    """

    if with_fused:
        print("\n| - | Red #1 | Orange | Yellow #2 | Green #1 | Turquoise | Blue #2 | Blue #1 | Turquoise | Green #2 | Yellow #1 | Orange | Red #2 |")
        print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    else:
        print(
            "\n| - | Red #1 | Yellow #2 | Green #1 | Blue #2 | Blue #1 | Green #2 | Yellow #1 | Red #2 |")
        print("|---|---|---|---|---|---|---|---|---|")
    for metric in ['max', 'upper', 'mean', 'average', 'lower', 'min']:
        print("| "+metric+" | ", end =" ")
        for entry in stats_data:
            print(str(round(entry[metric], 1)) + " |", end =" ")
        print("")
    print("\n")


def graphical_box_plot(task_values_by_groups_dsl: list[list[float]],
                       task_values_by_groups_ide: list[list[float]],
                       include_fused: bool,
                       palette: list[str], extraction_metric: str, filename: str):
    """
    Produces a boxplot for the refactoring time measured per group.

    :param task_values_by_groups_dsl: list of 6 lists. Every inner lists contains values
    expressing refactoring times for the group adherents. The last two entries are group combos.
    :param task_values_by_groups_ide: list of 6 lists. Every inner lists contains values
    expressing refactoring times for the group adherents. The last two entries are group combos.
    :param include_fused set to true of the boxplot should contain arange and turquoise groups.
    :param palette: provides the colour codes (string with hash + hexcode) to use for skills.
    :param extraction_metric: as string to print on Y axis to describe nature of measured values.
    :param filename: as the name to used for persistence on disk.
    """

    # define frame size (not intuitive, but this must happen BEFORE clf)
    plt.rcParams["figure.figsize"] = (7.5, 2.5)

    # reset figure, to have separate drawings
    plt.clf()

    # combine task times (interleave the individual lists, to obtain one list with all int entries)
    task_values_ordered: list[list[int]] = interleave_human_intuitive(task_values_by_groups_dsl,
                                                                      task_values_by_groups_ide)

    # We use the same interleaving algorithm for the colour codes to use in the resulting boxplot
    # sequence. We have two values per group, so we just interleave the series of predefined
    # sample colours with itself - this way the colours match the same interleaving strategies as
    # applied to the sample data.
    palette_colours: list[str] = interleave_human_intuitive(list(palette), list(palette))

    # create boxplot positions that represent grouping in box-plots of three
    box_plot_positions: list[float] = build_bundle_positions(include_fused)
    # prepare empty array of dictionaries for statistical data of every boxplot.
    stats_data: [dict] = []
    for index, task_values in enumerate(task_values_ordered):
        # skill_values if a series fo seven skill values for a given group and skill,
        # that we want to turn into a boxplot.

        # Add condition for intermediate groups: skip if
        is_fused: bool = index % 3 == 1
        if not include_fused and is_fused:
            None
        else:

            # set plot colour to group colour (use integer division to advance only every two
            # iterations)
            plotter_colour = palette_colours[index]

            # add a single boxplot, based on the time series provided for the current group
            plot_data: dict = plt.boxplot(task_values,
                                          positions=[box_plot_positions[index]], notch=False,
                                          patch_artist=True,
                                          showfliers=True,
                                          boxprops=dict(facecolor=plotter_colour, color="#FFFFFF"),
                                          capprops=dict(color=plotter_colour),
                                          whiskerprops=dict(color=plotter_colour),
                                          flierprops=dict(color=plotter_colour,
                                                          markeredgecolor=plotter_colour),
                                          medianprops=dict(color='#000000'), showmeans=True,
                                          meanprops={"marker": "s", "markerfacecolor": "white",
                                                     "markeredgecolor": plotter_colour})

            # register numeric data of the single boxplot we just added. We need it later to create a
            # table.
            stats_data.append(extract_numeric_stats(task_values, plot_data))

    # print textual version of numeric boxplot data
    print_numeric_table(stats_data, include_fused)

    # Set axis limit, so series of plots use same references
    # plt.ylim([0, reference_ceiling])
    plt.ylabel("Conversion " + extraction_metric)

    # update effective figure boarders to include labels
    plt.tight_layout()

    # plot the axis ticks on x (indicating skill groups)
    if include_fused:
        labels = ["#1", "#*\nBookStore: DSL", "#2", "#1", "#*\nBookStore: Manual", "#2", "#1",
                "#*\nXox: DSL", "#2", "#1", "#*\nXox: Manual", "#2"]
    else:
        labels = ["#1", "\nBookStore: DSL", "#2", "#1", "\nBookStore: Manual", "#2", "#1",
                "\nXox: DSL", "#2", "#1", "\nXox: Manual", "#2"]
    plt.xticks(box_plot_positions, labels)
    plt.savefig(filename, dpi=300)
    plt.show()
