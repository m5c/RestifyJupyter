"""
Utils module to create boxplots (skill distribution by group allocation).
Deeply inspired by: https://stackoverflow.com/a/10138308
"""

import matplotlib.pyplot as plt

from restify_mining.markers import skills_markers, group_tint_markers


def time_plot_box(task_times_by_group: list[list[int]], palette: list[str], reference_ceiling: int, filename: str):
    """
    Produces a boxplot for the refactoring time measured per group.
    :param task_times_by_group: list of 4 lists. Every inner lists contains 7 values expressing refactoring times for
    the adherents.
    :param reference_ceiling: indicates the maximum value to uses for y-axis of plot. This is useful for creation of
    series with uniform scaling.
    skill and a specific group. Those are the ones we want to turn into boxplots. The outer list enumerates all skills
    for all groups. Namely, sequences of four for the groups of a giving skill.
    :param palette: provides the colour codes (string with hash + hexcode) to use for skills.
    :param filename: as the name to used for persistence on disk.
    """

    # define frame size (not intuitive, but this must happen BEFORE clf)
    plt.rcParams["figure.figsize"] = (14, 4)

    # reset figure, to have separate drawings
    plt.clf()


    # plot the boxes, iterate over all skills.
    for group_index, task_time_values in enumerate(task_times_by_group):
        # skill_values if a series fo seven skill values for a given group and skill, that we want to turn into a
        # boxplot.

        # set plot colour to group colour
        plotter_colour = list(palette)[int(group_index)]

        # add a single boxplot, based on the time series provided for the corrent group
        plt.boxplot(task_time_values,
                    positions=[group_index + 1], notch=False,
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
    plt.ylim([0, reference_ceiling])

    # plot the axis ticks on x (indicating skill groups)
    amount_groups: int = len(task_times_by_group)
    plt.xticks(range(1, amount_groups + 1), list(group_tint_markers.group_tints.keys()))
    plt.savefig(filename)
    plt.show()
