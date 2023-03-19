"""
Extractor implementation that extracts the time needed for conversion of a provided vanilla
application to a RESTful service.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.scatter_plotters.extractors.application_extractor import ApplicationExtractor


class ApplicationTimeExtractor(ApplicationExtractor):
    """
    This extractor retrieves the time needed for refactoring the bookstore/xox implementation.
    """

    def extract(self, participants: list[AssessedParticipant]) -> list[float]:
        """
        Implementation of the extract method that provides refactoring time in milliseconds used by
        participants.
        """
        result: list[int] = []
        for assessed_participant in participants:
            if self.application == "bookstore":
                result.append(assessed_participant.time_bs)
            if self.application == "xox":
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
