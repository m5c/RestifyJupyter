"""
Helper module to gain convenient access on a subset of the entire population (all participants),
notably access by control group name
"""
from restify_mining.participant import Participant


def get_group_names(population: list[Participant]) -> list(str):
    """"Iterates over all participants in population and collects all group names encountered"""
    return list(map(lambda x: x.get('group_name'), population))
