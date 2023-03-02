"""
Helper module to normalize a population, that is to say add fields that put absolute values into
relation to the samples of the entire population.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.normalized_participant import NormalizedParticipant


def normalize(population: list[AssessedParticipant]) -> list[NormalizedParticipant]:
    """
    Iterates over entire population and searches for outer limits of measured task solving times.
    The runs a second iteration over all participants and transforms them into a normalized
    version, where additional normalized fields are added for convenient usage in grapher/stat
    tools.
    :param population: as the full experiment population, assessed.
    :return: normalized version of the population.
    """
    # TODO: implement
    return []
