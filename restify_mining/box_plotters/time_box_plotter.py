"""
Utils module to create boxplots (skill distribution by group allocation).
Deeply inspired by: https://stackoverflow.com/a/10138308
"""

import matplotlib.pyplot as plt

from restify_mining.markers import skills_markers


def time_plot_box(group_time_values: list[list[int]], palette: list[str], filename: str):
    """Prints a boxplot, with packs of four, based on a single array with all participant skill values, ordered by
    skill index and group index. Illustration: first there come all values of participants fo
    group 1, skill one. Then come all values of participants of group 2, skill 1, and so on.
    """

    # reset figure, to have separate drawings
    plt.clf()

    # define frame size
    plt.rcParams["figure.figsize"] = (14, 4)


    # plot the boxes
    for skill_index, skill_values in enumerate(all_skill_values_by_skill_by_group):
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
    plt.xticks(
        [1 * amount_partitions, 2 * amount_partitions, 3 * amount_partitions, 4 * amount_partitions,
         5 * amount_partitions,
         6 * amount_partitions, 7 * amount_partitions, 8 * amount_partitions],
        skills_markers.skill_tags)
    plt.savefig(filename)
    plt.show()
