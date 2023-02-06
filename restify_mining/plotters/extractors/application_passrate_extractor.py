"""
Extractor implementation that extracts the time needed for conversion of a provided vanilla
application to a RESTful service.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.extractors.extractor import Extractor


class ApplicationPassRateExtractor(Extractor):
    """
    This extractor retrieves the percentage of passed unit tests for the bookstore/xox
    implementation.
    """

    def __init__(self, application: str) -> Extractor:
        """
        :param application: as string to indicate which application we are interested in (bs/xox)
        Implementation of the extract method that provides refactoring quality in passed unit test
        percentage.
        """
        if application == "bookstore" or application == "xox":
            self.__application = application
        else:
            raise Exception("Invalid application: " + application)

    def extract(self, participants: list[AssessedParticipant]) -> list[float]:
        """
        :param participants: as the list of participants whose values we are interested in.
        :return: list of float values extracted from the provided participants.
        """

        result: list[float] = []
        for assessed_participant in participants:
            if self.__application == "bookstore":
                result.append(assessed_participant.test_percentage_bs)
            if self.__application == "xox":
                result.append(assessed_participant.test_percentage_xox)
        return result

    def axis_label(self) -> str:
        """
        Implementation of the axis label method that provides a string usable for plotting the
        extracted values in a 2D correlation plotter.
        """
        return self.__application.capitalize() + " unit test pass rate [%]"

    def filename_segment(self) -> str:
        return self.__application.capitalize() + "UnitPassRate"
