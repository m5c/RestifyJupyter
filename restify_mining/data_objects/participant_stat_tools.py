"""Module for everything related to participant statistics."""

import numpy as np

from restify_mining.data_objects.participant import Participant
from restify_mining.data_objects.participant_filter_tools import extract_group_names, \
    filter_population_by_group


def build_mean_skills(participants: list[Participant]):
    """Computes the actual average of participant skills"""
    return [number / len(participants) for number in build_summed_skills(participants)]


def extract_skill_values_by_index(index: int, participants: list[Participant]):
    """Returns a vector of all a given skill over all participants"""
    skill_values = []
    for participant in participants:
        skill_values.append(participant.skills[index])
    return skill_values


def compute_single_skill_deviation(skill_values):
    """Computes the standard deviation for a given set of skills"""
    return np.std(skill_values)


def build_standard_deviation_skills(participants):
    """Computes an array of standard deviations. Every position in the result array corresponds
    to the skills of all participants at the given position."""
    standard_deviations = []

    amount_skills = len(participants[0].skills)
    for skill_index in range(amount_skills):
        skill_values = extract_skill_values_by_index(skill_index, participants)
        standard_deviations.append(compute_single_skill_deviation(skill_values))
    return standard_deviations


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
