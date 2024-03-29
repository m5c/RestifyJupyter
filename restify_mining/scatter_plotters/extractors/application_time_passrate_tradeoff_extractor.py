"""
Extractor implementation that extracts the time-to-passrate tradeoff for of a provided vanilla
application to a RESTful service, regardless the methodology used.
Note: This extractor makes most sense if the provided population is homogenous, is to say
followed the same app-methodology combinations. This is e.g. the case for red+yellow and
blue+green. A filter should be applied to reduce the input population, before calling this
extractor.
Author: Maximilian Schiedermeier
"""
from restify_mining.data_objects.normalized_participant import NormalizedParticipant
from restify_mining.scatter_plotters.extractors.application_extractor import ApplicationExtractor


class ApplicationTimeToPassRateTradeoffExtractor(ApplicationExtractor):
    """
    This extractor retrieves the time to passrate tradeoff resulting from the refactoring of a
    given application.
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
            if self.application == "bookstore":
                ratio: float = \
                    (1 - quality_weight) * (1 - assessed_participant.norm_time_bs) + \
                    quality_weight * (0.01 * assessed_participant.test_percentage_bs)
            if self.application == "xox":
                ratio: float = \
                    (1 - quality_weight) * (1 - assessed_participant.norm_time_xox) + \
                    quality_weight * (0.01 * assessed_participant.test_percentage_xox)
            result.append(ratio)
        return result

    def axis_label(self) -> str:
        """
        Implementation of the axis label method that provides a string usable for plotting the
        extracted values in a 2D correlation plotter.
        """
        return "Refactoring time " + self.__application.capitalize() + " [sec]"

    def filename_segment(self) -> str:
        return self.__application.capitalize() + "RefactorTime"
