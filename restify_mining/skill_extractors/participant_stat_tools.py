"""Module for everything related to participant statistics."""

import numpy as np
from scipy import stats
from scipy.stats._morestats import ShapiroResult

from restify_mining.data_objects.participant import Participant
from restify_mining.data_objects.participant_filter_tools import extract_group_names, \
    filter_population_by_group
from restify_mining.markers.skills_markers import full_skill_tags
from restify_mining.utils.shapiro_interpreter import print_normal_dist_interpretation


def extract_skill_values_by_index(index: int, participants: list[Participant]) -> list[int]:
    """Returns a vector of all values for a single given skill over all participants"""
    skill_values = []
    for participant in participants:
        skill_values.append(participant.skills[index])
    return skill_values


def extract_skill_sum_values(participants: list[Participant]) -> list[int]:
    """
    Computes sum of all skills per participant and returns a list with all results.
    :param participants: as the population to analyze
    :return: list of all total skill values.
    """
    total_values = []
    for participant in participants:
        total_values.append(sum(participant.skills))
    return total_values


def build_normalized_skills(participants):
    """Compute the normalized vector of participant skills"""
    summed_skills = build_summed_skills(participants)
    return summed_skills / np.sqrt(np.sum(summed_skills ** 2))


def build_summed_skills(participants):
    """Computes a summed vector of all participant skills"""
    # sum of all participant skills
    summed_skills = [0, 0, 0, 0, 0, 0, 0, 0]
    for participant in participants:
        summed_skills = np.add(summed_skills, participant.skills)
    return summed_skills


def extract_control_group_size(population: list[Participant]) -> int:
    """
    Analyzes a provided population and returns the amount of participants of the first control
    group found. Throws an error if not all detected control groups make up the same amount of
    participants.
    :param population: as the list of participants (all control groups) to analyze
    :return: amount of participants per control group
    """
    # compute amount of participants by control group
    control_group_names: list[str] = extract_group_names(population)
    control_group_sizes: list[int] = []
    for group_name in control_group_names:
        control_group_sizes.append(len(filter_population_by_group(population, group_name)))
    # Verify only a single value is contained, by converting to dictionary and back
    unique_group_sizes = list(dict.fromkeys(control_group_sizes))
    if len(unique_group_sizes) != 1:
        raise Exception(
            "Cannot determine unique control group size. There are multiple groups with different "
            "amount of participants.")
    return unique_group_sizes[0]


def compute_shapiro_will_skills_standarddev_pvalue(population: list[Participant]) -> list[float]:
    """
    Analyzes all the self assessed skill declarations of provided list of participants and tests
    for the null hypothesis (whether the samples can be approximated by a normal distribution).
    Internally uses the scipy shapiro package:
    https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.shapiro.html
    :param population: as a list of participants, providing self-declared skill vectors
    :return: list of p-values. Greater 0.5 is interpreted as safe-to-model as normal
    distribution
    """

    for idx, skill in enumerate(full_skill_tags):
        skill_values: list[float] = extract_skill_values_by_index(idx, population)
        # print(skill_values)
        shapiro_result: ShapiroResult = stats.shapiro(skill_values)
        print_normal_dist_interpretation(skill, shapiro_result)

# Null Hypothesis: The data comes from a normal distribution
# Threshold: 0.05
# P = 0.0001315
# Interpretation: p is lower than threshold. That means...
# https://developer.ibm.com/articles/statistical-si
# The test result is significant: The hypothesis should be rejected.
# The samples can be assumed not to stem from a normal distribution.
