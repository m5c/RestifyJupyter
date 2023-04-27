"""
Utils module to create boxplots (skill distribution by group allocation).
Deeply inspired by: https://stackoverflow.com/a/10138308
"""

import matplotlib.pyplot as plt

from restify_mining.markers import skills_markers


def skill_plot_box(all_skill_values_by_skill_by_group: list[list[int]], palette: list[str],
                   amount_partitions: int, filename: str):
    """
    :param all_skill_values_by_skill_by_group: list of 32 lists. Every inner lists contains 7 values for a specific
    skill and a specific group. Those are the ones we want to turn into boxplots. The outer list enumerates all skills
    for all groups. Namely, sequences of four for the groups of a giving skill.
    :param palette: provides the colour codes (string with hash + hexcode) to use for skills.
    :param amount_partitions: as the amount of groups.
    :param filename: as the name to used for persistence on disk.
    """

    # reset figure, to have separate drawings
    plt.clf()

    # define frame size
    plt.rcParams["figure.figsize"] = (7, 2)

    # plot the boxes, iterate over all skills.
    for skill_index, skill_values in enumerate(all_skill_values_by_skill_by_group):

        # skill_values if a series fo seven skill values for a given group and skill, that we want to turn into a
        # boxplot.
        plotter_colour = palette[int(skill_index / amount_partitions)]
        plt.boxplot(skill_values,
                    positions=[skill_index + 1], notch=False,
                    patch_artist=True,
                    showfliers=True,
                    boxprops=dict(facecolor=plotter_colour, color="#FFFFFF"),
                    capprops=dict(color=plotter_colour),
                    whiskerprops=dict(color=plotter_colour),
                    flierprops=dict(color=plotter_colour, markeredgecolor=plotter_colour),
                    medianprops=dict(color='#000000'), showmeans=True,
                    meanprops={"marker": "s", "markerfacecolor": "white",
                               "markeredgecolor": plotter_colour})

    # plot the axis ticks on x (indicating skill groups)
    plt.xticks(
        [0.625 * amount_partitions, 1.625 * amount_partitions, 2.625 * amount_partitions, 3.625 * amount_partitions,
         4.625 * amount_partitions,
         5.625 * amount_partitions, 6.625 * amount_partitions, 7.625 * amount_partitions],
        skills_markers.skill_tags)
    plt.savefig(filename)
    plt.show()
