"""
Helper module to gain convenient access on a subset of the entire population (all participants),
notably access by control group name.
"""
from restify_mining.participant import Participant


def get_group_names(population: list[Participant]) -> list[str]:
    """
    Iterates over all participants in population and collects all group names encountered.
    :param population: the set of participants to scan for group names.
    :return: duplicate free string list of group names found in the provided pariticpant list.
    """
    groups_with_duplicates: list[str] = list(map(lambda x: x.group_name, population))
    groups: list[str] = list(dict.fromkeys(groups_with_duplicates))
    return groups


def filter_population_by_group(population: list[Participant], target_group: str) -> list[
    Participant]:
    """
    Reduces a given list of participants to those matching the provided group_name in their
    corresponding field.
    :param population: the set of participants to filter down to the match criteria, a control
    group name.
    :param target_group: the match criteria, only participants matching this group will remain.
    :return: a subset of the provided input population, containing only those participants that
    fall into the provided control group.
    """
    target_population = list(
        filter(lambda participant: participant.group_name == target_group, population))
    return target_population


def get_skill_values_by_index(population: list[Participant], skill_index: int) -> list[int]:
    """
    Extracts all skill value of the list of provided participants and a given skill index. The
    order of values in the result list corresponds to the order of participants in
    the population received as argument.
    :param population: as the set of participants to analyze
    :param skill_index: as the index position of the skill to extract
    :return: a list of integere values, representing the values extracted for each participant.
    """
    return list(map(lambda participant: participant.skills[skill_index], population))


def get_average_skill_value_by_index(population: list[Participant], skill_index: int) -> list[int]:
    """
    Computes the average skill value for a given set of participants and skill.
    :param population: as the list of participants for which we want to analyze skill values
    :param skill_index: as the index of the specific skill to analyze
    :return: a single floating point value, representing the average skill competence value for
    the given population and skill index.
    """
    skill_values: list[int] = get_skill_values_by_index(population, skill_index)
    return sum(skill_values) / len(skill_values)
