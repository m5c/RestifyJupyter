"""
Most simple miner implementation. Analyzes all provided participants and mines their test
restuls. Stores outcome in 2D array where passed tests are represented by1, failed tests by 0.
"""
from restify_mining.data_objects import participant_stat_tools
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.unit_test_miners.abstract_miner import AbstractMiner


class AllGroupsAllTestsMiner(AbstractMiner):
    """
    Extension of abstract miner, produces result values for all participants and all tests.
    """

    def mine(self, participants: list[AssessedParticipant]) -> list[list[float]]:
        grid_values: list[list[float]] = []

        for control_group_name in participant_stat_tools.extract_group_names(participants):

            # build list of average test success rate for this control group, every unit test (
            # both apps)
            group_average_results: list[float] = []
            group_participants: list[
                AssessedParticipant] = participant_stat_tools.filter_population_by_group(
                participants, control_group_name)

            # for every test, compute participant mean (only participants of this group)
            test_amount: int = len(group_participants[0].all_test_results())
            for test_index in range(test_amount):
                average_test_result: float = 0.0
                for participant in group_participants:
                    average_test_result = average_test_result + participant.all_test_results()[
                        test_index]
                average_test_result = average_test_result / len(group_participants)
                group_average_results.append(average_test_result)

            # Append list of average results of this control group to overall result grid
            grid_values.append(group_average_results)

        # Once the average test results are constructed for every control group, return result grid
        return grid_values

    def colour_zone_size(self, participants: list[AssessedParticipant]) -> int:
        """
        This miner creates a single line for every control group (reduces every test result to
        group average).
        As such the size of each associated colour zone is exactly one.
        :param participants: as the population to analyze. Not needed here.
        :return: size of one for every control_group colour zone.
        """
        return 1

    def y_axis_label(self) -> list[str]:
        return "Control Groups"

    def x_axis_label(self) -> list[str]:
        return "Unit Tests"

    def file_label(self) -> str:
        return "06-test-heatmap"
