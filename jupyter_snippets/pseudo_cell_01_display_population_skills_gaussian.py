"""
Author: Maximilian Schiedermeier
"""
import collections

from csv_tools import file_load_utils
from restify_mining.data_objects.participant import Participant
from restify_mining.markers.skills_markers import full_skill_tags
from restify_mining.skill_extractors.participant_stat_tools import \
    compute_shapiro_will_skills_standarddev_pvalue, extract_skill_sum_values, \
    extract_skill_values_by_index
import matplotlib.pyplot as plt


def cell_01() -> None:
    """
    Jupyter cell 01. See markdown description.
    :return: None
    """
    # Load all participant objects (specifies skills, codename, control-group) from csv file
    population: list[Participant] = file_load_utils.load_all_participants()

    # Provide evidence that skill data is not normal-distributed.
    compute_shapiro_will_skills_standarddev_pvalue(population)

    # Int he following we provide bar charts to provide evidence that out population is diverse

    # Generate boxplots for skill distribution among participants
    total_participant_skills: list[int] = extract_skill_sum_values(population)
    print_bar_distribution(total_participant_skills, "Summed Total")

    # Generate barcharts for each and every skill distribution (full population)
    for idx, skill in enumerate(full_skill_tags):
        print(skill)
        one_skill_for_all_participants: list[int] = extract_skill_values_by_index(idx, population)
        print_bar_distribution(one_skill_for_all_participants, skill)


def print_bar_distribution(samples: list[int], tag: str) -> None:
    """
    A method that simply prints sample frequency for discrete sets.
    :param samples: discrete sample values
    :return: None
    """
    distribution = collections.Counter(samples)
    plt.bar(distribution.keys(), distribution.values())
    plt.title(tag + " Skill Distribution")
    plt.xlabel(tag + " Skill Score")
    plt.ylabel("Participant Amount")
    plt.show()
