"""
Helper module to normalize a population, that is to say add fields that put absolute values into
relation to the samples of the entire population.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.data_objects.normalized_participant import NormalizedParticipant
from restify_mining.scatter_plotters.extractors.application_time_extractor import \
    ApplicationTimeExtractor
from restify_mining.scatter_plotters.extractors.methodology_time_extractor import \
    MethodologyTimeExtractor


def normalize(population: list[AssessedParticipant]) -> list[NormalizedParticipant]:
    """
    Iterates over entire population and searches for outer limits of measured task solving times.
    The runs a second iteration over all participants and transforms them into a normalized
    version, where additional normalized fields are added for convenient usage in grapher/stat
    tools.
    :param population: as the full experiment population, assessed.
    :return: normalized version of the population.
    """
    # First step: extract min and max times per methodology and per app.
    # Use extractors for this
    bs_times: list[int] = ApplicationTimeExtractor("bs").extract(population)
    min_bs_time: int = min(bs_times)
    max_bs_time: int = max(bs_times)
    bs_time_range: int = max_bs_time - min_bs_time
    xox_times: list[int] = ApplicationTimeExtractor("xox").extract(population)
    min_xox_time: int = min(xox_times)
    max_xox_time: int = max(xox_times)
    xox_time_range: int = max_xox_time - min_xox_time
    ide_times: list[int] = MethodologyTimeExtractor("ide").extract(population)
    min_ide_time: int = min(ide_times)
    max_ide_time: int = max(ide_times)
    ide_time_range: int = max_ide_time - min_ide_time
    tc_times: list[int] = MethodologyTimeExtractor("tc").extract(population)
    min_tc_time: int = min(tc_times)
    max_tc_time: int = max(tc_times)
    tc_time_range: int = max_tc_time - min_tc_time

    # Second step: iterate over every participant and set the four relative time values,
    # based on the normal comparison in the total population
    normalized_population: list[NormalizedParticipant] = []
    participant: AssessedParticipant
    for participant in population:
        norm_time_bs: float = (participant.time_bs - min_bs_time) / bs_time_range
        norm_time_xox: float = (participant.time_xox - min_xox_time) / xox_time_range
        norm_time_ide: float = (participant.time_ide - min_ide_time) / ide_time_range
        norm_time_tc: float = (participant.time_tc - min_tc_time) / tc_time_range

        normalized_participant: NormalizedParticipant = NormalizedParticipant(participant,
                                                                              norm_time_bs,
                                                                              norm_time_xox,
                                                                              norm_time_ide,
                                                                              norm_time_tc)
        normalized_population.append(normalized_participant)

    # Last step: Return resulting new list of normalized participants.
    return normalized_population
