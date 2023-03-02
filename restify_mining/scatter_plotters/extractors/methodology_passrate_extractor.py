"""
Extractor implementation that extracts the time needed for conversion using a given methodology.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.assessed_participant import AssessedParticipant
from restify_mining.scatter_plotters.extractors.methodology_extractor import MethodologyExtractor


class MethodologyPassrateExtractor(MethodologyExtractor):
    """
    This extractor retrieves the percentage of passed unit tests for the target application
    refactored with the requested methodology.
    """


    def extract(self, participants: list[AssessedParticipant]) -> list[float]:
        """
        :param participants: as the list of participants whose values we are interested in.
        :return: list of float values extracted from the provided participants.
        """

        result: list[float] = []
        for assessed_participant in participants:
            if self.methodology == "tc":
                result.append(assessed_participant.test_percentage_tc)
            if self.methodology == "ide":
                result.append(assessed_participant.test_percentage_ide)
        return result

    def axis_label(self) -> str:
        """
        Implementation of the axis label method that provides a string usable for plotting the
        extracted values in a 2D correlation plotter.
        """
        return self.methodology.capitalize() + " unit test pass rate [%]"

    def filename_segment(self) -> str:
        return self.methodology.capitalize() + "UnitPassRate"
