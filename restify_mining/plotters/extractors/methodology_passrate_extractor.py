"""
Extractor implementation that extracts the time needed for conversion using a given methodology.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.plotters.extractors.extractor import Extractor


class MethodologyPassrateExtractor(Extractor):
    """
    This extractor retrieves the percentage of passed unit tests for the target application
    refactored with the requested methodology.
    """

    def __init__(self, methodology: str) -> Extractor:
        """
        :param methodology: as string to indicate which methodology we are interested in (tc/ide)
        Initializes the extractor implementation with the received target value.
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
                result.append(assessed_participant.test_percentage_tc)
            if self.__methodology == "ide":
                result.append(assessed_participant.test_percentage_ide)
        return result

    def axis_label(self) -> str:
        """
        Implementation of the axis label method that provides a string usable for plotting the
        extracted values in a 2D correlation plotter.
        """
        return self.__methodology.capitalize() + " unit test pass rate [%]"

    def filename_segment(self) -> str:
        return self.__methodology.capitalize() + "UnitPassRate"
