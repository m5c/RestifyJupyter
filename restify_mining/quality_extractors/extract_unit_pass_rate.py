"""
This module reduces a provided set of participants to an array of unit test results percentages.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant


def extract_unit_pass_rates_bs(assessed_participants: list[AssessedParticipant]) -> list[float]:
    result: list[float] = []
    for assessed_participant in assessed_participants:
        result.append(assessed_participant.test_percentage_bs)
    return result


def extract_refactor_times_bs(assessed_participants: list[AssessedParticipant]) -> list[int]:
    result: list[int] = []
    for assessed_participant in assessed_participants:
        result.append(assessed_participant.time_bs)
    return result
