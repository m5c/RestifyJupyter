"""
Extractor implementation that extracts the time needed for conversion of bookstore to a RESTful
service.
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.extractors.extractor import Extractor


class BsTimeExtractor(Extractor):
    """
    This extractor retrieves the time needed for refactoring the bookstore implementation.
    """

    def extract(self, participants: list[AssessedParticipant]) -> list[float]:
        """
        Implementation of the extract method that provides refactoring time in milliseconds used by
        participants.
        """
        result: list[int] = []
        for assessed_participant in participants:
            result.append(assessed_participant.time_bs)
        return result

    def axis_label(self) -> str:
        """
        Implementation of the axis label method that provides a string usable for plotting the
        extracted values in a 2D correlation plotter.
        """
        return "Refactoring time BS [ms]"
