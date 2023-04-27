"""
Utils module to create boxplots (skill distribution by group allocation).
Deeply inspired by: https://stackoverflow.com/a/10138308
"""

import matplotlib.pyplot as plt

from restify_mining.markers import skills_markers


# TODO: refactor. Do not pass amount partitions as extra value but provide 2D list for skill values, already separated
#  by group. See implementation of time box plotter. Ideally refactor to use common code for plotting.
def skill_plot_box(all_skill_values_by_skill_by_group: list[int], palette: list[str],
                   amount_partitions: int, filename: str):
    """Prints a boxplot, with packs of four, based on a single array with all participant skill values, ordered by
    skill index and group index. Illustration: first there come all values of participants for
    group 1, skill one. Then come all values of participants of group 2, skill 1, and so on.
    """

    # reset figure, to have separate drawings
    plt.clf()

    # define frame size
    plt.rcParams["figure.figsize"] = (7, 2)

    # plot the boxes, iterate over all skills.
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

    # plot the axis ticks on x (indicating skill groups)
    plt.xticks(
        [0.625 * amount_partitions, 1.625 * amount_partitions, 2.625 * amount_partitions, 3.625 * amount_partitions,
         4.625 * amount_partitions,
         5.625 * amount_partitions, 6.625 * amount_partitions, 7.625 * amount_partitions],
        skills_markers.skill_tags)
    plt.savefig(filename)
    plt.show()
