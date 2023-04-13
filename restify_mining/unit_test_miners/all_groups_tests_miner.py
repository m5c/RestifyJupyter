"""
Most simple miner implementation. Analyzes all provided participants and mines their test
restuls. Stores outcome in 2D array where passed tests are represented by1, failed tests by 0.
"""
from restify_mining.skill_extractors import participant_stat_tools
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.unit_test_miners.abstract_miner import AbstractTestMiner


class AllGroupsTestsMiner(AbstractTestMiner):
    """
    Extension of abstract miner, produces result values for all participants and all tests.
    """

    def mine(self, participants: list[AssessedParticipant]) -> list[list[float]]:
        """
        :param participants: as the set of participants to analyze
        :param scope: can be "all", "bs", or "xox". Result list changes depending on the scope
        selected.
        :return: 2D list of float values. Outer list for the control groups, inner for the
        considered test cases in order. Float value encodes average success rate for test.
        """

        # Define outer list for the control groups.
        grid_values: list[list[float]] = []

        # Iterate over the control groups (used by set of received participants)
        for control_group_name in participant_stat_tools.extract_group_names(participants):

            # Build list of average test success rate for this control group
            group_average_results: list[float] = []

            # Extract the set of group participants (participants of current control group)
            group_participants: list[
                AssessedParticipant] = participant_stat_tools.filter_population_by_group(
                participants, control_group_name)

            # Iterate over target tests (based on scope), determine average score for each by
            # iterating over participants and computing average.
            if self.scope == "bs":
                test_amount: int = len(participants[0].test_results_bs)
            elif self.scope == "xox":
                test_amount: int = len(participants[0].test_results_xox)
            else:
                test_amount: int = len(participants[0].all_test_results())

            # Iterate over the amount of tests covered by scope
            for test_index in range(test_amount):

                # Compute the average success rate for the current test and the current set of
                # participants
                average_test_result: float = 0.0
                for participant in group_participants:
                    average_test_result = average_test_result + self.__test_result_for_participant(
                        test_index, participant)
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
        return "07-test-heatmap-" + self.scope

    def __test_result_for_participant(self, test_index: int,
                                      participant: AssessedParticipant) -> float:
        """
        Helper function to determine the test score for a given participant, based on the current
        test index and scope used for this miner
        :param test_index: as the integer index of the test of interest, given the applied scope
        :param participant: as the participant providing the test result
        :return:
        """
        if self.scope == "bs":
            return participant.test_results_bs[test_index]
        if self.scope == "xox":
            return participant.test_results_xox[test_index]
        return participant.all_test_results()[test_index]
