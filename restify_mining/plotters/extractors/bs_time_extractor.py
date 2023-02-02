"""
Extractor implementation that extracts the time needed for conversion of bookstore to a RESTful
service.
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.extractors.extractor import Extractor


class BsTimeExtractor(Extractor):
    """
    Implementation of the extract method that provides refactoring time in milliseconds used by
    participants.
    """

    def extract(self, participants: list[AssessedParticipant]) -> list[float]:
        result: list[int] = []
        for assessed_participant in participants:
            result.append(assessed_participant.time_bs)
        return result

    """
    Implementation of the axis label method that provides a string usable for plotting the 
    extracted values in a 2D correlation plotter.
    """
    def axis_label(self) -> str:
        return "Refactoring time BS [ms]"
