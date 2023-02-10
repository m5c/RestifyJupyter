"""
Extractor implementation that extracts the time needed for conversion of a provided vanilla
application to a RESTful service.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.extractors.extractor import Extractor


class ApplicationTimeExtractor(Extractor):
    """
    This extractor retrieves the time needed for refactoring the bookstore/xox implementation.
    """

    def __init__(self, application: str) -> Extractor:
        """
        :param application: as string to indicate which application we are interested in (bs/xox)
        Implementation of the extract method that provides refactoring time in milliseconds used by
        """
        if application in {"bookstore", "xox"}:
            self.__application = application
        else:
            raise Exception("Invalid application: " + application)

    def extract(self, participants: list[AssessedParticipant]) -> list[float]:
        """
        Implementation of the extract method that provides refactoring time in milliseconds used by
        participants.
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
        return "Refactoring time "+self.__application.capitalize()+" [sec]"

    def filename_segment(self) -> str:
        return self.__application.capitalize() + "RefactorTime"
