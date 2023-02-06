"""
Extractor implementation that produces the time spent on reading task description for a given
methodology.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.extractors.extractor import Extractor


class MethodologyPretimeExtractor(Extractor):
    """
    This extractor retrieves the percentage of passed unit tests for the bookstore/xox
    implementation.
    """

    def __init__(self, methodology: str) -> Extractor:
        """
        :param methodology: as string to indicate which methodology we are interested in (tc/ide)
        Implementation of the extract method that provides refactoring quality in passed unit test
        percentage.
        """
        if methodology == "tc" or methodology == "ide":
            self.__methodology = methodology
        else:
            raise Exception("Invalid methodology: " + methodology)

    def extract(self, participants: list[AssessedParticipant]) -> list[float]:
        """
        :param participants: as the list of participants whose values we are interested in.
        :return: list of float values extracted from the provided participants.
        """

        result: list[float] = []
        for assessed_participant in participants:
            if self.__methodology == "tc":
                result.append(assessed_participant.pre_time_tc)
            if self.__methodology == "ide":
                result.append(assessed_participant.pre_time_ide)
        return result

    def axis_label(self) -> str:
        """
        Implementation of the axis label method that provides a string usable for plotting the
        extracted values in a 2D correlation plotter.
        """
        return self.__methodology.capitalize() + " task familiarization [sec]"

    def filename_segment(self) -> str:
        return self.__methodology.capitalize() + "PreTaskTime"
