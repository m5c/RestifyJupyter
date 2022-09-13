"""
Extended participant class (inherits form participant.py), representing a participant along with
all additional quantifiable data extracted from fused csv file.
"""
from restify_mining.participant import Participant


class AssessedParticipant(Participant):
    """Assessed Participant class. Represents all quantifiable information regarding a
    participant obtained at any point in time throughout the study. This is a one-to-one
    representation of the lines in the generated-csv-files/restify.csv file."""

    def __init__(self, codename: str, skills: list[int], test_results_bs: list[bool],
                 test_results_xox: list[bool]):
        """
        :type self: object
        """
        # invoke super with base attributes
        super().__init__(codename, skills)

        # store additional info in private variables
        self.__test_results_bs: list[bool] = test_results_bs
        self.__test_results_xox: list[bool] = test_results_xox

    @property
    def test_results_bs(self) -> list[bool]:
        """
        Property / Getter for manual task unit test results.
        :return: a boolean array where every position indicates whether a test was successful or not
        """
        return self.__test_results_bs

    @property
    def test_results_xox(self) -> list[bool]:
        """
        Property / Getter for manual task unit test results.
        :return: a boolean array where every position indicates whether a test was successful or not
        """
        return self.__test_results_xox

    def __str__(self):
        participant_str = self.group_name + "-" + self.animal_name + ": \t["
        for skill in self.skills:
            participant_str += str(skill) + ","
        participant_str += "], \tXox Tests: ["
        for result in self.test_results_xox:
            participant_str += str(result) + ","
        participant_str += "], \tBookStore Tests: ["
        for result in self.test_results_bs:
            participant_str += str(result) + ","
        participant_str += "]"

        return participant_str
