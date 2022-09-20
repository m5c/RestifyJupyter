"""
Abstract base class for all miners. Consumes a list of assessed participants, produces a list of
float values, ready for subsequent colourizing / passing to plotter. The algorithm used to
produce the output values depends on the specific miner implementation.
See: https://blog.teclado.com/python-abc-abstract-base-classes/
"""

from abc import ABC, abstractmethod

from restify_mining.assessed_participant import AssessedParticipant


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
