"""
Abstract base class for all miners. Consumes a list of assessed participants, produces a list of
float values, ready for subsequent colourizing / passing to plotter. The algorithm used to
produce the output values depends on the specific miner implementation.
See: https://blog.teclado.com/python-abc-abstract-base-classes/
"""

from abc import ABC, abstractmethod

from restify_mining.data_objects.assessed_participant import AssessedParticipant


class AbstractMiner(ABC):
    """
    Abstract miner class serves as interface for all miner implementations.
    """

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
        :return: amount of rows designated to one colour zone (control group) for girds produced
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
