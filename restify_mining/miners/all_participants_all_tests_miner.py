"""
Most simple miner implementation. Analyzes all provided participants and mines their test
restuls. Stores outcome in 2D array where passed tests are represented by1, failed tests by 0.
"""
from restify_mining.assessed_participant import AssessedParticipant
from restify_mining.miners.abstract_miner import AbstractMiner


class AllParticipantsAllTestsAbstractMiner(AbstractMiner):
    """
    Extension of abstract miner, produces result values for all participants and all tests.
    """

    def mine(self, participants: list[AssessedParticipant]) -> list[list[float]]:
        grid_values: list[list[float]] = []
        for assessed_participant in participants:
            grid_values.append(assessed_participant.all_test_results())
        return grid_values
