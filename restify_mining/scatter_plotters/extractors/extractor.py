"""
Abstract base class for all extractors. Extractors produce metrics when provided with a list
of participants. Implementing classes must provide two things: an extraction
method to extract the exact values out of a provided participant list and a string that can be
used as axis label. Extractors are different from miners in so far as that they only generate a
single list of values. Extractors are typically combined with another extractor, e.g. by a
Correlator, to conveniently produce a sample based plot.
Important: Extractors are not filters. They do not reduce the participant set. The purpose is only
to map each participant in a given list to a numeric metric. For filtering,
use ParticipantFilterTools.
Author: Maximilian Schiedermeier
"""

from abc import ABC, abstractmethod

from restify_mining.data_objects.assessed_participant import AssessedParticipant


class Extractor(ABC):
    """
    Abstract miner class serves as interface for all miner implementations.
    """

    @abstractmethod
    def extract(self, participants: list[AssessedParticipant]) -> list[float]:
        """
        Abstract method for data analysis of provided participants. Behaviour depends on
        implementation class.
        :param participants: as the list of participants to analyze
        :return: list of float values, representing one dimension of sample correlations to be
        plotted.
        """

    @abstractmethod
    def axis_label(self) -> str:
        """
        Abstract method that produces an axis label consumable by plotter.
        :return: label for plot axis.
        """

    @abstractmethod
    def filename_segment(self) -> str:
        """
        Abstract method that produces an filename segment describing the executor.
        :return: executor name.
        """
