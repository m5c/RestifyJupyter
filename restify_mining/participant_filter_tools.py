"""
Helper module to gain convenient access on a subset of the entire population (all participants),
notably access by control group name
"""
from restify_mining.participant import Participant


def get_group_names(population: list[Participant]) -> list[str]:
    """"Iterates over all participants in population and collects all group names encountered"""
    groups_with_duplicates: list[str] = list(map(lambda x: x.group_name, population))
    groups: list[str] = list(dict.fromkeys(groups_with_duplicates))
    return groups


def filter_population_by_group(population: list[Participant], target_group: str) -> list[
    Participant]:
    """Reduces a given list of participants to those matching the provided group_name in their
    corresponding field"""
    target_population = list(
        filter(lambda participant: participant.group_name == target_group, population))
    return target_population


def get_skill_values_by_index(population: list[Participant], skill_index: int) -> list[int]:
    """Extracts a single skill value of the list of provided participants and fuses them into a
    new list. The order of values in the result list corresponds to the order of participants in
    the population received as argument."""
    return list(map(lambda participant: participant.skills[skill_index], population))
