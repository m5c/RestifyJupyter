"""
Extractor implementation that extracts the time-to-passrate tradeoff for of a provided vanilla
application to a RESTful service, regardless the methodology used.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.scatter_plotters.extractors.application_extractor import ApplicationExtractor
from restify_mining.scatter_plotters.extractors.extractor import Extractor


class ApplicationTimeToPassRateTradeoffExtractor(ApplicationExtractor):
    """
    This extractor retrieves the time to passrate tradeoff resulting from the refactoring of a
    given application.
    """

    def extract(self, participants: list[AssessedParticipant]) -> list[float]:
        """
        Implementation of the extract method that provides refactoring time in milliseconds used by
        participants.
        TODO: figure out a way to normalize time.
        """
        result: list[int] = []
        for assessed_participant in participants:
            if self.__application == "bookstore":
                result.append(assessed_participant.time_bs)
            if self.__application == "xox":
                result.append(assessed_participant.time_xox)
        return result

    def axis_label(self) -> str:
        """
        Implementation of the axis label method that provides a string usable for plotting the
        extracted values in a 2D correlation plotter.
        """
        return "Refactoring time " + self.__application.capitalize() + " [sec]"

    def filename_segment(self) -> str:
        return self.__application.capitalize() + "RefactorTime"
