"""
Label extractor abstract superclass. Implementations return ordered list of participant labels,
based on received collection and the labeling strategy they implement.
Author: Maximilian Schiedermeier
"""

from abc import ABC, abstractmethod

from restify_mining.data_objects.assessed_participant import AssessedParticipant


class LabelMaker(ABC):

    @abstractmethod
    def make_labels(self, participants: list[AssessedParticipant], reduce_to_outliers: bool) -> \
            list[str]:
        """
        Abstract label maker method. All label makers must implement this method with their own
        strategy.
        :param participants: as the set of participants to create labels for.
        :param reduce_to_outliers: set to true to apply a filter that stripes all non-outliers to
        the empty string.
        :return: list of participant labels.
        """

    # TODO: define filter method that reduces all non outliers (outliers provided in CSV) to
    #  empty string.
