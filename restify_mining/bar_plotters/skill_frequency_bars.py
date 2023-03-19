"""
Helper util to rapidly print barcharts for skills
"""
import collections

import numpy as np
from matplotlib import pyplot as plt

from restify_mining.data_objects import participant
from restify_mining.markers import skills_markers
from restify_mining.markers.skills_markers import full_skill_tags
from restify_mining.skill_extractors.participant_stat_tools import extract_skill_sum_values, \
    extract_skill_values_by_index


def plot_skill_bars(population: list[participant]) -> None:
    """
    Generate boxplots for skill distribution among participants
    :param population: list of all participants to include in statistics
    :return: None
    """
    total_participant_skills: list[int] = extract_skill_sum_values(population)
    distribution: dict[int, int] = collections.Counter(total_participant_skills)
    print_bar_distribution(distribution, "Summed Total", min(total_participant_skills),
                           max(total_participant_skills), max(distribution.values()), "#555555")

    # Generate distributions and then bar-charts for each and every skill distribution (full
    # population)
    # Must be in two steps, so we can keep plot dimensions.
    all_skill_distributions: list[dict[int, int]] = []
    for idx, skill in enumerate(full_skill_tags):
        print(skill)
        one_skill_for_all_participants: list[int] = extract_skill_values_by_index(idx, population)
        distribution: dict[int, int] = collections.Counter(one_skill_for_all_participants)
        all_skill_distributions.append(distribution)

    # now determine max frequency on all distributions, as reference point for all plots
    max_frequency: int = max(max(distr.values()) for distr in all_skill_distributions)
    for idx, skill in enumerate(full_skill_tags):
        tint = skills_markers.palette[idx]
        print_bar_distribution(all_skill_distributions[idx], skill, 1, 5, max_frequency, tint)


def print_bar_distribution(distribution: dict[int, int], tag: str, lower_bound_x: int,
                           upper_bound_x: int, upper_bound_y: int, tint: str) -> None:
    """
    A method that simply prints sample frequency for discrete sets
    :param distribution: distribution of sample values
    :param tag: label to use for plot description
    :param lower_bound_x: lowest value to appear on x
    :param upper_bound_x: highest value to appear on x
    :param upper_bound_y: highest value to appear on y
    :param tint: as color to use for bars
    :return: None
    """

    plt.bar(distribution.keys(), distribution.values(), color=tint)
    plt.title(tag + " Skill Distribution")
    plt.xlabel(tag + " Skill Score")
    plt.xticks(np.arange(lower_bound_x, upper_bound_x + 1, 1.0))
    plt.yticks(np.arange(0, upper_bound_y + 1, 1.0))
    plt.xlim(lower_bound_x - 0.5, upper_bound_x + 0.5)
    plt.ylim(0, upper_bound_y + 0.5)
    plt.ylabel("Participant Amount")
    plt.savefig("generated-plots/01-participant-" + tag + "-bars.png")
    plt.show()
