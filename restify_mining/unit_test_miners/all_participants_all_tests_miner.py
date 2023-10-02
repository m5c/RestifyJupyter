"""
Most simple miner implementation. Analyzes all provided participants and mines their test
restuls. Stores outcome in 2D array where passed tests are represented by1, failed tests by 0.
"""
from restify_mining.skill_extractors import participant_stat_tools
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.unit_test_miners.abstract_miner import AbstractTestMiner


def all_bool_to_float(bool_test_results: list[bool]) -> list[float]:
    """
    Helper function to convert all test results, stored as boolean list to float list. Although
    python seems not to have whatsoever type safety and just converts back and forth between
    anything with unpredictable outcome.
    :param
    :return:
    """
    float_test_results: list[float] = []
    for test_result in bool_test_results:
        if test_result:
            float_test_results.append(1.0)
        else:
            float_test_results.append(0.0)
    return float_test_results


class AllParticipantsAllTestsMiner(AbstractTestMiner):
    """
    Extension of abstract miner, produces result values for all participants and all tests.
    """

    def mine(self, participants: list[AssessedParticipant]) -> list[list[float]]:
        grid_values: list[list[float]] = []
        for assessed_participant in participants:
            if self.scope == "bs":
                numeric_test_results: list[float] = all_bool_to_float(
                    assessed_participant.test_results_bs)
            elif self.scope == "xox":
                numeric_test_results: list[float] = all_bool_to_float(
                    assessed_participant.test_results_xox)
            else:
                numeric_test_results: list[float] = all_bool_to_float(
                    assessed_participant.all_test_results)
            grid_values.append(numeric_test_results)
        return grid_values

    def colour_zone_size(self, participants: list[AssessedParticipant]) -> int:
        return participant_stat_tools.extract_control_group_size(participants)

    def y_axis_label(self) -> list[str]:
        return "All Participants"

    def x_axis_label(self) -> list[str]:
        return "Unit Tests "+self.scope

    def file_label(self) -> str:
        return "06-test-individual-"+self.scope
