"""
Utils module to create boxplots (skill distribution by group allocation).
Deeply inspired by: https://stackoverflow.com/a/10138308
"""

import matplotlib.pyplot as plt

from restify_mining.markers import skills_markers


def skill_plot_box(all_skill_values_by_skill_by_group: list[list[int]], palette: list[str],
                   amount_partitions: int, filename: str):
    """
    :param all_skill_values_by_skill_by_group: list of 32 lists. Every inner lists contains 7
    values for a specific
    skill and a specific group. Those are the ones we want to turn into boxplots. The outer list
    enumerates all skills
    for all groups. Namely, sequences of four for the groups of a giving skill.
    :param palette: provides the colour codes (string with hash + hexcode) to use for skills.
    :param amount_partitions: as the amount of groups.
    :param filename: as the name to used for persistence on disk.
    """
    # define frame size
    plt.rcParams["figure.figsize"] = (7.5, 2.2)
    #
    # plt.rcParams["figure.figsize"] = (8, 3)

    # For reasons only python affictionados know, figsize is only effective if cleared afterwards
    plt.clf()

    # plot the boxes, iterate over all skills.
    for skill_index, skill_values in enumerate(all_skill_values_by_skill_by_group):
        # skill_values if a series fo seven skill values for a given group and skill,
        # that we want to turn into a
        # boxplot.
        plotter_colour = palette[int(skill_index / amount_partitions)]
        plt.boxplot(skill_values,
                    positions=[0.5 * (skill_index)], notch=False,
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
        generate_tick_pos(8, 4), skills_markers.skill_tags)
    # plt.xlabel("Skill")
    plt.ylabel("Declared Proficiency")
    plt.savefig(filename, dpi=300)
    plt.show()


def generate_tick_pos(amount_skills: int, amount_groups: int) -> float:
    tick_positions: list[int] = []
    for i in range(amount_skills):
        tick_positions.append(i * 0.5 * amount_groups + 0.75)
    return tick_positions
