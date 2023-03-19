"""
Extractor implementation that extracts the time needed for conversion of a provided vanilla
application to a RESTful service.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.scatter_plotters.extractors.application_extractor import ApplicationExtractor


class ApplicationPassrateExtractor(ApplicationExtractor):
    """
    This extractor retrieves the percentage of passed unit tests for the bookstore/xox
    implementation.
    """

    def extract(self, participants: list[AssessedParticipant]) -> list[float]:
        """
        :param participants: as the list of participants whose values we are interested in.
        :return: list of float values extracted from the provided participants.
        """

        result: list[float] = []
        for assessed_participant in participants:
            if self.application == "bookstore":
                result.append(assessed_participant.test_percentage_bs)
            if self.application == "xox":
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
