"""
Extractor implementation that extracts the time-to-passrate tradeoff for a specified methodology,
 regardless the application refactored to a RESTful service.
Note: This extractor makes most sense if the provided population is homogenous, is to say
followed the same app-methodology combinations. This is e.g. the case for red+yellow and
blue+green. A filter should be applied to reduce the input population, before calling this
extractor.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.normalized_participant import NormalizedParticipant
from restify_mining.scatter_plotters.extractors.methodology_extractor import MethodologyExtractor


class MethodologyTimeToPassRateTradeoffExtractor(MethodologyExtractor):
    """
    This extractor retrieves the time to passrate tradeoff resulting from the refactoring using a
    given methodology.
    """

    def extract(self, participants: list[NormalizedParticipant]) -> list[float]:
        """
        Implementation of the extract method that provides ratio of normalized refactoring time
        to passrate of the outcome. The exact formula is:
        (1- "normalized time*) /2 + passrate/2. (note the passrate value is in percentages and
        needs to be divided by 100).
        Reason for inverting time is that be need higher valued to represent desirable results.
        """
        # The tradeoff can put more weight on the time or the test passrate factor. By default, both
        # are considered equally important.
        # A value of 1.0 means only correctness is considered. A value of 0 means only time is
        # considered.
        quality_weight: float = 0.5
        result: list[float] = []
        for assessed_participant in participants:
            if self.methodology == "tc":
                ratio: float = \
                    (1 - quality_weight) * (1 - assessed_participant.norm_time_tc) + \
                    quality_weight * (0.01 * assessed_participant.test_percentage_tc)
            if self.methodology == "ide":
                ratio: float = \
                    (1 - quality_weight) * (1 - assessed_participant.norm_time_ide) + \
                    quality_weight * (0.01 * assessed_participant.test_percentage_ide)
            result.append(ratio)
        return result

    def axis_label(self) -> str:
        """
        Implementation of the axis label method that provides a string usable for plotting the
        extracted values in a 2D correlation plotter.
        """
        return "Quality Tradeoff " + self.methodology.capitalize() + " [0-1]"

    def filename_segment(self) -> str:
        return self.methodology.capitalize() + "Quality Tradeoff "
