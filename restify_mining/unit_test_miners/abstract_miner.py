"""
Abstract base class for all unit_test_miners. Consumes a list of assessed participants, produces
a list of float values, ready for subsequent colourizing / passing to plotter. The algorithm used
to produce the output values depends on the specific miner implementation.
See: https://blog.teclado.com/python-abc-abstract-base-classes/
"""

from abc import ABC, abstractmethod

from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.markers.unit_tests_markers import xox_unit_tests, bs_unit_tests


class AbstractTestMiner(ABC):
    """
    Abstract miner class serves as interface for all miner implementations.
    """

    def __init__(self, scope: str):
        """
        Common miner constructor to store the scope parameter.
        :param scope:
        """
        # Validate input param
        if scope not in {"bs", "xox", "all"}:
            raise Exception("Invalid scope parameter: " + scope)
        self.__scope = scope

    @abstractmethod
    def mine(self, participants: list[AssessedParticipant]) -> list[list[float]]:
        """
        Abstract method for data analysis of provided participants. Behaviour depends on
        implementation class.
        :param participants: as the list of participants to analyze
        :return: 2D array of float values, representing the data to be plotted.
        """

    @abstractmethod
    def colour_zone_size(self, participants: list[AssessedParticipant]) -> int:
        """
        Abstract method that every implementing class has to override. Returns the size of each
        colour zone grids produced by this miner.
        :param: the population for which colour zones must be extracted
        :return: amount of rows designated to one colour zone (control group) for grids produced
        by this plotter.
        """

    @abstractmethod
    def y_axis_label(self) -> list[str]:
        """
        Abstract method that every implementing class has to override. Returns the label that
        describes entries on y axes.
        :return: label for rows in miner output grid.
        """

    @abstractmethod
    def x_axis_label(self) -> list[str]:
        """
        Abstract method that every implementing class has to override. Returns the label that
        describes entries on x axes.
        :return: label for columns in miner output grid.
        """

    @property
    def x_tics(self) -> list[str]:
        """
        Abstract method to retrieve the entries for all tecis on x-axis. This is usually the
        tests in order, associated to the app registered on concrete miner instantiation.
        :return: list of tests names for given app, for use as tics on plot.
        """
        if self.__scope == "xox":
            return xox_unit_tests
        if self.__scope == "bs":
            return bs_unit_tests
        return xox_unit_tests + bs_unit_tests

    @abstractmethod
    def file_label(self) -> str:
        """
        Abstract method that every implementing class has to override. Returns the label that
        describes file base name if persisted to disk.
        :return: label for file name.
        """

    @property
    def scope(self):
        """
        Python getter equivalent for the application scope variable of this abstract miners
        superclass.
        :return: name of app / all apps this miner is branded to.
        """
        return self.__scope
