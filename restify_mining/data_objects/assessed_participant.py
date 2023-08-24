"""
Extended participant class (inherits form participant.py), representing a participant along with
all additional quantifiable data extracted from fused csv file.
"""
from restify_mining.data_objects.control_group import ControlGroup
from restify_mining.markers import unit_tests_markers
from restify_mining.data_objects.participant import Participant


class AssessedParticipant(Participant):
    """Assessed Participant class. Represents all quantifiable information regarding a
    participant obtained at any point in time throughout the study. This is a one-to-one
    representation of the lines in the generated-csv-files/restify.csv file."""

    # pylint: disable=too-many-arguments
    # pylint: disable=too-many-instance-attributes

    def __init__(self, codename: str, control_group: ControlGroup, skills: list[int],
                 test_results_bs: list[bool], test_results_xox: list[bool], time_bs: int,
                 time_xox: int, pre_time_tc: int, pre_time_ide: int):
        """
        :type self: object
        """
        # invoke super with base attributes
        super().__init__(codename, control_group, skills)

        # store additional info in private variables
        # Individual test results for both apps
        self.__test_results_bs: list[bool] = test_results_bs
        self.__test_results_xox: list[bool] = test_results_xox

        # Percentage test rate for both apps (is calculated, not extracted from CSV)
        self.__test_percentage_bs: float = test_results_bs.count(True) / len(
            test_results_bs) * 100.0
        self.__test_percentage_xox: float = test_results_xox.count(True) / len(
            test_results_xox) * 100.0

        self.__time_bs: int = int(time_bs)
        self.__time_xox: int = int(time_xox)

        self.__pre_time_tc: int = int(pre_time_tc)
        self.__pre_time_ide: int = int(pre_time_ide)

    @property
    def time_bs(self) -> int:
        """
        Property / Getter for time in seconds required for bookstore refactoring.
        :return: amount of seconds this participant needed for the bookstore task.
        """
        return self.__time_bs

    @property
    def time_xox(self) -> int:
        """
        Property / Getter for time in seconds required for bookstore refactoring.
        :return: amount of seconds this participant needed for the bookstore task.
        """
        return self.__time_xox

    @property
    def pre_time_tc(self) -> int:
        """
        Property / Getter for time in seconds spend on task familiarization with touchcore task.
        """
        return self.__pre_time_tc

    @property
    def pre_time_ide(self) -> int:
        """
        Property / Getter for time in seconds spend on task familiarization with ide task.
        """
        return self.__pre_time_ide

    @property
    def time_first(self) -> int:
        """
        Getter to retrieve the time it took for the first refactoring task, whatever the
        methodology or application concerned.
        :return: integer value expressing the time in seconds for the first refactoring task
        """
        if self.group_name in {"red", "green"}:
            return self.__time_bs
        if self.group_name in {"blue", "yellow"}:
            return self.__time_xox
        raise Exception("Participant group is detached.")

    @property
    def app_first(self) -> str:
        if self.group_name in {"red", "green"}:
            return "bs"
        if self.group_name in {"blue", "yellow"}:
            return "xox"

    @property
    def app_second(self) -> str:
        if self.group_name in {"red", "green"}:
            return "xox"
        if self.group_name in {"blue", "yellow"}:
            return "bs"

    @property
    def meth_first(self) -> str:
        if self.group_name in {"red", "blue"}:
            return "tc"
        if self.group_name in {"green", "yellow"}:
            return "ide"

    @property
    def meth_second(self) -> str:
        if self.group_name in {"red", "blue"}:
            return "ide"
        if self.group_name in {"green", "yellow"}:
            return "tc"

    @property
    def time_second(self) -> int:
        """
        Getter to retrieve the time it took for the second refactoring task, whatever the
        methodology or application concerned.
        :return: integer value expressing the time in seconds for the second refactoring task
        """
        if self.group_name in {"blue", "yellow"}:
            return self.__time_bs
        if self.group_name in {"red", "green"}:
            return self.__time_xox
        raise Exception("Participant group is detached.")

    @property
    def test_percentage_first(self) -> float:
        """
        Getter to retrieve the test success rate for the first refactoring task, whatever the
        methodology or application concerned.
        :return: float value expressing the test success rate for the first refactoring task
        """
        if self.group_name in {"red", "green"}:
            return self.__test_percentage_bs
        if self.group_name in {"blue", "yellow"}:
            return self.__test_percentage_xox
        raise Exception("Participant group is detached.")

    @property
    def test_percentage_second(self) -> float:
        """
        Getter to retrieve the test success rate for the second refactoring task, whatever the
        methodology or application concerned.
        :return: float value expressing the test success rate for the second refactoring task
        """
        if self.group_name in {"blue", "yellow"}:
            return self.__test_percentage_bs
        if self.group_name in {"red", "green"}:
            return self.__test_percentage_xox
        raise Exception("Participant group is detached.")

    @property
    def time_tc(self) -> int:
        """
        Property / Getter for time in seconds required for touchcore based refactoring, whatever
        the application.
        """
        if self.group_name in {"green", "blue"}:
            return self.__time_xox
        if self.group_name in {"red", "yellow"}:
            return self.__time_bs
        raise Exception("Participant group is detached.")

    @property
    def time_ide(self) -> int:
        """
        Property / Getter for time in seconds required for ide based refactoring, whatever the
        application.
        """
        if self.group_name in {"blue", "green"}:
            return self.__time_bs
        if self.group_name in {"red", "yellow"}:
            return self.__time_xox
        raise Exception("Participant group is detached.")

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

    def all_test_results(self) -> list[bool]:
        """
        Helper function to create a single list with all unit tests results (both applications).
        :return: list with all unit test results. First come all BookStore test results,
        then come all Xox test results.
        """
        all_test_results: list[bool] = self.__test_results_bs.copy()
        all_test_results.extend(self.__test_results_xox)
        return all_test_results

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

    @property
    def test_percentage_tc(self) -> int:
        """
        Property / Getter for pass rate percentage for touchcore based refactoring, whatever the
        application.
        """
        if self.group_name in {"green", "blue"}:
            return self.__test_percentage_xox
        if self.group_name in {"red", "yellow"}:
            return self.__test_percentage_bs
        raise Exception("Participant group is detached.")

    @property
    def test_percentage_ide(self) -> int:
        """
        Property / Getter for pass rate percentage for ide based refactoring, whatever the
        application.
        """
        if self.group_name in {"blue", "green"}:
            return self.__test_percentage_bs
        if self.group_name in {"red", "yellow"}:
            return self.__test_percentage_xox
        raise Exception("Participant group is detached.")

    def __str__(self):
        """
        Overloaded default to string method. Prints all information stored about this participant.
        :return: string representation of current objects.
        """
        # print name + control group
        participant_str = self.group_name + "-" + self.animal_name + ": \t["
        for skill in self.skills:
            participant_str += str(skill) + ","

        # Print test results and percentage for Xox
        participant_str += "], \tXox Tests: ["
        for index, result in enumerate(self.test_results_xox):
            participant_str += unit_tests_markers.xox_unit_tests[index] + ": " + str(result) + ", "
        participant_str += "] => " + str(round(self.__test_percentage_xox, 2)) + "% "

        # Print test results and percentage for BookStore
        participant_str += ", \tBookStore Tests: ["
        for index, result in enumerate(self.test_results_bs):
            participant_str += unit_tests_markers.bs_unit_tests[index] + ": " + str(result) + ", "
        participant_str += "] => " + str(round(self.__test_percentage_bs, 2)) + "% "

        # Return fully concatenated string representing all data of this participant
        return participant_str
