"""
Extended participant class (inherits form participant.py), representing a participant along with
all additional quantifiable data extracted from fused csv file.
"""
from restify_mining import unit_tests_markers
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
        # Individual test results for both apps
        self.__test_results_bs: list[bool] = test_results_bs
        self.__test_results_xox: list[bool] = test_results_xox

        # Percentage test rate for both apps (is calculated, not extracted from CSV)
        self.__test_percentage_bs: float = test_results_bs.count(True) / len(
            test_results_bs) * 100.0
        self.__test_percentage_xox: float = test_results_xox.count(True) / len(
            test_results_xox) * 100.0
        print("yolo")

    @property
    def test_results_bs(self) -> list[bool]:
        """
        Property / Getter for bookstore task unit test results.
        :return: a boolean array where every position indicates whether a test was successful or not
        """
        return self.__test_results_bs

    @property
    def test_results_xox(self) -> list[bool]:
        """
        Property / Getter for xox task unit test results.
        :return: a boolean array where every position indicates whether a test was successful or not
        """
        return self.__test_results_xox

    @property
    def test_percentage_bs(self) -> float:
        """
        Property / Getter for bookstore task unit test results as overall percentage.
        :return: a float value representing bookstore test success rate.
        """
        return self.__test_percentage_bs

    @property
    def test_percentage_xox(self) -> float:
        """
        Property / Getter for xox task unit test results as overall percentage.
        :return: a float value representing xox test success rate.
        """
        return self.__test_percentage_xox

    def __str__(self):
        """
        Overloaded default to string method. Prints all information stored about this participant.
        :return: string representation of current objects.
        """
        # TODO Figure out why percentage wrong and not all test results printed.

        # print name + control group
        participant_str = self.group_name + "-" + self.animal_name + ": \t["
        for skill in self.skills:
            participant_str += str(skill) + ","

        # Print test results and percentage for Xox
        participant_str += "], \tXox Tests: ["
        for index, result in enumerate(self.test_results_xox):
            participant_str += unit_tests.xox_unit_tests[index] + ": " + str(result) + ", "
        participant_str += "] => " + str(round(self.__test_percentage_xox, 2)) + "% "

        # Print test results and percentage for BookStore
        participant_str += ", \tBookStore Tests: ["
        for index, result in enumerate(self.test_results_bs):
            participant_str += unit_tests.bs_unit_tests[index] + ": " + str(result) + ", "
        participant_str += "] => " + str(round(self.__test_percentage_bs, 2)) + "% "

        # Return fully concatenated string representing all data of this participant
        return participant_str
