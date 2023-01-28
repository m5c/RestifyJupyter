"""
This module reduces a provided set of participants to an array of unit test results percentages.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant


def extract_unit_pass_rates_bs(assessed_participants: list[AssessedParticipant]) -> list[float]:
    """
    Helper method to extract the pass rate of all unit tests for the bookstore.
    :param assessed_participants:  the list of participants to analyze.
    :return: list of pass rates, every entry represents one participant.
    """
    result: list[float] = []
    for assessed_participant in assessed_participants:
        result.append(assessed_participant.test_percentage_bs)
    return result


def extract_refactor_times_bs(assessed_participants: list[AssessedParticipant]) -> list[int]:
    """
        Helper method to extract the pass rate of all unit tests for the xox.
        :param assessed_participants:  the list of participants to analyze.
        :return: list of pass rates, every entry represents one participant.
        """
    result: list[int] = []
    for assessed_participant in assessed_participants:
        result.append(assessed_participant.time_bs)
    return result
