"""
Extended partitipant class (inherits form participant.py), representing a participant along with
all additional quantifiable data extracted from fused csv file.
"""
from restify_mining.participant import Participant


class AssessedParticipant(Participant):
    """Assessed Participant class. Represents all quantifiable information regarding a
    participant obtained at any point in time throughout the study. This is a one-to-one
    representation of the lines in the generated-csv-files/restify.csv file."""


def __init__(self, codename: str, skills: list[int], test_results_manual: list[bool],
             test_results_assisted: list[bool]):
    # invoke super with base attributes
    super().__init__(codename, skills)

    # store additional info in private variables
    self.__test_results_manual = test_results_manual
    self.__test_results_assisted = test_results_assisted


@property
def test_results_manual(self) -> list[bool]:
    """
    Property / Getter for manual task unit test results.
    :return: a boolean array where every position indicates whether a test was successful or not
    """
    return self.__test_results_manual


@property
def test_results_assisted(self) -> list[bool]:
    """
    Property / Getter for manual task unit test results.
    :return: a boolean array where every position indicates whether a test was successful or not
    """
    return self.__test_results_assisted
