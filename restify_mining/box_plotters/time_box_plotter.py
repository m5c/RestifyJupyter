"""
Utils module to create boxplots (skill distribution by group allocation).
Deeply inspired by: https://stackoverflow.com/a/10138308
"""
import itertools

import matplotlib.pyplot as plt

from restify_mining.markers import skills_markers, group_tint_markers


def time_plot_box(task_times_by_group_1: list[list[int]], task_times_by_group_2: list[list[int]],
                  palette: list[str], filename: str):
    """
    Produces a boxplot for the refactoring time measured per group.
    :param task_times_by_group_1: list of 4 lists. Every inner lists contains 7 values expressing
    refactoring times for
    the adherents.
    :param task_times_by_group_2: list of 4 lists. Every inner lists contains 7 values expressing
    refactoring times for
    the adherents.
    :param palette: provides the colour codes (string with hash + hexcode) to use for skills.
    :param filename: as the name to used for persistence on disk.
    """

    # define frame size (not intuitive, but this must happen BEFORE clf)
    plt.rcParams["figure.figsize"] = (9, 3)

    # reset figure, to have separate drawings
    plt.clf()

    # combine task times (interleave the individual lists)
    task_times_by_group_double: list[list[int]] = \
        list(itertools.chain(*zip(task_times_by_group_1, task_times_by_group_2)))

    # plot the boxes, iterate over all skills. We still iterate over only
    for group_index, task_time_values in enumerate(task_times_by_group_double):
        # skill_values if a series fo seven skill values for a given group and skill,
        # that we want to turn into a
        # boxplot.

        # set plot colour to group colour (use integer division to advance only every two
        # iterations)
        plotter_colour = list(palette)[int(group_index) // 2]

        # add a single boxplot, based on the time series provided for the corrent group
        plt.boxplot(task_time_values,
                    positions=[0.5*(group_index + 1)], notch=False,
                    patch_artist=True,
                    showfliers=True,
                    boxprops=dict(facecolor=plotter_colour, color="#FFFFFF"),
                    capprops=dict(color=plotter_colour),
                    whiskerprops=dict(color=plotter_colour),
                    flierprops=dict(color=plotter_colour, markeredgecolor=plotter_colour),
                    medianprops=dict(color='#000000'), showmeans=True,
                    meanprops={"marker": "s", "markerfacecolor": "white",
                               "markeredgecolor": plotter_colour})

    # Set axist limit, so series of plots use same references
    # plt.ylim([0, reference_ceiling])
    plt.ylabel("Refactoring time [seconds]")

    # update effective figure boarders to include labels
    plt.tight_layout()

    # plot the axis ticks on x (indicating skill groups)
    amount_groups: int = len(task_times_by_group_double)
    # TODO: Avoid hard coding of axisticks and labels
    plt.xticks([0.5,1,1.5,2,2.5,3,3.5,4], ["DSL\nBookStore", "Manual\nXox","DSL\nXox", "Manual\nBookStore","DSL\nXox", "Manual\nBookStore","DSL\nBookStore", "Manual\nXox"])
    plt.savefig(filename, dpi=300)
    plt.show()
