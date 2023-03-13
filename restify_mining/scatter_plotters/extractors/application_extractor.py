"""
Intermediate abstract class for all methodology extractors.
Author Maximilian Schiedermeier
"""
from abc import ABC

from restify_mining.scatter_plotters.extractors.extractor import Extractor


class ApplicationExtractor(Extractor, ABC):
    """
    Defines just a common constructor.
    """

    def __init__(self, application: str) -> Extractor:
        """
        :param application: as string to indicate which application we are interested in (bs/xox)
        Implementation of the extract method that provides refactoring quality in passed unit test
        percentage.
        """
        if application in {"bookstore", "xox"}:
            self.__application = application
        else:
            raise Exception("Invalid application: " + application)

    @property
    def application(self) -> str:
        """
        Just some boilerplate code that would be completely needless in any proper OO language
        to emulate polymorphism and class secrets.
        """
        return self.__application
