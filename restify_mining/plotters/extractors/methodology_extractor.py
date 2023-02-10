"""
Intermediate abstract class for all methodology extractors.
Author Maximilian Schiedermeier
"""
from abc import ABC

from restify_mining.plotters.extractors.extractor import Extractor


class MethodologyExtractor(Extractor, ABC):
    """
    Defines just a common constructor.
    """

    def __init__(self, methodology: str) -> Extractor:
        """
        :param methodology: as string to indicate which methodology we are interested in (tc/ide)
        Initializes the extractor implementation with the received target value.
        """
        if methodology in {"tc", "ide"}:
            self.__methodology = methodology
        else:
            raise Exception("Invalid methodology: " + methodology)

    @property
    def methodology(self) -> str:
        """
        Just some boilerplate code that would be completely needless in any proper OO language
        to emulate polymorphism and class secrets. #pythonisnotpretty
        """
        return self.__methodology
